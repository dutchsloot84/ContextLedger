import argparse
import json
import sys
from pathlib import Path


def parse_args(argv=None):
    p = argparse.ArgumentParser(
        prog="contextledger",
        description="Generate weekly/on-demand history snapshots (scaffold).",
    )
    p.add_argument("--since", required=True, help="Window start (e.g., 7d or 2025-09-01)")
    p.add_argument("--until", default="now", help="Window end (default: now)")
    p.add_argument("--output", required=True, help="Output folder for history files")
    p.add_argument("--config", help="Path to defaults.yml (optional)")
    p.add_argument("--template", help="Path to markdown template (optional)")
    p.add_argument("--debug-scan", action="store_true", help="Verbose debug output")
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    idx = out_dir / "context-index.json"
    payload = {
        "since": args.since,
        "until": args.until,
        "generated_by": "ContextLedger 0.1.0 (scaffold)",
        "files": [],
        "notes": "Replace scaffold with real collectors during refactor.",
    }
    idx.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    if args.debug_scan:
        print(json.dumps({"args": vars(args), "index_path": str(idx)}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
