---
name: geo
description: >
  Herramienta de análisis SEO con prioridad GEO (Generative Engine Optimization). Optimiza sitios web para motores de búsqueda con IA
  (ChatGPT, Claude, Perplexity, Gemini, Google AI Overviews) manteniendo
  las bases del SEO tradicional. Realiza auditorías GEO completas, puntuación de citabilidad,
  análisis de rastreadores de IA, generación de llms.txt, escaneo de menciones de marca, optimización
  específica por plataforma, marcado de esquema (schema), SEO técnico, calidad de contenido (E-E-A-T), y
  generación de reportes GEO listos para clientes. Usar cuando el usuario diga "geo", "seo", "audit", "auditar", "auditoria",
  "AI search", "AI visibility", "visibilidad IA", "optimize", "optimizar", "citability", "citabilidad", "llms.txt", "schema", "esquema",
  "brand mentions", "menciones de marca", "GEO report", "reporte GEO", o cualquier URL para análisis.
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# Herramienta de Análisis GEO-SEO — Claude Code Skill (Febrero 2026)

> **Filosofía:** Prioridad GEO, soporte SEO. La búsqueda con IA está devorando a la búsqueda tradicional.
> Esta herramienta optimiza hacia donde va el tráfico, no donde solía estar.

---

## Referencia Rápida

| Comando | Qué Hace |
|---------|-------------|
| `/geo audit <url>` | Auditoría GEO + SEO completa con subagentes en paralelo |
| `/geo page <url>` | Análisis GEO profundo de una sola página |
| `/geo citability <url>` | Puntúa el contenido según su preparación para ser citado por IA |
| `/geo crawlers <url>` | Verifica acceso de rastreadores de IA (análisis robots.txt) |
| `/geo llmstxt <url>` | Analiza o genera archivo llms.txt |
| `/geo brands <url>` | Escanea menciones de marca en plataformas citadas por IA |
| `/geo platforms <url>` | Optimización específica por plataforma (ChatGPT, Perplexity, Google AIO) |
| `/geo schema <url>` | Detecta, valida y genera datos estructurados (schema) |
| `/geo technical <url>` | Auditoría SEO técnica tradicional |
| `/geo content <url>` | Evaluación de calidad del contenido y E-E-A-T |
| `/geo report <url>` | Genera entregable GEO listo para el cliente |
| `/geo report-pdf <url>` | Genera reporte profesional en PDF con gráficos y puntuaciones |
| `/geo quick <url>` | Instantánea de visibilidad GEO de 60 segundos |
| `/geo prospect <cmd>` | CRM-ligero: gestionar prospectos a través del embudo de ventas |
| `/geo proposal <domain>` | Autogenerar propuesta para cliente a partir de datos de auditoría |
| `/geo compare <domain>` | Reporte de diferencia mensual: mostrar mejoras de puntuación al cliente |
| `/geo update` | Obtener las últimas actualizaciones de la habilidad GEO desde el repositorio principal |

---

## Contexto del Mercado (Por qué importa el GEO)

| Métrica | Valor | Fuente |
|--------|-------|--------|
| Mercado de servicios GEO (2025) | $850M-$886M | Yahoo Finance / Superlines |
| Mercado GEO proyectado (2031) | $7.3B (34% CAGR) | Analistas de la industria |
| Crecimiento de sesiones referidas por IA | +527% (Ene-May 2025) | SparkToro |
| Conversión de tráfico IA vs orgánico | 4.4x mayor | Datos de la industria |
| Alcance de Google AI Overviews | 1.5B usuarios/mes, 200+ países | Google |
| Usuarios activos semanales de ChatGPT | 900M+ | OpenAI |
| Consultas mensuales de Perplexity | 500M+ | Perplexity |
| Gartner: caída del tráfico de búsqueda para 2028 | -50% | Gartner |
| Marketers invirtiendo en GEO | Solo 23% | Encuestas de la industria |
| Menciones de marca vs backlinks para IA | Correlación 3x más fuerte | Ahrefs (Dic 2025) |

---

## Lógica de Orquestación

### Auditoría Completa (`/geo audit <url>`)

**Fase 1: Descubrimiento (Secuencial)**
1. Obtener HTML de la página de inicio (curl o WebFetch)
2. Detectar tipo de negocio (SaaS, Local, E-commerce, Publicador, Agencia, Otro)
3. Extraer páginas clave de sitemap.xml o enlaces internos (hasta 50 páginas)

**Fase 2: Análisis en Paralelo (Delegar a Subagentes)**
Lanzar estos 5 subagentes simultáneamente:

| Subagente | Archivo | Responsabilidad |
|----------|------|---------------|
| geo-ai-visibility | `agents/geo-ai-visibility.md` | Auditoría GEO, citabilidad, rastreadores de IA, llms.txt, menciones de marca |
| geo-platform-analysis | `agents/geo-platform-analysis.md` | Optimización específica por plataforma (ChatGPT, Perplexity, Google AIO) |
| geo-technical | `agents/geo-technical.md` | SEO Técnico, Core Web Vitals, rastreabilidad, indexabilidad |
| geo-content | `agents/geo-content.md` | Calidad de contenido, E-E-A-T, legibilidad, detección de contenido de IA |
| geo-schema | `agents/geo-schema.md` | Detección, validación y generación de marcado de esquema |

**Fase 3: Síntesis (Secuencial)**
1. Recopilar reportes de todos los subagentes
2. Calcular Puntuación GEO compuesta (0-100)
3. Generar plan de acción priorizado
4. Producir reporte listo para cliente

### Metodología de Puntuación

| Categoría | Peso | Medido Por |
|----------|--------|-------------|
| Visibilidad y Citabilidad por IA | 25% | Puntuación de pasajes, calidad del bloque de respuestas, acceso de rastreadores de IA |
| Señales de Autoridad de Marca | 20% | Menciones en Reddit, YouTube, Wikipedia, LinkedIn; presencia de entidad |
| Calidad de Contenido y E-E-A-T | 20% | Señales de experiencia, datos originales, credenciales del autor |
| Fundamentos Técnicos | 15% | SSR, Core Web Vitals, rastreabilidad, móvil, seguridad |
| Datos Estructurados | 10% | Integridad de esquema, validación JSON-LD, elegibilidad de resultados enriquecidos |
| Optimización de Plataforma | 10% | Preparación específica de plataforma (Google AIO, ChatGPT, Perplexity) |

---

## Detección de Tipo de Negocio

Analizar página de inicio en busca de patrones:

| Tipo | Señales |
|------|---------|
| **SaaS** | Página de precios, "Regístrate", "Prueba gratis", "/app", "/dashboard", docs de API |
| **Servicio Local** | Número de teléfono, dirección, "Cerca de mí", mapa de Google embebido, área de servicio |
| **E-commerce** | Páginas de producto, carrito, "Añadir al carrito", elementos de precio, schema Product |
| **Publicador** | Blog, artículos, firmas de autor, fechas de publicación, schema Article |
| **Agencia** | Portafolio, casos de estudio, "Nuestros servicios", logos de clientes, testimonios |
| **Otro** | Por defecto — aplicar mejores prácticas generales de GEO |

Ajustar recomendaciones basadas en el tipo detectado. Negocios locales necesitan esquema LocalBusiness y optimización del Perfil de Empresa de Google. SaaS necesita esquema SoftwareApplication y estrategia de página de comparación. E-commerce necesita esquema Product y agregación de reseñas.

---

## Subhabilidades (14 Componentes Especializados)

| # | Habilidad | Directorio | Propósito |
|---|-------|-----------|---------|
| 1 | geo-audit | `skills/geo-audit/` | Orquestación de auditoría completa y puntuación |
| 2 | geo-citability | `skills/geo-citability/` | Preparación para citación por IA a nivel de pasaje |
| 3 | geo-crawlers | `skills/geo-crawlers/` | Acceso de rastreadores de IA y robots.txt |
| 4 | geo-llmstxt | `skills/geo-llmstxt/` | Análisis y generación del estándar llms.txt |
| 5 | geo-brand-mentions | `skills/geo-brand-mentions/` | Presencia de marca en plataformas citadas por IA |
| 6 | geo-platform-optimizer | `skills/geo-platform-optimizer/` | Optimización de búsqueda por IA específica por plataforma |
| 7 | geo-schema | `skills/geo-schema/` | Datos estructurados para descubribilidad por IA |
| 8 | geo-technical | `skills/geo-technical/` | Bases de SEO técnico |
| 9 | geo-content | `skills/geo-content/` | Calidad de contenido y E-E-A-T |
| 10 | geo-report | `skills/geo-report/` | Generación de entregable listo para cliente |
| 11 | geo-prospect | `skills/geo-prospect/` | CRM-ligero para gestión de prospectos y clientes |
| 12 | geo-proposal | `skills/geo-proposal/` | Autogenerar propuestas para clientes con datos de auditoría |
| 13 | geo-compare | `skills/geo-compare/` | Seguimiento de diferencias mensuales y reportes de progreso |
| 14 | geo-update | `skills/geo-update/` | Obtener últimas actualizaciones desde repositorio principal |

---

## Subagentes (5 Trabajadores Paralelos)

| Agente | Archivo | Habilidades Usadas |
|-------|------|-------------|
| geo-ai-visibility | `agents/geo-ai-visibility.md` | geo-citability, geo-crawlers, geo-llmstxt, geo-brand-mentions |
| geo-platform-analysis | `agents/geo-platform-analysis.md` | geo-platform-optimizer |
| geo-technical | `agents/geo-technical.md` | geo-technical |
| geo-content | `agents/geo-content.md` | geo-content |
| geo-schema | `agents/geo-schema.md` | geo-schema |

