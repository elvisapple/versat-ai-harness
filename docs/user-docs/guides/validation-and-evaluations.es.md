# Validación y evaluaciones

[English](validation-and-evaluations.md) | [Português](validation-and-evaluations.pt.md) | [Español](validation-and-evaluations.es.md)

Elige la verificación según el repositorio y el resultado: consistencia del paquete Harness, suites de la aplicación consumidora o comportamiento supervisado de Skills. Prepara Python 3.11+ y las dependencias de validación del proveedor; las dependencias de la aplicación son independientes.

## Pruébalo

Solicitud ilustrativa; reemplaza el ID o proporciona los datos reales del proyecto:

```text
Usa $versat-sdd para validar <change-id> según el plan aprobado. Informa evidencia real y vacíos. No corrijas archivos del producto en esta solicitud de solo validación.
```

## Resultado esperado

En la raíz del Harness, ./scripts/validate/run.sh verifica paquete, registros SDD y regresiones mantenidas. No ejecuta pruebas de la aplicación de otro proyecto. La ejecución de consumidores y evaluación supervisada de las guías especializadas son capacidades de código fuente aún no publicadas: usa un proveedor exacto que las contenga y sigue los prerrequisitos de adopción. Suites obligatorias completas, ejecuciones dirigidas y observaciones supervisadas tienen límites de evidencia distintos.

## Recuperación y límites

Espera pass, fail o unable-to-verify con conteos/resultados reales y entradas probadas. Conserva intentos fallidos; falta de acceso, pruebas vacías u observaciones no disponibles no demuestran éxito. Evalúa cada obligación de aceptación y regresión; el éxito estructural no demuestra aceptación semántica, identidad humana ni merge remoto.

## Referencias

- [Project validation (inglés)](../../guides/project-validation.md)
- [Skill evaluations (inglés)](../../guides/skill-evaluations.md)
- [SDD validation (inglés)](../../../validators/sdd/README.md)

[Inicio rápido](../quickstart.es.md) · [Harness](../../../README.es.md)
