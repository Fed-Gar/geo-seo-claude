---
name: geo-compare
description: >
  Seguimiento mensual del cambio (delta) y reportes de progreso para clientes de GEO. Compara dos
  auditorías GEO (base vs. actual), calcula mejoras de puntuación en todas
  las categorías, realiza el seguimiento del completado de elementos de acción, y genera un
  reporte para el cliente del tipo "aquí está tu progreso". Úsalo cuando el usuario diga "comparar", "delta", "reporte mensual", "progreso",
  "confronta", "progressi", "report mensile", o cuando se ejecute una revisión mensual con el cliente.
version: 1.0.0
tags: [geo, business, delta, monthly, reporting, client, progress]
allowed-tools: Read, Write, Bash, Glob
---

# Generador de Reporte Mensual Delta GEO

## Propósito

La herramienta de retención más poderosa para una agencia de GEO: mostrar a los clientes **exactamente** qué mejoró desde que empezaron a trabajar contigo. Cada punto ganado en la puntuación GEO es prueba de valor. Esta habilidad genera el reporte de "aquí está tu progreso".

---

## Comandos

```
/geo compare <dominio>
/geo compare <archivo-base> <archivo-actual>
/geo compare electron-srl.com --month march-2026
```

**Ejemplos:**
```
/geo compare electron-srl.com
/geo compare ~/.geo-prospects/audits/electron-srl.com-2026-01-15.md ~/.geo-prospects/audits/electron-srl.com-2026-03-12.md
```

---

## Flujo de Trabajo

### Paso 1: Encontrar Archivos de Auditoría

Si solo se provee el dominio:
1. Busca en `~/.geo-prospects/audits/` por archivos que coincidan con `<dominio>-*.md`
2. Ordena por fecha
3. Usa el más antiguo como línea base (baseline), el más nuevo como actual
4. Si solo existe un archivo: úsalo como línea base, ejecuta una nueva auditoría rápida como actual
5. Si no existen archivos: sugiere ejecutar `/geo prospect audit <dominio>` primero

### Paso 2: Analizar Ambas Auditorías

Extrae de cada archivo de auditoría:
- Puntuación GEO General
- Puntuaciones por categoría (6 categorías)
- Puntuaciones por plataforma (5 plataformas)
- Estado de rastreadores IA (14 rastreadores)
- Lista de problemas críticos
- Lista de elementos de acción con estado

### Paso 3: Calcular Deltas

Para cada métrica:
- Delta = Actual - Línea base (Baseline)
- Tendencia = ▲ (mejorado), ▼ (disminuido), ── (sin cambios)
- Código de colores en el reporte: verde (+), rojo (-), gris (=)

### Paso 4: Generar Reporte Mensual

Salida a `~/.geo-prospects/reports/<dominio>-monthly-<fecha>.md`

---

## Plantilla de Reporte

Genera el siguiente documento:

```markdown
# Reporte de Progreso Mensual GEO
## [NOMBRE EMPRESA] — [MES AÑO]

**Período de reporte:** [FECHA BASE] → [FECHA ACTUAL]
**Preparado por:** [NOMBRE AGENCIA]
**Referencia del reporte:** GEO-MONTHLY-[DOMINIO]-[AAMMDD]

---

## Resumen Ejecutivo

[2-3 oraciones: Qué mejoró, cuál es la tendencia, en qué enfocarse el próximo mes.]

Ejemplo: "La puntuación GEO de Electron Srl mejoró de 32 a 44 este mes (+12 puntos), ubicando al sitio firmemente en el nivel 'Por debajo del promedio' y en camino a alcanzar 'Moderado' para Mayo. Las mayores victorias fueron el acceso de rastreadores IA (+3 rastreadores ahora permitidos) y la implementación de esquemas (+esquemas Organization y LocalBusiness activos). El enfoque del próximo mes es la citabilidad del contenido — la brecha restante con mayor peso."

---

## Progreso de Puntuación GEO

```
PUNTUACIÓN GEO GENERAL

  Línea base [▓▓▓▓░░░░░░░░░░░░░░░░]  32/100  (Crítico)
  Actual     [▓▓▓▓▓▓▓▓░░░░░░░░░░░░]  44/100  (Por debajo del promedio)
  Cambio     ▲ +12 puntos (+37.5%)

  Objetivo:  65/100 para el Mes 6 (en camino ✓)
