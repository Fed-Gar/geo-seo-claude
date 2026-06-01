# Referencia de Comandos

Este archivo documenta cada comando en el paquete de habilidades `geo-seo-claude`. Los comandos se invocan dentro de Claude Code usando el prefijo `/geo`. La habilidad principal en `geo/SKILL.md` actúa como un enrutador: lee el primer argumento después de `/geo` y delega a la sub-habilidad coincidente bajo `skills/`. Todos los comandos aceptan una URL como su argumento principal; los comandos de CRM operan sobre nombres de dominio o IDs de prospectos en su lugar. Cada comando que produce una puntuación hace referencia al modelo de ponderación descrito en [scoring-methodology.md](scoring-methodology.md). La arquitectura de subagentes paralelos utilizada por `/geo audit` se describe en [architecture.md](architecture.md).

---

## Categorías de comandos

**Auditoría** — análisis completo del sitio y enfocado

| Comando | Descripción |
|---------|-------------|
| `/geo audit <url>` | Auditoría completa GEO + SEO con subagentes en paralelo |
| `/geo quick <url>` | Instantánea de visibilidad GEO en 60 segundos |
| `/geo citability <url>` | Puntúa una sola página para preparación de citas de IA |
| `/geo crawlers <url>` | Comprueba el acceso de rastreadores de IA a través de robots.txt y etiquetas meta |
| `/geo llmstxt <url>` | Analiza un llms.txt existente o genera uno desde cero |
| `/geo brands <url>` | Escanea menciones de marca en plataformas citadas por IA |
| `/geo platforms <url>` | Puntuaciones de preparación específicas de plataforma (AIO, ChatGPT, Perplexity, Gemini, Copilot) |

**Diagnósticos** — comprobaciones técnicas y de contenido dirigidas

| Comando | Descripción |
|---------|-------------|
| `/geo schema <url>` | Detecta, valida y genera datos estructurados Schema.org |
| `/geo technical <url>` | Auditoría técnica SEO con comprobaciones específicas de GEO |
| `/geo content <url>` | Evaluación de calidad de contenido y E-E-A-T |

**Reportes** — entregables listos para clientes

| Comando | Descripción |
|---------|-------------|
| `/geo report <url>` | Genera un reporte GEO listo para cliente en Markdown |
| `/geo report-pdf <url>` | Genera un reporte PDF profesional con gráficos y visualizaciones |

**CRM** — gestión de pipeline de prospectos y clientes

| Comando | Descripción |
|---------|-------------|
| `/geo prospect <cmd>` | Gestiona prospectos a través del pipeline de ventas |
| `/geo proposal <dominio>` | Auto-genera una propuesta para cliente a partir de datos de auditoría |
| `/geo compare <dominio>` | Reporte delta mensual mostrando mejoras de puntuación |

---

## /geo audit

Realiza una auditoría comprensiva GEO + SEO de un sitio web utilizando cinco subagentes en paralelo.

**Uso**

```
/geo audit https://example.com
```

**Qué hace**

- Fase 1 (secuencial): obtiene la página de inicio, detecta el tipo de negocio (SaaS, Local, E-commerce, Publisher, Agency), y rastrea hasta 50 páginas del sitemap o enlaces internos.
- Fase 2 (en paralelo): delega a cinco subagentes especializados simultáneamente — visibilidad IA, análisis de plataformas, SEO técnico, E-E-A-T de contenido y marcado de schema. Ver [architecture.md](architecture.md) para el flujo de subagentes.
- Fase 3 (secuencial): agrega las puntuaciones de los subagentes en una Puntuación GEO compuesta y ponderada (0–100). Ver [scoring-methodology.md](scoring-methodology.md) para la fórmula de ponderación.
- Clasifica cada problema por severidad: Crítico, Alto, Medio o Bajo.
- Produce un plan de acción de 30 días con temas semanales.

**Entradas**

| Argumento | Requerido | Descripción |
|----------|----------|-------------|
| `<url>` | Sí | URL de la página de inicio del sitio a auditar |

**Salida**

