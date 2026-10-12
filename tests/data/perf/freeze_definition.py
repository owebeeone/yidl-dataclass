"""Combine untimed minor checks into one reviewable sampling definition."""

import argparse
import copy
import importlib.util
import json
from pathlib import Path


def load(name, filename):
    spec = importlib.util.spec_from_file_location(
        name, Path(__file__).with_name(filename)
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def merge(documents):
    common = None
    minor_provenance = {}
    for document in documents:
        row = copy.deepcopy(document)
        provenance = row.pop("provenance")
        minor = ".".join(provenance["python"].split(".")[:2])
        if minor in minor_provenance:
            raise ValueError("duplicate minor definition")
        minor_provenance[minor] = provenance
        if common is None:
            common = row
        elif row != common:
            raise ValueError(
                "case/source/configuration drift between minor definitions"
            )
    if common is None or set(minor_provenance) != set(common["minors"]):
        raise ValueError("all three minor definitions required")
    common["minor_provenance"] = minor_provenance
    return common


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", nargs=3, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError("definition already exists; preserve prior definition")
    validation = load("perf_validation", "validation.py")
    provenance = load("perf_provenance", "provenance.py")
    documents = [json.loads(path.read_text()) for path in args.inputs]
    for row in documents:
        validation.validate_definition(row)
        if row["source_sha256"] != provenance.source_hashes():
            raise ValueError("source changed after minor definition preparation")
    common = merge(documents)
    args.output.write_text(json.dumps(common, sort_keys=True, indent=2) + "\n")
    print(
        json.dumps(
            {
                "definition_sha256": provenance.canonical_digest(common),
                "minors": sorted(common["minor_provenance"]),
                "timing_cases": len(common["timing_keys"]),
                "memory_cases": len(common["memory_keys"]),
                "scope": "untimed definition freeze candidate",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
