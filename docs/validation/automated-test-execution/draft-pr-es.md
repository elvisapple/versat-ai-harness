# Borrador: ejecutar pruebas y verificar las Skills con subagentes supervisados

Los proyectos que adoptan `.versat/validation.yaml` pueden ejecutar todas sus suites obligatorias, incluidas las regresiones existentes, con recuentos reales, límites de tiempo y evidencia SDD vinculada a las entradas probadas. Durante la implementación, el agente reutiliza cobertura suficiente y añade las pruebas que faltan; no se exige un archivo nuevo por cada cambio. Suites vacías, fallos y evidencia obsoleta impiden un resultado satisfactorio.

La solución revisada conserva CI determinista y utiliza seis escenarios de subagentes nativos con verificación independiente para el comportamiento crítico de `versat-sdd`. Se retiraron el adaptador CLI y el workflow privilegiado que aún no se habían publicado. No se requiere una API key específica ni infraestructura de evaluación aislada. Los subagentes comparten permisos de sesión; sus directorios no son un sandbox de seguridad.

## Validación local

- La suite completa mantiene 131 pruebas de validadores y añade 48 pruebas de ejecución, consumidores, CI y verificación supervisada.
- Los escenarios supervisados incluyen el primer gate, cobertura ausente, reutilización suficiente, regresión fallida, evidencia obsoleta y validación sin autorización para corregir. El coordinador inspecciona los artefactos y repite las pruebas, con mutaciones controladas en copias separadas.
- La primera adopción verifica éxito, fallo de regresión, requisito previo no disponible, preservación de comandos y rollback.
- Una regresión del ejecutor conserva la ruta del intérprete virtual al lanzarlo; resolver antes su enlace simbólico seleccionaba el Python base y perdía las dependencias del entorno.
- Resultados, límites y evaluación individual: [revisión actual](review-r2.md). Elegibilidad SDD local: [reporte](delivery-r2.json).

## Alcance y entrega

Cambio `automated-test-execution`, Proposal/Requirements R2, Design R3, Tasks R2 y ADR-0015. Rama `codex/automated-test-execution`; expediente preparado en `specs/archive/automated-test-execution/`, con `closure: prepared`. No se proporcionó una Story y no se inventó un identificador.

La adopción compone los artefactos sobre base, conserva pruebas propias y requiere una referencia exacta revisada al proveedor. El rollback restaura conjuntamente configuración, wrapper, CI y pin; después se ejecutan las suites anteriores. No hay actualización automática de consumidores o Marketplace.

El desarrollador autorizó el archivo documental, la publicación de la PR y la ejecución remota de CI. El expediente está preparado en esta misma rama; el preflight con `--require-archive` se verifica antes de publicar. CI remoto, reglas efectivas, revisión humana y merge se verifican posteriormente sobre la revisión presentada. La política y las Skills siguen sujetas a CODEOWNERS; una revisión local no acredita esos controles externos.
