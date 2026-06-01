# Habilidades, Agentes, Scripts y Schemas

Esta referencia describe cada parte móvil en el paquete de habilidades `geo-seo-claude`. El paquete optimiza los sitios web para la Optimización de Motores Generativos (GEO) — haciendo que el contenido sea descubrible y citable por las plataformas de búsqueda de IA (ChatGPT, Perplexity, Google AI Overviews, Gemini, Bing Copilot) — mientras se mantienen los fundamentos tradicionales de SEO. Está estructurado como una habilidad orquestadora, 14 sub-habilidades, 5 subagentes paralelos, 6 scripts de ayuda en Python, y 6 plantillas de esquema JSON-LD.

Consulta [commands-reference.md](commands-reference.md) para la referencia completa de los comandos slash y [architecture.md](architecture.md) para ver cómo funciona el flujo de subagentes en paralelo durante una auditoría completa.

---

## Orquestador

- **geo** (`geo/SKILL.md`) — Punto de entrada para todos los comandos GEO. Detecta el tipo de negocio, despacha sub-habilidades para comandos individuales, y coordina el flujo de auditoría completa de tres fases: descubrimiento, delegación de subagentes paralelos y síntesis de puntuación. Produce una Puntuación GEO compuesta (0–100) ponderada a través de seis categorías.

---

## Sub-habilidades

### geo-audit

**Propósito:** Orquesta una auditoría completa de GEO + SEO de un sitio web mediante la ejecución del descubrimiento, delegando a cinco subagentes en paralelo, y agregando sus puntuaciones en una única Puntuación GEO compuesta.

**Entradas:** Una URL. Opcionalmente, datos de página pre-rastreados.

**Salidas:** `GEO-AUDIT-REPORT.md` — puntuación compuesta, desglose por categoría, lista de severidad de problemas (Crítico / Alto / Medio / Bajo), plan de acción de 30 días, y un apéndice de las páginas analizadas.

**Pesos de puntuación:**
- Citabilidad IA 25%, Autoridad de Marca 20%, E-E-A-T de Contenido 20%, GEO Técnico 15%, Datos Estructurados 10%, Optimización de Plataforma 10%

**Dependencias:** Delega a todos los cinco subagentes (`geo-ai-visibility`, `geo-platform-analysis`, `geo-technical`, `geo-content`, `geo-schema`).

Consulta [commands-reference.md](commands-reference.md) para `/geo audit`.

---

### geo-citability

**Propósito:** Puntúa pasajes de contenido individuales en una escala de 0–100 para la preparación a la citación por IA. Mide la probabilidad de que un sistema de IA extraiga y cite un pasaje literalmente.

**Entradas:** Una URL (obtenida con WebFetch).

**Salidas:** `GEO-CITABILITY-SCORE.md` — puntuaciones por sección, pasajes principales listos para cita, bloques más débiles con sugerencias de reescritura y un porcentaje de cobertura de citabilidad.

**Dimensiones de puntuación (por pasaje):** Calidad del Bloque de Respuesta (30%), Auto-contención (25%), Legibilidad Estructural (20%), Densidad Estadística (15%), Unicidad (10%).

**Umbral clave:** Los pasajes óptimos citados por IA tienen entre 134–167 palabras, son independientes, ricos en hechos y responden una pregunta en las primeras 1–2 oraciones.

Consulta [commands-reference.md](commands-reference.md) para `/geo citability`.

---

### geo-crawlers

**Propósito:** Audita qué rastreadores de IA pueden acceder al sitio parseando `robots.txt`, etiquetas meta robots, y encabezados HTTP `X-Robots-Tag`. Produce un mapa de acceso completo a través de 14 rastreadores en tres niveles.

**Entradas:** La URL de un dominio.

**Salidas:** `GEO-CRAWLER-ACCESS.md` — estado por rastreador (Permitido / Bloqueado / No Mencionado), Puntuación de Visibilidad IA, configuración recomendada de `robots.txt`, y evaluación del renderizado de JavaScript.

