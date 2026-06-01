---
name: geo-report
description: Genera un reporte GEO profesional y enfocado al cliente, combinando todos los resultados de auditorías en un único entregable con puntuaciones, hallazgos y acciones priorizadas
version: 1.0.0
author: geo-seo-claude
tags: [geo, report, client-deliverable, executive-summary, action-plan]
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# Generador de Reporte para Cliente GEO

## Propósito

Esta habilidad agrega los resultados de todas las habilidades de auditoría GEO en un único reporte profesional que puede ser entregado directamente a un cliente o parte interesada (stakeholder). El reporte está escrito para **dueños de negocios y líderes de marketing**, no para desarrolladores — los hallazgos técnicos se traducen en impacto comercial y elementos de acción claros con niveles de prioridad.

## Cómo Usar Esta Habilidad

1. Ejecuta las siguientes auditorías primero (o usa datos de reportes existentes):
   - `geo-platform-optimizer` -> GEO-PLATFORM-OPTIMIZATION.md
   - `geo-schema` -> GEO-SCHEMA-REPORT.md
   - `geo-technical` -> GEO-TECHNICAL-AUDIT.md
   - `geo-content` -> GEO-CONTENT-ANALYSIS.md
   - (Opcional) `geo-llmstxt` -> evaluación de llms.txt
   - (Opcional) `geo-brand-mentions` -> datos de autoridad de marca
2. Recopila todas las puntuaciones y hallazgos
3. Calcula la Puntuación de Preparación GEO compuesta
4. Genera el reporte del cliente usando la plantilla a continuación
5. Salida: GEO-CLIENT-REPORT.md

---

## Cálculo de Puntuación de Preparación GEO

### Pesos de los Componentes

| Componente | Peso | Habilidad de Origen |
|---|---|---|
| Preparación para Plataformas IA | 25% | geo-platform-optimizer |
| Calidad de Contenido y E-E-A-T | 25% | geo-content |
| Base Técnica | 20% | geo-technical |
| Esquema y Datos Estructurados | 15% | geo-schema |
| Autoridad de Marca y Presencia de Entidad | 15% | geo-platform-optimizer (señales de entidad) |

### Fórmula de Puntuación
```
Puntuación GEO = (Punt. Plataforma * 0.25) + (Punt. Contenido * 0.25) + (Punt. Técnica * 0.20) + (Punt. Esquema * 0.15) + (Punt. Marca * 0.15)
```

Redondear al entero más cercano. Límite máximo en 100.

### Interpretación de Puntuación para Clientes

| Rango de Puntuación | Etiqueta | Descripción para el Cliente |
|---|---|---|
| 85-100 | Excelente | Su sitio está bien posicionado para la búsqueda por IA. Enfóquese en mantener y expandir su ventaja. |
| 70-84 | Bueno | Base sólida con oportunidades claras para mejorar la visibilidad en IA. Optimizaciones dirigidas producirán resultados significativos. |
| 55-69 | Moderado | Su sitio tiene brechas en preparación para IA que los competidores podrían estar explotando. Un plan de optimización estructurado cerrará estas brechas. |
| 40-54 | Por debajo del promedio | Existen barreras significativas para la visibilidad en búsquedas por IA. Sin acción, su marca corre el riesgo de ser invisible en las respuestas generadas por IA. |
| 0-39 | Necesita Atención | Problemas críticos de preparación para IA requieren acción inmediata. Sus competidores probablemente están capturando el tráfico de búsqueda por IA que su marca debería poseer. |

---

## Plantilla del Reporte

El reporte completo sigue esta estructura exacta. Cada sección incluye instrucciones sobre qué escribir y cómo.

---

### Sección 1: Resumen Ejecutivo

Escribe exactamente UN párrafo (4-6 oraciones) cubriendo:
- Qué se analizó (dominio, número de páginas, fecha del análisis)
- La Puntuación de Preparación GEO general con contexto ("XX/100, lo que sitúa a [marca] en el nivel [etiqueta]")
- El hallazgo individual más impactante (positivo o negativo)
- Las top 3 recomendaciones de prioridad en una sola oración
- Una oración sobre el impacto comercial ("Abordar estas recomendaciones podría aumentar el tráfico impulsado por IA en un estimado XX%, representando aproximadamente $X,XXX/mes basado en patrones de tráfico actuales")

**Tono**: Confiado, directo, profesional. Sin jerga. Sin rodeos. Escribe como un consultor entregando hallazgos, no como una herramienta generando un reporte.

### Sección 2: Puntuación de Preparación GEO

Presenta la puntuación general de manera destacada:

```
## Puntuación de Preparación GEO: XX/100 — [Etiqueta]
```

