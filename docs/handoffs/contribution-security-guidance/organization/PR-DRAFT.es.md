# feat: definir reporte privado de vulnerabilidades y procedencia de contribuciones

Las instrucciones actuales de contribución no distinguen bugs comunes de reportes confidenciales ni explicitan la procedencia de materiales. Este cambio conserva la ruta pública y los formularios existentes, añade orientación de derechos y define GitHub Private Vulnerability Reporting para repositorios públicos y email a los CODEOWNERS por canales internos para privados. Los CODEOWNERS acompañan la clasificación y resolución.

Incluye SECURITY en inglés, portugués y español y el formulario nativo .github/VULNERABILITY_REPORT.yml. El formulario no crea una issue ordinaria ni habilita PVR. La guía propia de cada repositorio y sus formularios específicos conservan precedencia. Las referencias privadas al Harness siguen siendo opcionales para contribuir sin la herramienta.

Validación local: YAML/campos, equivalencia EN/PT/ES, enlaces y hashes, lectura anónima de la ruta pública vigente y preservación de formularios/perfil/README. Patch verificado contra la revisión base. No se verificó renderizado/herencia del formulario nuevo en GitHub, configuración ni recepción; requieren el rollout autorizado. No se publica dirección de email ni se modifica licencia o configuración de seguridad.

Seguimiento: Harness #35 / H02; reutiliza la entrega de issue 22, PR33 y organización PR3. No completa H03 ni adopciones P01/P03. Esta descripción es un borrador privado; no se creó PR.