**Niveles de rastreadores:**
- Nivel 1 (visibilidad en búsqueda): GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot
- Nivel 2 (ecosistema IA más amplio): Google-Extended, GoogleOther, Applebot-Extended, Amazonbot, FacebookBot
- Nivel 3 (solo entrenamiento): CCBot, anthropic-ai, Bytespider, cohere-ai

Consulta [commands-reference.md](commands-reference.md) para `/geo crawlers`.

---

### geo-llmstxt

**Propósito:** Analiza un archivo `llms.txt` existente en busca de cumplimiento de formato e integridad, o genera uno nuevo desde cero rastreando el sitio. El estándar `llms.txt` le brinda a los sistemas de IA una orientación explícita sobre la estructura del sitio y las páginas clave.

**Entradas:** La URL de un dominio. Opera en modo de análisis (el archivo existe) o en modo de generación (el archivo está ausente).

**Salidas (modo análisis):** `GEO-LLMSTXT-ANALYSIS.md` — tabla de validación de formato, páginas faltantes, puntuación global de llms.txt (Completitud 40%, Precisión 35%, Utilidad 25%).

**Salidas (modo generación):** Un archivo `llms.txt` listo para desplegar y `GEO-LLMSTXT-GENERATION.md` explicando la lógica de selección de las páginas.

**Dependencias:** `scripts/llmstxt_generator.py` provee ayudantes de validación y generación.

Consulta [commands-reference.md](commands-reference.md) para `/geo llmstxt`.

---

### geo-brand-mentions

**Propósito:** Escanea la presencia de marca a través de plataformas que los modelos de IA usan para el reconocimiento de entidades y las decisiones de citación. Produce una Puntuación de Autoridad de Marca basada en la presencia ponderada por plataforma.

**Entradas:** Nombre de marca, URL del dominio, industria (recopilada del sitio si no se proporciona).

**Salidas:** `GEO-BRAND-MENTIONS.md` — puntuaciones por plataforma (YouTube 25%, Reddit 25%, Wikipedia/Wikidata 20%, LinkedIn 15%, Otras 15%), evaluación de sentimiento, Puntuación compuesta de Autoridad de Marca y recomendaciones priorizadas.

**Perspectiva clave:** La correlación de la mención en YouTube con la cita por IA es ~0.737; la correlación con la Clasificación del Dominio (Domain Rating) es ~0.266 (Estudio de Ahrefs, Diciembre 2025 de 75,000 marcas).

**Dependencias:** `scripts/brand_scanner.py` provee el marco de verificación por plataforma. Las revisiones de Wikipedia usan la API de Wikipedia directamente a través de Bash (la búsqueda web sola produce falsos negativos).

Consulta [commands-reference.md](commands-reference.md) para `/geo brands`.

---

### geo-platform-optimizer

**Propósito:** Audita la preparación para cada una de las cinco principales plataformas de búsqueda con IA individualmente, dado que solo el 11% de los dominios son citados tanto por ChatGPT como por Google AI Overviews para la misma consulta.

**Entradas:** Una URL y el tema principal o industria del sitio.

**Salidas:** `GEO-PLATFORM-OPTIMIZATION.md` — puntuaciones por plataforma y brechas para Google AI Overviews, Búsqueda Web de ChatGPT, Perplexity AI, Google Gemini y Bing Copilot; un plan de acción prioritario entre plataformas.

**Factores principales específicos por plataforma:** AIO → clasificación top-10 + estructura de P&R; ChatGPT → entidad de Wikipedia; Perplexity → presencia en Reddit + investigación original; Gemini → YouTube + Panel de Conocimiento (Knowledge Panel); Bing Copilot → IndexNow + Bing Webmaster Tools.

Consulta [commands-reference.md](commands-reference.md) para `/geo platforms`.

---

### geo-schema

**Propósito:** Detecta, valida, y genera datos estructurados de Schema.org (se prefiere JSON-LD). Los datos estructurados son la principal señal legible por máquinas que los modelos de IA usan para identificar y confiar en las entidades.

