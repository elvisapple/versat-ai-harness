# Default ownership validation

The approved local dossier repairs PR #36's missing SDD record. CODEOWNERS itself already contains the approved fallback; it required no further edit.

## Attempts

The original remote run failed with ARCHIVE_SELECTION while all 179 tests passed. An initial local review attempt failed an assertion expecting 13 rules. Direct inspection established 12 rules. Proposal/Requirements revision 2, Design revision 3 and Tasks revision 3 were subsequently reviewed and approved in chat. The final bounded ownership review and full suite passed; their matching input snapshots are recorded in snapshots.json.

## Scope and limitations

The concrete ownership paths and unchanged rule list are recorded in ownership.txt. Approval quote and fingerprint review plus the full suite are recorded in suite.txt. This evidence does not prove GitHub permissions, remote required-check enforcement, merge or deployment. The final submission preflight is recorded separately after the documentary archive move. At the initial local preparation stage, nothing had been pushed or posted.

## Final preflight

Selected delivery passed before and after archive preparation. The full package submission command with baseline 597b81c71a0fc0908ff5264fe9987bb5c0d8feec and --require-archive passed after the move, including 131 validator and 48 execution tests. See submission.txt. The dossier is prepared locally; this initial statement preceded publication; the subsequent remote attempt and correction are recorded below.

## Remote attempt and correction

[Run 42905157716](https://github.com/versat-labs/versat-ai-harness/actions/runs/42905157716) on f79328f4ce3abe005702b020341a7c841a0da1d8 passed all 179 tests but rejected CHECK-002 with INPUT_STALE. The local ignored sdd/.DS_Store file was included in its broad input scope and absent from Git. Its contents were preserved outside the repository. Fresh package and test suite runs passed; the current snapshot matches an independent clean Git clone. Original evidence is retained under attempt-01. New execution evidence is in rerun-suites.txt and rerun-snapshots.json. No policy or input exclusions changed.