Luego desglosa por componente en una tabla:

```markdown
| Componente | Puntuación | Peso | Puntuación Ponderada |
|---|---|---|---|
| Preparación para Plataformas IA | XX/100 | 25% | XX |
| Calidad de Contenido y E-E-A-T | XX/100 | 25% | XX |
| Base Técnica | XX/100 | 20% | XX |
| Esquema y Datos Estructurados | XX/100 | 15% | XX |
| Autoridad de Marca | XX/100 | 15% | XX |
| **General** | | | **XX/100** |
```

### Sección 3: Panel de Visibilidad en IA (Dashboard)

Presenta las puntuaciones de preparación por plataforma:

```markdown
## Panel de Visibilidad en IA

| Plataforma IA | Puntuación de Preparación | Brecha Clave | Acción Prioritaria |
|---|---|---|---|
| Google AI Overviews | XX/100 | [Brecha en una línea] | [Acción en una línea] |
| ChatGPT Web Search | XX/100 | [Brecha en una línea] | [Acción en una línea] |
| Perplexity AI | XX/100 | [Brecha en una línea] | [Acción en una línea] |
| Google Gemini | XX/100 | [Brecha en una línea] | [Acción en una línea] |
| Bing Copilot | XX/100 | [Brecha en una línea] | [Acción en una línea] |
```

Añade un breve párrafo explicando qué significan estas puntuaciones: "Estas puntuaciones reflejan qué tan probable es que su contenido sea citado por cada plataforma de búsqueda de IA. Una puntuación por debajo de 50 indica barreras significativas para la citación en esa plataforma."

### Sección 4: Estado de Acceso a Rastreadores de IA

Preséntalo como una tabla clara:

```markdown
## Acceso a Rastreadores de IA

| Rastreador de IA | Plataforma | Estado | Impacto | Recomendación |
|---|---|---|---|---|
| Googlebot | Google Search + AIO | Permitido/Bloqueado | Crítico | [Acción] |
| GPTBot | ChatGPT / OpenAI | Permitido/Bloqueado | Alto | [Acción] |
| Bingbot | Bing + Copilot + ChatGPT | Permitido/Bloqueado | Alto | [Acción] |
| PerplexityBot | Perplexity AI | Permitido/Bloqueado | Medio | [Acción] |
| Google-Extended | Entrenamiento de Gemini | Permitido/Bloqueado | Medio | [Acción] |
| ClaudeBot | Anthropic Claude | Permitido/Bloqueado | Medio | [Acción] |
| Applebot-Extended | Apple Intelligence | Permitido/Bloqueado | Medio | [Acción] |
```

**Traduce para el cliente**: "Bloquear rastreadores de IA es como cerrar su tienda durante el horario comercial. Si un rastreador no puede acceder a su sitio, la plataforma de IA que alimenta no puede citar su contenido. Recomendamos permitir todos los rastreadores de IA importantes a menos que tenga una preocupación específica de licencia de datos."

### Sección 5: Análisis de Autoridad de Marca

Presenta la presencia de la entidad en todas las plataformas:

```markdown
## Autoridad de Marca

| Plataforma | Presencia | Estado | Impacto en Visibilidad de IA |
|---|---|---|---|
| Wikipedia | Sí/No | [Detalle] | Muy Alto — 47.9% de citas de ChatGPT son de Wikipedia |
| Wikidata | Sí/No | [Detalle] | Alto — datos de entidad legibles por máquina |
| LinkedIn | Sí/No | [Detalle] | Alto — señal para Bing Copilot y ChatGPT |
| YouTube | Sí/No | [Detalle] | Alto — señal para Gemini y Perplexity |
| Reddit | Sí/No | [Detalle] | Muy Alto — 46.7% de citas de Perplexity son de Reddit |
| Panel de Conocimiento Google | Sí/No | [Detalle] | Alto — reconocimiento de entidad para Gemini |
| Crunchbase | Sí/No | [Detalle] | Medio — validación de entidad |
| GitHub | Sí/No | [Detalle] | Medio — señal para marcas tecnológicas |
```

**Traduce para el cliente**: "Las plataformas de IA construyen confianza al cruzar referencias de su marca en múltiples fuentes de autoridad. Cada plataforma donde su marca tiene una presencia precisa y consistente incrementa la probabilidad de ser citada en respuestas de IA."

### Sección 6: Análisis de Citabilidad

#### Top 5 Páginas Más Citables
Para cada página:
- URL
- Por qué es citable (estructura, profundidad, señales E-E-A-T)
- Una mejora específica que la haría aún más citable