**Entradas:** Una URL. Usa `scripts/fetch_page.py` para obtener HTML crudo incluyendo el contenido en `<head>` (WebFetch lo elimina).

**Salidas:** `GEO-SCHEMA-REPORT.md` — esquemas detectados con resultados de validación, auditoría de vinculación de entidades `sameAs`, advertencias sobre esquemas obsoletos (HowTo eliminado en Septiembre de 2023, FAQPage restringido en Agosto de 2023), y bloques de código JSON-LD listos para pegar.

**Schemas críticos para GEO:** Organization + `sameAs`, Article + Author (Person), propiedad speakable, BreadcrumbList, WebSite + SearchAction.

**Dependencias:** `scripts/fetch_page.py` (extracción de HTML en bruto); plantillas en `schema/*.json` (usadas como referencia para la generación).

Consulta [commands-reference.md](commands-reference.md) para `/geo schema`.

---

### geo-technical

**Propósito:** Audita ocho categorías de salud técnica con énfasis en factores que afectan de forma única la visibilidad de los rastreadores de IA: renderizado del lado del servidor (SSR) y acceso de rastreadores de IA.

**Entradas:** La URL de la página de inicio más 2–3 páginas internas clave.

**Salidas:** `GEO-TECHNICAL-AUDIT.md` — puntuaciones por categoría, tabla de acceso de rastreadores IA, evaluación de SSR, riesgo de Core Web Vitals (LCP / INP / CLS), encabezados de seguridad, y estado de la optimización móvil.

**Categorías de puntuación (puntos máximos):** Renderizado del lado del servidor 15, Core Web Vitals 15, Rastreabilidad 15, Indexabilidad 12, Seguridad 10, Móvil 10, Velocidad de Página 15, Estructura de URL 8.

**Chequeo Crítico:** Los rastreadores de IA no ejecutan JavaScript. Una SPA del lado del cliente sin SSR renderiza una página vacía a GPTBot, ClaudeBot y PerplexityBot.

Consulta [commands-reference.md](commands-reference.md) para `/geo technical`.

---

### geo-content

**Propósito:** Evalúa la calidad del contenido a través del marco E-E-A-T (Experiencia, Conocimiento, Autoridad, Confiabilidad) y mide la profundidad del contenido, la legibilidad, indicadores de contenido de IA, y la autoridad temática.

**Entradas:** Una URL (obtenida con WebFetch).

**Salidas:** `GEO-CONTENT-ANALYSIS.md` — puntuaciones de E-E-A-T (25 puntos cada una), tabla de métricas de contenido, evaluación de contenido IA, calificación de autoridad temática, evaluación de frescura, y recomendaciones de reescritura.

**Modificadores de puntuación:** La autoridad temática suma de +10 a −5 puntos sobre la base de 100 puntos de la puntuación E-E-A-T.

Consulta [commands-reference.md](commands-reference.md) para `/geo content`.

---

### geo-report

**Propósito:** Agrega los resultados de todas las sub-habilidades de auditoría en un único entregable orientado al cliente, escrito para propietarios de empresas y no para desarrolladores — los hallazgos técnicos se traducen al impacto empresarial y a una perspectiva de valor económico.

**Entradas:** Archivos de salida de `geo-platform-optimizer`, `geo-schema`, `geo-technical`, `geo-content`, y opcionalmente `geo-llmstxt` y `geo-brand-mentions`.

**Salidas:** `GEO-CLIENT-REPORT.md` — resumen ejecutivo, Puntuación de Preparación GEO, Panel de Visibilidad IA, tabla de acceso a rastreadores, tabla de autoridad de marca, análisis de citabilidad, resumen de salud técnica, estado de los esquemas, plan de acción con impacto en plataforma y esfuerzo requerido, y un apéndice con glosario completo. Longitud objetivo: 3,000–6,000 palabras.

Consulta [commands-reference.md](commands-reference.md) para `/geo report`.

---

### geo-report-pdf

