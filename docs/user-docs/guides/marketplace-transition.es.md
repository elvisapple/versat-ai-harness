# Transición del marketplace

[English](marketplace-transition.md) | [Português](marketplace-transition.pt.md) | [Español](marketplace-transition.es.md)

La candidata local 0.4.0 cambia el catálogo a `versat` / `Versat Plugins`. El plugin sigue siendo `versat-ai-harness`; la clave local prevista es `versat-ai-harness@versat`. La clave anterior `versat-ai-harness@versat-internal` no es un alias automático. Preparar el código no equivale a integración, release o instalación. La etiqueta exacta `v0.4.0` seguía ausente el 19/11/2026.

## Entrega del código en el alcance aprobado

El propietario informa que solo Elvis y Everton usan el Harness, que el catálogo administrado sigue `main` y que ambos reinstalarán manualmente después. Es un alcance informado, no una auditoría de miembros ni un resultado de instalación individual. La decisión aprobada no exige fijación/pausa previa del workspace ni ensayo nativo desechable antes de entregar el código. La sincronización puede exponer el catálogo modificado antes de reinstalar, causar interrupción temporal o requerir reparación manual. Source/Path/sync e IDs administrados siguen sin verificar. Si aparece otro usuario afectado, detenga la activación y reevalúe el alcance.

La aceptación del código exige comprobaciones deterministas del paquete, suites mantenidas completas y documentación fiel. La integración futura sigue exigiendo CI exitosa y aprobación elegible de CODEOWNER distinto del autor, sobre la revisión efectiva de la PR. Revise los cambios desde la base registrada antes de presentar el código. La aceptación local no exime esos controles. Etiqueta/release exige autorización separada; compruebe nuevamente v0.4.0 y nunca reescriba una etiqueta existente.

## Reinstalación manual posterior

Lea [configuración del workspace](workspace-setup.es.md) y [notas de la candidata](../../releases/0.4.0-candidate.es.md). Elvis y Everton realizarán sus propias reinstalaciones después. Esta preparación no instala, modifica el workspace ni migra consumidores.

1. Registre la referencia del catálogo por separado de la referencia exacta del paquete, identidad/versión, proveedor efectivo y lock/snapshots compatibles del proyecto. Conserve rutas privadas e IDs administrados en evidencia restringida, sin credenciales. Las observaciones anteriores de 0.4.0 personal y 0.3.0 en caché administrada no demuestran el proveedor efectivo de una sesión nueva.
2. Compruebe un paquete exacto disponible y soportado y sus recursos canónicos antes de instalar. Un catálogo que selecciona una etiqueta ausente no basta; main seleccionando v0.4.0 todavía no publicada no es un par de recuperación verificado. Conserve un registro compatible de origen/paquete/proyecto. Nunca seleccione `latest` silenciosamente ni reduzca SDD v3 activo a un proveedor incompatible.
3. Compruebe los controles/ayuda soportados del cliente instalado para registro, selección de identidad y recuperación. Comandos de transición, registro con la misma URL Git, colisiones y continuidad de identidad administrada siguen sin verificar. Los comandos históricos no son instrucciones actuales. Deténgase si la ruta necesaria no está soportada o requiere administrador; delimite esa acción concreta por separado.
4. Después de reinstalar realmente, registre identidad y versión exactas devueltas y confirme un único proveedor efectivo previsto. En un proyecto sintético, pida a ese proveedor localizar las cinco Skills y sus recursos canónicos correspondientes; después use `versat-sdd` para preparar una pequeña Proposal/Requirements sin implementación. Resultado esperado: borrador del proveedor correspondiente, detenido en su gate de planificación, o un prerrequisito/fallo explícito. Esta acción representativa no se ejecutó aquí.
5. Registre por separado los resultados de Elvis y Everton: identidad, versión exacta, proveedor/recursos efectivos, resultado de la Skill y error/recuperación. La aceptación del código o el resultado de una persona no demuestra el éxito de la otra.

## Fallo y recuperación

Ante referencia ausente, colisión, proveedores ambiguos, recursos faltantes o runtime incompatible, detenga la instalación afectada. Conserve o vuelva a seleccionar un par proveedor/proyecto compatible verificado mediante controles soportados; registre recuperación o fallo sin resolver. Si no hay recuperación compatible verificada, mantenga el pendiente. No renombre cachés, edite bases de instalación, copie credenciales, cambie locks como efecto secundario ni use `pluginId` o eliminación/reimportación como solución genérica.

Cambios de importación/ref/política del workspace, eliminación administrada e instalaciones automatizadas necesitan autoridad propia. La identidad local no demuestra recursos compartidos, roles o continuidad de IDs administrados. La limpieza anterior es opcional y posterior, bajo autoridad del propietario/admin, tras comprobar dependencias y recuperación; eliminar un marketplace solo para renombrarlo no forma parte de este handoff.

## Observaciones diferidas

El [registro pendiente](../../validation/harness-marketplace-transition/inputs/transition-r2.json) mantiene siete escenarios nativos sin verificar: descubrimiento/recursos nuevos; instalación anterior conservada; misma URL Git; colisión de nombres; dos proveedores/uno efectivo; referencia exacta ausente; recuperación del fallo. La reinstalación posterior registra solo escenarios realmente observados, sin exigir simular los siete antes de entregar el código. No se provisiona VM, contenedor ni cuenta de prueba; los fixtures desechables verifican rutas del paquete, no aislamiento de seguridad ni ejecución nativa.

Fork/CI externo, recepción/confidencialidad de reportes privados e instalación/actualización/recuperación nativa externa siguen pendientes independientemente. Validación local, archivo documental y merge no cierran esas observaciones.
