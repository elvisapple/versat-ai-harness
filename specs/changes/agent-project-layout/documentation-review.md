# Documentation review

Reviewed the repository's Markdown documentation, structured template/configuration files and existing enforcement entry points for the consumer artifact change. This review concerns architecture, terminology, paths, composition and readiness claims; it is not verification of external services or workspace installation.

| Area | Result |
|---|---|
| Root README, AGENTS and architecture overview | Separate Plugin packaging from consumer capabilities, native Codex agents and operational workflows. |
| Standards and index | Add one canonical artifact contract to core resolution; clarify agent/hybrid responsibilities and English technical workflow definitions. Other core, domain and technology rules remain applicable without duplication. |
| Project templates and bootstrap documentation | Replace root consumer directories, add the generated architecture guide, document overlay semantics and provide opt-in authoring templates and a non-executable finance example. |
| Bootstrap, audit, maintenance and architecture-review Skills | Point to resolved contracts and version-matched composition guidance; distinguish package validation from consumer readiness. No parallel policy list is introduced. |
| Plugin role documents | Add a directory explanation and clarify the orchestrator's scope. Architect and reviewer responsibilities remain applicable. |
| SDD process, templates, schemas and procedures | Explain the operational/lifecycle distinction in the process. Existing lifecycle steps and metadata schemas need no path migration. The versat-sdd Skill already resolves the canonical process. |
| ADRs and historical SDD changes | Add ADR-0012 and this active change; preserve accepted/historical decisions and evidence. Root paths in ADR-0011 continue to describe the Plugin correctly. |
| Validator and test documentation | Clarify project and Plugin validation boundaries. Existing architecture, security, Standards, SDD and test contracts remain valid; no claim of a new consumer validator is made. |
| Release guidance, manifests and marketplace | Keep exact version references and package paths unchanged. No release or consumer migration is performed. |
| Resources, company context and base README | Remain non-normative knowledge or project-purpose placeholders; no structural adaptation needed. |
| CI, PR template and CODEOWNERS | Existing validation entry point and PR gates remain valid. Replace obsolete `/plugin/` ownership with current Skills, roles and template paths so these changes select architecture review. |

## Acceptance review

- Agent and hybrid composition now produces the consumer directories, preserves the shared base and leaves illustrative named artifacts inactive.
- All profiles resolve the artifact contract; only projects using those artifacts incur the corresponding obligations.
- Workflows explicitly declare an executor and dependency bindings. Their presence does not imply automatic discovery, connector readiness or deterministic execution.
- The supplier-payment example covers invoice and non-invoice branches, uncertain classification, unavailable capabilities, authorization, duplicate lookup and recovery after ERP or Drive writes. It prepares invoice records and attachments without claiming payment execution.
- Technical artifact names use English and `SKILL.md` retains Codex-compatible casing.
- Existing consumers require classification, conversion where needed, exact-version adoption and behavior verification. Plugin exports and application code are not blindly relocated.

## Limits

Codex loading of a concrete consumer agent, live Gmail/ERP/Drive integrations, finance outcomes, remote required checks and human policy approval were not exercised. The example's three dependency Skills are deliberately not implemented by this change. The Harness currently has no automated consumer composer or workflow engine.