```

---

## Desglose de Puntuación: Antes vs. Después

| Categoría | Base | Actual | Cambio | Tendencia |
|----------|---------|---------|--------|-------|
| Citabilidad & Visibilidad IA | [X]/100 | [X]/100 | [+/-X] | [▲/▼/──] |
| Señales de Autoridad de Marca | [X]/100 | [X]/100 | [+/-X] | [▲/▼/──] |
| Calidad de Contenido & E-E-A-T | [X]/100 | [X]/100 | [+/-X] | [▲/▼/──] |
| Fundamentos Técnicos | [X]/100 | [X]/100 | [+/-X] | [▲/▼/──] |
| Datos Estructurados | [X]/100 | [X]/100 | [+/-X] | [▲/▼/──] |
| Optimización de Plataformas | [X]/100 | [X]/100 | [+/-X] | [▲/▼/──] |
| **TOTAL** | **[X]/100** | **[X]/100** | **[+/-X]** | **[▲/▼]** |

---

## Preparación de Plataformas: Antes vs. Después

| Plataforma IA | Base | Actual | Cambio |
|-------------|---------|---------|--------|
| Google AI Overviews | [X]/100 | [X]/100 | [+/-X] |
| ChatGPT Web Search | [X]/100 | [X]/100 | [+/-X] |
| Perplexity AI | [X]/100 | [X]/100 | [+/-X] |
| Google Gemini | [X]/100 | [X]/100 | [+/-X] |
| Bing Copilot | [X]/100 | [X]/100 | [+/-X] |

---

## Cambios en el Acceso a Rastreadores IA

| Rastreador | Base | Actual | Cambio |
|---------|---------|---------|--------|
| GPTBot (ChatGPT) | Bloqueado/Permitido | Bloqueado/Permitido | ✓ Arreglado / Sin cambio |
| ClaudeBot (Anthropic) | Bloqueado/Permitido | Bloqueado/Permitido | ✓ Arreglado / Sin cambio |
| PerplexityBot | Bloqueado/Permitido | Bloqueado/Permitido | ✓ Arreglado / Sin cambio |
| Google-Extended (Gemini) | Bloqueado/Permitido | Bloqueado/Permitido | ✓ Arreglado / Sin cambio |
| Bingbot | Bloqueado/Permitido | Bloqueado/Permitido | ✓ Arreglado / Sin cambio |

[Muestra solo los rastreadores que cambiaron, o todos si son pocos.]

---

## Progreso del Plan de Acción

### Victorias Rápidas — Actualización de Estado

| # | Acción | Asignado | Estado | Impacto |
|---|--------|---------|--------|--------|
| 1 | Permitir todos los rastreadores IA en robots.txt | Dev cliente | ✅ Hecho | +3 rastreadores |
| 2 | Añadir esquema de Organización al inicio | Dev cliente | ✅ Hecho | Puntuación esquema +15 |
| 3 | Crear llms.txt | Agencia | ✅ Hecho | Visibilidad IA +8 |
| 4 | Añadir firmas de autor a todos los artículos | Contenido cliente | 🔄 En progreso | — |
| 5 | Arreglar meta descripciones (faltan en 47 pág.) | Dev cliente | ❌ No iniciado | — |

**Victorias rápidas completadas: [X]/[Y] ([%])**

### Medio Plazo — Actualización de Estado

| # | Acción | Mes Objetivo | Estado |
|---|--------|-------------|--------|
| 1 | Reestructurar top 10 páginas con Preg/Resp | Mes 2 | 🔄 3/10 hecho |
| 2 | E-E-A-T: Crear páginas de autor | Mes 2 | ❌ No iniciado |
| 3 | Registrar Bing Webmaster Tools | Mes 1 | ✅ Hecho |
| 4 | Implementar IndexNow | Mes 2 | 🔄 En progreso |

### Estratégico — Actualización de Estado

| # | Acción | Objetivo | Estado |
|---|--------|--------|--------|
| 1 | Creación de entidad en Wikipedia | Mes 4 | 📋 Planeado |
| 2 | Lanzamiento de canal de YouTube | Mes 3 | 📋 Planeado |
| 3 | Presencia en Reddit (subreddits industria) | Mes 3 | 📋 Planeado |

---

## Victorias de Este Mes

> Usa esta sección para celebrar — los clientes necesitan ver el valor claramente.

✅ **[VICTORIA 1]:** [Resultado específico y tangible — ej., "GPTBot y ClaudeBot ahora están permitidos. ChatGPT ahora puede rastrear y citar tu contenido."]
✅ **[VICTORIA 2]:** [ej., "Esquema Organization implementado en la página de inicio. Tu entidad de marca ahora es legible por máquinas."]
✅ **[VICTORIA 3]:** [ej., "llms.txt creado y desplegado en electron-srl.com/llms.txt — uno del escaso ~12% de sitios en tu industria que lo tienen."]

---

## Nuevos Problemas Descubiertos

> Problemas encontrados en la auditoría actual que no estaban en la línea base.

⚠️ **[PROBLEMA 1]:** [Qué es, qué significa, cómo lo arreglaremos]
⚠️ **[PROBLEMA 2]:** [Qué es, qué significa, cómo lo arreglaremos]

---

## Enfoque del Próximo Mes

### Acciones Prioritarias para [PRÓXIMO MES]:

| Prioridad | Acción | Propietario | Impacto Esperado |
|----------|--------|-------|----------------|
| 1 | [Acción mayor ROI] | [Agencia/Cliente] | +[X] puntos GEO |
| 2 | [Segunda prioridad] | [Agencia/Cliente] | +[X] puntos GEO |
| 3 | [Tercera prioridad] | [Agencia/Cliente] | +[X] puntos GEO |

**Puntuación GEO Objetivo para el próximo mes:** [ACTUAL + ganancia estimada]/100

---

## Trayectoria de 6 Meses

| Mes | Fecha | Puntuación | Delta | Logro Clave |
|-------|------|-------|-------|----------------|
| Línea Base | [Fecha] | [Puntuación] | — | Auditoría inicial |
| Mes 1 | [Fecha] | [Puntuación] | [+X] | Victorias rápidas implementadas |
| Mes 2 | [Fecha] | [Puntuación] | [+X] | *Mes actual* |
| Mes 3 | [Fecha] | — | — | Citabilidad de contenido |
| Mes 4 | — | — | — | Autoridad de marca |
| Mes 5 | — | — | — | Iniciativas estratégicas |
| Mes 6 | — | **Objetivo: [X]** | — | Revisión completa |

[Llena solo las filas de meses que ya ocurrieron. Muestra filas proyectadas como "—"]

---

## Impacto Estimado en Negocio

Basado en la mejora de [X] puntos este mes:

- **Probabilidad de cita IA:** Incrementada en aprox. [X]%
- **Rastreadores con acceso:** [X]/14 → [Y]/14 (mejor cobertura en [plataformas])
- **Mejora estimada de tráfico mensual referido por IA:** +[X]% (conservador)
- **Valor del tráfico a tasas de conversión actuales:** +€[X]/mes en valor orgánico

*Nota: El impacto completo en el tráfico por los cambios GEO típicamente toma de 4-8 semanas para materializarse a medida que las plataformas de IA re-indexan y actualizan sus bases de conocimiento.*

---

*Reporte Mensual GEO — [NOMBRE EMPRESA] — [FECHA]*
*¿Preguntas o comentarios? [EMAIL CONTACTO]*
```

