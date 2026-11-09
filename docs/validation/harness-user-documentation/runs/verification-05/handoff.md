# Coordinated delivery handoff

Change: harness-user-documentation. Approved Proposal/Requirements R2, Design R1, Tasks R1; only completion and validation bookkeeping changed. Retain the immutable content target `27735687a37e896cd6b0c95cd9d2d848ee166d90`; no release or installed provider is changed.

The Harness PR is https://github.com/versat-labs/versat-ai-harness/pull/33. The organization PR is https://github.com/versat-labs/.github/pull/3 at candidate commit `1b6a0a127c85e2c928f4437423be5aaa6f72ae30`. Both are currently drafts and unmerged; the organization candidate still matches the approved snapshot and its clean checkout. No new organization edit is needed. Actual remote review/check/merge outcomes remain separate from local documentary readiness.

Integrate Harness first after its mandatory human review and final required CI; integrate the organization routing second under that repository's review and checks. Until those merges, report organization consolidation as prepared, not activated. Existing organization main entry remains the route in use. Rollback restores the original/verified organization contribution entry first, then reverts affected Harness prose if needed. Original snapshots and earlier missing-target observations remain retained.

## Prepared Harness PR summary (Spanish)

La documentación de uso del Harness está disponible en inglés, portugués y español. Se verificaron 39 páginas, 21 enlaces entre repositorios y vistas renderizadas de README, inicio rápido, preparación, producto y contribución en los tres idiomas. El recorrido local verifica el proveedor exacto, los artefactos de planificación y la detención en Gate 1; no representa una evaluación independiente de otro agente.

Cambio SDD: harness-user-documentation; archivo preparado en specs/archive/harness-user-documentation/. Evidencias actuales en docs/validation/harness-user-documentation/runs/verification-05/. El comando completo posterior al traslado, con baseline y --require-archive, aprobó 131 pruebas de validadores y 48 de ejecución. El preflight de entrega aprobó cinco checks y 46 evaluaciones, sin hallazgos abiertos ni resultados obsoletos. Relacionado con https://github.com/versat-labs/versat-ai-harness/issues/22 y coordinado con https://github.com/versat-labs/.github/pull/3.

La revisión humana del PR, los checks remotos finales y el merge siguen siendo pasos separados. Integrar primero Harness y después la organización. No se publican releases ni se actualizan consumidores. Los videos internos siguen siendo referencias complementarias no revisadas.

## Prepared organization PR summary (Spanish)

La contribución pública conserva las rutas para reportar problemas, la precedencia de cada repositorio y la información propia de la organización. Las instrucciones internas detalladas apuntan al commit inmutable 27735687a37e896cd6b0c95cd9d2d848ee166d90 del Harness, con enlaces localizados y acceso privado indicado. README y CONTRIBUTING se mantienen alineados en inglés, portugués y español; perfil y formularios permanecen sin cambios.

Los archivos candidatos coinciden con el snapshot revisado, sus enlaces y vistas Markdown fueron verificados y git diff --check no encontró errores. No hay aplicación ni suite de build propia en este repositorio. Cambio gobernado por https://github.com/versat-labs/versat-ai-harness/pull/33 e Issue 22. Mantener pendiente la activación hasta integrar Harness y completar la revisión/checks propios; restaurar una entrada verificada antes de retirar destinos si se necesita rollback.

## Observed local checks

The complete package preclosure command passed: 131 validator tests and 48 execution tests. Harness and organization git diff --check passed. All five check results and all 46 acceptance/regression assessments are current. The final move/preflight output is recorded separately; remote CI and human review are not inferred from these local results.

The post-move full package command with trusted baseline 5fa618aed07703c8181f4f753ca6aac393551089 and --require-archive passed (package-validation.txt). The unique archived dossier has closure: prepared, with Proposal, Requirements and Design unchanged byte-for-byte and the Tasks approval/plan digest preserved. The developer also confirmed the selected Codex folder manually in this chat.
