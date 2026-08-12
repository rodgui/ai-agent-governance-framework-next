# Source baseline

## Authoritative migration snapshot

| Field | Value |
|---|---|
| GitHub repository | <https://github.com/rodgui/ai-agent-governance-framework> |
| Remote default branch | `main` |
| Authoritative commit | `5545d9227624400ab8bb707b6032b2f61329a36e` |
| Selection | Rodgui explicitly selected GitHub/main after the protected local copy and GitHub were found at different commits. |
| Working snapshot | `/Users/rodgui/.hermes/workspaces/ai-agent-governance-rebuild/source-snapshot` |
| Tracked files | 216 |
| Aggregate tracked-content manifest SHA-256 | `18f6803b7e9404a396f8d9202149c508097af914f26552c538ca964ef7e05063` |
| Snapshot status | clean |
| Recorded at | `2026-08-11T20:16:34-03:00` |

The authoritative snapshot was obtained in a separate clone. The protected local repository was not fetched, pulled, checked out or otherwise modified.

## Protected local repository

| Field | Value |
|---|---|
| Path | `/Users/rodgui/Nox/Projects/ai-agent-governance-framework` |
| Baseline commit | `a1a91ba5675f6e0261b86e2991f2093c59fda276` |
| Tracked files | 199 |
| Aggregate tracked-content manifest SHA-256 | `b08b03c5002abed3e2bebdf691e1e729eb4b01375a6e65a61c681871205c507f` |
| Baseline status | clean |

The protected local commit differs from the selected authoritative remote commit. It is retained only as an immutable local checkout and is not the migration authority.

## Evidence files

- `source-manifest.csv`: file metadata for every tracked file in the authoritative snapshot.
- `source-manifest.sha256`: per-file SHA-256 manifest for the authoritative snapshot.
- `protected-local-manifest.sha256`: per-file SHA-256 manifest for the protected local checkout.
- `source-baseline.json`: machine-readable authoritative baseline.
- `protected-local-baseline.json`: machine-readable protected-local baseline.
- `github-releases.json`: releases visible at baseline.
- `git-tags.txt` and `git-history-name-status.txt`: tag and history evidence.

## Final immutability check

The final validation must independently recalculate both manifests and compare commit, branch, tags and `git status --porcelain` with this baseline. Any difference is a stop condition and must be reported rather than repaired silently.
