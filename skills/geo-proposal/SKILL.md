---
name: geo-proposal
description: >
  Genera automáticamente una propuesta de servicios GEO profesional y lista para el cliente a partir de datos de auditoría.
  Crea una propuesta completa en markdown y PDF incluyendo resumen ejecutivo, hallazgos,
  paquetes de servicios recomendados (Básico/Estándar/Premium), precios, línea de tiempo y términos.
  Úsalo cuando el usuario diga "propuesta", "proposal", "proposta", "offerta", "preventivo", "generar propuesta",
  o después de completar una auditoría GEO para un prospecto.
version: 1.0.0
tags: [geo, business, proposal, sales, pricing, client]
allowed-tools: Read, Write, Bash, Glob, WebFetch
---

# Generador de Propuesta GEO

## Propósito

Generar una propuesta de servicios GEO completamente personalizada y lista para el cliente que:
1. Extraiga hallazgos directamente de la auditoría GEO del prospecto
2. Traduzca las brechas técnicas en puntos de dolor comerciales (pain points)
3. Presente 3 niveles de servicio con precios claros
4. Incluya una proyección de ROI realista
5. Genere un documento markdown profesional listo para enviar

---

## Comando

```
/geo proposal <dominio-o-archivo-auditoria> [--tier basic|standard|premium] [--client-name "Nombre"] [--monthly EUR]
```

**Ejemplos:**
```
/geo proposal electron-srl.com
/geo proposal electron-srl.com --tier standard --client-name "Electron Srl"
/geo proposal ~/.geo-prospects/audits/electron-srl.com-2026-03-12.md
```

---

## Flujo de Trabajo

### Paso 1: Cargar Datos de Auditoría

1. Comprueba si existe `~/.geo-prospects/audits/<dominio>*.md`
2. Si no, sugiere ejecutar `/geo quick <dominio>` primero
3. Extrae de la auditoría:
   - Puntuación GEO (general y por categoría)
   - Top 3 hallazgos críticos
   - Lista de victorias rápidas (quick wins)
   - Tipo de negocio
   - Impacto estimado en tráfico orgánico

### Paso 2: Personalizar la Propuesta

Rellena automáticamente la plantilla de propuesta con:
- Nombre de la empresa (del dominio o registro de prospecto)
- Puntuación GEO y etiqueta de nivel
- 3 puntos de dolor más críticos (traducidos a lenguaje comercial)
- Ingresos estimados en riesgo por el cambio a búsqueda por IA
- Nivel de servicio recomendado basado en la puntuación:
  - Puntuación 0-40 → Recomendar Premium (problemas críticos necesitan atención total)
  - Puntuación 41-60 → Recomendar Estándar (brechas significativas, necesita trabajo mensual)
  - Puntuación 61-75 → Recomendar Básico (base sólida, necesita monitoreo)

### Paso 3: Generar Archivo de Propuesta

Genera la salida en `~/.geo-prospects/proposals/<dominio>-proposal-<fecha>.md`
También actualiza el registro del prospecto si existe en `~/.geo-prospects/prospects.json`

---

## Plantilla de Propuesta

Genera el siguiente documento, rellenando todos los `[MARCADORES]` con datos reales de la auditoría:

---

