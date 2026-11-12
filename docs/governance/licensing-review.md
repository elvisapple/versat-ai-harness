# H01 licensing review ledger

Private, non-sensitive record · Observed 2026-11-10 · Owner: @elviszoz.
Policy/terms are private implementation candidates, not adopted/released artifacts.

## Baseline and scope

The connected repository and local approved provider still identify `597b81c71a0fc0908ff5264fe9987bb5c0d8feec`; no source drift was found in that comparison. VERSION and manifests remain 0.3.0; marketplace remains v0.3.0. No installed consumer reference changed. The baseline has 1,040 tracked files; this is not a full export/history or rights audit.

The [notices inventory](../licensing/harness-plugin-notices.md) separates observed direct dependency metadata from unverified rights, transitive/distribution scope and copied material. Confidential contracts, personal data and legal analysis are not stored here. The owner subsequently attested first-party creation for Versat E.A.S.; see [technical review](../licensing/technical-review/README.md). No unseen contract is asserted.

## Roles and decisions

| Input | Evidence/status | Next action |
|---|---|---|
| Declared holder | User named Versat E.A.S. and confirmed he produced all reviewed first-party material for it; bounded source inventory complete. | Owner attestation and technical inventory recorded; no further first-party input gap identified in this scope. |
| Executor and accountable licensing/security contact | User appointed @elviszoz. | Coordinate explicit decisions and reviewer capacity. |
| Technical review | CODEOWNERS: @elviszoz and @evertonspohrversat. | Actual review remains pending; no reviewer notification was sent. |
| D01 — installation/use/modification/redistribution | Owner decided: free official Codex plugin installation/use by internal/external people only to guide contributions to other Versat Labs repositories, public or private; modification only by Versat team developers with source access; no user redistribution, commercialization or forks. | Draft-0.2 reflects the decision. H03 must resolve official distribution mechanics without silently granting user redistribution. |
| D02 — legal identity/authority | Owner declared Paraguay and Elvis Luis Zoz (@elviszoz) as company approver. | Record as owner-supplied facts, not independent corporate verification or a governing-law choice. |
| D03 — rights and notices | Bounded source inventory, owner provenance attestation and seven installed dependency license texts reviewed. | Complete for this private source candidate. H03 reviews the actual future exported/bundled surface separately. |
| D04 — approve actual text | Approved by Elvis Luis Zoz on 2026-11-10: “H01 revisado e aprovado.” | Complete for the presented wording; see [approval record](h01-approval.md). D03 evidence is separate. |

Actual approval is recorded in [H01 approval](h01-approval.md), with reviewed/current hashes and administrative-only status changes. No effective date or publication is introduced.

## Per-product adoption

| Product / executor | Selected model | Current disposition and unverified scope |
|---|---|---|
| Harness/plugin — H01/H02/H03 | Proprietary, private source; public plugin distribution intended separately. | `defer` for any new terms/distribution clearance: D01–D04 documentary evidence recorded; actual full export/distribution scope remains H03 work. Existing access is not expanded. |
| Platform — P01/P02 | Apache-2.0 intended. | `defer`: product-specific rights/dependencies, license/notices, export and adoption evidence pending. |
| Workspace — P01/P02 | Apache-2.0 intended. | `defer`: its own evidence and publication remain separate from Platform. |
| Discover — P03 | Private/proprietary. | `retain-private` reflects the selected model only; concrete terms, grants, authorized distribution and P02 integration remain unverified. |
| CRM — P03 | Private/proprietary. | Same model boundary, with its own unverified terms, rights, distribution and integration. |

These rows are not a license change, public export clearance, adoption result or completed product handoff. No SDK repository is introduced.

## Synthetic decision walkthroughs

Illustrative cases, not real product evidence:

| Input | Expected disposition | Evidence/recovery |
|---|---|---|
| Apache component with complete compatible rights, notices, full export review and identified approvals | `publish` recommendation for that exact surface only | Separate operational authorization/executor still required. |
| Owner elects private proprietary component with known private access scope | `retain-private` | Record scope and authority; do not imply unrelated rights are cleared. |
| Missing contributor grant | `defer` | Owner obtains/verifies grant; no acceptance inferred from a commit. |
| Incompatible dependency combination | `defer` | Technical/licensing owner resolves actual combination or changes scope through review. |
| Secret present in history but absent from current tree | `defer` | Security owner remediates and re-reviews actual export surface. |
| Missing actual licensing reviewer/authority | `defer` | Establish actual authority/review rather than use CODEOWNERS as legal approval. |
| Required remote control not verified | `defer` | Administrator verifies actual control; no protection claim from local tests. |

## Handoff and recovery

H02 may reference the approved candidate and its exact review record; approval does not make the terms effective or prove missing third-party rights. H03 must resolve complete root-package export and distribution independently. P01/P03 each own actual terms and adoption; P02 owns integration runtime.

If terms/evidence changes, invalidate affected acceptance and obtain fresh review. Preserve non-sensitive decision history. Actual confidential sources must be inspected by authorized reviewers without copying them into this package.

## Owner decision source — 2026-11-10

The owner answered the drafting questions in this chat. Exact source excerpts:

> Como se trata de um repositório interno/privado da Versat, a modificação está permitida somente à equipe Versat, cujos desenvolvedores possuem acesso ao repositorio, mas nenhum deles e ninguém está permitido a redistribuir, comercializar ou fazer fork. No entanto, estará disponível como plugin de skills do Codex para que qualquer pessoa (interna ou externa) possa instalá-lo e utilizá-lo, sem custo, para orientações e guia de padrões internos da Versat ao contribuir em algum outro repositório da organization Versat Labs no Github, seja público ou privado.

> País: Paraguay; Quem pode aprovar: Elvis Luis Zoz (ou @elviszoz).

These are drafting inputs, not approval of a subsequently generated candidate. Public installation does not make the plugin open source or the private source public. Official owner distribution is distinguished from prohibited user redistribution; H03 must review any delivery-specific permission need.

Current reviewable text: `docs/licensing/harness-plugin-terms.md`, draft-0.2, SHA-256 `ba84ea407a9402c2e653bb4450ca79e0e9032582bf5c0283e16b3b45a3ddbb2c`. This identifies the frozen reviewed text; actual approval and the status-only current hash are recorded in [H01 approval](h01-approval.md).

## Technical review completed — 2026-11-10

Owner quote: “Sim, tudo foi produzido por mim para a Versat E.A.S.” This answers the specific question about Harness/bootstrap/templates/documentation and organization source provenance and company licensing authority. The [source/dependency review](../licensing/technical-review/README.md) and [reviewed notices](../licensing/harness-plugin-notices.md) resolve the first-party drafting gap. No user decision remains pending for the current H01 wording/source review. Effective application and actual exported/bundled artifact clearance remain outside this phase.
