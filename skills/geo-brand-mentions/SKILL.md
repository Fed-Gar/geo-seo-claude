---
name: geo-brand-mentions
description: Escáner de autoridad y menciones de marca para visibilidad en IA. Analiza la presencia de la marca en plataformas de las que dependen los modelos de IA para el reconocimiento de entidades y decisiones de citación. Produce una Puntuación de Autoridad de Marca (0-100) con recomendaciones específicas por plataforma.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Habilidad de Escáner de Menciones de Marca

## Idea Central

Las menciones de marca se correlacionan aproximadamente 3 veces más fuertemente con la visibilidad en IA que los backlinks tradicionales. Un estudio de Ahrefs publicado en diciembre de 2025, analizando 75,000 marcas en plataformas de búsqueda por IA, encontró que las **menciones de marca sin enlace** (unlinked brand mentions) -- referencias a un nombre de marca sin un hipervínculo -- son un predictor más fuerte de si los sistemas de IA citan y recomiendan una marca que el Domain Rating (DR) o el conteo de backlinks.

El hallazgo crítico: **la plataforma donde aparece la mención importa enormemente**. No todas las menciones son iguales. Una mención en YouTube o Reddit tiene mucho más peso para la citación de IA que una mención en un blog de baja autoridad, porque los datos de entrenamiento de IA y los sistemas de recuperación indexan desproporcionadamente las plataformas de alta interacción (engagement).

Esto invierte una suposición fundamental del SEO tradicional. En el SEO tradicional, un backlink (dofollow) desde un sitio de alto DR es el estándar de oro. En GEO, una mención sin enlace en Reddit o en la descripción de un video de YouTube puede ser más valiosa que un backlink dofollow de un blog DR 70.

---

## Clasificación de Importancia de Plataformas para Citas de IA

Basado en el estudio de Ahrefs de diciembre de 2025 y en la investigación corroborante de Profound (2025) y Terakeet (2025):

### 1. Menciones en YouTube -- Correlación ~0.737 (LA MÁS FUERTE)

**Por qué importa más YouTube:**
- YouTube es el segundo motor de búsqueda más grande y la plataforma de video más grande a nivel global (2.5B+ usuarios mensuales).
- Los conjuntos de datos de entrenamiento de IA incorporan en gran medida transcripciones, descripciones y metadatos de YouTube.
- Gemini y los Resúmenes de IA (AI Overviews) de Google referencian directamente el contenido de YouTube.
- Tanto Perplexity como ChatGPT indexan y citan contenido de video de YouTube.
- Las transcripciones de YouTube son particularmente valiosas porque contienen menciones en lenguaje natural en un contexto conversacional, lo que se alinea con cómo los modelos de IA procesan y generan texto.

**Qué revisar:**
- **Canal de YouTube de la marca:** ¿Tiene la marca un canal activo de YouTube? ¿Cuántos suscriptores? ¿Cantidad de videos? ¿Frecuencia de carga?
- **Menciones en videos de terceros:** ¿Otros YouTubers o canales mencionan la marca? ¿En qué contexto (reseñas, tutoriales, comparaciones)?
- **Descripciones de videos:** ¿Aparece el nombre de la marca en descripciones de videos de contenido relevante para la industria?
- **Transcripciones de videos:** ¿Se menciona la marca en el contenido hablado de videos relevantes? (Los modelos de IA indexan las transcripciones)
- **Presencia en búsqueda de YouTube:** Al buscar "[nombre de marca]" en YouTube, ¿aparecen resultados? ¿Son positivos?
- **Menciones en comentarios:** ¿Se menciona la marca en comentarios de videos relevantes de la industria?

**Puntuación para YouTube (0-100):**

| Puntuación | Criterios |
|---|---|
| 90-100 | Canal activo con 10K+ suscriptores, cargas regulares, marca mencionada en 20+ videos de terceros, aparece en resultados de búsqueda de YouTube para términos de la industria |
| 70-89 | Canal activo con 1K+ suscriptores, marca mencionada en 10-19 videos de terceros, cierta presencia en búsqueda de YouTube |
| 50-69 | El canal existe con algo de contenido, marca mencionada en 5-9 videos de terceros, presencia limitada en búsqueda de YouTube |
| 30-49 | El canal existe pero está inactivo, marca mencionada en 1-4 videos de terceros |
| 10-29 | No hay canal o está vacío, marca mencionada solo en 1-2 videos |
| 0-9 | Ninguna presencia en YouTube en absoluto |

