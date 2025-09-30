# Automating ContextLedger workflows

ContextLedger ships with a weekly GitHub Actions workflow that demonstrates how
to schedule history generation. The workflow lives at
[`.github/workflows/weekly-history.yml`](../.github/workflows/weekly-history.yml)
and runs `python -m contextledger.cli --since 7d --until now --output docs/history`.

## GitHub token scopes

The default `${{ secrets.GITHUB_TOKEN }}` works for repositories where the
workflow has `contents: write` and `pull-requests: write` permissions. If you
run the workflow outside GitHub Actions, provide a personal access token with:

* `repo` scope for private repositories.
* `public_repo` for public repositories.
* `project` if you plan to re-enable Projects v2 collectors.

Store the token in the `GITHUB_TOKEN` environment variable for local runs or as
a GitHub Actions secret when automating.

## Windows notes

* Ensure Python is added to the PATH. `py -m contextledger.cli ...` works when
  the launcher is available.
* When using PowerShell, quote arguments: `--template "templates/weekly.md"`.
* If Git is installed via GitHub Desktop, launch a Developer PowerShell to gain
  access to the CLI and Git utilities required by the collectors.

## Rate limits and retries

ContextLedger reuses the Historian collectors, so GitHub API rate limits still
apply. Mitigate issues by:

* Using a PAT instead of the default GITHUB_TOKEN when scanning large windows.
* Narrowing the `--since` window (e.g., `3d`) to reduce API calls.
* Disabling optional sources in `config/defaults.yml` when not needed.

If you depend on S3 artifacts, install the optional `s3` extra (`pip install
contextledger[s3]`) and confirm network access to AWS from your environment.
