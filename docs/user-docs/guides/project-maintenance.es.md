# Mantener un proyecto existente

[English](project-maintenance.md) | [Português](project-maintenance.pt.md) | [Español](project-maintenance.es.md)

Usa mantenimiento para actualizaciones o desviaciones en un repositorio existente. Proporciona identidad/lockfile actual, release destino explícita, adaptaciones locales y comandos de validación mantenidos.

## Pruébalo

Solicitud ilustrativa; reemplaza el ID o proporciona los datos reales del proyecto:

```text
Usa $project-maintenance para comparar este repositorio con la release destino exacta del Harness que proporcioné. Conserva los cambios locales, presenta conflictos de migración y un plan de rollback, y no publiques cambios remotos.
```

## Resultado esperado

Espera un diff revisable de snapshots de Standards, plantillas, referencias de capacidades y metadatos. Clasifica los artefactos del consumidor antes de moverlos. Conserva wrappers y pruebas propios. Valida con el proveedor destino; registra la versión exacta adoptada y los resultados de integración.

## Recuperación y límites

Si no se proporcionó un destino, resuélvelo antes de cambiar pins; nunca uses latest. Expón los conflictos en lugar de sobrescribirlos. Revierte configuración y referencias del proveedor juntas y ejecuta la suite original restaurada.

## Referencias

- [Skill (inglés)](../../../skills/project-maintenance/SKILL.md)
- [Changelog (inglés)](../../../CHANGELOG.md)
- [Migration (inglés)](../../../project-templates/README.md)

[Inicio rápido](../quickstart.es.md) · [Harness](../../../README.es.md)
