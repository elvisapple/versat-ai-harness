# Auditar un proyecto

[English](project-audit.md) | [Português](project-audit.pt.md) | [Español](project-audit.es.md)

Usa una auditoría para evaluar cumplimiento, preparación o desviaciones. Prepara instrucciones, .versat/project.yaml, .versat/standards.lock, especificaciones activas y el proveedor seleccionado. Es más amplio que una revisión de código habitual.

## Pruébalo

Solicitud ilustrativa; reemplaza el ID o proporciona los datos reales del proyecto:

```text
Usa $project-audit para evaluar este repositorio según su perfil declarado y los Standards resueltos. Informa evidencia, gravedad y opciones de corrección. No modifiques archivos.
```

## Resultado esperado

Espera hallazgos que distingan cumplimiento verificado, incumplimiento y verificación no disponible, con contratos afectados y próximos pasos concretos. La validación determinista aporta evidencia limitada; la revisión cualitativa también considera seguridad, pruebas/evals, documentación, operaciones y perfil/criticidad.

## Recuperación y límites

La identidad o el contexto del proveedor faltantes son vacíos explícitos, no evidencia de cumplimiento. Pedir una auditoría no autoriza corregir. Usa mantenimiento o un cambio SDD para tratar hallazgos aprobados.

## Referencias

- [Skill (inglés)](../../../skills/project-audit/SKILL.md)
- [Standards index (inglés)](../../../standards/index.yaml)
- [Validators (inglés)](../../../validators/README.md)

[Inicio rápido](../quickstart.es.md) · [Harness](../../../README.es.md)
