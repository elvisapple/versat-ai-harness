# Contribuir con procedencia clara

[English](contributing.md) | [Português](contributing.pt.md) | [Español](contributing.es.md)

El repositorio del Harness es público. El material elegible creado por Versat está disponible bajo la [licencia Apache-2.0](../../../LICENSE) en la raíz del repositorio. El material de terceros conserva sus propios términos y [avisos](../../../THIRD-PARTY-NOTICES.md).

## Preparar y contribuir

1. Seleccione el repositorio real y lea README, AGENTS e instrucciones de contribución. Sus reglas prevalecen sobre los valores de la organización. Otros productos conservan términos y rutas independientes.
2. Seleccione una issue existente o formulario disponible de error, funcionalidad o mantenimiento. Describa necesidad, resultado esperado y reproducción cuando corresponda. No invente números de issue o Story.
3. Identifique material propio/de terceros, fuentes, versiones, permisos y avisos. Los derechos faltantes impiden aceptación. Lea [licencias](licensing.es.md); la licencia de la herramienta no determina términos del material independiente de destino.
4. Siga la [preparación](workspace-setup.es.md). En el checkout del Harness use Python 3.11+, instale `requirements-validation.txt` en un entorno virtual y ejecute `./scripts/validate/run.sh --quality-base origin/main` desde la raíz. En otros proyectos use sus verificaciones propias.
5. Para contribuir al Harness desde fuera de la organización, haga un fork del repositorio público, cree una rama en su fork y abra una pull request hacia la rama `main` del Harness. Siga la [convención Git](../../../standards/core/git.md). Es posible que un mantenedor deba aprobar la ejecución del workflow antes de que se inicie la CI. El acceso público permite leer el repositorio y hacer forks. La escritura, el merge y el release en el repositorio original requieren permisos propios.
6. Para cambios materiales, siga las [tres aprobaciones SDD](sdd-with-codex.es.md); solicite implementación explícitamente después de aprobar Tasks. Incluya documentación mantenida y verificaciones relevantes. Siga la [entrega](github-delivery.es.md) para archivo documental, revisión del PR y verificaciones finales, con autorización efectiva de operaciones remotas.

Resultado esperado: contribución revisable con referencias reales de issue/procedencia y verificaciones observadas. Declare verificaciones no disponibles; un resultado local no demuestra protección de ramas ni aceptación.

## Términos de contribución

La sección 5 de la [licencia Apache-2.0](../../../LICENSE) en la raíz del repositorio rige las contribuciones enviadas intencionalmente para inclusión, salvo indicación expresa en contrario, conforme a las definiciones de la licencia y cualquier acuerdo separado. Esta guía no agrega CLA, DCO ni cesión de propiedad intelectual. Para otros repositorios o versiones, verifique los términos aplicables y solicite una aclaración si no están disponibles.

## Revisión y recuperación

El mantenedor debe revisar alcance, procedencia y verificaciones obligatorias. CODEOWNERS identifica contactos técnicos, sin demostrar cualificación jurídica ni protección activa. Derechos o revisión obligatoria faltantes impiden aceptación. Corrija fallos y obtenga evidencia nueva; los cambios de alcance reabren la aprobación pertinente. Sin acceso, use la ruta pública existente del destino sin el Harness cuando proceda, o pida instrucciones al mantenedor visible sin divulgar información confidencial.

No exponga vulnerabilidades en issues públicas; use [reporte de seguridad](security-reporting.es.md). Política canónica: [Contribution](../../../standards/core/contribution.md).

[Quickstart](../quickstart.es.md) · [Harness](../../../README.es.md)
