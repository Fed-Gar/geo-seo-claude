# Habilidad de Código GEO-SEO Claude — Documentación

`geo-seo-claude` es un paquete de habilidades de Claude Code que ejecuta auditorías de GEO (Generative Engine Optimization) y SEO contra un sitio web. Orquesta 13 sub-habilidades, 5 subagentes en paralelo, y un conjunto de utilidades en Python para producir una Puntuación GEO (0–100) compuesta y un plan de acción priorizado.

Si eres nuevo aquí, comienza con **Primeros Pasos (Getting Started)**. Si estás contribuyendo, echa un vistazo primero a **Arquitectura** y **Habilidades & Agentes**.

## Contenidos

| Documento | Qué contiene |
|-----|--------------|
| [Primeros Pasos (Getting Started)](getting-started.md) | Prerrequisitos, instalación (macOS/Linux/Windows), primera auditoría, solución de problemas, desinstalación. |
| [Referencia de Comandos](commands-reference.md) | Todos los comandos slash `/geo` con uso, argumentos, salida y cuándo usarlos. |
| [Arquitectura](architecture.md) | Disposición del repositorio, flujo de auditoría, despacho de subagentes en paralelo, almacenamiento de datos. |
| [Habilidades & Agentes](skills-and-agents.md) | Referencia para cada sub-habilidad, subagente, script de Python y plantilla de esquema. |
| [Metodología de Puntuación](scoring-methodology.md) | Cómo se calcula la Puntuación GEO compuesta, señales por categoría, advertencias. |
| [Preguntas Frecuentes (FAQ)](faq.md) | Preguntas comunes para usuarios y colaboradores. |
| [Contribuyendo (Contributing)](../CONTRIBUTING.md) | Cómo reportar errores, proponer características y abrir PRs. |

## Enlaces rápidos

- Primera auditoría: [Primeros Pasos → Tu Primera Auditoría](getting-started.md#your-first-audit)
- Lista completa de comandos: [Referencia de Comandos](commands-reference.md)
- Tabla de pesos: [Metodología de Puntuación](scoring-methodology.md)
- Flujo de auditoría en paralelo: [Arquitectura → Flujo Completo de Auditoría](architecture.md)
