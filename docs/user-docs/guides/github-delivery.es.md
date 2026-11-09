# Entrega mediante GitHub

[English](github-delivery.md) | [Português](github-delivery.pt.md) | [Español](github-delivery.es.md)

Usa esta guía al preparar un cambio vinculado a una issue para revisión humana. Necesitas la URL real de la issue, instrucciones del repositorio, alcance aprobado y entorno de validación del proyecto.

## Pruébalo

Solicitud ilustrativa; reemplaza el ID o proporciona los datos reales del proyecto:

```text
Usa $versat-sdd para inspeccionar <change-id>, preparar el resumen de entrega e identificar prerrequisitos de archivo o validación faltantes. No publiques un PR ni hagas merge.
```

## Resultado esperado

Trabaja en una rama según la convención Git resuelta. Mantén trazabilidad entre issue, requisitos y commits; no inventes un ID de Shortcut. La planificación o el trabajo incompleto se revisan en un PR draft. Antes de presentar la implementación completa, prepara el archivo documental en la misma rama y supera el preflight de archivo seleccionado. Solicita explícitamente la publicación del PR; después obtén revisión humana y CI obligatorio final antes del merge.

## Recuperación y límites

Informa en el PR las verificaciones fallidas o no disponibles. Los comentarios de revisión permanecen con el mismo ID; los cambios de alcance reabren la revisión correspondiente. Verifica el merge real por separado de la preparación local. Un merge no publica una release ni actualiza consumidores instalados.

## Referencias

- [Git (inglés)](../../../standards/core/git.md)
- [SDD (inglés)](../../../sdd/README.md)
- [SDD validation (inglés)](../../../validators/sdd/README.md)

[Grabación del equipo](https://versat.slack.com/archives/C0B7G255DPY/p1793910356829109) — requiere acceso a Slack. Capacitación complementaria; el contenido del video no fue verificado para esta guía. Los pasos escritos permiten continuar.

[Inicio rápido](../quickstart.es.md) · [Harness](../../../README.es.md)