Escribe `GEO-AUDIT-REPORT.md` en el directorio de trabajo. Contiene: resumen ejecutivo, tabla de desglose de puntuación, inmersiones profundas por categoría, lista de problemas por severidad, victorias rápidas y un plan de acción de 30 días semana a semana. También se imprime un resumen en línea en la terminal.

**Cuándo usarlo**

Ejecuta esto primero para cualquier cliente o sitio nuevo; es el punto de entrada para todos los demás análisis.

---

## /geo quick

Entrega una instantánea de visibilidad GEO de 60 segundos sin escribir ningún archivo de salida.

**Uso**

```
/geo quick https://example.com
```

**Qué hace**

- Obtiene la página de inicio y una pequeña muestra de páginas clave.
- Ejecuta una pasada ligera a través de las principales señales GEO: acceso de rastreadores IA, presencia de llms.txt, schema en la página de inicio, y una lectura aproximada de citabilidad en el contenido principal (hero content).
- Produce una puntuación GEO aproximada y una corta lista de las brechas de mayor impacto.
- Alimenta directamente a `/geo prospect audit` cuando se llama desde el flujo de trabajo de CRM.

**Entradas**

| Argumento | Requerido | Descripción |
|----------|----------|-------------|
| `<url>` | Sí | URL a fotografiar |

**Salida**

Resumen en terminal en línea únicamente — no se escribe archivo. La puntuación se almacena en el registro del prospecto cuando se invoca a través de `/geo prospect audit`.

**Cuándo usarlo**

Usa esto para una rápida comprobación de cualificación antes de comprometerte a una auditoría completa, o cuando el subcomando `/geo prospect audit` lo llama automáticamente.

---

## /geo citability

Puntúa una sola página para su preparación a la cita por IA utilizando una rúbrica de cinco dimensiones.

**Uso**

```
/geo citability https://example.com/blog/my-article
```

**Qué hace**

- Obtiene la página y segmenta el contenido en bloques en cada límite H2/H3.
- Puntúa cada bloque en: calidad de bloque de respuesta (30%), auto-contención de pasaje (25%), legibilidad estructural (20%), densidad estadística (15%), y unicidad/datos originales (10%).
- Identifica los tres bloques más fuertes y los tres bloques más débiles.
- Genera sugerencias de reescritura específicas — incluyendo una oración de apertura sugerida — para cada bloque con puntuación por debajo de 60. Ver [scoring-methodology.md](scoring-methodology.md) para el detalle de la rúbrica.

**Entradas**

| Argumento | Requerido | Descripción |
|----------|----------|-------------|
| `<url>` | Sí | URL de la página específica a puntuar |

**Salida**

Escribe `GEO-CITABILITY-SCORE.md`. Contiene: puntuación general de citabilidad, tabla de puntuación ponderada, análisis de bloque más fuerte/débil con extractos citados, sugerencias de reescritura y una tabla de puntuación por sección.

**Cuándo usarlo**

Usa esto en cualquier página de contenido antes de publicar, o para priorizar qué páginas existentes reescribir para citas de IA.

---

## /geo crawlers

Analiza qué rastreadores de IA pueden acceder al sitio y proporciona una configuración de robots.txt recomendada.

**Uso**

```
/geo crawlers https://example.com
```

**Qué hace**

- Obtiene y parsea `robots.txt`, mapeando cada directiva User-agent a los 14 rastreadores de IA conocidos.
- Revisa una muestra de páginas clave en busca de overrides de `<meta name="robots">` y encabezados HTTP `X-Robots-Tag`.
- Comprueba la presencia de `/llms.txt` y `/.well-known/ai-plugin.json`.
- Evalúa si el contenido clave requiere renderizado de JavaScript (los rastreadores de IA no ejecutan JS).
- Puntúa el acceso de rastreadores en tres niveles: Nivel 1 (ChatGPT, Claude, Perplexity — críticos para búsqueda por IA), Nivel 2 (Gemini, Copilot, Apple Intelligence, Meta AI), y Nivel 3 (rastreadores solo para entrenamiento).

**Entradas**

| Argumento | Requerido | Descripción |
|----------|----------|-------------|
| `<url>` | Sí | URL raíz del dominio |

