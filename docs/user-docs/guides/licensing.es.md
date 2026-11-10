# Revisión de licencias y publicación

[English](licensing.md) | [Português](licensing.pt.md) | [Español](licensing.es.md)

Usa esta guía para preparar la revisión de un componente. La política y los términos de esta fuente privada son candidatos en implementación, no licencias adoptadas ni una release pública. El [candidato de términos (inglés)](../../licensing/harness-plugin-terms.md) tiene aprobación del texto por el responsable; consulta el [registro de aprobación (inglés)](../../governance/h01-approval.md). Todavía no está vigente; la verificación de derechos y avisos de componentes es independiente.

## Preparación

Identifica el componente, revisión exacta, público/distribución previstos, material original y de terceros, referencias de derechos/autorizaciones y avisos. Un revisor autorizado necesita acceso a la evidencia real; no copies contratos, credenciales ni datos personales al paquete.

Usa la [política común (inglés)](../../../standards/core/licensing-publication.md), el [inventario de avisos (inglés)](../../licensing/harness-plugin-notices.md) y el [registro privado de revisión (inglés)](../../governance/licensing-review.md). Separa los términos de la herramienta de los del proyecto destinatario.

## Prueba una revisión

Ejemplo: un componente propuesto para publicación contiene una plantilla copiada sin autorización verificada. Registra componente/revisión y evidencia faltante, usa la decisión `defer`, identifica al responsable y exige verificación antes de reconsiderar. No supongas permisos desde una URL pública o un commit.

Resultado esperado: un registro atribuible con la carencia y la siguiente acción, no aplicación de licencia ni publicación. Una superficie hipotética completamente revisada podría recibir recomendación `publish`, pero publicar aún necesita autoridad y evidencia separadas del ejecutor.

## Recuperación y handoff

Si faltan derechos, dependencias, autoridad del revisor o revisión completa de la superficie de exportación, mantén la decisión pendiente. Historia, tags, releases, LFS, fixtures, CI y adjuntos relevantes forman parte del handoff de publicación real; un árbol actual limpio no basta.

Platform, Workspace, Discover y CRM necesitan términos/evidencia de adopción propios. La distribución del Harness/plugin es separada. Cambiar la fuente no actualiza consumidores instalados ni concede derechos. Consulta [contribución](contributing.es.md) para participar y [entrega por GitHub](github-delivery.es.md) para el proceso gobernado.

[Inicio rápido](../quickstart.es.md) · [Harness](../../../README.es.md)
