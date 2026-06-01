# Metodología de Puntuación

La Puntuación GEO (GEO Score) es un número compuesto único del 0 al 100 que resume qué tan bien optimizado está un sitio web para el descubrimiento, la citación y la recomendación por sistemas de IA como ChatGPT, Perplexity, Claude y Google AI Overviews. Se calcula como un promedio ponderado de seis sub-puntuaciones de categoría, cada una evaluada independientemente por un subagente especializado. Una puntuación alta indica una fuerte preparación para la visibilidad en motores generativos; una puntuación baja apunta a brechas concretas con un plan de acción priorizado acompañante.

---

## Tabla de pesos

| Categoría | Peso |
|---|---|
| Citabilidad & Visibilidad IA | 25% |
| Señales de Autoridad de Marca | 20% |
| Calidad de Contenido & E-E-A-T | 20% |
| Fundamentos Técnicos | 15% |
| Datos Estructurados | 10% |
| Optimización de Plataformas | 10% |

---

## Cómo se calcula la puntuación compuesta

Cada subagente devuelve una sub-puntuación en una escala de 0–100. El orquestador en [`skills/geo-audit/SKILL.md`](../skills/geo-audit/SKILL.md) multiplica cada sub-puntuación por su peso y suma los resultados.

**Fórmula (de `skills/geo-audit/SKILL.md`):**

```
GEO_Score = (Citability   * 0.25)
          + (Brand        * 0.20)
          + (EEAT         * 0.20)
          + (Technical    * 0.15)
          + (Schema       * 0.10)
          + (Platform     * 0.10)
```

**Pseudocódigo:**

```python
weights = {
    "citability": 0.25,
    "brand":      0.20,
    "eeat":       0.20,
    "technical":  0.15,
    "schema":     0.10,
    "platform":   0.10,
}

geo_score = sum(sub_scores[k] * w for k, w in weights.items())
# geo_score está en el rango [0, 100]
```

**Interpretación de la puntuación (de `skills/geo-audit/SKILL.md`):**

| Rango | Calificación | Significado |
|---|---|---|
| 90–100 | Excelente | Altamente probable de ser citado por la IA |
| 75–89 | Bueno | Fuerte base con espacio para mejora |
| 60–74 | Aceptable | Presencia moderada; oportunidades significativas |
| 40–59 | Pobre | Señales débiles; sistemas de IA pueden batallar para citar |
| 0–39 | Crítico | Mayormente invisible para los sistemas de IA |

---

## Citabilidad & Visibilidad IA (25%)

**Implementado por:** [`agents/geo-ai-visibility.md`](../agents/geo-ai-visibility.md) y [`scripts/citability_scorer.py`](../scripts/citability_scorer.py)

### Lo que revisa el calificador

La sub-puntuación de citabilidad es en sí misma un compuesto ponderado de cuatro componentes (pesos de `agents/geo-ai-visibility.md`):

| Componente | Peso |
|---|---|
| Puntuación de Citabilidad | 35% |
| Puntuación de Mención de Marca | 30% |
| Puntuación de Acceso a Rastreadores | 25% |
| Puntuación de llms.txt | 10% |

**La puntuación de citabilidad** (`scripts/citability_scorer.py`) analiza cada bloque sustancial de contenido en la página — secciones delimitadas por encabezados — y puntúa cada uno en cinco dimensiones:

| Dimensión | Puntos máx | Señales clave |
|---|---|---|
| Calidad de Bloque de Respuesta | 30 | Patrones de definición ("X es un…", "X se refiere a…"), respuesta apareciendo en las primeras 60 palabras, encabezado basado en preguntas, oraciones cortas y claras (5–25 palabras), afirmaciones atribuidas ("la investigación muestra que…") |
| Auto-Contención | 25 | Conteo de palabras en rango óptimo de 134–167 (10 pts), rango de 100–200 (7 pts), rango de 80–250 (4 pts); densidad de pronombres por debajo del 2% (8 pts); 3+ nombres propios (7 pts) |
| Legibilidad Estructural | 20 | Longitud promedio de oración de 10–20 palabras (8 pts); palabras de transición tipo lista (4 pts); ítems numerados o referencias a pasos (4 pts); saltos de párrafo (4 pts) |
| Densidad Estadística | 15 | Porcentajes (3 pts c/u, máx 6); cantidades monetarias (3 pts c/u, máx 5); números con contexto de unidad (2 pts c/u, máx 4); referencias a años (2 pts); fuentes nombradas (2 pts) |
| Señales de Unicidad | 10 | Lenguaje de investigación original ("nuestro estudio encontró…") (5 pts); referencias a casos de estudio o ejemplos del mundo real (3 pts); menciones a herramientas/productos específicos (2 pts) |

La puntuación del pasaje es la suma de las cinco dimensiones (máximo 100). La puntuación de citabilidad a nivel de página es el promedio de los cinco bloques con mayor puntuación, o de todos los bloques cuando hay menos de cinco.

**Puntuación de Acceso a Rastreadores** (`agents/geo-ai-visibility.md`) comienza en 100 y deduce:
- 15 puntos por cada rastreador crítico bloqueado (GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot, GoogleBot)
- 5 puntos por cada rastreador secundario bloqueado
- 10 puntos si no se hace referencia a ningún sitemap en robots.txt
- Piso en 0

**Puntuación de llms.txt** (`agents/geo-ai-visibility.md` y `scripts/llmstxt_generator.py`):
- 0 — ausente
- 30 — presente pero malformado
- 50 — presente, formato válido, contenido mínimo
- 70 — presente, válido, cubre áreas de contenido principales
- 90–100 — integral, con `/llms-full.txt` también disponible

### Cómo se ve lo bueno vs lo malo

Una buena puntuación de Citabilidad en IA (70+) significa que la página tiene múltiples pasajes que son autónomos, densos en hechos y responden directamente preguntas; se permiten todos los principales rastreadores de IA en robots.txt; y un archivo llms.txt está presente y bien estructurado. Una puntuación pobre (por debajo de 40) típicamente indica prosa delgada o altamente dependiente del contexto, rastreadores IA bloqueados, y la falta de llms.txt.

---

## Señales de Autoridad de Marca (20%)

**Implementado por:** [`agents/geo-ai-visibility.md`](../agents/geo-ai-visibility.md) y [`scripts/brand_scanner.py`](../scripts/brand_scanner.py)

### Lo que revisa el calificador

La autoridad de la marca se evalúa comprobando la presencia de la marca en las plataformas de las que los modelos de IA se alimentan en gran medida al formar el conocimiento de las entidades. La Puntuación de Mención de Marca (utilizada como entrada para el compuesto de Visibilidad IA más arriba) se construye a partir de:

| Plataforma | Puntos disponibles | Método |
|---|---|---|
| Wikipedia | 30 | Búsqueda en API Wikipedia; Búsqueda de entidad Wikidata (`scripts/brand_scanner.py`) |
| Fuentes de industria / nicho | 25 | Plataformas de reseñas (G2, Trustpilot, Capterra), menciones en prensa, sitios de industria autorizados |
| Reddit | 20 | Presencia, recencia y sentimiento de discusiones de la marca |
| YouTube | 15 | Existencia de canal oficial y cobertura en videos de terceros |
| LinkedIn | 10 | Presencia de página de empresa y actividad |

Los valores de correlación citados en `scripts/brand_scanner.py` provienen de un estudio de Ahrefs en Diciembre de 2025 de 75,000 marcas: YouTube muestra la mayor correlación (0.737) con citas en IA; calificación de dominio / enlaces entrantes muestran una correlación débil (0.266).

### Cómo se ve lo bueno vs lo malo

