# Preguntas Frecuentes (FAQ)

---

## General

### ¿Qué es GEO y cómo se diferencia de SEO?

El SEO (Optimización para Motores de Búsqueda) se centra en clasificar en los resultados tradicionales de enlaces azules de motores de búsqueda como Google. GEO (Generative Engine Optimization u Optimización para Motores Generativos) apunta a la visibilidad dentro de respuestas generadas por IA de sistemas como ChatGPT, Perplexity, Claude, Gemini, y Google AI Overviews. Ambas disciplinas se superponen — los fundamentos técnicos y la calidad del contenido importan para ambas — pero GEO agrega preocupaciones específicas a la recuperación por IA: puntuación de citabilidad, densidad de menciones de marca, llms.txt, y reconocimiento de entidades a través de plataformas citadas por IA.

### ¿Es esta una herramienta o servicio de pago?

La herramienta en sí es gratuita y tiene licencia MIT. Se ejecuta completamente dentro de tu propia sesión de Claude Code usando tu suscripción existente a Anthropic. No hay clave de API separada, medidor de uso o suscripción para el paquete de habilidades en sí.

### ¿Para quién es esto?

Agencias GEO que ejecutan auditorías de clientes, equipos de marketing in-house que monitorean visibilidad de búsqueda en IA, creadores de contenido optimizando páginas individuales para citas de IA, y desarrolladores que construyen o mantienen propiedades web y que desean feedback procesable sobre GEO y SEO sin una suscripción SaaS.

### ¿Esto reemplaza mi stack de herramientas SEO existente?

No. Complementa las herramientas existentes. El comando `/geo technical` cubre fundamentos de SEO técnico, pero la herramienta no reemplaza a rastreadores como Screaming Frog, plataformas de búsqueda de palabras clave, o rastreadores de posicionamiento. Su valor principal es la capa GEO — citabilidad de IA, acceso de rastreadores, señales de marca y preparación de plataformas — que la mayoría de herramientas SEO tradicionales no cubren.

---

## Instalación & Configuración

### ¿Por qué necesito la CLI de Claude Code?

El paquete de habilidades está implementado como comandos slash de Claude Code. Todos los comandos (`/geo audit`, `/geo quick`, etc.) son enrutados a través del sistema de agentes y habilidades de Claude Code. La CLI es el entorno de ejecución; sin él, no hay nada que ejecute los archivos de la habilidad. Instálalo con `npm install -g @anthropic-ai/claude-code`.

### ¿Puedo ejecutar esto en Windows sin WSL?

Sí, pero debes usar Git Bash, no PowerShell ni Símbolo del sistema (Command Prompt). El instalador para Windows es `install-win.sh` y requiere Git para Windows (el cual incluye Git Bash). Haz clic derecho en la carpeta del repositorio y selecciona "Open Git Bash here", luego ejecuta `./install-win.sh`. WSL no es requerido.

### ¿Qué hace realmente `install.sh`?

Comprueba si existen Git, Python 3.8+ y la CLI de Claude Code, luego copia los archivos a tu directorio de configuración de Claude (`~/.claude/`). Específicamente: la habilidad principal va a `~/.claude/skills/geo/`, cada una de las 13 sub-habilidades va a `~/.claude/skills/geo-<nombre>/`, y los 5 archivos de agente van a `~/.claude/agents/`. Luego instala las dependencias de Python desde `requirements.txt` utilizando `pip install --user`. Si lo ejecutas de forma interactiva, también ofrece instalar el navegador Chromium de Playwright para soporte de capturas de pantalla. El instalador funciona tanto desde un directorio local clonado como a través de una tubería `curl | bash` desde la URL del repositorio.

### ¿Necesito Playwright?

Playwright es opcional. El instalador te solicita instalarlo (`python3 -m playwright install chromium`). Sin él, las características basadas en capturas de pantalla no están disponibles pero todos los demás comandos de análisis y auditoría funcionan normalmente. Puedes instalarlo luego en cualquier momento.

---

## Uso

### ¿Cuál es la diferencia entre `/geo quick` y `/geo audit`?

`/geo quick` produce una instantánea de visibilidad en línea en 60 segundos y no escribe archivo de salida. Es útil para una lectura rápida sobre una URL antes de comprometerse con una corrida completa. `/geo audit` es el flujo de trabajo completo: obtiene el sitio, detecta el tipo de negocio, lanza 5 subagentes en paralelo, suma puntuaciones a través de todas las categorías, y escribe un `GEO-AUDIT-REPORT.md` con un plan de acción priorizado. Ver [commands-reference.md](commands-reference.md) para la lista completa de comandos.

