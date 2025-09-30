# ContextLedger (working title)

ContextLedger turns repository activity into weekly or on-demand history ledgers for compliance, onboarding, and executive visibility.

## Quick start
```bash
python -m pip install -e .
python -m contextledger.cli --since 7d --until now --output docs/history --debug-scan
# => docs/history/context-index.json
```

See [`docs/getting-started.md`](docs/getting-started.md) for a guided walkthrough
and [`docs/workflows.md`](docs/workflows.md) for automation notes.
