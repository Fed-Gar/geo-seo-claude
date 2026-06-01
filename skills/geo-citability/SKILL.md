---
name: geo-citability
description: Puntuación y optimización de citabilidad para IA. Analiza el contenido de páginas web para determinar qué tan probable es que los sistemas de IA (ChatGPT, Claude, Perplexity, Gemini) citen o extraigan pasajes de la página. Proporciona una puntuación de citabilidad (0-100) con sugerencias de reescritura específicas.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Habilidad de Puntuación de Citabilidad para IA

## Idea Central

Los modelos de lenguaje de IA citan pasajes que cumplen criterios estructurales específicos. Investigaciones de Princeton, Georgia Tech y IIT Delhi (2024) encontraron que el contenido optimizado para GEO logra un 30-115% más de visibilidad en respuestas generadas por IA. El hallazgo clave: Los sistemas de IA extraen y citan preferentemente pasajes que tienen entre **134-167 palabras de largo**, son **autocontenidos** (comprensibles sin el contexto circundante), **ricos en datos** (que contienen estadísticas específicas, fechas o entidades nombradas), y **responden directamente a una pregunta** en las primeras 1-2 oraciones.

Esto es fundamentalmente diferente a la redacción SEO tradicional, la cual optimiza para densidad de palabras clave y métricas de compromiso de usuario (engagement). La citabilidad en GEO optimiza para la **extractabilidad** -- la facilidad con la que un sistema de IA puede extraer un pasaje de tu contenido y presentarlo como una respuesta directa.

---

## Rúbrica de Puntuación de Citabilidad (0-100)

### Categoría 1: Calidad del Bloque de Respuesta (30% de la puntuación total)

Esto mide si el contenido contiene pasajes de respuesta claros y citables que los sistemas de IA puedan extraer palabra por palabra (verbatim).

**Criterios de Puntuación:**

| Puntuación | Criterios |
|---|---|
| **90-100** | Cada sección importante abre con una respuesta directa de 1-2 oraciones. Usa patrones "X es..." o "X se refiere a...". Las primeras 40-60 palabras de cada sección pueden sostenerse por sí solas como una respuesta completa. |
| **70-89** | La mayoría de las secciones tienen aperturas de respuesta claras. Algunos patrones de definición presentes. Las respuestas son identificables pero pueden necesitar algo de contexto. |
| **50-69** | Algunas secciones tienen aperturas tipo respuesta pero muchas ocultan la respuesta en el medio o final de los párrafos. Pocos patrones de definición explícitos. |
| **30-49** | Las respuestas generalmente están enterradas en párrafos largos. Sin patrones de definición consistentes. El contenido se basa más en narrativa que en respuestas. |
| **0-29** | Sin bloques de respuesta identificables. El contenido es completamente narrativo, conversacional o fragmentado. A la IA le costaría extraer cualquier pasaje citable. |

**Qué buscar:**

- **Patrones de definición:** "X es [definición]." / "X se refiere a [explicación]." / "X significa [significado]."
- **Estructura donde la respuesta va primero:** La respuesta aparece en la primera oración, seguida del detalle de apoyo.
- **Respuestas cuantificadas:** "El costo promedio de X es $Y" en lugar de "Muchos factores afectan el costo de X."
- **Respuestas de comparación:** "X difiere de Y en tres aspectos: [lista]" en lugar de "X e Y se confunden a menudo."

**Ejemplo de alta citabilidad:**
```
Las redes de distribución de contenido (CDNs) son sistemas de servidores distribuidos que almacenan en caché y sirven contenido web desde ubicaciones geográficamente cercanas a los usuarios finales. Una CDN reduce la latencia en un 50-70% en promedio al servir los activos desde servidores de borde en lugar de un único servidor de origen. Los tres mayores proveedores de CDN a partir de 2025 son Cloudflare (sirviendo aproximadamente el 20% de todos los sitios web), Amazon CloudFront y Akamai Technologies.
```
Cantidad de palabras: 76. Autocontenido: Sí. Datos/Hechos: 3 puntos de datos específicos. Patrón de definición: Sí.

**Ejemplo de baja citabilidad:**
```
Si alguna vez te has preguntado por qué algunos sitios web cargan más rápido que otros, la respuesta podría sorprenderte. Hay esta increíble tecnología que ha existido desde hace un tiempo. Ha cambiado la forma en que pensamos sobre el rendimiento web. Déjame explicarte cómo funciona y por qué debería importarte para tu negocio.
```
Cantidad de palabras: 55. Autocontenido: No (no identifica el tema). Datos/Hechos: 0. Patrón de definición: No.

---

### Categoría 2: Autocontención del Pasaje (25% de la puntuación total)

Esto mide si los pasajes individuales pueden extraerse y entenderse sin necesidad del contenido circundante.