#### Top 5 Páginas Menos Citables
Para cada página:
- URL
- Por qué es poco probable que sea citada (contenido delgado/pobre, mala estructura, señales faltantes)
- Recomendación específica de reescritura o reestructuración

**Encuadre de impacto comercial**: "Sus páginas más citables son sus mejores candidatas para aparecer en respuestas generadas por IA. Mejorar las 5 páginas menos citables representa la inversión en contenido de mayor ROI que puede hacer para la visibilidad en IA."

### Sección 7: Resumen de Salud Técnica

Presenta los hallazgos técnicos clave en lenguaje amigable para los negocios:

```markdown
## Salud Técnica

| Área | Estado | Impacto de Negocio |
|---|---|---|
| Core Web Vitals | Bueno/Necesita Trabajo/Pobre | [Impacto en experiencia de usuario y rankings] |
| Renderizado en Servidor (SSR) | Sí/Parcial/No | [Impacto en visibilidad para rastreadores de IA] |
| Optimización Móvil | Bueno/Necesita Trabajo/Pobre | [Impacto en indexación mobile-first de Google] |
| Seguridad (HTTPS + Cabeceras) | Bueno/Necesita Trabajo/Pobre | [Impacto en señales de confianza] |
| Velocidad de Página | Rápida/Promedio/Lenta | [Impacto en experiencia de usuario y presupuesto de rastreo] |
| Protocolo IndexNow | Implementado/No | [Impacto en velocidad de indexación de Bing/ChatGPT] |
```

**Aviso de hallazgo crítico**: Si el SSR falta o es parcial, resalta esto prominentemente: "Su sitio utiliza renderizado en el lado del cliente, lo que significa que los rastreadores de IA ven una página vacía cuando la visitan. Este es el problema técnico más impactante para la visibilidad en búsquedas por IA. Hasta que esto se resuelva, la mayoría de plataformas de IA no pueden citar su contenido."

### Sección 8: Esquema y Datos Estructurados

```markdown
## Esquema y Datos Estructurados

### Implementación Actual
| Tipo de Esquema | Presente | Estado | Impacto en IA |
|---|---|---|---|
| Organization | Sí/No | [Válido/Problemas] | Crítico — reconocimiento de entidad |
| Article + Author | Sí/No | [Válido/Problemas] | Alto — señal E-E-A-T |
| sameAs (enlaces de entidad) | Sí/No | [Cantidad] enlaces | Crítico — grafo de entidades cruzado entre plataformas |
| [Específico del Negocio] | Sí/No | [Válido/Problemas] | [Impacto] |
| WebSite + SearchAction | Sí/No | [Válido/Problemas] | Medio — sitelinks |
| BreadcrumbList | Sí/No | [Válido/Problemas] | Medio-Bajo — contexto de navegación |
```

Si faltan esquemas, anota: "El código de datos estructurados listo para usarse ha sido preparado y está incluido en el apéndice técnico. Su equipo de desarrollo puede añadir esto a su sitio con un esfuerzo mínimo."

### Sección 9: Estado de llms.txt

```markdown
## llms.txt — Guía de Contenido para IA

| Archivo | Estado | Recomendación |
|---|---|---|
| /llms.txt | Presente/Ausente | [Acción] |
| /llms-full.txt | Presente/Ausente | [Acción] |
```

**Traduce para el cliente**: "llms.txt es un estándar emergente (similar a robots.txt) que indica a los sistemas de IA de qué trata su sitio y cuáles páginas son más importantes. Aunque todavía no es adoptado universalmente, implementarlo posiciona a su marca por delante de los competidores y provee guía directa a las plataformas de IA."

### Sección 10: Plan de Acción Priorizado

Esta es la sección más importante del reporte. Organiza las acciones por línea de tiempo e impacto.

```markdown
## Plan de Acción Priorizado

### Victorias Rápidas (Esta Semana)
*Alto impacto, bajo esfuerzo — puede implementarse de inmediato*

| # | Acción | Impacto | Esfuerzo | Plataformas Afectadas |
|---|---|---|---|---|
| 1 | [Acción específica] | [Alto/Med] | [Horas est.] | [Cuáles plataformas IA] |
| 2 | [Acción específica] | [Alto/Med] | [Horas est.] | [Cuáles plataformas IA] |
```

**Criterios de Victoria Rápida**: Se puede hacer en < 4 horas por una persona. Ejemplos:
- Desbloquear rastreadores IA en robots.txt
- Añadir fechas de publicación al contenido existente
- Añadir firmas de autor con credenciales
- Arreglar meta descripciones rotas
- Añadir propiedades sameAs a esquema Organization existente
- Crear/reclamar archivo llms.txt