**Propósito:** Genera un PDF formateado profesionalmente y listo para el cliente a partir de los datos de auditoría GEO utilizando ReportLab. Incluye medidores de puntuación, gráficos de barras, y tablas codificadas por color.

**Entradas:** Archivos `GEO-AUDIT-REPORT.md` o `GEO-CLIENT-REPORT.md` existentes en el directorio actual. Si se le pasa una URL, primero ejecuta la auditoría completa.

**Salidas:** `GEO-REPORT-[marca].pdf` — portada con medidor de puntuación, desglose de puntuación con gráfico de barras, tabla de preparación de plataformas IA, tabla de acceso a rastreadores (codificada verde/rojo), hallazgos por severidad, plan de acción, y apéndice de metodología.

**Dependencias:** `scripts/generate_pdf_report.py` (requiere `pip install reportlab`).

Consulta [commands-reference.md](commands-reference.md) para `/geo report-pdf`.

---

### geo-prospect

**Propósito:** Un CRM ligero para gestionar prospectos de agencias GEO a través de un canal de ventas de cinco etapas (lead → calificado → propuesta → ganado → perdido). Persiste todos los datos en `~/.geo-prospects/prospects.json`.

**Entradas:** Nombres de dominios, detalles de contacto, actualizaciones de estado, y notas introducidas mediante sub-comandos.

**Salidas:** Actualizaciones a `prospects.json`; instantáneas de auditoría en `~/.geo-prospects/audits/`; tabla de resumen del pipeline impresa en la terminal.

**Sub-comandos clave:** `new`, `list`, `show`, `audit`, `note`, `status`, `won`, `lost`, `pipeline`.

**Dependencias:** `scripts/crm_dashboard.py` provee un rico tablero (dashboard) en la terminal (requiere `pip install rich`).

Consulta [commands-reference.md](commands-reference.md) para `/geo prospect`.

---

### geo-proposal

**Propósito:** Auto-genera una propuesta de servicio GEO lista para el cliente a partir de los datos de la auditoría, incluyendo el resumen ejecutivo, desglose de la puntuación, tres niveles de servicio con precios, proyección de ROI y línea de tiempo de compromiso.

**Entradas:** Nombre de dominio o ruta a un archivo de auditoría existente. Lee el registro de prospecto desde `~/.geo-prospects/prospects.json` si está disponible.

**Salidas:** `~/.geo-prospects/proposals/<dominio>-proposal-<fecha>.md` — una propuesta completa lista para enviarse. También actualiza el estado del registro del prospecto a `proposal`.

**Lógica de recomendación de niveles:** Puntuación 0–40 → Premium (€9,500/mes); 41–60 → Estándar (€5,000/mes); 61–75 → Básico (€2,500/mes).

Consulta [commands-reference.md](commands-reference.md) para `/geo proposal`.

---

### geo-compare

**Propósito:** Genera un informe delta mensual que compara dos auditorías GEO (base vs. actual), haciendo un seguimiento de las mejoras en la puntuación en todas las categorías y del estado de finalización de los elementos de acción.

**Entradas:** Un nombre de dominio o las rutas a dos archivos de auditoría. Lee archivos desde `~/.geo-prospects/audits/` ordenados por fecha si solo se proporciona el dominio.

**Salidas:** `~/.geo-prospects/reports/<dominio>-monthly-<YYYY-MM>.md` — barra de progreso de puntuación, tabla de desglose del antes y el después, tablas de delta de rastreadores y plataformas, estado del plan de acción, sección de victorias, nuevos problemas descubiertos, y una trayectoria de 6 meses.

Consulta [commands-reference.md](commands-reference.md) para `/geo compare`.

---

## Subagentes en Paralelo

Estos cinco agentes se ejecutan simultáneamente durante un `/geo audit` para reducir el tiempo total de ejecución. Cada uno devuelve una sección estructurada en markdown y una puntuación de categoría (0–100) que alimenta a la Puntuación GEO compuesta. Consulta [architecture.md](architecture.md) para el diagrama del flujo en paralelo.