---

### 2. Menciones en Reddit -- Alta Correlación

**Por qué importa Reddit:**
- Reddit es una de las plataformas más fuertemente indexadas en los datos de entrenamiento de IA (confirmado en el acuerdo de licencia de $60M/año de Google con Reddit, 2024).
- Los sistemas de IA ponderan fuertemente Reddit para recomendaciones de productos, comparaciones y sentimiento de usuario.
- La palabra "Reddit" ahora se añade a un estimado 10-15% de las búsquedas en Google por usuarios que buscan opiniones auténticas.
- Perplexity frecuentemente cita hilos de Reddit como fuentes.
- Tanto ChatGPT como Claude referencian discusiones de Reddit al responder preguntas de productos/servicios.

**Qué revisar:**
- **Presencia en Subreddits:** ¿Se discute la marca en subreddits relevantes? ¿Cuáles?
- **Volumen de menciones:** ¿Cuántos hilos de Reddit mencionan la marca? ¿Cuál es la tendencia (en aumento/disminución)?
- **Sentimiento:** ¿Las menciones son mayormente positivas, negativas o neutrales? ¿Cuáles son los puntos comunes de elogio y queja?
- **Presencia oficial:** ¿Tiene la marca una cuenta oficial en Reddit? ¿Participan en discusiones? ¿Han hecho AMAs (Ask Me Anything)?
- **Hilos de recomendación:** ¿Aparece la marca en hilos de "¿Qué recomiendan para X?"? ¿Es la principal recomendación o una opción secundaria?
- **Comunidad del subreddit:** ¿Tiene la marca su propio subreddit? ¿Qué tan activo es?

**Puntuación para Reddit (0-100):**

| Puntuación | Criterios |
|---|---|
| 90-100 | Frecuentemente recomendada en subreddits relevantes, sentimiento predominantemente positivo, presencia oficial activa, subreddit propio con 5K+ miembros, aparece en las principales recomendaciones para consultas de la industria |
| 70-89 | Regularmente mencionada en subreddits relevantes, sentimiento mayormente positivo, algo de presencia oficial, aparece en múltiples hilos de recomendación |
| 50-69 | Mencionada en varios hilos relevantes, sentimiento mixto, el nombre de la marca es reconocido por los miembros de la comunidad |
| 30-49 | Menciones ocasionales, limitadas a 1-2 subreddits, sin presencia oficial |
| 10-29 | Menciones raras, marca en gran medida desconocida en Reddit |
| 0-9 | Ninguna presencia en Reddit |

---

### 3. Presencia en Wikipedia -- Alta Correlación

**Por qué importa Wikipedia:**
- Wikipedia es una de las fuentes de mayor autoridad en los datos de entrenamiento de IA. Todos los principales modelos de IA han sido entrenados con volcados (dumps) de Wikipedia.
- Los sistemas de IA usan Wikipedia como fuente principal para el reconocimiento de entidades -- determinando si una marca es una entidad "real" que vale la pena conocer.
- Wikidata (el hermano de datos estructurados de Wikipedia) proporciona hechos legibles por máquina que los modelos de IA usan para la construcción de grafos de conocimiento.
- Tener una página de Wikipedia es una fuerte señal de notabilidad, lo que se correlaciona con que los sistemas de IA traten a la marca como una entidad autorizada.

**Qué revisar:**
- **Página de Wikipedia:** ¿La marca o empresa tiene su propio artículo en Wikipedia? ¿Está marcado para eliminación o problemas de calidad?
- **Página del Fundador:** ¿El fundador/CEO tiene una página en Wikipedia? (Fuerte señal de autoridad)
- **Citas en Wikipedia:** ¿Se cita el sitio web de la marca como referencia en algún artículo de Wikipedia?
- **Entrada en Wikidata:** ¿Tiene la marca un elemento de Wikidata (número Q)? ¿Qué tan completo está?
- **Menciones en Wikipedia:** ¿Se menciona la marca en otros artículos de Wikipedia (artículos de la industria, páginas de competidores, páginas de categorías)?
- **Calidad del artículo:** Si existe una página de Wikipedia, ¿es un esbozo (stub), clase inicial (start-class), o de mayor calidad?