Una puntuación fuerte en autoridad de marca requiere una presencia activa en Wikipedia (la señal de mayor peso), discusión a nivel comunitario en Reddit y presencia en YouTube con contenido educativo o de reseñas. Una marca sin página de Wikipedia, sin discusión en Reddit y sin presencia en YouTube obtendrá una puntuación cercana a 0 en esta sub-puntuación, sin importar cuán conocida sea en la búsqueda tradicional.

---

## Calidad de Contenido & E-E-A-T (20%)

**Implementado por:** [`agents/geo-content.md`](../agents/geo-content.md)

### Lo que revisa el calificador

El agente de contenido evalúa la página frente al marco de E-E-A-T de Google. Cada una de las cuatro dimensiones se puntúa de 0–25 y luego se normaliza a 0–15 para la ponderación dentro de la puntuación de contenido:

| Dimensión | Máx (bruto) | Señales clave revisadas |
|---|---|---|
| Experiencia (Experience) | 25 | Investigación o datos originales, estudios de caso con resultados medibles, relatos en primera persona, comparaciones antes/después, nombres y cifras específicas |
| Conocimiento (Expertise) | 25 | Autor nombrado con credenciales, página de autor enlazada con biografía, profundidad técnica, transparencia en la metodología, Schema de Persona |
| Autoridad (Authoritativeness) | 25 | Calidad de página Acerca de, citas externas, reconocimiento de la industria, menciones en medios, enlaces schema sameAs |
| Confiabilidad (Trustworthiness) | 25 | HTTPS, información de contacto visible, política de privacidad, estándares editoriales, fuentes transparentes, fechas de publicación y actualización |

Más allá del E-E-A-T, la puntuación de contenido total (0–100) también incorpora:

| Componente | Peso | Señales |
|---|---|---|
| E-E-A-T (combinado, normalizado) | 60% | Las cuatro dimensiones arriba |
| Métricas de Contenido | 15% | Clasificación de conteo de palabras (delgado < 300 palabras; inmersión profunda 3000+), legibilidad Flesch aproximada, longitud de párrafo, jerarquía de encabezados |
| Evaluación Contenido IA | 10% | Ausencia de frases patrón de IA genéricas, presencia de voz autoral, datos originales |
| Autoridad Temática | 10% | Amplitud del contenido (páginas relacionadas), profundidad de enlazado interno, estructura hub-y-cluster |
| Frescura de Contenido | 5% | Fechas de publicación y modificación visibles, recencia para temas sensibles al tiempo |

### Cómo se ve lo bueno vs lo malo

Una puntuación de 70+ requiere un autor claramente identificado con credenciales verificables, datos originales o casos de estudio, fuentes transparentes, HTTPS, y contenido que vaya más allá de la cobertura superficial del tema. Una puntuación por debajo de 30 normalmente significa sin atribución al autor, sin fuentes externas, sin HTTPS, y un contenido que podría haber sido escrito por cualquiera sin experiencia en la materia.

---

## Fundamentos Técnicos (15%)

**Implementado por:** [`agents/geo-technical.md`](../agents/geo-technical.md)

### Lo que revisa el calificador

El agente técnico calcula una puntuación a partir de nueve componentes ponderados:

| Componente | Peso |
|---|---|
| Renderizado en Servidor / dependencia JS | 25% |
| Etiquetas meta e indexabilidad | 15% |
| Rastreabilidad (robots.txt, sitemap) | 15% |
| Encabezados de seguridad | 10% |
| Riesgo de Core Web Vitals | 10% |
| Optimización móvil | 10% |
| Estructura de URL | 5% |
| Encabezados de respuesta y estado | 5% |
| Controles adicionales | 5% |

El renderizado del lado del servidor (SSR) tiene el mayor peso porque los rastreadores de IA (GPTBot, ClaudeBot, PerplexityBot) generalmente no ejecutan JavaScript. Una página que requiere JS para renderizar su contenido principal es efectivamente invisible para los rastreadores IA sin importar qué tan bien esté escrito el contenido en sí.

