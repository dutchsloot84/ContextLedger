# ContextLedger (working title)

ContextLedger turns repository activity into weekly or on-demand history ledgers for compliance, onboarding, and executive visibility.

## Quick start (scaffold)
```bash
python -m pip install -e .
python -m contextledger.cli --since 7d --until now --output docs/history --debug-scan
# => docs/history/context-index.json
```