**Puntuación para Wikipedia (0-100):**

| Puntuación | Criterios |
|---|---|
| 90-100 | Artículo detallado en Wikipedia (clase B o superior), entrada de Wikidata con propiedades completas, marca citada como referencia en múltiples artículos, fundador tiene página de Wikipedia |
| 70-89 | Artículo de Wikipedia existe (clase inicial o superior), entrada de Wikidata existe, marca mencionada en 2+ otros artículos de Wikipedia |
| 50-69 | Artículo de Wikipedia existe (esbozo o inicial), entrada básica de Wikidata, menciones limitadas en otros artículos |
| 30-49 | Sin artículo de Wikipedia pero la marca se menciona en otros artículos o se cita como referencia; puede existir entrada en Wikidata |
| 10-29 | Marca mencionada en 1-2 artículos de Wikipedia solo como una referencia pasajera |
| 0-9 | Sin presencia en Wikipedia ni Wikidata de ningún tipo |

---

### 4. Presencia en LinkedIn -- Correlación Moderada

**Por qué importa LinkedIn:**
- El contenido de LinkedIn es cada vez más indexado por sistemas de IA para contexto profesional y B2B.
- Las páginas de empresas en LinkedIn y las publicaciones de liderazgo intelectual (thought leadership) de los empleados construyen señales de entidad de marca.
- Los modelos de IA referencian LinkedIn para obtener información de la empresa, credenciales del equipo y autoridad profesional.
- Los artículos y publicaciones de LinkedIn son indexados por motores de búsqueda y rastreadores de IA.

**Qué revisar:**
- **Página de empresa:** ¿Tiene la marca una página de empresa en LinkedIn? ¿Cantidad de seguidores? ¿Frecuencia de publicación?
- **Liderazgo intelectual de empleados:** ¿Están los empleados (especialmente el liderazgo) publicando contenido de liderazgo intelectual que mencione la marca?
- **Menciones a la empresa:** ¿Es la marca mencionada en publicaciones de LinkedIn por personas que no son empleados? ¿Analistas de la industria? ¿Clientes?
- **Artículos de LinkedIn:** ¿Hay artículos de formato largo en LinkedIn acerca de la marca o mencionándola?
- **Perfiles de empleados:** ¿Los empleados listan la empresa con descripciones detalladas? ¿Tienen perfiles profesionales fuertes?
- **Métricas de interacción:** ¿Cuál es la interacción típica (likes, comentarios, compartidos) en las publicaciones de la empresa?

**Puntuación para LinkedIn (0-100):**

| Puntuación | Criterios |
|---|---|
| 90-100 | Página de empresa activa con 10K+ seguidores, el liderazgo publica regularmente liderazgo intelectual, marca frecuentemente mencionada por profesionales de la industria, fuertes perfiles de empleados |
| 70-89 | Página de empresa activa con 5K+ seguidores, algo de liderazgo intelectual de empleados, menciones ocasionales de terceros |
| 50-69 | La página de la empresa existe con 1K+ seguidores, publicación irregular, menciones limitadas de terceros |
| 30-49 | La página de la empresa existe pero es escasa o inactiva, pocos seguidores, sin menciones de terceros |
| 10-29 | Página de empresa básica con información mínima |
| 0-9 | Sin página de empresa en LinkedIn |

---

### 5. Presencia en Otras Plataformas -- Suplementario

Estas plataformas tienen una correlación más baja, pero aun así significativa con la visibilidad en IA:

#### Quora
- **Relevancia:** Las respuestas de Quora se incluyen frecuentemente en datos de entrenamiento de IA y son citadas por Perplexity.
- **Qué revisar:** ¿Se menciona la marca en respuestas de Quora a preguntas relevantes de la industria? ¿Tiene la marca una presencia oficial en Quora?
- **Fuerza de la señal:** Moderada para B2C, baja para B2B.

#### Stack Overflow / Stack Exchange
- **Relevancia:** Crítica para marcas dirigidas a desarrolladores (SaaS, herramientas dev, APIs).
- **Qué revisar:** ¿El producto de la marca es discutido en preguntas/respuestas de Stack Overflow? ¿Tiene la marca una etiqueta (tag)? ¿Tienen una cuenta oficial respondiendo preguntas?
- **Fuerza de la señal:** Alta para productos técnicos, irrelevante para la mayoría de B2C.