Deducciones de los encabezados de seguridad (de `agents/geo-technical.md`):
- Sin HTTPS: -30 puntos
- Sin HSTS: -10 puntos
- Sin CSP: -10 puntos
- Sin X-Frame-Options: -5 puntos
- Sin X-Content-Type-Options: -5 puntos
- Sin Referrer-Policy: -5 puntos
- Sin Permissions-Policy: -3 puntos

Core Web Vitals (LCP, INP, CLS) se evalúan como riesgo Bajo / Medio / Alto desde un análisis HTML estático. El agente señala explícitamente que las medidas reales requieren datos de campo (PageSpeed Insights o CrUX).

### Cómo se ve lo bueno vs lo malo

Una alta puntuación técnica requiere un renderizado del lado del servidor completo, un robots.txt bien formado que permita los rastreadores IA, un sitemap XML referenciado, HTTPS con HSTS, y etiquetas meta limpias. Un hallazgo crítico es cualquier SPA (Single Page Application) del lado del cliente donde el cuerpo HTML esté vacío sin ejecución de JavaScript — en ese estado, ninguna cantidad de optimización de contenido ayuda a la descubribilidad por IA.

---

## Datos Estructurados (10%)

**Implementado por:** [`agents/geo-schema.md`](../agents/geo-schema.md)

### Lo que revisa el calificador

El agente de schema detecta datos estructurados JSON-LD, Microdata, y RDFa en el código fuente de la página y califica la integridad en diez componentes:

| Componente | Puntos máx | Criterios |
|---|---|---|
| Organization / LocalBusiness | 20 | Presente (10 pts); enlaces sameAs hacia 3+ plataformas (20 pts) |
| Article / Schema de contenido | 15 | Presente (8 pts); autor como objeto Person (12 pts); dateModified presente (15 pts) |
| Schema Person para autor | 15 | Presente (8 pts); sameAs presente (12 pts); jobTitle y knowsAbout presentes (15 pts) |
| Completitud sameAs | 15 | 1–2 plataformas (5 pts); 3–4 plataformas (10 pts); 5+ plataformas incluyendo Wikipedia (15 pts) |
| Propiedad speakable | 10 | Presente y apuntando a secciones de contenido (10 pts) |
| BreadcrumbList | 5 | Presente y válido (5 pts) |
| WebSite + SearchAction | 5 | Presente y válido (5 pts) |
| Sin schemas obsoletos | 5 | Ningún schema HowTo (eliminado Sep 2023) o SpecialAnnouncement presente |
| Formato JSON-LD | 5 | Todos los schemas en JSON-LD y no en Microdata ni RDFa |
| Validación (sin errores) | 5 | Todos los schemas pasan validación de sintaxis y propiedades |

El agente también señala los esquemas inyectados por JavaScript en lugar de estar presentes en la respuesta HTML inicial, ya que los rastreadores de IA no ejecutarán JavaScript y no verán esos esquemas en absoluto.

Estados obsoletos y restringidos verificados (de `agents/geo-schema.md`):
- HowTo: removido de los resultados enriquecidos de Google en Septiembre de 2023
- FAQPage: restringido a sitios gubernamentales y de autoridades de salud desde Agosto de 2023
- SpecialAnnouncement: obsoleto

### Cómo se ve lo bueno vs lo malo

Una alta puntuación de schema requiere un esquema de Organization con enlaces sameAs a al menos cinco plataformas incluyendo Wikipedia, esquemas de Person adecuadamente anidados para todos los autores de contenido, schema Article con dateModified, y que todos los esquemas se entreguen como JSON-LD renderizado por el servidor. Una puntuación cercana a cero significa que no hay datos estructurados en absoluto, lo cual quita cualquier señal de vinculación de entidad explícita para los modelos de IA.

---

## Optimización de Plataformas (10%)

**Implementado por:** [`agents/geo-platform-analysis.md`](../agents/geo-platform-analysis.md)

### Lo que revisa el calificador

El agente de plataforma califica de forma independiente la preparación de cinco plataformas de búsqueda mediante IA y las agrega. Cada plataforma tiene su propio desglose de sub-calificaciones:

**Google AI Overviews:** Estructura de contenido (40 pts) — encabezados basados en preguntas, párrafos de respuesta directa, tablas comparativas; señales de autoridad de fuente (30 pts); señales técnicas (30 pts).

**Búsqueda web de ChatGPT:** Reconocimiento de entidad (35 pts) — presencia en Wikipedia y Wikidata, esquema sameAs; preferencias de contenido (40 pts) — afirmaciones fácticas y citables con atribución; acceso de rastreadores (25 pts) — OAI-SearchBot y ChatGPT-User permitidos en robots.txt.

**Perplexity AI:** Validación comunitaria (Reddit, Quora, Stack Overflow) y la franqueza de la fuente se califican por separado.

**Google Gemini y Bing Copilot:** Cada plataforma se evalúa frente a sus señales de obtención de fuentes y posicionamiento documentadas.

El README destaca que solo el 11% de los dominios son citados tanto por ChatGPT como por Google AI Overviews para la misma consulta, lo cual motiva a tratar a la preparación por plataforma como una dimensión de puntuación distinta en lugar de plegarla a categorías técnicas o de contenido.

### Cómo se ve lo bueno vs lo malo

Una puntuación de plataforma fuerte requiere pasar las verificaciones de acceso a rastreadores y reconocimiento de entidades que aparecen en otras categorías, además de patrones estructurales específicos de plataforma: encabezados de preguntas-respuestas y párrafos de respuesta directa para Google AIO, presencia de Wikipedia y Wikidata para ChatGPT, y presencia de plataformas comunitarias para Perplexity. Debido a que esta categoría se solapa con varias otras categorías, un sitio que puntúa bien en Citabilidad IA y Autoridad de Marca normalmente también puntuará razonablemente bien aquí.

---

## Advertencias (Caveats)

**Puntuación Determinística vs Juzgada por LLM.** El puntuador de citabilidad (`scripts/citability_scorer.py`) y el validador de llms.txt (`scripts/llmstxt_generator.py`) son totalmente determinísticos: dado el mismo HTML, retornan el mismo resultado numérico siempre. Las Puntuaciones de Autoridad de Marca, E-E-A-T de Contenido, Técnico, Schema y Plataforma son producidas por subagentes LLM que siguen rúbricas documentadas; son evaluaciones guiadas en lugar de cálculos reproducibles. Dos ejecuciones sobre la misma URL pueden producir pequeñas diferencias en categorías juzgadas por el LLM.

**Los pesos son subjetivos.** La distribución de peso 25/20/20/15/10/10 refleja el juicio de los autores de la herramienta acerca de la importancia relativa de cada categoría en la probabilidad de citación en IA al momento de escribir. Estos pesos no se derivan de un estudio controlado y están sujetos a cambios a medida que las plataformas de búsqueda IA evolucionan.

**Diagnóstico, no garantía.** La Puntuación GEO es un instrumento diagnóstico. Una alta puntuación mejora las condiciones estructurales para la cita de la IA pero no garantiza que ningún sistema de IA en particular citará o recomendará el sitio. El comportamiento del modelo de IA depende de muchos factores fuera del alcance de esta herramienta, incluyendo la información de entrenamiento del modelo, formulación de consultas, y el contenido del competidor.

**Validación de Schema es estructural, no semántica.** El agente de schema comprueba que JSON-LD sea sintácticamente válido, utilice tipos y propiedades reconocidas de Schema.org, e incluya los campos requeridos. No verifica que los valores sean exactos o que la entidad descrita coincida con la organización o persona real. Un bloque de schema que apruebe la validación puede aún contener información incorrecta.

**llms.txt es un estándar emergente.** La especificación llms.txt referenciada por `scripts/llmstxt_generator.py` y `agents/geo-ai-visibility.md` aún no es adoptada universalmente por los rastreadores de IA. Su presencia o ausencia no garantiza ningún comportamiento específico del rastreador en este momento.