```markdown
### Mejoras a Medio Plazo (Este Mes)
*Impacto significativo, esfuerzo moderado — requiere cambios técnicos o de contenido*

| # | Acción | Impacto | Esfuerzo | Plataformas Afectadas |
|---|---|---|---|---|
| 1 | [Acción específica] | [Alto/Med] | [Días est.] | [Cuáles plataformas IA] |
```

**Criterios a Medio Plazo**: 1-5 días de trabajo. Ejemplos:
- Reestructurar top 10 páginas con encabezados basados en preguntas y respuestas directas
- Implementar marcado completo de Schema.org
- Crear páginas de autor con credenciales y enlaces sameAs
- Optimizar Core Web Vitals (compresión de imágenes, división de código)
- Registrarse y configurar Bing Webmaster Tools
- Implementar protocolo IndexNow

```markdown
### Iniciativas Estratégicas (Este Trimestre)
*Ventaja competitiva a largo plazo, requiere inversión continua*

| # | Acción | Impacto | Esfuerzo | Plataformas Afectadas |
|---|---|---|---|---|
| 1 | [Acción específica] | [Alto/Med] | [Semanas est.] | [Cuáles plataformas IA] |
```

**Criterios Estratégicos**: Esfuerzo continuo durante semanas/meses. Ejemplos:
- Construir presencia de entidad en Wikipedia/Wikidata
- Desarrollar estrategia activa de interacción en la comunidad de Reddit
- Crear estrategia de contenido en YouTube alineada con consultas de búsqueda
- Implementar renderizado en servidor (si actualmente se renderiza en el cliente)
- Construir autoridad tópica a través de estrategia de contenido exhaustiva
- Establecer programa de publicación de investigaciones/datos originales

### Estimación de Impacto
Después del plan de acción, incluye una estimación del impacto:

"Basado en puntos de referencia (benchmarks) de la industria y las brechas específicas identificadas en esta auditoría:
- **Solo las Victorias Rápidas** podrían mejorar su puntuación GEO en aproximadamente [X-Y] puntos
- La **implementación completa** de este plan de acción podría mejorar su puntuación GEO a aproximadamente [XX]/100
- A los niveles de tráfico actuales y tasas de conversión, la visibilidad mejorada en IA representa un estimado de **$X,XXX - $XX,XXX por mes** en valor orgánico adicional"

Usa estimaciones conservadoras. Basa la cifra en dólares en:
- Valor estimado del tráfico orgánico actual (desde analíticas si están disponibles, o estima desde benchmarks de la industria)
- Se proyecta que la búsqueda por IA impulse el 25-40% del descubrimiento orgánico para fines de 2026
- Una mejora de 10 puntos en la puntuación GEO típicamente se correlaciona con un incremento del 15-25% en la frecuencia de citación en IA

### Sección 11: Comparación con Competidores (si se proveen URLs de competidores)

Si las URLs de los competidores fueron analizadas junto con el dominio principal:

```markdown
## Comparación con Competidores

| Métrica | [Su Marca] | [Competidor 1] | [Competidor 2] |
|---|---|---|---|
| Puntuación GEO General | XX/100 | XX/100 | XX/100 |
| Preparación Google AIO | XX/100 | XX/100 | XX/100 |
| Preparación ChatGPT | XX/100 | XX/100 | XX/100 |
| Preparación Perplexity | XX/100 | XX/100 | XX/100 |
| Cobertura de Esquema | [Detalle] | [Detalle] | [Detalle] |
| Presencia en Wikipedia | Sí/No | Sí/No | Sí/No |
| Autoridad en Reddit | [Detalle] | [Detalle] | [Detalle] |
| Estado SSR | Sí/No | Sí/No | Sí/No |

### Donde Usted Lidera
[Áreas específicas donde la marca supera a la competencia]

### Donde Usted Está Rezagado
[Áreas específicas donde los competidores tienen ventaja, con acciones para cerrar la brecha]
```

### Sección 12: Apéndice