### geo-ai-visibility

**Archivo:** `agents/geo-ai-visibility.md`

**Rol:** Especialista en GEO que cubre las cuatro dimensiones de visibilidad en IA de mayor peso.

**Se despacha cuando:** Inicia la Fase 2 del `/geo audit`.

**Qué hace:** Puntúa cada bloque de contenido para citabilidad (rúbrica de 5 dimensiones), parsea `robots.txt` para 12 rastreadores IA, valida el formato y la integridad de `llms.txt`, y escanea la presencia de la marca en YouTube, Reddit, Wikipedia y LinkedIn.

**Devuelve:** Puntuación de Visibilidad IA = Citabilidad (35%) + Menciones de Marca (30%) + Acceso a Rastreadores (25%) + llms.txt (10%).

**Sub-habilidades usadas:** geo-citability, geo-crawlers, geo-llmstxt, geo-brand-mentions.

---

### geo-platform-analysis

**Archivo:** `agents/geo-platform-analysis.md`

**Rol:** Especialista en optimización de plataformas.

**Se despacha cuando:** Inicia la Fase 2 del `/geo audit` (concurrente con otros agentes).

**Qué hace:** Evalúa la preparación para cada una de las cinco plataformas de búsqueda de IA — Google AI Overviews, Búsqueda Web de ChatGPT, Perplexity AI, Google Gemini, y Bing Copilot — utilizando rúbricas de puntuación y verificaciones de señales específicas a la plataforma.

**Devuelve:** Puntuaciones por plataforma (0–100 cada una) y un Promedio de Preparación de Plataformas; acciones de sinergia multiplataforma.

**Sub-habilidad usada:** geo-platform-optimizer.

---

### geo-technical

**Archivo:** `agents/geo-technical.md`

**Rol:** Especialista en SEO técnico.

**Se despacha cuando:** Inicia la Fase 2 del `/geo audit` (concurrente con otros agentes).

**Qué hace:** Obtiene el HTML sin procesar y los encabezados de respuesta; audita renderizado SSR frente a CSR (el control de mayor ponderación), la capacidad de rastreo, las meta etiquetas, los encabezados de seguridad, los indicadores de riesgo de Core Web Vitals, la optimización para dispositivos móviles, y la estructura de la URL.

**Devuelve:** Puntuación Técnica (0–100) con desglose por categoría; calificación de severidad de SSR (Crítica / Alta / Media / Baja).

**Sub-habilidad usada:** geo-technical.

---

### geo-content

**Archivo:** `agents/geo-content.md`

**Rol:** Especialista en calidad de contenido.

**Se despacha cuando:** Inicia la Fase 2 del `/geo audit` (concurrente con otros agentes).

**Qué hace:** Evalúa el E-E-A-T en sus cuatro dimensiones (25 puntos cada una), mide el recuento de palabras, legibilidad (Flesch), estructura de encabezados, vinculación interna, detecta señales de calidad de contenido por IA, evalúa la autoridad temática y la frescura del contenido.

**Devuelve:** Puntuación de Contenido (0–100); desglose de E-E-A-T; etiqueta de evaluación de contenido de IA.

**Sub-habilidad usada:** geo-content.

---

### geo-schema

**Archivo:** `agents/geo-schema.md`

**Rol:** Especialista en marcado Schema.

**Se despacha cuando:** Inicia la Fase 2 del `/geo audit` (concurrente con otros agentes).

**Qué hace:** Usa `fetch_page.py` para obtener el HTML sin procesar, detecta todos los bloques JSON-LD / Microdata / RDFa, valida cada uno según las especificaciones de Schema.org, audita enlaces de entidad `sameAs`, advierte sobre esquemas obsoletos o inyectados por JS, y genera plantillas JSON-LD listas para pegar para los esquemas faltantes.

**Devuelve:** Puntuación de Schema (0–100); inventario de esquemas validados; bloques de código JSON-LD generados.

**Sub-habilidad usada:** geo-schema.