---

## Lógica de Cálculo de Delta

Al analizar dos archivos de auditoría, busca estos patrones:

```
Marcadores de puntuación a extraer:
- "GEO Score: XX/100"
- "Overall Score: XX"
- "AI Citability: XX/100"
- "Brand Authority: XX/100"
- "Technical: XX/100"
- "Schema: XX/100"
- "Platform: XX/100"
- "Content: XX/100"
- "GPTBot: Allowed/Blocked"
- "ClaudeBot: Allowed/Blocked"
```

Si no se encuentran las puntuaciones exactas en los archivos de auditoría, usa el análisis contextual de los hallazgos escritos para estimar puntuaciones aproximadas basándose en los problemas descritos.

---

## Interpretación de Tendencia

| Delta | Símbolo de Tendencia | Significado |
|-------|-------------|---------|
| +5 o más | ▲▲ | Fuerte mejora |
| +1 a +4 | ▲ | Mejora |
| 0 | ── | Sin cambio |
| -1 a -4 | ▼ | Ligera disminución |
| -5 o más | ▼▼ | Fuerte disminución — necesita discusión |

Una disminución no es necesariamente mala — puede significar que nuevos problemas fueron descubiertos en la auditoría nueva que no eran visibles antes. Encuadra las disminuciones como "oportunidades recientemente descubiertas".

---

## Salida

1. Guarda el reporte en `~/.geo-prospects/reports/<dominio>-monthly-<YYYY-MM>.md`
2. Imprime la confirmación con métricas clave:
   ```
   ✓ Reporte mensual generado: ~/.geo-prospects/reports/electron-srl.com-monthly-2026-03.md

   RESUMEN:
   Puntuación GEO: 32 → 44 (+12 puntos) ▲
   Victorias rápidas completadas: 3/5 (60%)
   Nuevos problemas encontrados: 2 (menores)
   En camino para objetivo del Mes 6: SÍ (65/100)
   ```
3. Sugiere siguiente acción: "Compartir con el cliente o ejecutar `/geo report-pdf` para una versión visual"