```markdown
# Propuesta de Optimización GEO
## [NOMBRE EMPRESA] — Visibilidad en Búsqueda por IA

**Preparado por:** [NOMBRE DE TU AGENCIA]
**Preparado para:** [NOMBRE CONTACTO], [NOMBRE EMPRESA]
**Fecha:** [FECHA]
**Válido hasta:** [FECHA + 30 DÍAS]
**Referencia:** GEO-PROP-[AAMMDD]-[DOMINIO]

---

## Resumen Ejecutivo

[NOMBRE EMPRESA] opera en [INDUSTRIA] y sirve a clientes en todo [GEOGRAFÍA].
Nuestra auditoría GEO de [DOMINIO], llevada a cabo el [FECHA], revela una Puntuación
de Preparación GEO de **[PUNTUACIÓN]/100 ([ETIQUETA DE NIVEL])**.

Esto significa que su sitio web actualmente tiene [DESCRIPCIÓN DE NIVEL — usa la tabla de interpretación de puntuación].
Como la búsqueda impulsada por IA (ChatGPT, Google AI Overviews, Perplexity) ahora influye en
el **[X]% del descubrimiento en línea** y está creciendo a un 527% interanual, esta brecha
representa un riesgo medible para su canal de ventas (pipeline).

Los tres problemas más urgentes son:
1. **[HALLAZGO CRÍTICO 1]** — [Impacto de negocio en una oración]
2. **[HALLAZGO CRÍTICO 2]** — [Impacto de negocio en una oración]
3. **[HALLAZGO CRÍTICO 3]** — [Impacto de negocio en una oración]

Recomendamos el **paquete [NOMBRE DE NIVEL]** a **€[PRECIO]/mes**, el cual aborda
todos los problemas críticos dentro de 90 días y posiciona a [EMPRESA] como una
autoridad visible en IA en [INDUSTRIA].

---

## La Oportunidad: Por Qué Importa GEO para [NOMBRE EMPRESA]

### El Cambio a la Búsqueda por IA Ya Está Ocurriendo

| Métrica | Valor |
|--------|-------|
| Crecimiento de tráfico referido por IA (2025) | +527% interanual |
| Conversión de tráfico IA vs. orgánico | 4.4x más alto |
| Usuarios activos semanales en ChatGPT | 900M+ |
| Alcance mensual de Google AI Overviews | 1.5B usuarios, 200+ países |
| Gartner: caída de tráfico de búsqueda tradicional para 2028 | -50% |
| Especialistas de marketing invirtiendo en GEO hoy | Solo 23% |

**La ventaja del pionero es real.** Las compañías que inviertan en GEO ahora
capturarán el canal de búsqueda de IA antes de que lo hagan los competidores.

### Su Posición Actual

| Métrica | [EMPRESA] | Promedio Industria | Top Rendimiento |
|--------|-----------|------------------|----------------|
| Puntuación GEO | [PUNTUACIÓN]/100 | 45/100 | 75+/100 |
| Rastreadores IA Permitidos | [X]/14 | 8/14 | 14/14 |
| Menciones de Marca (plataformas IA) | [ESTADO] | Moderado | Alto |
| Cobertura de Esquema | [ESTADO] | Parcial | Completa |
| llms.txt | [Sí/No] | 12% lo tienen | 78% lo tienen |

---

## Resumen de Hallazgos de Auditoría

### Desglose de Puntuación GEO

| Categoría | Su Puntuación | Peso | Ponderada | Prioridad |
|----------|-----------|--------|---------|----------|
| Citabilidad & Visibilidad IA | [PUNTUACIÓN]/100 | 25% | [PONDERADA] | [ALTA/MED/BAJA] |
| Señales de Autoridad de Marca | [PUNTUACIÓN]/100 | 20% | [PONDERADA] | [ALTA/MED/BAJA] |
| Calidad de Contenido & E-E-A-T | [PUNTUACIÓN]/100 | 20% | [PONDERADA] | [ALTA/MED/BAJA] |
| Fundamentos Técnicos | [PUNTUACIÓN]/100 | 15% | [PONDERADA] | [ALTA/MED/BAJA] |
| Datos Estructurados | [PUNTUACIÓN]/100 | 10% | [PONDERADA] | [ALTA/MED/BAJA] |
| Optimización de Plataformas | [PUNTUACIÓN]/100 | 10% | [PONDERADA] | [ALTA/MED/BAJA] |
| **PUNTUACIÓN GEO TOTAL** | | | **[PUNTUACIÓN]/100** | **[NIVEL]** |

### Problemas Críticos Encontrados

[Para cada problema crítico de la auditoría:]

#### 🔴 [TÍTULO DEL PROBLEMA]
**Qué encontramos:** [Hallazgo técnico en lenguaje llano]
**Impacto en negocio:** [Lo que esto significa para sus ingresos/visibilidad]
**Nuestra solución:** [Qué haremos para resolverlo]
**Línea de tiempo:** [Cuándo verán mejora]

---

## Nuestra Solución: Paquetes de Servicios

Ofrecemos tres modelos de compromiso basados en el alcance de la optimización necesaria.

---

### BÁSICO — €2,500/mes
*Ideal para: Sitios con puntuación 61-75 que necesitan mejoras dirigidas*

**Qué incluye:**
- Auditoría GEO completa trimestral (4x/año)
- Reporte trimestral para el cliente con seguimiento de puntuación
- Implementación de Schema.org (Organización + esquemas de páginas clave)
- Optimización de acceso a rastreadores de IA (robots.txt)
- Creación y mantenimiento de llms.txt
- Soporte por correo (respuesta en 48 horas)

**Mejora estimada de puntuación GEO:** +10-20 puntos en 6 meses
**Contrato:** Mínimo 6 meses

---

### ESTÁNDAR — €5,000/mes ⭐ Recomendado para [EMPRESA]
*Ideal para: Sitios con puntuación 40-60 que necesitan trabajo mensual estructurado*

**Todo en Básico, más:**
- Auditoría GEO completa mensual + reporte de cambios (delta)
- Llamada de estrategia mensual (60 minutos)
- Optimización de citabilidad de contenido (hasta 10 páginas/mes)
- Construcción de autoridad de marca (optimización en Wikipedia, Wikidata, LinkedIn)
- Optimización específica de plataformas (Google AIO, ChatGPT, Perplexity)
- Mejoras E-E-A-T (páginas de autor, credenciales, señales de frescura)
- Canal de Slack para comunicación rápida (respuesta en 24 horas)

**Mejora estimada de puntuación GEO:** +25-40 puntos en 6 meses
**Contrato:** Mínimo 6 meses

---

### PREMIUM — €9,500/mes
*Ideal para: Sitios con puntuación 0-40 con problemas críticos, o industrias competitivas*

**Todo en Estándar, más:**
- Llamadas de estrategia quincenales
- Soporte de implementación técnica SEO (Core Web Vitals, SSR, velocidad)
- Estrategia + producción de contenido completa (4 artículos optimizados/mes)
- Construcción activa de marca (Reddit, YouTube, citas de industria)
- Monitoreo de competidores y respuesta
- Gerente de cuenta dedicado
- Soporte prioritario (respuesta en 4 horas)

**Mejora estimada de puntuación GEO:** +40-60 puntos en 6 meses
**Contrato:** Mínimo 12 meses

---

## Proyección de ROI para [NOMBRE EMPRESA]

Basado en su actual puntuación GEO de [PUNTUACIÓN]/100 y benchmarks de la industria:

| Escenario | Puntuación en 6 Meses | Incremento Tráfico IA | Est. Valor Adicional/Mes |
|----------|--------------|--------------------|-----------------------------|
| Sin acción | [PUNTUACIÓN + 2]/100 | +5% (crecimiento orgánico) | €[BAJO] |
| Paquete Básico | [PUNTUACIÓN + 15]/100 | +30-40% | €[MEDIO] |
| Paquete Estándar | [PUNTUACIÓN + 32]/100 | +60-90% | €[ALTO] |
| Paquete Premium | [PUNTUACIÓN + 50]/100 | +100-150% | €[MUY ALTO] |

**Supuestos:**
- Basado en un estimado de [X] visitantes orgánicos mensuales a [DOMINIO]
- Se proyecta que la búsqueda por IA impulse el 25-40% del descubrimiento orgánico para fines de 2026
- El tráfico referido por IA convierte a 4.4x la tasa de tráfico orgánico regular
- Los cálculos usan estimaciones conservadoras — los resultados reales pueden variar

**Período de recuperación de inversión (Paquete Estándar):** [X] meses basado en tráfico actual

---

## Línea de Tiempo del Compromiso

### Mes 1 — Fundación
- Llamada de inicio (Kick-off) e incorporación (Semana 1)
- Auditoría técnica completa + captura de métricas de base
- Implementación de victorias rápidas: robots.txt, schema, llms.txt, meta descriptions
- Mejora de puntuación esperada: +5-10 puntos

### Mes 2-3 — Optimización
- Reescrituras para citabilidad de contenido (top 10 páginas)
- Mejoras E-E-A-T: páginas de autor, credenciales, fechas
- Optimización específica de plataformas (Google AIO, ChatGPT, Perplexity)
- Presencia de marca: LinkedIn, bases en Wikipedia/Wikidata
- Mejora de puntuación esperada: +15-25 puntos acumulados

### Mes 4-6 — Construcción de Autoridad
- Campañas de menciones de marca (Reddit, sitios de la industria, YouTube)
- Estrategia de contenido de autoridad tópica
- Reportes mensuales mostrando mejoras de puntuación
- Mejora de puntuación esperada: +30-45 puntos acumulados

### Mes 6 — Revisión
- Re-auditoría completa con comparación de antes/después
- Reporte de ROI
- Discusión de renovación

---

## Por Qué Nosotros

- **Especialistas en GEO**: Nos enfocamos exclusivamente en optimización de búsqueda por IA, no somos una agencia SEO tradicional adaptándose a GEO
- **Reportes transparentes**: Los reportes mensuales muestran exactamente qué cambió y por qué
- **Sin ataduras más allá del mínimo**: Mes a mes después del compromiso inicial
- **Metodología probada**: Auditoría GEO de 11 dimensiones cubriendo todas las grandes plataformas de IA
- **Resultados rápidos**: Victorias rápidas visibles dentro de los primeros 30 días

---

## Resumen de Inversión

| Paquete | Mensual | 6-Meses | 12-Meses |
|---------|---------|---------|----------|
| Básico | €2,500 | €15,000 | €30,000 |
| Estándar | €5,000 | €30,000 | €60,000 |
| Premium | €9,500 | €57,000 | €114,000 |

*Todos los precios excluyen el IVA (VAT). Términos de pago: mensual, a pagar dentro de 15 días de la factura.*

---

## Próximos Pasos

Para avanzar:

1. **Revise esta propuesta** y comparta cualquier pregunta
2. **Programe una llamada de 30 minutos** para repasar juntos los hallazgos: [ENLACE CALENDARIO]
3. **Firme el acuerdo de servicios** (se envía por separado una vez aceptado)
4. **Llamada de inicio (Kick-off)** programada para la fecha de inicio elegida

Esta propuesta es válida por **30 días** desde la fecha indicada arriba.

---

## Términos y Condiciones

- **Compromiso mínimo:** Como se indica por paquete arriba
- **Cancelación:** Aviso por escrito de 30 días después del término mínimo
- **Confidencialidad:** Todos los hallazgos de auditoría y datos del cliente son estrictamente confidenciales
- **Resultados:** Garantizamos el esfuerzo y la metodología, no resultados de posicionamiento específicos
- **Reportes:** Reportes mensuales entregados para el día 5 de cada mes
- **Acceso requerido:** Acceso de lectura a Google Analytics / Search Console (si está disponible)

---

*Esta propuesta fue preparada usando herramientas de análisis GEO-SEO y refleja hallazgos
de la auditoría de [DOMINIO] conducida el [FECHA]. Todas las puntuaciones y recomendaciones
están basadas en las mejores prácticas actuales de la industria para Generative Engine Optimization.*
```

---

## Salida

1. Guarda la propuesta en `~/.geo-prospects/proposals/<dominio>-proposal-<fecha>.md`
2. Actualiza el registro de prospecto: establece `status` a `proposal`, guarda la ruta `proposal_file`
3. Imprime confirmación:
   ```
   ✓ Propuesta generada: ~/.geo-prospects/proposals/electron-srl.com-proposal-2026-03-12.md
   ✓ Estado del prospecto actualizado: Calificado → Propuesta
   ✓ Paquete recomendado: ESTÁNDAR (€5,000/mes) — Puntuación 32/100

   Siguiente: Comparte el archivo de propuesta o ejecuta `/geo report-pdf` para una versión visual.
   ```

## Lógica de Recomendación de Precios

Basar recomendación en la puntuación GEO:
- Puntuación 0-40 → Recomendar **Premium** (problemas críticos requieren trabajo intensivo)
- Puntuación 41-60 → Recomendar **Estándar** (optimización mensual estructurada)
- Puntuación 61-75 → Recomendar **Básico** (mantenimiento + mejoras dirigidas)
- Puntuación 76+ → Ofrecer **Básico** o revisión periódica trimestral