---

## Archivos de Salida

Todos los comandos generan salidas estructuradas:

| Comando | Archivo de Salida |
|---------|------------|
| `/geo audit` | `GEO-AUDIT-REPORT.md` |
| `/geo page` | `GEO-PAGE-ANALYSIS.md` |
| `/geo citability` | `GEO-CITABILITY-SCORE.md` |
| `/geo crawlers` | `GEO-CRAWLER-ACCESS.md` |
| `/geo llmstxt` | `llms.txt` (listo para implementar) |
| `/geo brands` | `GEO-BRAND-MENTIONS.md` |
| `/geo platforms` | `GEO-PLATFORM-OPTIMIZATION.md` |
| `/geo schema` | `GEO-SCHEMA-REPORT.md` + JSON-LD generado |
| `/geo technical` | `GEO-TECHNICAL-AUDIT.md` |
| `/geo content` | `GEO-CONTENT-ANALYSIS.md` |
| `/geo report` | `GEO-CLIENT-REPORT.md` (listo para presentación) |
| `/geo report-pdf` | `GEO-REPORT.pdf` (PDF profesional con gráficos) |
| `/geo quick` | Resumen en línea (sin archivo) |
| `/geo prospect` | Actualiza `~/.geo-prospects/prospects.json` |
| `/geo proposal` | `~/.geo-prospects/proposals/<domain>-proposal-<date>.md` |
| `/geo compare` | `~/.geo-prospects/reports/<domain>-monthly-<YYYY-MM>.md` |

---

## Generación de Reporte PDF

El comando `/geo report-pdf <url>` convierte `GEO-AUDIT-REPORT.md` en un PDF estilizado, listo para el cliente.

### Requisitos
- **pandoc** — `brew install pandoc`
- **Google Chrome** — `/Applications/Google Chrome.app/` (instalación estándar Mac)

No requiere dependencias de Python para la generación de PDF.

### Qué Incluye el PDF
- **Página de portada** — gradiente azul marino oscuro, insignia de puntuación GEO, metadatos de marca/dominio/fecha/ubicación
- **Tablas de puntuación con colores** — celdas con valores `XX/100` se colorean automáticamente de verde/azul/ámbar/naranja/rojo
- **Hallazgos etiquetados por severidad** — Secciones Crítico/Alto/Medio/Bajo obtienen bloques resaltados con borde izquierdo coloreado
- **Saltos de página por sección** — las secciones principales saltan a nuevas páginas automáticamente
- **Bloques de código estilizados** — las plantillas de esquema JSON se renderizan con tema oscuro monoespaciado

### Plantillas
Se incluyen en `~/.claude/skills/geo/templates/`:
- `geo-report-style.css` — hoja de estilos (edita colores, fuentes, diseño aquí)
- `geo-report-template.html` — plantilla HTML pandoc (edita campos de portada aquí)

### Flujo de Trabajo
1. Ejecuta `/geo audit <url>` para producir `GEO-AUDIT-REPORT.md`
2. Ejecuta `/geo report-pdf` — extrae metadatos del reporte y ejecuta:
   ```bash
   pandoc GEO-AUDIT-REPORT.md \
     --to html5 --standalone --embed-resources \
     --template ~/.claude/skills/geo/templates/geo-report-template.html \
     --css ~/.claude/skills/geo/templates/geo-report-style.css \
     --metadata brand_name="..." --metadata geo_score="..." \
     -o GEO-REPORT.html

   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
     --headless=new --disable-gpu --no-sandbox \
     --print-to-pdf="$(pwd)/GEO-REPORT.pdf" \
     --print-to-pdf-no-header --no-pdf-header-footer \
     --virtual-time-budget=5000 \
     "file://$(pwd)/GEO-REPORT.html"
   ```
3. Salida: `GEO-REPORT.pdf` en el directorio actual

---

## Controles de Calidad

- **Límite de rastreo:** Máx. 50 páginas por auditoría (enfoque en calidad sobre cantidad)
- **Tiempo de espera:** 30 segundos por obtención de página
- **Límite de peticiones:** 1 segundo de retraso entre solicitudes, máx. 5 simultáneas
- **Robots.txt:** Siempre respetar, siempre verificar
- **Detección de duplicados:** Omitir páginas con >80% de similitud de contenido

---

## Ejemplos de Inicio Rápido

```
# Auditoría GEO completa de un sitio web
/geo audit https://example.com

# Verificar si los bots de IA pueden ver tu sitio
/geo crawlers https://example.com

# Puntuar una página específica para citabilidad por IA
/geo citability https://example.com/blog/mejor-articulo

# Generar un archivo llms.txt para tu sitio
/geo llmstxt https://example.com

# Obtener una instantánea de visibilidad de 60 segundos
/geo quick https://example.com

# Generar un reporte listo para clientes
/geo report https://example.com
```