**Salida**

Escribe `GEO-CRAWLER-ACCESS.md`. Contiene: tabla de resumen de acceso por rastreador, una puntuación de visibilidad IA (0–100), lista de problemas críticos, y un bloque robots.txt completo listo para pegar configurado para máxima visibilidad en IA.

**Cuándo usarlo**

Usa esto como una comprobación rápida independiente cuando un cliente reporte que no aparece en los resultados de búsqueda de IA, o para verificar un cambio en robots.txt antes de desplegarlo.

---

## /geo llmstxt

Analiza un archivo `llms.txt` existente por su calidad, o genera uno nuevo desde cero si no existe ninguno.

**Uso**

```
/geo llmstxt https://example.com
```

**Qué hace**

- Obtiene `https://example.com/llms.txt` y `llms-full.txt` y comprueba el estado HTTP.
- **Modo de análisis** (el archivo existe): valida formato (título H1, descripción de blockquote, secciones H2, URLs absolutas, descripciones de entradas, Hechos Clave, sección Contacto); puntúa integridad (40%), precisión (35%), y utilidad (25%); identifica páginas importantes que faltan en el archivo.
- **Modo de generación** (el archivo no existe): rastrea el sitemap y la página de inicio, prioriza páginas por tipo, escribe descripciones de 10-30 palabras para cada página seleccionada, recopila hechos clave del negocio, y ensambla un `llms.txt` completo listo para desplegar.

**Entradas**

| Argumento | Requerido | Descripción |
|----------|----------|-------------|
| `<url>` | Sí | URL raíz del dominio |

**Salida**

- Modo análisis: escribe `GEO-LLMSTXT-ANALYSIS.md` con resultados de validación, páginas faltantes, y un archivo sugerido actualizado.
- Modo generación: escribe el archivo `llms.txt` listo para desplegar y un breve `GEO-LLMSTXT-GENERATION.md` resumiendo las decisiones de priorización.

**Cuándo usarlo**

Usa esto en cualquier sitio para validar un `llms.txt` existente o producir uno nuevo. Menos del 5% de los sitios tenían un `llms.txt` a principios de 2026, convirtiéndolo en una victoria rápida y accesible.

---

## /geo brands

Escanea menciones de marca en las plataformas en las que los sistemas de IA confían para el reconocimiento de entidades y decisiones de citación.

**Uso**

```
/geo brands https://example.com
```

**Qué hace**

- Comprueba la presencia de la marca en YouTube (existencia del canal, recuento de suscriptores, menciones de videos de terceros), Reddit (volumen de hilos, sentimiento, presencia oficial, subreddit), Wikipedia/Wikidata (existencia de artículos, número Q de Wikidata, clase de calidad), y LinkedIn (página de empresa, recuento de seguidores, frecuencia de publicaciones).
- Usa la API de Wikipedia directamente (`es.wikipedia.org/w/api.php` o `en...`) para evitar falsos negativos de búsquedas web.
- También escanea plataformas suplementarias: Quora, Stack Overflow, GitHub, Hacker News, y prensa/noticias.
- Calcula una Puntuación de Autoridad de Marca compuesta: YouTube 25%, Reddit 25%, Wikipedia/Wikidata 20%, LinkedIn 15%, otras plataformas 15%. Ver [scoring-methodology.md](scoring-methodology.md).

**Entradas**

| Argumento | Requerido | Descripción |
|----------|----------|-------------|
| `<url>` | Sí | URL del dominio (el nombre de marca se infiere del sitio) |

**Salida**

Escribe `GEO-BRAND-MENTIONS.md`. Contiene: Puntuación de Autoridad de Marca (0–100), tablas de desglose por plataforma, evaluación de sentimiento, tabla de contexto competitivo (si se identifican competidores), y recomendaciones priorizadas agrupadas por horizonte temporal (semana 1–2, mes 1–3, mes 3–12).

**Cuándo usarlo**

Usa esto cuando un sitio tiene contenido técnicamente sólido pero no aparece en las recomendaciones generadas por IA, o como parte de una estrategia de construcción de entidades.

---