#### GitHub
- **Relevancia:** Crítica para marcas enfocadas en código abierto y desarrolladores.
- **Qué revisar:** ¿Tiene la marca una organización en GitHub? ¿Estrellas en los repositorios? ¿Menciones en la documentación o discusiones de otros repositorios?
- **Fuerza de la señal:** Alta para herramientas de desarrollo y código abierto, baja para marcas no técnicas.

#### Foros y Comunidades de la Industria
- **Relevancia:** Señales de autoridad de nicho que los modelos de IA recogen de datos de entrenamiento específicos del dominio.
- **Qué revisar:** ¿Se discute la marca en foros específicos de la industria (ej., Hacker News para tecnología, ProductHunt para startups, comunidades de Slack específicas)?
- **Fuerza de la señal:** Moderada, pero valiosa para establecer autoridad de nicho.

#### Noticias y Prensa
- **Relevancia:** Las menciones en noticias construyen autoridad de entidad y señales de frescura (recencia).
- **Qué revisar:** ¿La marca ha sido cubierta por medios de noticias importantes o publicaciones de la industria? ¿Qué tan recientemente? ¿En qué contexto?
- **Fuerza de la señal:** Moderada. La frescura importa -- una mención en los últimos 6 meses es mucho más valiosa que una de hace 3 años.

#### Podcasts
- **Relevancia:** Fuente de datos de entrenamiento de IA en crecimiento. Las transcripciones se indexan cada vez más.
- **Qué revisar:** ¿La marca o su liderazgo han aparecido en podcasts? ¿Las transcripciones de podcasts que mencionan la marca están indexadas por los motores de búsqueda?
- **Fuerza de la señal:** Moderada y en crecimiento.

---

## Puntuación de Autoridad de Marca Compuesta

### Fórmula de Puntuación

| Plataforma | Peso | Justificación |
|---|---|---|
| Presencia en YouTube | 25% | Mayor correlación con citación de IA (0.737) |
| Presencia en Reddit | 25% | Segunda mayor correlación; crítica para recomendaciones de productos |
| Wikipedia / Wikidata | 20% | Base del reconocimiento de entidades; pilar de datos de entrenamiento IA |
| Autoridad en LinkedIn | 15% | Señales de autoridad profesional; relevancia B2B |
| Otras Plataformas | 15% | Señales suplementarias de Quora, GitHub, noticias, foros, podcasts |

**Fórmula:**
```
Puntuacion_Autoridad_Marca = (YouTube * 0.25) + (Reddit * 0.25) + (Wikipedia * 0.20) + (LinkedIn * 0.15) + (Otros * 0.15)
```

### Interpretación de Puntuación

| Rango de Puntuación | Calificación | Interpretación |
|---|---|---|
| 85-100 | Dominante | La marca es una entidad bien reconocida a través de plataformas de IA. Altamente probable de ser citada y recomendada por sistemas de IA. |
| 70-84 | Fuerte | La marca tiene una sólida presencia multiplataforma. Es probable que los sistemas de IA la reconozcan y citen para consultas relevantes. |
| 50-69 | Moderada | La marca tiene presencia en algunas plataformas pero existen vacíos. La citación en IA es inconsistente. |
| 30-49 | Débil | La marca tiene presencia limitada en las plataformas. Los sistemas de IA podrían no reconocerla como una entidad distinta. |
| 0-29 | Mínima | La marca tiene presencia insignificante en las plataformas. Es muy improbable que los sistemas de IA la citen o recomienden. |

---

## Procedimiento de Análisis

### Paso 1: Identificar Información de la Marca

Recopila lo siguiente del usuario o del sitio web:
- **Nombre de la marca** (ortografía exacta, incluyendo variantes oficiales)
- **Nombre(s) de Fundador/CEO**
- **URL del dominio**
- **Industria/categoría**
- **Productos o servicios clave** (top 3)
- **Principales competidores** (para contexto comparativo)

### Paso 2: Escaneo de Plataformas

Para cada plataforma, usa WebFetch para buscar y evaluar la presencia:

**Comprobación en YouTube:**
1. Buscar: `[nombre de marca] site:youtube.com`
2. Revisar: `youtube.com/@[nombre-marca]` o `youtube.com/c/[nombre-marca]` para el canal oficial
3. Buscar: `"[nombre de marca]" site:youtube.com` (coincidencia exacta para menciones en descripciones)
4. Nota: Cuenta de suscriptores del canal, recuento de videos, fecha de última carga, recuento de menciones de terceros

**Comprobación en Reddit:**
1. Buscar: `[nombre de marca] site:reddit.com`
2. Buscar: `"[nombre de marca]" site:reddit.com` (coincidencia exacta)
3. Revisar: `reddit.com/r/[nombre-marca]` para subreddit oficial
4. Revisar: `reddit.com/user/[nombre-marca]` para cuenta oficial
5. Nota: Cantidad de hilos, subreddits dominantes, sentimiento (positivo/negativo/neutral), frecuencia de recomendación

**Comprobación en Wikipedia (IMPORTANTE — usar AMBOS métodos para evitar falsos negativos):**

**Método 1 — Comprobación con API Python (EL MÁS CONFIABLE, haz este PRIMERO):**
```bash
python3 -c "
import requests, json
from urllib.parse import quote_plus
brand = '[Nombre_Marca]'
# Chequear API de Wikipedia directamente
api_url = f'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={quote_plus(brand)}&format=json'
r = requests.get(api_url, headers={'User-Agent': 'GEO-Audit/1.0'}, timeout=15)
data = r.json()
results = data.get('query', {}).get('search', [])
if results and brand.lower() in results[0].get('title', '').lower():
    print(f'LA PÁGINA DE WIKIPEDIA EXISTE: {results[0][\"title\"]}')
    print(f'URL: https://en.wikipedia.org/wiki/{results[0][\"title\"].replace(\" \", \"_\")}')
else:
    print('No se encontró página directa en Wikipedia')
# Chequear Wikidata
wd_url = f'https://www.wikidata.org/w/api.php?action=wbsearchentities&search={quote_plus(brand)}&language=en&format=json'
r2 = requests.get(wd_url, headers={'User-Agent': 'GEO-Audit/1.0'}, timeout=15)
wd = r2.json()
entities = wd.get('search', [])
if entities:
    print(f'ENTRADA DE WIKIDATA: {entities[0].get(\"id\", \"\")} — {entities[0].get(\"description\", \"\")}')
"
```

**Método 2 — Comprobación directa de URL (verificación de respaldo):**
1. WebFetch: `https://en.wikipedia.org/wiki/[Nombre_Marca]` — revisar si la página carga (no una redirección a la búsqueda)
2. WebFetch: `https://en.wikipedia.org/wiki/[Nombre_Fundador]` para el artículo del fundador

**Método 3 — Búsqueda (menos confiable, úsalo solo para info suplementaria):**
1. Buscar: `[nombre de marca] site:wikipedia.org`
2. Buscar: `[nombre de marca] site:wikidata.org`

**CRÍTICO:** La búsqueda web por sí sola NO es confiable para determinar la presencia en Wikipedia. SIEMPRE ejecuta primero la comprobación con la API de Python. Si la API dice que existe una página, existe — no invalides esto con un resultado de búsqueda que no la encuentre.

5. Nota: Existencia de artículo, calidad, historial de edición, exhaustividad de Wikidata

**Comprobación en LinkedIn:**
1. Buscar: `[nombre de marca] site:linkedin.com`
2. Revisar: `linkedin.com/company/[nombre-marca]` para la página de empresa
3. Nota: Cantidad de seguidores, frecuencia de publicación, recuento de empleados listados, niveles de interacción

**Otras Plataformas:**
1. Buscar: `[nombre de marca] site:quora.com`
2. Buscar: `[nombre de marca] site:stackoverflow.com` (si es marca técnica)
3. Buscar: `[nombre de marca] site:github.com` (si es marca técnica)
4. Buscar: `[nombre de marca] site:news.ycombinator.com` (Hacker News)
5. Buscar: `"[nombre de marca]"` ampliamente para menciones en noticias (filtrar a los últimos 6 meses)
6. Nota: Presencia/ausencia y calidad de las menciones en cada plataforma

### Paso 3: Evaluación de Sentimiento

Para Reddit y otras plataformas de discusión, evalúa el sentimiento analizando las menciones más recientes y prominentes:

| Sentimiento | Indicadores |
|---|---|
| **Positivo** | Recomendaciones ("Me encanta [marca]", "Cambiamos a [marca] y...", "Altamente recomendable"), menciones upvoteadas (con votos a favor), comparación positiva frente a competidores |
| **Neutral** | Menciones factuales ("Usamos [marca] para...", "[Marca] ofrece..."), preguntas sobre la marca, comparaciones equilibradas |
| **Negativo** | Quejas ("Evita [marca]", "[Marca] tiene un soporte terrible"), recomendaciones downvoteadas, comparaciones negativas |
| **Mixto** | Combinación de positivo y negativo. Anota la proporción y los temas principales. |

### Paso 4: Comparación Competitiva (Opcional)

Si se identifican competidores, haz un escaneo rápido de su presencia en las plataformas para dar contexto. Esto ayuda a calibrar la puntuación -- una marca con "moderada" presencia en Reddit en una industria donde los competidores tienen cero presencia en Reddit es relativamente fuerte.

### Paso 5: Cálculo de Puntuación

1. Puntúa cada plataforma (0-100) usando las rúbricas anteriores.
2. Aplica los pesos para calcular la Puntuación Compuesta de Autoridad de Marca.
3. Identifica las plataformas más fuertes y más débiles.
4. Genera recomendaciones específicas y accionables para las plataformas más débiles.

---

## Formato de Salida

Genera un archivo llamado `GEO-BRAND-MENTIONS.md`:

```markdown
# Reporte de Autoridad de Marca: [Nombre de Marca]

**Fecha de Análisis:** [Fecha]
**Marca:** [Nombre de Marca]
**Dominio:** [URL]
**Industria:** [Industria]

---

## Puntuación de Autoridad de Marca: [X]/100 ([Calificación])

### Desglose por Plataforma

| Plataforma | Puntuación | Peso | Ponderado | Estado |
|---|---|---|---|---|
| YouTube | [X]/100 | 25% | [X] | [Canal Activo / Mencionada / Ausente] |
| Reddit | [X]/100 | 25% | [X] | [Activa / Discutida / Ausente] |
| Wikipedia | [X]/100 | 20% | [X] | [Artículo / Mencionada / Ausente] |
| LinkedIn | [X]/100 | 15% | [X] | [Activa / Básica / Ausente] |
| Otras Plataformas | [X]/100 | 15% | [X] | [Resumen] |
| **Total** | | | **[X]/100** | |

---

## Detalle de Plataforma

### YouTube ([X]/100)

**Canal Oficial:** [Sí/No] | [URL si existe]
**Suscriptores:** [Cantidad o N/A]
**Videos:** [Cantidad o N/A]
**Última Carga:** [Fecha o N/A]
**Menciones de Terceros:** [Cantidad estimada]
**Hallazgos Clave:**
- [Hallazgo 1]
- [Hallazgo 2]

### Reddit ([X]/100)

**Cuenta Oficial:** [Sí/No] | [URL si existe]
**Subreddit Propio:** [Sí/No] | [URL y número de miembros si existe]
**Volumen de Menciones:** [Cantidad estimada de hilos]
**Subreddits Principales:** [Lista de subreddits donde se discute la marca]
**Sentimiento:** [Positivo/Negativo/Neutral/Mixto]
**Hallazgos Clave:**
- [Hallazgo 1]
- [Hallazgo 2]

### Wikipedia ([X]/100)

**Artículo de la Empresa:** [Sí/No] | [URL si existe]
**Artículo del Fundador:** [Sí/No] | [URL si existe]
**Entrada en Wikidata:** [Sí/No] | [Número Q si existe]
**Citada en Otros Artículos:** [Sí/No] | [Cuáles artículos]
**Hallazgos Clave:**
- [Hallazgo 1]
- [Hallazgo 2]

### LinkedIn ([X]/100)

**Página de Empresa:** [Sí/No] | [URL si existe]
**Seguidores:** [Cantidad o N/A]
**Frecuencia de Publicación:** [Semanal/Mensual/Rara vez/Nunca]
**Hallazgos Clave:**
- [Hallazgo 1]
- [Hallazgo 2]

### Otras Plataformas ([X]/100)

| Plataforma | Presencia | Notas |
|---|---|---|
| Quora | [Sí/No] | [Nota breve] |
| Stack Overflow | [Sí/No] | [Nota breve] |
| GitHub | [Sí/No] | [Nota breve] |
| Hacker News | [Sí/No] | [Nota breve] |
| Noticias/Prensa | [Sí/No] | [Nota breve] |
| Podcasts | [Sí/No] | [Nota breve] |

---

## Recomendaciones

### Acciones Inmediatas (Semana 1-2)

1. **[Plataforma]:** [Acción específica a tomar con impacto esperado]
2. **[Plataforma]:** [Acción específica]

### Estrategia a Corto Plazo (Mes 1-3)

1. **[Plataforma]:** [Estrategia con tácticas]
2. **[Plataforma]:** [Estrategia con tácticas]

### Construcción de Autoridad a Largo Plazo (Mes 3-12)

1. **[Plataforma]:** [Estrategia a largo plazo]
2. **[Plataforma]:** [Estrategia a largo plazo]

---

## Contexto Competitivo

[Si se analizaron competidores, mostrar una breve tabla de comparación]

| Marca | YouTube | Reddit | Wikipedia | LinkedIn | Otros | Total |
|---|---|---|---|---|---|---|
| [Marca Principal] | [X] | [X] | [X] | [X] | [X] | **[X]** |
| [Competidor 1] | [X] | [X] | [X] | [X] | [X] | **[X]** |
| [Competidor 2] | [X] | [X] | [X] | [X] | [X] | **[X]** |

## Conclusión Clave

[Resumen de 1-2 oraciones del estado de visibilidad en IA de la marca y la acción individual más impactante a tomar]
```