**Criterios de Puntuación:**

| Puntuación | Criterios |
|---|---|
| **90-100** | 80%+ de los bloques de contenido son totalmente autocontenidos. Cada pasaje nombra a su sujeto explícitamente. No depende de pronombres que referencien contenido anterior. Contiene hechos específicos dentro del pasaje. |
| **70-89** | 60-79% de los bloques de contenido son autocontenidos. La mayoría de los pasajes nombran a su sujeto. Uso ocasional de pronombres que requieren contexto. |
| **50-69** | 40-59% de los bloques de contenido son autocontenidos. Uso mixto de sujetos explícitos y pronombres. Algunos pasajes requieren leer secciones anteriores. |
| **30-49** | 20-39% de los bloques de contenido son autocontenidos. Fuerte dependencia de pronombres y referencias contextuales. La mayoría de los pasajes necesitan el texto circundante. |
| **0-29** | Menos del 20% es autocontenido. El contenido se lee como una narrativa continua donde al extraer cualquier párrafo se pierde el significado. |

**Lista de comprobación de autocontención para cada pasaje:**

1. ¿El pasaje nombra explícitamente el sujeto (no "eso," "este," "ellos")?
2. ¿Alguien puede entender el punto principal leyendo SOLAMENTE este pasaje?
3. ¿El pasaje contiene al menos un dato específico, estadística o entidad nombrada?
4. ¿Tiene el pasaje entre 50-200 palabras (la longitud óptima de extracción)?
5. ¿Evita el pasaje comenzar con conjunciones ("Pero," "Sin embargo," "Y") que impliquen contexto previo?

---

### Categoría 3: Legibilidad Estructural (20% de la puntuación total)

Esto mide el formato estructural que ayuda a los sistemas de IA a analizar y segmentar el contenido.

**Criterios de Puntuación:**

| Puntuación | Criterios |
|---|---|
| **90-100** | Jerarquía limpia de H1 > H2 > H3. Encabezados basados en preguntas para contenido informativo. Párrafos cortos (2-4 oraciones). Tablas para comparaciones. Listas ordenadas para procesos. Listas desordenadas para características/opciones. |
| **70-89** | Buena jerarquía de encabezados con omisiones menores. Algunos encabezados basados en preguntas. Mayormente párrafos cortos. Cierto uso de tablas y listas. |
| **50-69** | Jerarquía de encabezados presente pero inconsistente. Pocos encabezados basados en preguntas. Mezcla de párrafos cortos y largos. Tablas/listas limitadas. |
| **30-49** | Estructura de encabezados mínima. Sin encabezados basados en preguntas. Dominan los párrafos largos. Raro uso de tablas/listas. |
| **0-29** | Sin estructura de encabezados o jerarquía severamente rota. Párrafos "muros de texto". Sin tablas o listas. |

**Mejores prácticas estructurales para citabilidad IA:**

- **Jerarquía de encabezados:** H1 (título de la página) > H2 (secciones principales) > H3 (subsecciones). Nunca omitas niveles.
- **Encabezados basados en preguntas:** "¿Qué es [tema]?" y "¿Cómo funciona [tema]?" se asocian directamente a las consultas a la IA.
- **Longitud de párrafo:** 2-4 oraciones por párrafo. Los sistemas de IA analizan párrafos cortos de manera más confiable.
- **Tablas:** Úsalas para cualquier comparación de 3+ elementos. Los sistemas de IA extraen datos de tablas con gran precisión.
- **Listas:** Usa listas ordenadas para procesos secuenciales, listas desordenadas para elementos no secuenciales.
- **Negrita para términos clave:** Pon en negrita el primer uso de términos importantes. Esto ayuda al reconocimiento de entidades de la IA.

---

### Categoría 4: Densidad Estadística (15% de la puntuación total)

Esto mide la presencia de puntos de datos específicos y verificables que los sistemas de IA priorizan al seleccionar fuentes de citación.

**Criterios de Puntuación:**

| Puntuación | Criterios |
|---|---|
| **90-100** | 5+ estadísticas específicas por cada 500 palabras. Todas las afirmaciones respaldadas por fuentes nombradas o fechas. Usa números exactos (no "muchos" o "varios"). Incluye porcentajes, cantidades de dinero, plazos temporales y estudios nombrados. |
| **70-89** | 3-4 estadísticas por cada 500 palabras. La mayoría de las afirmaciones tienen fuentes. Mayormente números específicos con cuantificadores vagos ocasionales. |
| **50-69** | 1-2 estadísticas por cada 500 palabras. Algunas afirmaciones documentadas (con fuentes). Mezcla de números específicos y vagos. |
| **30-49** | Menos de 1 estadística por cada 500 palabras. Pocas afirmaciones documentadas. Predominantemente cuantificadores vagos. |
| **0-29** | Sin estadísticas. Sin afirmaciones documentadas. Todos los cuantificadores son vagos ("muchos," "la mayoría," "un montón"). |

