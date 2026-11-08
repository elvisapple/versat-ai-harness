# SDD con Codex

[English](sdd-with-codex.md) | [Português](sdd-with-codex.pt.md) | [Español](sdd-with-codex.es.md)

Usa esta ruta para convertir una historia en especificaciones revisadas y retomar el trabajo entre chats. Comienza con un repositorio preparado, sus instrucciones, una issue real cuando exista y la versión seleccionada del Harness.

## Pruébalo

Solicitud ilustrativa; reemplaza el ID o proporciona los datos reales del proyecto:

```text
Usa $versat-sdd para inspeccionar el cambio <change-id> e informar su fase, aprobaciones, bloqueos y próxima acción permitida. No modifiques archivos.
```

## Resultado esperado

El informe identifica el mismo expediente y la evidencia de cada aprobación. En una planificación nueva, espera primero Proposal/Requirements; Design y Tasks siguen después de las aprobaciones correspondientes. Tras revisar Tasks, solicita explícitamente la implementación. Para pedir correcciones junto con validación, inclúyelo en la solicitud.

## Recuperación y límites

Si falta evidencia de revisión, revisa la versión presentada en lugar de recrear aprobaciones. Un requisito modificado reabre los gates afectados. Al retomar, conserva el ID del cambio; su ubicación en archivo no demuestra entrega.

## Referencias

- [SDD (inglés)](../../../sdd/README.md)
- [Process (inglés)](../../../sdd/process.md)
- [Metadata (inglés)](../../../sdd/metadata.md)

[Grabación del equipo](https://versat.slack.com/files/U04PSSJ2W/F0CF8AH2SVC/pantalla_compartida_-_2026-11-05_16_09_27.mp4) — requiere acceso a Slack. Capacitación complementaria; el contenido del video no fue verificado para esta guía. Los pasos escritos permiten continuar.

[Inicio rápido](../quickstart.es.md) · [Harness](../../../README.es.md)
