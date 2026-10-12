"""Record sanitized counters from one actor; never copy its conversation text."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path


def collect(session: Path):
    observations = []
    model = None
    effort = None
    for line in session.read_text(encoding="utf-8").splitlines():
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        payload = row.get("payload", {})
        if row.get("type") == "turn_context":
            model = payload.get("model")
            effort = payload.get("effort")
        if row.get("type") != "event_msg" or payload.get("type") != "token_count":
            continue
        info = payload.get("info") or {}
        counts = info.get("total_token_usage")
        if counts:
            observations.append({
                "time": row["timestamp"], "counts": counts,
                "request_input_tokens": (info.get("last_token_usage") or {}).get("input_tokens"),
                "model": model, "effort": effort,
            })
    return observations


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session", type=Path, required=True)
    parser.add_argument("--actor", required=True)
    parser.add_argument("--phase", required=True)
    parser.add_argument("--start", required=True)
    parser.add_argument("--at")
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("usage.jsonl"))
    args = parser.parse_args()
    rows = collect(args.session)
    before = [row for row in rows if row["time"] < args.start]
    selected = [row for row in rows if args.at is None or row["time"] <= args.at]
    if not selected:
        raise SystemExit("No usage observation available")
    last = selected[-1]
    baseline = before[-1]["counts"] if before else {key: 0 for key in last["counts"]}
    delta = {key: value - baseline.get(key, 0) for key, value in last["counts"].items()}
    if any(value < 0 for value in delta.values()):
        raise SystemExit("Counter reset: establish a separate segment baseline")
    during = [row for row in selected if row["time"] >= args.start]
    sizes = [row["request_input_tokens"] for row in during if row["request_input_tokens"] is not None]
    input_tokens = delta.get("input_tokens", 0)
    cached = delta.get("cached_input_tokens", 0)
    writes = delta.get("cache_write_input_tokens", 0)
    if cached + writes > input_tokens:
        raise SystemExit("Cache read/write counts exceed total input")
    estimate = None
    assumption = "unavailable: model/rate or request length not established"
    if last["model"] == "gpt-6.1-sol" and sizes and max(sizes) <= 272_000:
        estimate = ((input_tokens - cached - writes) * 2 + cached * .1
                    + writes * 2.5 + delta.get("output_tokens", 0) * 10) / 1_000_000
        assumption = "Standard API-equivalent USD, ordinary context; excludes regional/mode/tool premiums and actual Codex billing"
    record = {
        "actor": args.actor, "phase": args.phase, "start_utc": args.start,
        "recorded_utc": datetime.now(timezone.utc).isoformat(),
        "observed_utc": last["time"], "baseline": baseline,
        "cumulative": last["counts"], "delta": delta,
        "model": last["model"], "reasoning_effort": last["effort"],
        "maximum_observed_request_input_tokens": max(sizes) if sizes else None,
        "standard_api_equivalent_usd": estimate, "estimate_assumption": assumption,
        "actual_billed_usd": None,
        "pricing_checked_date": "2026-10-12",
        "pricing_source": "https://developers.openai.com/api/docs/models/gpt-6.1-sol",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("a", encoding="utf-8") as output:
        output.write(json.dumps(record, sort_keys=True) + "\n")
    print(json.dumps({"actor": args.actor, "phase": args.phase, "delta": delta,
                      "standard_api_equivalent_usd": estimate}))


if __name__ == "__main__":
    main()
