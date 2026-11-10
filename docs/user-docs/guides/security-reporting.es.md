# Reportar una preocupación de seguridad con cuidado

[English](security-reporting.md) | [Português](security-reporting.pt.md) | [Español](security-reporting.es.md)

Estado actual del candidato H02: **el responsable indicó un destino, pero ninguna ruta confidencial fue verificada en este trabajo**. No se activó un canal ni se envió un test/reporte. Esta guía no promete plazo de respuesta ni monitoreo continuo.

Los CODEOWNERS pertinentes son responsables de supervisar, clasificar y coordinar la resolución de reportes de seguridad de sus componentes, tanto mediante PVR en repositorios públicos como por email interno en los privados. Los mantenedores configuran los permisos y notificaciones necesarios; la asignación en CODEOWNERS no configura por sí sola la recepción en GitHub.

## Encaminamiento elegido — candidato privado

Para bugs comunes, usa Bug report. Para sospechas de vulnerabilidad en repositorios públicos, usa Private Vulnerability Reporting de GitHub cuando esté habilitado. En los privados, envía email a los CODEOWNERS pertinentes por los canales internos existentes de Versat. No divulgues detalles de vulnerabilidades en issues comunes. Consulta [reportes de seguridad](../../handoffs/contribution-security-guidance/organization/candidate/SECURITY.es.md) para encaminamiento y recuperación cuando el canal no esté disponible.

## Antes de compartir detalles

Lee las instrucciones reales de seguridad del repositorio destinatario y confirma su alcance. El nombre de un mantenedor o un enlace accesible con autenticación no acredita una ruta confidencial. No incluyas detalles de explotación, credenciales, datos de clientes ni adjuntos sensibles en un issue público.

## Cuando no exista una ruta verificada

Usa un contacto existente y visible del repositorio/mantenedor sólo para solicitar instrucciones de reporte privado, sin revelar la vulnerabilidad. Ejemplo seguro: “Necesito instrucciones confidenciales de reporte de seguridad para este repositorio.” Espera una ruta adecuada antes de enviar detalles sensibles. Este ejemplo no envía un mensaje ni autoriza a un agente a hacerlo.

Resultado esperado: una solicitud no sensible de instrucciones, no un reporte verificado ni servicio activo. Si no puedes establecer una ruta adecuada, conserva el reporte privado y la carencia de verificación explícita.

## Qué debe acreditar una ruta verificada

Deben registrarse destino real, responsable de recepción, público autorizado a reportar, destinatarios/límite de acceso y tratamiento de datos aprobado por el responsable. Observaciones de configuración/acceso y un marcador sintético no sensible con recepción, explícitamente autorizado, deben sustentar cualquier afirmación de verificación. No supongas acceso público desde una sesión administrativa.

El [registro privado de la ruta (inglés)](../../governance/security-reporting.md) enumera las carencias. La orientación alternativa sin canal verificado no completa H02. Una ruta cambiada o fallida exige nueva verificación y retirada de afirmaciones de actividad sin respaldo.

Reglas canónicas: [Security (inglés)](../../../standards/core/security.md). Configurar canales, cambiar permisos y enviar mensajes de prueba requiere autorización específica separada. Cada producto verifica su propio alcance adoptado.

[Contribución](contributing.es.md) · [Harness](../../../README.es.md)