## /geo platforms

Audita la preparación para cada plataforma de búsqueda por IA de forma individual y produce puntuaciones por plataforma.

**Uso**

```
/geo platforms https://example.com
```

**Qué hace**

- Ejecuta una lista de verificación y una rúbrica de puntuación separada para cada una de las cinco plataformas: Google AI Overviews, ChatGPT Web Search, Perplexity AI, Google Gemini, y Bing Copilot.
- Lista de Google AIO cubre: ranking orgánico en el top-10, encabezados basados en preguntas, estructura de respuesta directa, tablas, secciones de preguntas frecuentes, estadísticas con atribución, firmas de autor, y fechas de publicación.
- Lista de ChatGPT cubre: entidad de Wikipedia/Wikidata, cobertura del índice de Bing, menciones en Reddit, presencia en YouTube, consistencia de la entidad, e integridad del contenido.
- Lista de Perplexity cubre: presencia en Reddit, menciones en foros, frescura del contenido, investigación original, párrafos citables, y validación de reclamos en múltiples fuentes.
- Lista de Gemini cubre: Google Knowledge Panel, Google Business Profile, estrategia en YouTube, marcado de Schema.org, y presencia en el ecosistema de Google.
- Lista de Copilot cubre: Bing Webmaster Tools, implementación de IndexNow, página de LinkedIn, meta descripciones, y velocidad de carga de la página.

**Entradas**

| Argumento | Requerido | Descripción |
|----------|----------|-------------|
| `<url>` | Sí | URL de la página de inicio del sitio |

**Salida**

Escribe `GEO-PLATFORM-OPTIMIZATION.md`. Contiene: una puntuación general combinada, tabla de puntuación por plataforma, análisis de brechas por plataforma con acciones específicas, y un plan de acción priorizado (victorias rápidas, medio plazo, estratégico). Ver [scoring-methodology.md](scoring-methodology.md) para el peso de la plataforma en la puntuación compuesta.

**Cuándo usarlo**

Usa esto cuando necesites saber en qué plataformas específicas de IA tiene un rendimiento deficiente el sitio, o para construir una hoja de ruta de optimización orientada a la plataforma.

---

## /geo schema

Detecta todos los datos estructurados en un sitio, los valida con las especificaciones de Schema.org y genera bloques JSON-LD listos para pegar en caso de esquemas faltantes o incompletos.

**Uso**

```
/geo schema https://example.com
```

**Qué hace**

- Obtiene HTML crudo utilizando `fetch_page.py` (no WebFetch, que elimina el contenido del `<head>`) para extraer todos los bloques JSON-LD, Microdata y RDFa.
- Valida cada esquema: sintaxis JSON, `@type` válido, propiedades requeridas, propiedades recomendadas, enlaces `sameAs`, validez de URL, anidamiento, y si el esquema es renderizado por servidor o inyectado por JS.
- Revisa tipos de schema críticos para GEO: Organization, LocalBusiness, Article con Author, Product, FAQPage, SoftwareApplication, WebSite con SearchAction, y BreadcrumbList.
- Audita la propiedad `sameAs` frente a una lista prioritaria de 14 plataformas (Wikipedia, Wikidata, LinkedIn, YouTube, Twitter/X, GitHub, Crunchbase, etc.).
- Genera bloques de código JSON-LD completos utilizando el patrón `@graph` para cualquier esquema que falte o esté incompleto. Ver [scoring-methodology.md](scoring-methodology.md) para ver cómo la puntuación de esquema alimenta la Puntuación GEO compuesta.

**Entradas**

| Argumento | Requerido | Descripción |
|----------|----------|-------------|
| `<url>` | Sí | URL de la página o dominio a auditar |

**Salida**

Escribe `GEO-SCHEMA-REPORT.md`. Contiene: puntuación de esquema (0–100), tabla de esquemas detectados, resultados de validación por propiedad, lista de esquemas faltantes, tabla de auditoría de sameAs, y bloques de código JSON-LD listos para pegar con notas de implementación.

**Cuándo usarlo**

Usa esto para dar a un equipo de desarrolladores un ticket de implementación independiente, o para verificar la calidad del esquema después de una migración del CMS.

