# ContextLedger Historian Inventory & Dependency Report

_Repo branch scanned: `work` (no `feat/oss-scaffold` branch present; `main` also unavailable in local clone)._ 

## Files in Scope

| Path | Size (bytes) | Last Commit | Commit Date |
| --- | ---: | --- | --- |
| scripts/generate_history.py | 43816 | 25a1d76494c627468efbfd1fc7dae1d54feae797 | 2025-09-30T12:33:06-07:00 |
| config/defaults.yml | 1130 | 5f19d90b8ac01c8c34bc8714083c9ce5f9640326 | 2025-09-26T11:16:31-07:00 |
| .github/workflows/weekly-history.yml | 3217 | f78d06352ec527ebc397c54a59b5c87515226f60 | 2025-09-26T13:56:13-07:00 |
| docs/history/README.md | 1042 | 0e41343c550ad95eabead4727f2959d4a7058f48 | 2025-09-26T10:55:11-07:00 |
| docs/history/HISTORY_TEMPLATE.md | 473 | 0e41343c550ad95eabead4727f2959d4a7058f48 | 2025-09-26T10:55:11-07:00 |
| docs/history/2025-09-25-checkin.md | 1023 | 0e41343c550ad95eabead4727f2959d4a7058f48 | 2025-09-26T10:55:11-07:00 |
| docs/history/2025-09-26-checkin.md | 13696 | 236484ca97a620b4c222e4ebb4cad80bbfa047db | 2025-09-26T14:56:03-07:00 |
| docs/history/2025-09-29-checkin.md | 17488 | d4d9eda08836c72a84529c30f34b9c2715651a84 | 2025-09-29T10:14:38-07:00 |
| docs/history/notes/2025-09-26-dutchsloot84-ReleaseCopilot-AI-137.md | 2582 | b8e3f1206edcf20964093e626ddf51449fd218d5 | 2025-09-26T21:59:45+00:00 |
| docs/history/notes/2025-09-29-dutchsloot84-ReleaseCopilot-AI-137.md | 2582 | d4d9eda08836c72a84529c30f34b9c2715651a84 | 2025-09-29T10:14:38-07:00 |
| docs/history/notes/.gitkeep | 0 | 5f19d90b8ac01c8c34bc8714083c9ce5f9640326 | 2025-09-26T11:16:31-07:00 |
| docs/context/context-index.json | 1382 | d4d9eda08836c72a84529c30f34b9c2715651a84 | 2025-09-29T10:14:38-07:00 |

_No dedicated `templates/` directory exists; historian templates currently live under `docs/history/`._

## Dependency & Feature Highlights

- **Core script**: `scripts/generate_history.py` orchestrates data collection, rendering, and index maintenance. It depends on:
  - Local module `scripts.github.ProjectsV2Client` (missing in this snapshot; required for Projects v2 GraphQL queries).
  - External libraries: `requests` (REST calls), `PyYAML` (config parsing), optional `boto3` (S3 artifacts).
  - Assets: `config/defaults.yml`, `docs/history/HISTORY_TEMPLATE.md`, mirrored notes under `docs/history/notes/**/*.md`, and it writes to `docs/context/context-index.json`.
- **Projects v2**: `_collect_project_section` expects `ProjectsV2Client.query_issues_with_status(...)` to populate in-progress/backlog sections. Falls back to label filtering if Projects v2 fails or token missing.
- **Marker parsing**: `_extract_comment_markers` and `_collect_notes_section` scan GitHub issue/PR comments for `Decision:`, `Note:`, `Blocker:`, `Action:` prefixes, optionally mirroring via `_mirror_note_markers`.
- **Artifact aggregation**: `_collect_github_actions_artifacts` enumerates workflow runs (`ci.yml`, `weekly-history.yml`) and `_collect_s3_artifacts` scans buckets/prefixes when enabled.
- **Jira enrichment**: `_collect_jira_references` parses commit messages with `HISTORIAN_JIRA_REGEX` when `HISTORIAN_ENABLE_JIRA=true`.
- **Index writer**: `_ensure_history_index` maintains `docs/context/context-index.json` alongside Markdown exports.

### Runtime & Configuration

- Minimum Python: `>=3.9` (workflow pins Python 3.10).
- Required environment variables/secrets:
  - `GITHUB_TOKEN` (API access & workflow PRs).
  - `GITHUB_REPOSITORY` (repo auto-detection fallback).
  - `HISTORIAN_ENABLE_JIRA`, `HISTORIAN_JIRA_REGEX` (optional Jira enrichment).
  - AWS credentials (`AWS_ACCESS_KEY_ID`/`AWS_SECRET_ACCESS_KEY`/`AWS_SESSION_TOKEN`/`AWS_DEFAULT_REGION`) when S3 scanning is enabled.
- Configuration: `config/defaults.yml` drives collectors (Projects v2, marker scanning, artifact sources, mirroring).
- Templates: `docs/history/HISTORY_TEMPLATE.md` used when `--template` not provided.
- Workflow automation: `.github/workflows/weekly-history.yml` schedules weekly snapshots and opens PRs when Markdown or context index changes.

### Feature Map

| Feature | Status | Implementation Notes |
| --- | --- | --- |
| GitHub Projects v2 | ✅ Enabled via `config.defaults` (`project_v2.enabled: true`); requires `ProjectsV2Client` (missing locally). |
| Marker parsing (Decision/Action/Note/Blocker) | ✅ `_collect_notes_section` + `_extract_comment_markers`; configurable markers. |
| Artifact aggregation | ✅ GitHub Actions + optional S3 via `_collect_github_actions_artifacts` / `_collect_s3_artifacts`. |
| Jira parsing | ✅ `_collect_jira_references`; gated by env vars. |
| History index writer | ✅ `_ensure_history_index` writes `docs/context/context-index.json`. |

## Proposed Mapping

- `scripts/generate_history.py` → `src/contextledger/cli.py` (then split into `collectors/`, `outputs/`, `renderers/`).
- `docs/history/**` → `examples/history/**`.
- `docs/context/**` → `examples/history/context/**`.
- `config/defaults.yml` → `config/defaults.yml` (unchanged, ensure package data inclusion).
- `.github/workflows/weekly-history.yml` → `.github/workflows/weekly-history.yml` (update module paths after move).
- `templates/**` → `templates/**` (create dedicated directory; migrate `HISTORY_TEMPLATE.md`).

## Risks & Recommendations

- **Missing dependency**: `scripts.github.ProjectsV2Client` is not present; port or re-implement GraphQL client before moving the CLI.
- **Token scopes & rate limits**: Projects v2 and artifact APIs require `repo`/`project` scopes; add exponential backoff and caching when refactoring.
- **S3 credentials**: Guard optional boto3 usage and clarify AWS credential requirements in documentation.
- **Index consistency**: `_ensure_history_index` rewrites chronological history; ensure new package layout preserves relative paths used in workflows.
- **Template relocation**: Creating `templates/` may require workflow updates to reference new path.

## Next Steps

- [ ] Run the "Move & Refactor" prompt using the Proposed Mapping above to migrate Historian assets into the `contextledger` package layout.
- [ ] Recreate or stub `ProjectsV2Client` within the new package (e.g., `contextledger/github/projects.py`).
- [ ] Update automation/workflows to import the relocated CLI entry point.
- [ ] Re-test GitHub Actions workflow with dry-run to confirm artifact/index generation.

Once the Move & Refactor prompt completes, proceed with integration testing (CI workflow + manual CLI run) to validate the new structure.
