# Getting started with ContextLedger

ContextLedger packages the Historian CLI as a Python module so you can install
and run it directly from this repository or any automation pipeline.

## 1. Install

```bash
python -m pip install --upgrade pip
python -m pip install -e .
```

## 2. Run a snapshot

Generate a weekly snapshot (adjust the window to taste):

```bash
python -m contextledger.cli --since 7d --until now --output docs/history --debug-scan
```

The command mirrors the preserved Historian behavior. When it completes you
will have a Markdown check-in file and an updated index:

```
docs/
  history/
    YYYY-MM-DD-checkin.md
    context-index.json
```

## 3. Explore shipped examples

The repository includes historical examples that you can reuse as templates or
sanity checks:

```
examples/history/
  README.md
  2025-09-25-checkin.md
  2025-09-26-checkin.md
  2025-09-29-checkin.md
  notes/
    ...
  context/
    context-index.json
```

Point the `--template` flag at `templates/weekly.md` to render using the
packaged template, or supply your own file.

## 4. Next steps

* Customize `config/defaults.yml` to tune collectors.
* Review [`docs/workflows.md`](docs/workflows.md) to automate weekly snapshots.
* Follow up issues to extract collectors into dedicated modules for easier
  testing and reuse.