---

## /geo technical

Realiza una auditoría técnica SEO en ocho categorías con énfasis especial en el renderizado del lado del servidor (SSR) y el acceso de rastreadores de IA.

**Uso**

```
/geo technical https://example.com
```

**Qué hace**

- Rastreabilidad (15 pts): validez de robots.txt, acceso de rastreadores IA para 11 bots nombrados, presencia y validez del sitemap XML, profundidad de rastreo, directivas noindex.
- Indexabilidad (12 pts): etiquetas canonical, contenido duplicado (www/HTTP/trailing-slash), paginación, hreflang.
- Seguridad (10 pts): aplicación HTTPS, HSTS, `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, CSP.
- Estructura de URL (8 pts): URLs limpias y legibles, jerarquía lógica, cadenas de redirección, manejo de parámetros.
- Optimización móvil (10 pts): metaetiqueta viewport, diseño responsivo, tamaño de objetivo táctil, legibilidad de fuente.
- Core Web Vitals (15 pts): LCP < 2.5s, INP < 200ms, CLS < 0.1 usando umbrales de 2026.
- Renderizado del lado del servidor (15 pts): compara la salida de `curl` con el DOM renderizado; advierte sobre el contenido renderizado por cliente que los rastreadores IA no pueden leer.
- Velocidad de página y rendimiento del servidor (15 pts): TTFB, peso de la página, optimización de imágenes, tamaño del bundle de JS, compresión, caché, CDN. Ver [scoring-methodology.md](scoring-methodology.md) para ver cómo la puntuación técnica alimenta el compuesto.

**Entradas**

| Argumento | Requerido | Descripción |
|----------|----------|-------------|
| `<url>` | Sí | URL raíz del dominio |

**Salida**

Escribe `GEO-TECHNICAL-AUDIT.md`. Contiene: puntuación técnica (0–100), tabla de puntuación por categoría con estado Pass/Warn/Fail, tabla de acceso de rastreadores IA, lista de problemas críticos, advertencias y recomendaciones.

**Cuándo usarlo**

Usa esto cuando el contenido de un sitio es fuerte pero la visibilidad en IA es pobre, o para producir una lista de remediación orientada al desarrollador.

---

## /geo content

Evalúa la calidad del contenido a través del marco E-E-A-T (Experiencia, Conocimiento, Autoridad, Confiabilidad) y evalúa la citabilidad por IA y autoridad temática.

**Uso**

```
/geo content https://example.com
```

**Qué hace**

- Puntúa cada una de las cuatro dimensiones de E-E-A-T en una escala de 25 puntos: Experiencia (relatos en primera persona, datos originales, estudios de caso), Conocimiento (credenciales del autor, profundidad técnica, metodología, afirmaciones respaldadas por datos), Autoridad (citas entrantes, menciones en prensa, premios, presencia en Wikipedia), Confiabilidad (información de contacto, política de privacidad, HTTPS, estándares editoriales, reclamos precisos).
- Aplica un modificador de autoridad temática: +10 para más de 20 páginas con un clustering fuerte, hasta −5 para menos de 5 páginas sobre el tema.
- Evalúa la frescura del contenido para cada página (< 3 meses hasta sin-fecha/24+ meses).
- Advierte patrones de contenido de IA de baja calidad (fraseo genérico, sin perspectiva original, exceso de coberturas cautelosas) e identifica señales de alta calidad.
- Comprueba puntos de referencia del recuento de palabras por tipo de página y estructura de párrafos para la extracción de IA. Ver [scoring-methodology.md](scoring-methodology.md) para cómo la puntuación de contenido alimenta al compuesto.

**Entradas**

| Argumento | Requerido | Descripción |
|----------|----------|-------------|
| `<url>` | Sí | URL raíz del dominio (analiza página de inicio más páginas clave de contenido) |

**Salida**

Escribe `GEO-CONTENT-ANALYSIS.md`. Contiene: puntuación de contenido (0–100), tabla de desglose E-E-A-T, tabla de páginas analizadas, hallazgos detallados por dimensión, problemas de calidad de contenido con sugerencias de reescritura, preocupaciones de contenido IA, evaluación de frescura, pasajes más y menos citables, recomendaciones de brechas de contenido y pasos de mejora de E-E-A-T.

**Cuándo usarlo**

Usa esto cuando un sitio tiene buenos fundamentos técnicos pero no está siendo citado por los sistemas de IA, lo que indica un problema en la calidad del contenido.

---

## /geo report

Agrega salidas de todas las habilidades de auditoría en un único reporte en Markdown profesional de cara al cliente.

**Uso**

```
/geo report https://example.com
```

**Qué hace**

- Lee los archivos existentes de auditoría `GEO-*.md` del directorio de trabajo; ejecuta auditorías faltantes de forma automática si es necesario.
- Calcula una Puntuación de Preparación GEO compuesta: Preparación de Plataformas IA 25%, E-E-A-T de Contenido 25%, Fundación Técnica 20%, Schema 15%, Autoridad de Marca 15%. Ver [scoring-methodology.md](scoring-methodology.md).
- Traduce todos los hallazgos técnicos al lenguaje de impacto empresarial dirigido a propietarios y líderes de marketing, no a desarrolladores.
- Produce 12 secciones estructuradas: resumen ejecutivo, panel de puntuación, panel de visibilidad IA (por plataforma), tabla de acceso a rastreadores IA, análisis de autoridad de marca, análisis de citabilidad (top 5 / bottom 5 páginas), resumen de salud técnica, estado del schema, estado de llms.txt, plan de acción priorizado (victorias rápidas / medio plazo / estratégico), comparación de competidores (si se analizaron competidores) y apéndice de glosario.
- Incluye estimaciones conservadoras del impacto del tráfico y los ingresos vinculadas a mejoras en la puntuación.

**Entradas**

| Argumento | Requerido | Descripción |
|----------|----------|-------------|
| `<url>` | Sí | URL del dominio; los archivos de auditoría existentes en el directorio de trabajo se consumen de forma automática |

**Salida**

Escribe `GEO-CLIENT-REPORT.md`. El informe tiene de 3,000–6,000 palabras, es independiente y está listo para entregarse sin edición adicional.

**Cuándo usarlo**

Usa esto para producir el entregable final después de ejecutar la suite de auditoría completa, o al final de cada ciclo de compromiso mensual.

---

## /geo report-pdf

Convierte los datos de la auditoría GEO en un PDF profesionalmente formateado con gráficos, indicadores de puntuación y tablas codificadas por colores.

**Uso**

```
/geo report-pdf https://example.com
```

**Qué hace**

- Revisa el directorio de trabajo en busca de `GEO-CLIENT-REPORT.md` o `GEO-AUDIT-REPORT.md`; si no se encuentran, ejecuta una auditoría completa primero.
- Parsea el reporte Markdown para extraer las puntuaciones, números de preparación de la plataforma, estado del rastreador, hallazgos, y elementos de acción.
- Ensambla los datos en el esquema JSON que espera el script de generación de PDF.
- Llama a `python3 ~/.claude/skills/geo/scripts/generate_pdf_report.py` (requiere `pip install reportlab`).
- El PDF usa el tamaño de letra (US Letter) con una paleta de colores azul marino/azul/coral; los medidores de puntuación utilizan colores de semáforo (verde 80+, azul 60–79, amarillo 40–59, rojo inferior a 40).

**Entradas**

| Argumento | Requerido | Descripción |
|----------|----------|-------------|
| `<url>` | Sí | URL del dominio; usada para ubicar o generar datos de auditoría |

**Salida**

Escribe `GEO-REPORT-<brand>.pdf` en el directorio de trabajo. El PDF contiene: portada con medidor de puntuación, resumen ejecutivo, gráfico de barras del desglose de la puntuación, gráfico de barras horizontales de preparación de la plataforma IA, tabla codificada por colores del acceso de rastreadores, principales hallazgos por gravedad, plan de acción priorizado y un apéndice de metodología/glosario. Se reporta la ruta y tamaño del archivo al completarlo.

**Cuándo usarlo**

Usa esto cuando el entregable necesite enviarse por correo electrónico directamente a un cliente que espere un documento pulido en lugar de un archivo Markdown.

---

## /geo prospect

Un gestor de pipeline (CRM-lite) para el seguimiento de prospectos y clientes desde el descubrimiento inicial hasta el contrato.

**Uso**

```
/geo prospect new <domain>
/geo prospect list [<status>]
/geo prospect show <id-or-domain>
/geo prospect audit <id-or-domain>
/geo prospect note <id-or-domain> "<text>"
/geo prospect status <id-or-domain> <new-status>
/geo prospect won <id-or-domain> <monthly-value>
/geo prospect lost <id-or-domain> "<reason>"
/geo prospect pipeline
```

**Qué hace**

- Almacena todos los datos de prospectos en `~/.geo-prospects/prospects.json` como registros JSON persistentes que contienen: ID, empresa, dominio, estado, puntuación GEO, ruta al archivo de auditoría, ruta a la propuesta, valor mensual del contrato, y notas con marca de tiempo.
- Rastrea cinco etapas del pipeline: `lead`, `qualified`, `proposal`, `won`, `lost`.
- `prospect audit` llama a `/geo quick` y guarda la puntuación resultante en el registro del prospecto.
- `prospect pipeline` imprime un resumen enfocado en los ingresos que muestra el MRR comprometido, el valor del pipeline y las próximas acciones sugeridas por registro.
- Todos los subcomandos imprimen una confirmación y el estado actual del prospecto en la terminal; no se escriben archivos externos excepto las instantáneas de auditoría y las propuestas.

**Entradas**

| Argumento | Requerido | Descripción |
|----------|----------|-------------|
| `<cmd>` | Sí | Subcomando: `new`, `list`, `show`, `audit`, `note`, `status`, `won`, `lost`, `pipeline` |
| `<id-or-domain>` | Contextual | ID del prospecto (ej., `PRO-001`) o nombre de dominio |
| `<status>` | Para `status`, `list` | Etapa del pipeline: `lead`, `qualified`, `proposal`, `won`, `lost` |
| `<monthly-value>` | Para `won` | Valor de contrato mensual numérico |
| `"<text>"` | Para `note`, `lost` | Nota en texto libre o razón de pérdida |

**Salida**

Actualiza `~/.geo-prospects/prospects.json`. Instantáneas de auditoría guardadas en `~/.geo-prospects/audits/`. Salida de terminal para todos los subcomandos.

**Cuándo usarlo**

Usa esto para administrar el pipeline de ventas constante de una agencia GEO y hacer un seguimiento del historial del cliente en múltiples sesiones.

---

## /geo proposal

Auto-genera una propuesta de servicio GEO totalmente personalizada, lista para el cliente, a partir de datos de auditoría.

**Uso**

```
/geo proposal <dominio>
/geo proposal <dominio> --tier basic|standard|premium --client-name "Nombre" --monthly EUR
```

**Ejemplos**

```
/geo proposal example.com
/geo proposal example.com --tier standard --client-name "Acme Corp"
/geo proposal ~/.geo-prospects/audits/example.com-2026-03-12.md
```

**Qué hace**

- Carga el archivo de auditoría más reciente desde `~/.geo-prospects/audits/<dominio>*.md` (o ejecuta `/geo quick` si no existe).
- Selecciona el nivel de servicio recomendado según la puntuación GEO: 0–40 → Premium, 41–60 → Estándar, 61–75 → Básico.
- Rellena una plantilla de propuesta de 12 secciones: resumen ejecutivo, tablas de contexto de mercado, hallazgos de auditoría, paquetes de servicio de tres niveles con precios (Básico €2,500/mes, Estándar €5,000/mes, Premium €9,500/mes), tabla de proyección de ROI, línea de tiempo de compromiso de seis meses, resumen de la inversión y términos.
- Actualiza el estado del registro del prospecto a `proposal` y guarda la ruta del archivo de propuesta.

**Entradas**

| Argumento | Requerido | Descripción |
|----------|----------|-------------|
| `<dominio>` | Sí | Nombre de dominio o ruta a un archivo de auditoría |
| `--tier` | No | Obliga un nivel específico en lugar de usar la recomendación basada en la puntuación |
| `--client-name` | No | Invalida/Sobrescribe el nombre de la empresa autodetectado |
| `--monthly` | No | Invalida/Sobrescribe el valor de contrato mensual estimado |

**Salida**

Escribe `~/.geo-prospects/proposals/<dominio>-proposal-<fecha>.md`. Imprime confirmación con el paquete recomendado y el precio. La propuesta está lista para enviarse sin editarse.

**Cuándo usarlo**

Usa esto inmediatamente después de una auditoría a un prospecto cuando la puntuación GEO indique una oportunidad de venta clara (puntuación por debajo de 75).

---

## /geo compare

Genera un reporte delta mensual que compara una auditoría base (baseline) con una auditoría actual, mostrando las mejoras de puntuación al cliente.

**Uso**

```
/geo compare <dominio>
/geo compare <archivo-base> <archivo-actual>
/geo compare <dominio> --month march-2026
```

**Qué hace**

- Localiza archivos de auditoría en `~/.geo-prospects/audits/` que coincidan con el dominio; usa el más antiguo como base y el más nuevo como el actual. Si solo hay un archivo, ejecuta una auditoría rápida fresca como instantánea actual.
- Extrae la puntuación GEO general, todas las seis puntuaciones de categoría, todas las cinco puntuaciones de plataforma, y el estado de los rastreadores de IA de ambos archivos.
- Calcula los deltas y asigna símbolos de tendencia (▲▲ fuerte mejora, ▲ mejora, ── sin cambios, ▼ disminución, ▼▼ fuerte disminución).
- Rastrea el estado de finalización de las victorias rápidas, acciones a mediano plazo y elementos de acción estratégicos.
- Incluye una tabla de la trayectoria de seis meses y un estimado de impacto empresarial conservador (cambio en la probabilidad de la cita IA, cobertura de rastreadores, valor de tráfico estimado).

**Entradas**

| Argumento | Requerido | Descripción |
|----------|----------|-------------|
| `<dominio>` | Sí (o 2 rutas a archivos) | Nombre de dominio, o rutas explícitas hacia archivos de auditoría base y actual |
| `--month` | No | Etiqueta de mes para el nombre del archivo del reporte |

**Salida**

Escribe `~/.geo-prospects/reports/<dominio>-monthly-<YYYY-MM>.md`. Imprime un resumen a la terminal mostrando el cambio en la puntuación, la tasa de finalización de las victorias rápidas, nuevos problemas encontrados, y si el objetivo de seis meses va por buen camino.

**Cuándo usarlo**

Ejecuta esto el primero de cada mes para cada cliente activo, para generar el reporte de progreso que justifica la iguala/mensualidad.

---

## Discrepancias

Se encontraron las siguientes discrepancias entre `geo/SKILL.md` y el directorio `skills/`:

- **`/geo quick`**: Aparece en `geo/SKILL.md` y referenciado por todo el código fuente (por `geo-prospect` y `geo-compare`), pero no hay un `skills/geo-quick/SKILL.md`. El comportamiento del escaneo rápido está documentado solamente a través de las instrucciones de orquestación en `geo/SKILL.md` y la habilidad `geo-prospect`. Este comando está documentado arriba con base a esas referencias.
- **`/geo page`**: Listado en la tabla de referencia rápida de `geo/SKILL.md` (como `/geo page <url>` — análisis GEO profundo de una página) y en la tabla de archivos de salida (produce `GEO-PAGE-ANALYSIS.md`), pero no hay un `skills/geo-page/SKILL.md`. No existe implementación. Este comando **no está documentado** en la referencia anterior dado que no hay archivo de habilidad del cual obtener la información.
- **`/geo quick` en el `docs/commands-reference.md` original**: La tabla anterior mostraba `/geo quick` pero `geo/SKILL.md` no lo muestra en la tabla de sub-habilidades (solo en la tabla de referencia rápida). Se hace referencia como un comportamiento real en las habilidades prospect y compare, por lo que se mantiene arriba.