```markdown
## Apéndice

### Metodología
Esta auditoría GEO se llevó a cabo utilizando la siguiente metodología:
- **Páginas analizadas**: [Lista de URLs específicas auditadas]
- **Plataformas evaluadas**: Google AI Overviews, ChatGPT, Perplexity AI, Google Gemini, Bing Copilot
- **Comprobaciones técnicas**: Cabeceras HTTP, robots.txt, análisis de código fuente HTML, validación de datos estructurados
- **Evaluación de contenido**: Marco E-E-A-T (Experiencia, Conocimiento, Autoridad, Confiabilidad) según Guías de Calidad de Google de Diciembre de 2025
- **Validación de esquema**: Parseo JSON-LD y cumplimiento de la especificación de Schema.org
- **Fecha de análisis**: [Fecha]

### Fuentes de Datos
- Guías de Calidad para Calificadores de Búsqueda de Google (actualización Dic 2025)
- Jerarquía completa de tipos de Schema.org
- Estudios de citación de la industria (Zyppy, Authoritas, investigación en búsqueda IA de Semrush, 2025-2026)
- Umbrales de Core Web Vitals (web.dev, estándares de 2026)
- Documentación de User-Agent de rastreadores de IA (docs oficiales de cada plataforma)

### Glosario

| Término | Definición |
|---|---|
| GEO | Optimización para Motores Generativos (Generative Engine Optimization) — optimizar contenido para ser citado por plataformas de búsqueda de IA |
| AIO | AI Overviews — cajas de respuesta generadas por IA de Google en la parte superior de los resultados de búsqueda |
| E-E-A-T | Experiencia, Conocimiento (Expertise), Autoridad, Confiabilidad (Trustworthiness) — marco de calidad de contenido de Google |
| SSR | Renderizado en Lado del Servidor (Server-Side Rendering) — generar HTML en el servidor para que los rastreadores lean contenido sin JavaScript |
| CWV | Core Web Vitals — métricas de experiencia de página de Google (LCP, INP, CLS) |
| LCP | Largest Contentful Paint — tiempo para renderizar el elemento visible más grande |
| INP | Interaction to Next Paint — métrica de responsividad (reemplazó FID en marzo de 2024) |
| CLS | Cumulative Layout Shift — métrica de estabilidad visual |
| JSON-LD | Notación de Objetos JavaScript para Datos Enlazados — formato de datos estructurados preferido |
| sameAs | Propiedad de Schema.org que enlaza una entidad a sus perfiles en otras plataformas |
| IndexNow | Protocolo para notificar instantáneamente a los motores de búsqueda sobre cambios de contenido |
| llms.txt | Archivo de estándar propuesto para guiar a sistemas de IA sobre el contenido de un sitio |
| YMYL | Your Money or Your Life — temas que requieren los estándares E-E-A-T más altos |
| SERP | Página de Resultados del Motor de Búsqueda (Search Engine Results Page) |
| Autoridad Tópica | La profundidad y amplitud de cobertura de un sitio en su área temática principal |
```

---

## Directrices de Formato y Tono

### Formato
- Usa markdown limpio en todo: tablas, encabezados (H2/H3), viñetas, negrita para énfasis
- Tablas para datos, viñetas para recomendaciones, negrita para términos clave
- Una línea en blanco entre secciones para legibilidad
- Usa líneas horizontales (---) para separar secciones mayores
- Todas las URLs deben ser absolutas (no relativas)

### Tono
- **Profesional pero accesible** — escrito para un dueño de negocio, no para un desarrollador
- **Confiado y directo** — expresa hallazgos como conclusiones, no posibilidades
- **Orientado a la acción** — cada hallazgo debe conectarse a una acción específica
- **Enfocado en impacto comercial** — traduce problemas técnicos a resultados de negocio
- Evita: jerga sin explicación, lenguaje dubitativo, voz pasiva, advertencias excesivas
- Usa: "Su sitio [hace/no hace]...", "Recomendamos...", "Esto impacta..."

### Encuadre en Valor Monetario (Dólares)
Donde sea posible, conecta las recomendaciones al valor comercial:
- "Mejorar su preparación de Google AIO de 35 a 70 podría aumentar su presencia en AI Overviews en un estimado de 50%, lo que a los volúmenes de búsqueda actuales representa aproximadamente 2,000 visitantes mensuales adicionales"
- "El renderizado en servidor haría que su contenido sea accesible a ChatGPT, Perplexity y otras plataformas IA — representando colectivamente una audiencia que sus competidores ya están alcanzando"
- "La inversión en marcado Schema.org (estimado 8-16 horas de desarrollador) podría incrementar su puntuación de reconocimiento de entidad de 20 a 75, mejorando significativamente la probabilidad de citación"

Sé conservador con las estimaciones. Expresa los supuestos claramente. Nunca garantices resultados específicos.

---

## Salida

Genera **GEO-CLIENT-REPORT.md** usando la plantilla completa anterior, rellenada con datos reales de la auditoría. El reporte debería ser:
- 40-80 páginas de equivalencia en detalle (3,000-6,000 palabras)
- Listo para enviar a un cliente sin editar
- Autónomo (sin referencias a otros archivos de reporte — toda la información relevante está incluida)
- Imprimible y presentable (formato markdown limpio)
