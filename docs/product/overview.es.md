# Visión del producto

[English](overview.md) | [Português](overview.pt.md) | [Español](overview.es.md)

## Producto y responsabilidad

Versat AI Harness ayuda al equipo Versat a convertir intenciones de desarrollo en cambios revisados y trazables. Versat mantiene el producto; los contactos incluyen elviszoz y evertonspohrversat, indicados en CODEOWNERS para componentes gobernados. Esta visión describe el repositorio fuente, sin suponer que todas las capacidades estén instaladas en cada workspace.

## Problema, trabajo y persona

La [Issue #22](https://github.com/versat-labs/versat-ai-harness/issues/22) indica que el equipo no sabe usar el nuevo Harness. La persona principal es el equipo Versat, especialmente quienes desarrollan con SDD. Al planificar o implementar una historia, necesitan consultar la documentación del repositorio para comprender y seguir el proceso. La frecuencia y el costo de este problema de onboarding no se midieron; valídalos con comentarios del equipo después del primer uso.

## Solución y valor

Un Plugin versionado reúne Standards canónicos, ciclo SDD, cinco Skills, plantillas compuestas y validación determinista. El equipo recibe orientación reutilizable para bootstrap, cambios, mantenimiento, auditoría y revisión arquitectónica. El valor esperado es mayor claridad en decisiones y verificaciones reproducibles; más productividad y menos defectos son resultados por medir, no resultados comprobados.

## Origen y momento

El historial de ADR registra la evolución hacia un paquete portátil y un ciclo gobernado único. La issue y las capacitaciones muestran una necesidad actual de una entrada más clara. Consolidar ese conocimiento apoya la adopción sin crear un proceso paralelo. Otras afirmaciones sobre el origen requieren evidencia del responsable del producto.

## Límites actuales

VERSION declara 0.3.0. La ejecución de pruebas de consumidores y evaluación supervisada presentes en el código fuente se identifican explícitamente como no publicadas en sus guías. El Harness no proporciona por sí mismo un motor de workflows operativos, aprovisionamiento remoto automático ni actualizaciones automáticas de consumidores. El éxito local del validador no demuestra aceptación semántica, autenticidad de aprobación, CI remoto ni merge.

## Valor interno y aplicabilidad de mercado

El alcance es una herramienta interna de desarrollo, sin precio externo ni modelo de comisión proporcionado. TAM, SAM, SOM y take rate no aplican a esta entrega documental. Evalúa el valor interno mediante finalización del onboarding, tiempo hasta el primer plan revisado y preguntas recurrentes; no hay baseline ni retorno financiero comprobado.

## Alternativas, diferenciación e innovación

Las alternativas incluyen instrucciones dispersas del equipo, listas propias de cada repositorio y asistencia genérica de código. El Harness combina Standards resueltos por contexto, gates explícitos y verificaciones vinculadas a la versión en un paquete. Es una elección de integración, sin afirmar novedad de mercado ni superioridad demostrada.

## Escalabilidad y responsabilidad

La adopción de releases exactas y plantillas compartidas apoya más repositorios; mantenimiento de traducciones, revisión humana, acceso y compatibilidad siguen siendo restricciones. La accesibilidad y orientación multilingüe pueden reducir barreras. El uso de modelos y evaluaciones repetidas consume recursos; mide antes de afirmar beneficios ambientales. Protege capacitaciones privadas e información de clientes.

## Preguntas abiertas y validación

Pide al responsable del producto confirmar baseline de adopción y medidas de éxito después de que el equipo siga el quickstart. Pide a la administración del workspace confirmar release instalada y política de distribución. Revisa transcripciones accesibles antes de usar pasos específicos de los videos. Estos vacíos de investigación no implican capacidades adicionales implementadas.

[Comenzar a usar el Harness](../user-docs/quickstart.es.md) · [ADRs (inglés)](../decisions/README.md)
