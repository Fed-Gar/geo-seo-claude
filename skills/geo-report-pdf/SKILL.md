---
name: geo-report-pdf
description: Genera un reporte profesional en PDF de una auditoría GEO utilizando pandoc + Chrome headless. Convierte GEO-AUDIT-REPORT.md en un PDF estilizado, listo para el cliente, con página de portada, tablas de puntuación codificadas por color, hallazgos etiquetados por severidad y una hoja de ruta de 90 días.
version: 2.0.0
author: geo-seo-claude
tags: [geo, pdf, report, client-deliverable, professional]
allowed-tools: Read, Grep, Glob, Bash, Write
---

# Generador de Reporte PDF GEO (tubería pandoc)

## Requisitos previos

- **pandoc** — `brew install pandoc`
- **Google Chrome** — debe estar instalado en `/Applications/Google Chrome.app/`

Sin dependencias de Python. Sin ReportLab. Sin manipulación de datos JSON.

## Cómo Funciona

1. Lee `GEO-AUDIT-REPORT.md` en el directorio actual (creado por `/geo audit`)
2. Extrae los metadatos de la portada del reporte (nombre de la marca, dominio, puntuación GEO, fecha, ubicaciones)
3. Ejecuta `pandoc` con la plantilla HTML + CSS integrada para producir un `GEO-REPORT.html` autónomo
4. Ejecuta Chrome en modo headless (sin interfaz) para imprimir el HTML a `GEO-REPORT.pdf`

La plantilla de pandoc (`~/.claude/skills/geo/templates/geo-report-template.html`) inyecta:
- Una sección de portada completa azul marino oscuro con la insignia de la puntuación GEO
- Metadatos de la portada por sección (fecha, tipo de negocio, ubicaciones, plataforma)
- JavaScript que se ejecuta dentro de Chrome antes de imprimir para codificar por colores las celdas de puntuación y etiquetar por severidad las secciones de hallazgos

## Flujo de Trabajo

### Paso 1: Comprobar el reporte de auditoría

Busca `GEO-AUDIT-REPORT.md` en el directorio actual. Si no está presente, dile al usuario que ejecute `/geo audit <url>` primero.

### Paso 2: Extraer metadatos de portada del reporte

Lee la parte superior de `GEO-AUDIT-REPORT.md` y extrae:

| Campo | Dónde encontrarlo |
|---|---|
| `brand_name` | Primer título H1 (después de "GEO Audit Report:") |
| `domain` | Segunda línea en negrita (ej. `**Domain:** alexamediasolutions.com`) |
| `geo_score` | Línea que coincide con `## Overall GEO Score: XX / 100` |
| `score_label` | Palabra después de la puntuación en esa misma línea (ej. "Poor" (Pobre), "Fair" (Aceptable), "Good" (Bueno)) |
| `date` | Línea de `**Audit Date:**` |
| `business_type` | Línea de `**Business Type:**` |
| `locations` | Línea de `**Locations:**` |
| `platform` | Línea de `**CMS:**` |

### Paso 3: Ejecutar pandoc

```bash
pandoc GEO-AUDIT-REPORT.md \
  --to html5 \
  --standalone \
  --embed-resources \
  --template ~/.claude/skills/geo/templates/geo-report-template.html \
  --css ~/.claude/skills/geo/templates/geo-report-style.css \
  --metadata title="Reporte de Auditoría GEO — <brand_name>" \
  --metadata brand_name="<brand_name>" \
  --metadata domain="<domain>" \
  --metadata geo_score="<geo_score>" \
  --metadata score_label="<score_label>" \
  --metadata date="<date>" \
  --metadata business_type="<business_type>" \
  --metadata locations="<locations>" \
  --metadata platform="<platform>" \
  -o GEO-REPORT.html
```

Reemplaza los marcadores `<field>` con los valores extraídos en el Paso 2. Si no se encuentra un campo en el reporte, omite esa bandera `--metadata` — la plantilla tiene valores predeterminados sensatos.

### Paso 4: Ejecutar Chrome headless

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new \
  --disable-gpu \
  --no-sandbox \
  --print-to-pdf="$(pwd)/GEO-REPORT.pdf" \
  --print-to-pdf-no-header \
  --no-pdf-header-footer \
  --virtual-time-budget=5000 \
  "file://$(pwd)/GEO-REPORT.html"
```

### Paso 5: Reportar finalización

Dile al usuario:
- Se generó `GEO-REPORT.pdf` en el directorio actual
- Tamaño del archivo
- Opcionalmente: `open GEO-REPORT.pdf` para previsualizarlo

## Qué Contiene el PDF

- **Página de portada** — Degradado azul marino oscuro, nombre de la marca, dominio, insignia de puntuación GEO (coloreada por puntuación), fecha de auditoría, tipo de negocio, ubicaciones, plataforma CMS
- **Tablas de puntuación** — Las celdas que contienen `XX/100` están codificadas por colores: ≥80 verde, ≥65 azul, ≥50 ámbar, ≥35 naranja, <35 rojo
- **Secciones de hallazgos** — Los encabezados `h3` que contienen "Critical / High / Medium / Low" (Crítico/Alto/Medio/Bajo) obtienen bloques de llamada con borde izquierdo coloreados por severidad (rojo / naranja / amarillo / verde)
- **Saltos de página de sección** — Las secciones principales (Prioridad Alta, Hoja de Ruta de 90 Días, Resumen de Puntuación de Componentes, Esquema Generado) saltan a nuevas páginas automáticamente
- **Bloques de código** — Las plantillas de esquema JSON se renderizan con estilo monoespaciado de tema oscuro
- **Pie de página** — Nombre de la marca · Auditoría GEO · fecha + números de página (vía `@page` de CSS)

## Personalización del Reporte

- **Colores / tipografía** — Edita `~/.claude/skills/geo/templates/geo-report-style.css`
- **Diseño de portada** — Edita `~/.claude/skills/geo/templates/geo-report-template.html`
- **Umbrales de puntuación para codificación de colores** — Edita la función `scoreColor()` en el bloque `<script>` de la plantilla
- **Qué secciones obtienen saltos de página** — Edita el array `breakBefore` en el bloque `<script>` de la plantilla

## Solución de Problemas

| Problema | Solución |
|---|---|
| `pandoc: command not found` | `brew install pandoc` |
| No se encuentra Chrome | Verifica ruta: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome` |
| PDF está en blanco / vacío | Aumenta `--virtual-time-budget` a 8000 |
| Metadatos de portada faltan | Comprueba que GEO-AUDIT-REPORT.md tenga el formato de cabecera estándar |
| Las fuentes no cargan | El PDF se renderiza fuera de línea; se usan fuentes del sistema como alternativa — esto es esperado |