---

## Datos de Referencia

### Fuerza de Correlaciones (Ahrefs Dic 2025, 75K Marcas)

| Señal | Correlación con Citas IA | Valor SEO Tradicional |
|---|---|---|
| Menciones en YouTube | ~0.737 | Bajo (no es factor de ranking) |
| Menciones en Reddit | Alto (coef. exacto no publicado) | Bajo |
| Presencia en Wikipedia | Alto | Moderado (señal de confianza) |
| Presencia en LinkedIn | Moderado | Bajo |
| Domain Rating (DR) | ~0.266 | Muy Alto |
| Cantidad de backlinks | ~0.266 | Muy Alto |
| Tráfico orgánico | Moderado | Muy Alto |

**Idea clave:** Las señales que más importan para la visibilidad en IA (YouTube, Reddit) son casi irrelevantes en SEO tradicional, y las señales que más importan en el SEO tradicional (backlinks, DR) son predictores débiles de visibilidad en IA. Esto requiere una estrategia de optimización fundamentalmente diferente.

### Consejos Específicos por Plataforma para Construir Presencia

**Victorias Rápidas en YouTube:**
- Crea un canal y sube 3-5 videos explicativos sobre tus temas principales.
- Asegúrate de que tu nombre de marca aparezca en los títulos, descripciones y contenido hablado de los videos.
- Busca apariciones como invitado en canales de YouTube relevantes de la industria.
- Crea videos de comparación o "alternativas" (estos son citados por IA para consultas de comparación).

**Victorias Rápidas en Reddit:**
- Identifica 3-5 subreddits donde tu audiencia objetivo sea activa.
- Participa de manera auténtica (no hagas spam/promoción engañosa -- las comunidades de Reddit detectan y castigan esto).
- Haz un AMA si es apropiado para tu marca.
- Monitorea y responde a las menciones de tu marca.
- Crea publicaciones genuinamente útiles que naturalmente mencionen la experiencia de tu marca.

**Estrategia para Wikipedia:**
- Contrata un consultor conocedor de Wikipedia -- NO edites tu propio artículo (conflicto de intereses).
- Construye notabilidad a través de cobertura de prensa, citas académicas y reconocimiento de la industria primero.
- Asegúrate de que tu entrada de Wikidata esté completa, incluso si no tienes un artículo en Wikipedia.
- Contribuye en artículos relevantes de la industria donde tu marca pueda ser naturalmente citada como fuente.

**Victorias Rápidas en LinkedIn:**
- Optimiza tu página de empresa con información completa y publicaciones regulares.
- Anima al liderazgo a publicar contenido de liderazgo intelectual (thought leadership) semanalmente.
- Publica artículos de LinkedIn sobre temas en los que tu marca tenga una experiencia única.
- Participa en discusiones de la industria para aumentar la visibilidad de la marca en contextos profesionales.
