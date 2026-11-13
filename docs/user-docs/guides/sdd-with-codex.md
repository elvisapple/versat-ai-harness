# SDD with Codex

[English](sdd-with-codex.md) | [Português](sdd-with-codex.pt.md) | [Español](sdd-with-codex.es.md)

Use this route to turn a story into reviewed specifications and resume work across chats. Start with a prepared repository, its instructions, a real issue when available and the selected Harness version.

## Try it

Example request; replace the change ID or supply the actual project inputs:

```text
Use $versat-sdd to inspect change <change-id> and report its current phase, approvals, blockers and next permitted action. Do not change files.
```

## Expected result

The report identifies the same change dossier and the evidence behind each approval. For new planning, expect Proposal/Requirements first, then Design and Tasks after their respective approvals. After reviewing Tasks, explicitly request implementation. To request fixes as well as validation, say so in the request.

## Recovery and limits

If review evidence is missing, review the presented revision rather than recreating approvals. A changed requirement reopens the affected gates. Keep the same change ID when resuming; never infer delivery from archive location.

## References

- [SDD (English)](../../../sdd/README.md)
- [Process (English)](../../../sdd/process.md)
- [Metadata (English)](../../../sdd/metadata.md)

[Quickstart](../quickstart.md) · [Harness](../../../README.md)