---

## Scripts en Python

| Script | Propósito | Usado por |
|--------|---------|---------|
| `scripts/fetch_page.py` | Obtiene una URL y devuelve datos estructurados incluyendo el HTML en bruto, etiquetas meta, estructura de encabezados, recuento de palabras, y bloques JSON-LD parseados. Evita la conversión de markdown que aplica WebFetch, preservando el contenido de `<head>`. | geo-schema (habilidad + agente), geo-technical |
| `scripts/citability_scorer.py` | Puntúa pasajes de texto individuales para la preparación a la citación por IA utilizando cinco dimensiones ponderadas (calidad de respuesta, auto-contención, estructura, densidad estadística, originalidad/unicidad). Proveee `score_passage()` como una función invocable. | geo-citability |
| `scripts/brand_scanner.py` | Revisa la presencia de la marca en todas las plataformas citadas por IA (YouTube, Reddit, Wikipedia, LinkedIn). Provee funciones de verificación por plataforma e instrucciones para la verificación basada en WebFetch. Requiere `requests` y `beautifulsoup4`. | geo-brand-mentions |
| `scripts/llmstxt_generator.py` | Valida un `llms.txt` existente en contra de la especificación (Título H1, descripción tipo blockquote, secciones H2, URLs absolutas, descripciones) y genera un nuevo archivo desde los datos rastreados del sitio. | geo-llmstxt |
| `scripts/generate_pdf_report.py` | Genera un PDF de múltiples páginas desde un archivo de datos de auditoría JSON usando ReportLab. Renderiza medidores de puntuación, gráficos de barras, tablas codificadas por color, y un plan de acción. Acepta la ruta del archivo JSON como un argumento de CLI o vía stdin. Requiere `reportlab`. | geo-report-pdf |
| `scripts/crm_dashboard.py` | Renderiza un tablero interactivo rico en la terminal para el CRM de prospectos. Lee `~/.geo-prospects/prospects.json` y muestra las etapas del pipeline, MRR, y las vistas de detalles de prospectos. Requiere `rich`. | geo-prospect |

---

## Plantillas de Schema

Estos archivos JSON-LD en la carpeta `schema/` sirven como referencias de generación cuando `geo-schema` o `geo-report` necesitan producir datos estructurados listos para ser pegados. Todos los marcadores de posición siguen el patrón `TU_NOMBRE_DE_CAMPO` o `REPLACE_WITH_VALUE`.

| Plantilla | Cuándo usarlo |
|----------|-------------|
| `schema/organization.json` | Cualquier sitio empresarial; provee el tipo completo de Organization con enlaces `sameAs` a Wikipedia, Wikidata, LinkedIn, YouTube, GitHub, y Crunchbase, más `knowsAbout` para señales de tema de la entidad. |
| `schema/local-business.json` | Negocios con una ubicación física; extiende Organization con la dirección, coordenadas `geo`, horario de apertura, área de servicio, calificación agregada, y un catálogo de ofertas. |
| `schema/article-author.json` | Páginas de publicación y blogs; tipo Article con un autor de tipo Person completamente rellenado (credenciales, `sameAs`, `alumniOf`, `knowsAbout`) y una especificación `speakable` para legibilidad por asistentes de IA. |
| `schema/product-ecommerce.json` | Páginas de productos de comercio electrónico; tipo Product con Offer (incluyendo detalles de envío y política de devolución), AggregateRating, y entradas de Review individuales. |
| `schema/software-saas.json` | Páginas de productos SaaS; tipo SoftwareApplication con niveles de precio AggregateOffer, `featureList`, capturas de pantalla, y enlaces `sameAs` a G2, Capterra, ProductHunt, y GitHub. |
| `schema/website-searchaction.json` | La página de inicio de cada sitio; tipo WebSite con un `potentialAction` de SearchAction para habilitar el cuadro de búsqueda en los enlaces del sitio (sitelinks search box) y proporcionar a los sistemas de IA el punto de enlace de la búsqueda del sitio. |
