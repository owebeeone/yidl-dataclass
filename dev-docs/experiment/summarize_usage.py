"""Summarize latest cumulative observations, normalizing historical actor aliases."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path,
                        default=Path(__file__).with_name("usage.jsonl"))
    args = parser.parse_args()
    aliases = {"owner": "lane-owner", "design-drafter": "dataclass-drafter"}
    latest = {}
    for line in args.input.read_text().splitlines():
        row = json.loads(line)
        actor = aliases.get(row["actor"], row["actor"])
        if actor not in latest or row["observed_utc"] >= latest[actor]["observed_utc"]:
            latest[actor] = row
    missing = [actor for actor, row in latest.items()
               if row["standard_api_equivalent_usd"] is None]
    print(json.dumps({
        "actors": sorted(latest),
        "delta": {key: sum(row["delta"].get(key, 0) for row in latest.values())
                  for key in ("input_tokens", "cached_input_tokens", "output_tokens",
                              "reasoning_output_tokens", "total_tokens")},
        "standard_api_equivalent_usd": (
            None if missing else sum(row["standard_api_equivalent_usd"]
                                     for row in latest.values())),
        "missing_estimates": missing,
        "actual_billed_usd": None,
        "observation_times": {actor: row["observed_utc"]
                              for actor, row in latest.items()},
    }, indent=2))


if __name__ == "__main__":
    main()