**Qué cuenta como una estadística:**
- Porcentajes específicos: "El 73% de los profesionales del marketing reportan..."
- Cantidades de dinero: "El costo promedio es de $4,500 por mes"
- Marcos temporales: "La implementación toma de 6-8 semanas en promedio"
- Estudios nombrados: "Según el Informe sobre el Estado del Marketing de HubSpot 2025..."
- Recuentos específicos: "La plataforma se integra con más de 340 herramientas"
- Datos de comparación: "Un 40% más rápido que el promedio de la industria"

**Qué NO cuenta:**
- "Muchas empresas usan..." (vago)
- "Un porcentaje significativo..." (vago)
- "Los estudios muestran que..." (sin nombrar la fuente)
- "Los expertos coinciden..." (sin nombrar a los expertos)

---

### Categoría 5: Unicidad y Datos Originales (10% de la puntuación total)

Esto mide si el contenido proporciona información que los sistemas de IA no pueden encontrar en otro lugar, convirtiéndolo en una fuente de citación necesaria.

**Criterios de Puntuación:**

| Puntuación | Criterios |
|---|---|
| **90-100** | Contiene investigación primaria (first-party), datos propietarios, encuestas originales o conjuntos de datos únicos. Presenta análisis o perspectivas que no se encuentran en ninguna otra página. Descripciones metodológicas claras. |
| **70-89** | Contiene algunas perspectivas originales o análisis únicos de datos existentes. Ofrece una perspectiva distinta con ejemplos originales. |
| **50-69** | Principalmente sintetiza información existente pero añade algún comentario o ejemplos únicos. |
| **30-49** | Contenido mayormente derivado que reitera conocimiento común con contribución original mínima. |
| **0-29** | Completamente derivado. Toda la información está disponible (a menudo palabra por palabra) en fuentes de mayor autoridad. |

**Señales de contenido único:**
- "Nuestro análisis de datos de [X] reveló..."
- "Encuestamos a [N] [profesionales] y encontramos..."
- "Basado en nuestra experiencia con [N] clientes..."
- Gráficos personalizados, tablas o visualizaciones de datos
- Casos de estudio con resultados nombrados específicos
- Marcos, metodologías o taxonomías originales

---

## Procedimiento de Análisis

### Paso 1: Obtener y Analizar el Contenido de la Página

1. Usa WebFetch para recuperar la URL objetivo.
2. Extrae el área de contenido principal (excluye navegación, pie de página, barra lateral, anuncios).
3. Conserva la estructura de encabezados (etiquetas H1-H6).
4. Conserva los límites de los párrafos, listas y tablas.
5. Calcula el recuento total de palabras del contenido principal.

### Paso 2: Segmentar el Contenido en Bloques

1. Divide el contenido en cada encabezado (H2 o H3) para crear bloques de contenido.
2. Para cada bloque, registra:
   - El texto del encabezado
   - Todo el contenido de texto debajo de ese encabezado
   - Cantidad de palabras del bloque
   - Número de párrafos
   - Número de listas y tablas
   - Número de estadísticas/puntos de datos
   - Si el bloque contiene un patrón de definición
   - Si las primeras 60 palabras forman una respuesta independiente

### Paso 3: Puntuar Cada Bloque

Para cada bloque de contenido, calcula:
- Subpuntuación de Calidad de Bloque de Respuesta (0-100)
- Subpuntuación de Autocontención (0-100)
- Subpuntuación de Legibilidad Estructural (0-100)
- Subpuntuación de Densidad Estadística (0-100)
- Subpuntuación de Unicidad (0-100)

**Puntuación de Citabilidad del Bloque** = (Respuesta * 0.30) + (AutoCont * 0.25) + (Estructura * 0.20) + (Estadísticas * 0.15) + (Único * 0.10)

### Paso 4: Calcular Puntuación a Nivel de Página

1. Calcula el promedio de todas las puntuaciones de los bloques para la puntuación de citabilidad a nivel de página.
2. Identifica los top 3 bloques con mayor puntuación (resáltalos como fortalezas).
3. Identifica los 3 bloques con menor puntuación (márcalos para reescritura).
4. Calcula el porcentaje de bloques que puntúan por encima de 70 (la métrica de "cobertura de citabilidad").

### Paso 5: Generar Sugerencias de Reescritura

Para cada bloque con puntuación por debajo de 60, genera una sugerencia de reescritura específica:
1. Identifica la debilidad principal (respuesta enterrada/oculta, falta de datos/hechos, mala estructura, etc.).
2. Propón una oración de apertura reescrita usando una definición o un patrón de respuesta-primero.
3. Sugiere estadísticas o hechos específicos que podrían añadirse.
4. Recomienda mejoras estructurales (añadir lista, añadir tabla, dividir párrafo).

