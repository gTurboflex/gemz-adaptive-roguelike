# GEMZ-6 prototype walkthrough вЂ” Zhangir

Initial verification checklist. Inspection, execution and findings must be recorded by Sailaubek Zhangir (GitHub ynagi-1, YouTrack Zhangir). This template contains no completed test claims.

Date: Pending
Browser/version: Pending
Commit tested: Pending

| Scenario | Expected | Actual result / finding | Status |
|---|---|---|---|
| Prepare | Easy/Hard and experiment mode can be chosen before start | Pending | Not run |
| Enter | Chamber 1 starts; difficulty and mode lock | Pending | Not run |
| Mine | First mining adds 12 Gemz and prevents duplicate mining | Pending | Not run |
| Preview | One bounded update and an explanatory notice are shown | Pending | Not run |
| Descend | Next chamber permits another mining action | Pending | Not run |
| Extract | Summary matches collected Gemz and depth | Pending | Not run |
| Reset | Scenario returns to initial state | Pending | Not run |
| Static control | Budget remains neutral | Pending | Not run |

## Findings and revisions

Pending. Record real inconsistencies, resulting changes and commit/PR links. Separate observed behaviour from assumptions. Do not mark GEMZ-6 Done until its acceptance criteria are checked.

### Preparation and source inspection — 22 October 2026

Agent-assisted preparation only. The browser tool blocked navigation to the local file URL; no interactive browser walkthrough was completed. All scenario rows above remain Not run. Date/browser/commit fields above refer to a future actual walkthrough, not to this source inspection.

- The original HTML SHA256 is ee25efcc6ea29fa0b93c5907c83e073c114fffcbd9faca9f5f9c28c0068ea0ff. No changes have been made to it in this preparation.
- Source inspection: mine adds 12 Gemz and disables repeat mining; preview advances EAS by at most 0.10 per simulated update; static mode targets EAS=1; descent resets mining availability. These are code observations, not observed browser results.
- Open check: at chamber 5, preview is still available but Descend is disabled. Check whether the next-encounter wording confuses a participant at maximum depth.
- Both profile and rules modes use simulated manual style selection. They do not demonstrate classifier inference, distinct profiling algorithms or measured telemetry.
- Actual offline browser execution, Easy/Hard, reset, all scenario rows and 720p/1080p readability remain pending. The source footer's original date has been preserved.

The separate PR #2 reference-controller review originally found a fallback discrepancy. Agent-assisted re-verification on 22 October 2026 at commit 71789680b7128e6aeb74c99e69ef25bf8199a96e confirmed the fix: all 13 controller tests and the materials check pass. An additional check covered Easy/Hard, rules/profile, stale/invalid/worker error, repeated updates while fallback is active, stale recovery rejection and fresh valid recovery at age 10 seconds. EAS remains 1 until explicit valid recovery and can then grow only at a safe boundary with the capped step. This verifies the Python reference controller only and does not complete any browser scenario above.

The ZIP has already been extracted locally. The requested ordinary Chrome walkthrough was not completed: the earlier local-file navigation restriction still applies to the available browser automation. No alternate opening method was used to bypass it. All eight browser scenarios remain Not run; no browser version or execution date is claimed. The prepared files have not been uploaded to GitHub; their import waits for Yergun to merge PR #2 into main.

## Limitations

This HTML file is an offline scenario mock-up with simulated inputs. It is not Unity gameplay, measured telemetry or a trained classifier. Review architecture/requirements for consistency and report discrepancies rather than claiming validation.