### ¿De dónde sale la Puntuación GEO compuesta?

La puntuación (0-100) es un agregado ponderado de seis categorías: Citabilidad y Visibilidad de IA (25%), Señales de Autoridad de Marca (20%), Calidad de Contenido y E-E-A-T (20%), Fundamentos Técnicos (15%), Datos Estructurados (10%), y Optimización de Plataformas (10%). Ver [scoring-methodology.md](scoring-methodology.md) para ver cómo se miden las señales individuales dentro de cada categoría.

### ¿Cómo funcionan los subagentes en paralelo?

Durante una auditoría completa, cinco subagentes se ejecutan simultáneamente después de la fase de descubrimiento inicial: `geo-ai-visibility`, `geo-platform-analysis`, `geo-technical`, `geo-content`, y `geo-schema`. Cada uno se asocia a un archivo de definición de agente en `~/.claude/agents/` y es responsable de una porción distinta del análisis. El sistema de agentes de Claude Code maneja el despacho paralelo; el orquestador luego recopila los cinco reportes y sintetiza la puntuación compuesta. Ver [architecture.md](architecture.md) para el flujo completo.

### ¿Dónde se guardan los datos de prospectos, propuestas y reportes?

Los datos de `/geo prospect`, `/geo proposal`, y `/geo compare` se escriben en `~/.geo-prospects/` fuera del directorio de Claude Code. La estructura es:

```
~/.geo-prospects/
├── prospects.json
├── proposals/<dominio>-proposal-<fecha>.md
└── reports/<dominio>-monthly-<YYYY-MM>.md
```

Este directorio intencionalmente no es borrado por `uninstall.sh`. Bórralo manualmente con `rm -rf ~/.geo-prospects` si quieres desechar tus datos de prospectos.

---

## Contribuyendo

### ¿Cómo agrego una nueva sub-habilidad?

Crea un nuevo directorio bajo `skills/` siguiendo el patrón de nomenclatura `geo-<nombre-habilidad>/`. Añade un `SKILL.md` dentro del mismo que defina el nombre, descripción y lógica de la habilidad. Si la habilidad debe participar en la auditoría completa, regístrala en el archivo de agente apropiado bajo `agents/`. Sigue la estructura de una sub-habilidad existente como `skills/geo-citability/` como referencia. Ver [skills-and-agents.md](skills-and-agents.md) para un mapa de cómo se relacionan las habilidades y los agentes.

### ¿Cómo pruebo mis cambios antes de abrir un PR (Pull Request)?

Ejecuta `./install.sh` desde tu clon local — el script detecta un `geo/SKILL.md` local e instala desde el directorio de trabajo en lugar de clonar desde GitHub. Abre Claude Code y prueba los comandos afectados contra una URL real. Verifica que todas las pruebas de estado pasen antes de enviar tu pull request, como se señala en `CONTRIBUTING.md`.

### ¿Dónde reporto errores o solicito funciones?

Abre un Issue en GitHub. Para errores, incluye una descripción clara, la URL que estabas auditando si es relevante, y cualquier salida de error. Para solicitudes de funciones, explica el caso de uso y por qué importa. Busca problemas existentes primero para evitar duplicados. Ambos se rastrean bajo la pestaña Issues del repositorio.

---

## Limitaciones

### ¿Puede esta herramienta garantizar citas o clasificaciones en la IA?

No. La herramienta audita señales que correlacionan con visibilidad en IA y provee recomendaciones para mejorarlas, pero ninguna herramienta puede garantizar que cualquier sistema de IA citará o mostrará un dominio específico. La recuperación por IA es probabilística y varía por consulta, plataforma, y versión del modelo.

### ¿Envía algo a servicios de terceros?

La habilidad utiliza `WebFetch` y `Bash` (vía `curl`) para obtener las URLs que provees, y el escáner de menciones de marca revisa plataformas públicamente accesibles (YouTube, Reddit, Wikipedia, LinkedIn, y otras) en busca de señales de marca. Ningún dato de auditoría es enviado a ningún endpoint operado por Anthropic o analíticas de terceros. Tus datos se mantienen dentro de tu sesión de Claude Code y tu sistema de archivos local.
