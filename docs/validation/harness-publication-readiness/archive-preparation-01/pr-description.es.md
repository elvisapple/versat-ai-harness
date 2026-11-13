# Preparar el candidato privado de distribución del Harness

La guía anterior asumía acceso interno y términos propietarios. Esta preparación incorpora el candidato Apache R1 aprobado, instrucciones EN/PT/ES de contribución, reporte e instalación, un parche de adopción separado y un plan operativo con evidencia restringida. La licencia raíz y la versión fuente siguen sin cambiar.

Validación local: diez verificaciones, 38 escenarios y 72 obligaciones retenidas; 179 pruebas en cada raíz; instalación individual y seis casos reales de primer uso, fallo, migración sintética y recuperación. Los intentos fallidos anteriores se conservan.

La publicación sigue aplazada por historial confidencial, evidencia inaccesible y verificaciones operativas pendientes. No se solicita aquí adoptar la licencia, publicar, cambiar visibilidad o migrar consumidores. Este texto es una vista previa local, sin PR creado. Rama existente sin Story asociada; no se inventa identificador. Subject propuesto: `chore: prepare private Harness publication candidate`.

## Preparación documental de entrega

El dossier único está en `specs/archive/harness-publication-readiness/`, con `closure: prepared`. La revisión de implementación y la validación seleccionada `--phase delivery --require-archive` pasaron. Los tres digests de aprobación y los diez snapshots de entrada permanecen idénticos tras mover el dossier; no se modificó el plan aprobado ni se refrescaron resultados antiguos.

Las evidencias posteriores al movimiento están en `docs/validation/harness-publication-readiness/archive-preparation-01/`. Esta preparación documental no demuestra merge ni sustituye la revisión obligatoria y los checks remotos. El repositorio y la propuesta siguen privados; este archivo no crea ni publica un PR.

Validación posterior al archivo: suite completa con baseline y `--require-archive`, exit 0; 131 pruebas de validadores y 48 de ejecución. Advertencias históricas legacy/v2 conservadas.