---

## Formato de Salida

Genera un archivo llamado `GEO-CITABILITY-SCORE.md`:

```markdown
# Análisis de Citabilidad para IA: [Título de la Página]

**URL:** [URL]
**Fecha de Análisis:** [Fecha]
**Puntuación General de Citabilidad: [X]/100**
**Cobertura de Citabilidad:** El [X]% de los bloques de contenido obtienen más de 70 puntos.

---

## Resumen de Puntuación

| Categoría | Puntuación | Peso | Ponderada |
|---|---|---|---|
| Calidad del Bloque de Respuesta | [X]/100 | 30% | [X] |
| Autocontención del Pasaje | [X]/100 | 25% | [X] |
| Legibilidad Estructural | [X]/100 | 20% | [X] |
| Densidad Estadística | [X]/100 | 15% | [X] |
| Unicidad y Datos Originales | [X]/100 | 10% | [X] |
| **General** | | | **[X]/100** |

---

## Bloques de Contenido Más Fuertes

### 1. "[Encabezado]" -- Puntuación: [X]/100
> [Primeras 2 oraciones del bloque]

**Por qué funciona:** [Explicación]

### 2. "[Encabezado]" -- Puntuación: [X]/100
> [Primeras 2 oraciones del bloque]

**Por qué funciona:** [Explicación]

---

## Bloques de Contenido Más Débiles (Prioridad de Reescritura)

### 1. "[Encabezado]" -- Puntuación: [X]/100

**Apertura actual:**
> [Primeras 2 oraciones tal y como existen]

**Problema:** [Problema específico -- respuesta enterrada, sin hechos, etc.]

**Reescritura sugerida:**
> [Apertura reescrita 2-3 oraciones con patrón de respuesta primero y hechos]

**Mejoras adicionales:**
- [Añadir tabla comparando X, Y, Z]
- [Incluir estadística sobre ...]
- [Dividir párrafo largo en 2-3 más cortos]

---

## Recomendaciones de Reformateo (Victorias Rápidas)

1. **[Recomendación específica]** -- Aumento de citabilidad esperado: +[X] puntos
2. **[Recomendación específica]** -- Aumento de citabilidad esperado: +[X] puntos
3. **[Recomendación específica]** -- Aumento de citabilidad esperado: +[X] puntos
4. **[Recomendación específica]** -- Aumento de citabilidad esperado: +[X] puntos
5. **[Recomendación específica]** -- Aumento de citabilidad esperado: +[X] puntos

---

## Puntuaciones por Sección

| Encabezado de Sección | Palabras | Calidad Respuesta | Autocontenido | Estructura | Estad. | Único | General |
|---|---|---|---|---|---|---|---|
| [Encabezado H2] | [N] | [X] | [X] | [X] | [X] | [X] | [X] |
```

---

## Datos de Referencia

### Características Óptimas del Pasaje (desde investigación GEO)

- **Longitud óptima para cita IA:** 134-167 palabras (Análisis de Bortolato 2025 de pasajes de AI Overview)
- **Los patrones de definición aumentan la tasa de citación por:** 2.1x (Georgia Tech 2024)
- **Agregar estadísticas a pasajes incrementa la citación en:** 40% (Estudio GEO Princeton 2024)
- **Agregar citas textuales de autoridades incrementa la citación por:** 115% en ciertas categorías (IIT Delhi 2024)
- **Optimizar la fluidez incrementa la visibilidad por:** 30% en promedio a lo largo de todo tipo de consultas
- **El contenido con citas a fuentes es citado:** 20-25% más frecuentemente por Perplexity y búsqueda de ChatGPT

### Preferencias de Cita del Sistema de IA

| Sistema de IA | Preferencia de Citación |
|---|---|
| **ChatGPT (Search)** | Prefiere pasajes con definiciones explícitas, fuentes nombradas y fechas recientes. Tiende a citar 2-4 fuentes por respuesta. |
| **Perplexity** | Favorece fuertemente los pasajes densos en hechos y con estadísticas. Cita 4-8 fuentes por respuesta. Valora enormemente la frescura (recencia). |
| **Claude** | Prefiere pasajes bien estructurados y exhaustivos. Valora el matiz y la precisión por encima de la brevedad. |
| **Gemini (AI Overviews)** | Prefiere bloques de respuesta concisos (40-60 palabras). Valora el contenido que ya está posicionado en los top 10 resultados orgánicos. |
| **Copilot (Bing)** | Similar a Gemini. Prefiere pasajes de dominios de alta autoridad con afirmaciones factuales claras. |
