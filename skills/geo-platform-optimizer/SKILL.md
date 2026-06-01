---
name: geo-platform-optimizer
description: Optimización de búsqueda de IA específica por plataforma — auditar y optimizar para Google AI Overviews, ChatGPT, Perplexity, Gemini y Bing Copilot individualmente
version: 1.0.0
author: geo-seo-claude
tags: [geo, ai-search, platform-optimization, chatgpt, perplexity, gemini, aio]
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# Optimizador de Plataformas GEO

## Idea Central

Solo el **11% de los dominios** son citados TANTO por ChatGPT como por Google AI Overviews para la misma consulta. Cada plataforma de búsqueda de IA usa diferentes índices, lógicas de clasificación y preferencias de fuentes. Una página optimizada para Google AI Overviews puede ser invisible para ChatGPT, y viceversa. La optimización específica por plataforma no es opcional — es la base de cualquier estrategia GEO seria.

## Cómo Usar Esta Habilidad

1. Recopila la URL objetivo y el tema/industria principal del sitio
2. Ejecuta cada lista de verificación de plataforma a continuación contra el sitio
3. Puntúa cada plataforma en la rúbrica de 0-100
4. Genera GEO-PLATFORM-OPTIMIZATION.md con puntuaciones por plataforma, brechas y elementos de acción

---

## Plataforma 1: Google AI Overviews (AIO)

### Cómo AIO Selecciona Fuentes
- El 92% de las citas de AIO provienen de páginas que ya clasifican en los **top 10 resultados orgánicos** — el SEO tradicional es la puerta de entrada
- Sin embargo, el 47% de las citas provienen de páginas que clasifican **por debajo de la posición 5** — AIO tiene su propia lógica de selección que favorece la claridad y franqueza sobre el ranking bruto
- AIO favorece fuertemente las páginas con **estructura limpia, respuestas directas y formato escaneable**
- La optimización de fragmentos destacados (featured snippets) tiene ~70% de superposición con la optimización para AIO
- AIO prefiere **respuestas concisas, fácticas y sin ambigüedades** — las evasivas y el relleno reducen la probabilidad de citación

### Lista de Verificación de Optimización

1. **Encabezados Basados en Preguntas**: Usa encabezados H2/H3 formulados como preguntas que coincidan con las consultas reales de los usuarios. Revisa la sección "Otras preguntas de los usuarios" (People Also Ask) de Google para el tema objetivo y refleja esas frases exactas.
2. **Respuesta Directa en el Primer Párrafo**: Después de cada encabezado de pregunta, proporciona una respuesta clara de 1-2 oraciones inmediatamente. Luego expande con detalles de apoyo. La primera oración debe ser una candidata a cita independiente.
3. **Tablas y Comparaciones Estructuradas**: AIO cita mucho las tablas. Convierte cualquier dato de comparación, precios, especificaciones o características en tablas HTML. Usa encabezados de columna claros.
4. **Listas Ordenadas y Desordenadas**: Los procesos paso a paso deben usar listas ordenadas. Las listas de características deben usar listas desordenadas. AIO las extrae directamente.
5. **Secciones FAQ**: Añade una sección dedicada de Preguntas Frecuentes con 5-10 preguntas reales. Usa encabezados H3 adecuados para cada pregunta. Aunque los resultados enriquecidos de schema FAQPage están restringidos a sitios gubernamentales/de salud desde agosto de 2023, el patrón de contenido sigue ayudando a la extracción de AIO.
6. **Definiciones y Cajas de Glosario**: Para cualquier término específico de la industria, proporciona una definición clara. Formato: "**[Término]** es [definición concisa]." AIO cita definiciones con frecuencia.
7. **Estadísticas con Fuentes**: Incluye números específicos con atribución. "Según [Fuente], [estadística]." AIO prefiere afirmaciones específicas y citables sobre aseveraciones vagas.
8. **Fecha de Publicación**: Incluye una fecha de publicación visible y una fecha de última actualización. AIO resta prioridad al contenido sin fecha para consultas sensibles al tiempo.
9. **Firma del Autor (Byline)**: Muestra el nombre del autor con credenciales. Enlaza a una página de autor con biografía, credenciales y enlaces sameAs.
10. **Profundidad de Página**: Mantén las páginas objetivo a no más de 3 clics de la página de inicio. AIO rara vez cita contenido profundo y huérfano.

### Rúbrica de Puntuación (0-100)

| Criterio | Puntos | Cómo Puntuar |
|---|---|---|
| Clasifica en el top 10 para consultas objetivo | 20 | 20 si sí, 10 si top 20, 0 si más allá |
| Encabezados basados en preguntas presentes | 10 | 2 puntos por encabezado de pregunta, máx 10 |
| Respuestas directas después de los encabezados | 15 | 3 puntos por respuesta directa, máx 15 |
| Tablas presentes para datos de comparación | 10 | 10 si se usan tablas apropiadamente, 5 si parcial, 0 si ausentes |
| Listas para procesos/características | 10 | 10 si presentes, 5 si parcial |
| Sección FAQ con 5+ preguntas | 10 | 10 si 5+, 5 si 1-4, 0 si ninguna |
| Estadísticas con citas | 10 | 2 puntos por estadística citada, máx 10 |
| Fecha de publicación/actualización visible | 5 | 5 si ambas fechas, 3 si una, 0 si ninguna |
| Firma de autor con credenciales | 5 | 5 si firma completa, 3 si solo nombre, 0 si ninguna |
| Jerarquía limpia de URLs + encabezados | 5 | 5 si H1>H2>H3 limpio, 3 si problemas menores, 0 si roto |

---

## Plataforma 2: ChatGPT Web Search

### Cómo ChatGPT Selecciona Fuentes
- Usa **el índice de búsqueda de Bing** como base (no Google)
- Principales fuentes de citación por cuota de dominio: **Wikipedia (47.9%)**, Reddit (11.3%), YouTube, principales medios de noticias
- ChatGPT pondera en gran medida el **reconocimiento de entidades** — si tu marca existe como una entidad estructurada (Wikipedia, Wikidata, Crunchbase), es mucho más probable que sea citada
- Prefiere **fuentes autorizadas y bien establecidas** sobre sitios nuevos o de nicho
- Los artículos más largos y completos son citados más a menudo que los textos cortos
- ChatGPT tiende a citar **la fuente más canónica** para una afirmación en lugar de la original

### Lista de Verificación de Optimización

1. **Presencia en Wikipedia**: Comprueba si la marca/persona/producto tiene un artículo en Wikipedia. Si no, evalúa los criterios de relevancia (notability). Si es relevante, crea un borrador. Si existe un artículo, asegúrate de que sea preciso y actual.
2. **Entidad Wikidata**: Verifica que la entidad existe en Wikidata (wikidata.org). Si no, crea un elemento en Wikidata con propiedades clave: instancia de, sitio web oficial, enlaces de redes sociales, fecha de fundación, ubicación de la sede.
3. **Bing Webmaster Tools**: Verifica que el sitio esté registrado en Bing Webmaster Tools. Envía el sitemap. Comprueba si hay errores de rastreo.
4. **Cobertura del Índice de Bing**: Usa `site:domain.com` en Bing para verificar que las páginas clave estén indexadas. Bing puede tener páginas indexadas diferentes a las de Google.
5. **Autoridad en Reddit**: Busca menciones de la marca en Reddit. Identifica subreddits relevantes. Evalúa si la marca participa auténticamente en las discusiones.
6. **Presencia en YouTube**: Verifica que exista un canal de YouTube con contenido relevante. Las descripciones de los videos deben contener URLs completas e información de la entidad.
7. **Backlinks de Autoridad**: ChatGPT/Bing dan mucho peso a los backlinks de dominios .edu, .gov y publicaciones importantes. Audita el perfil de backlinks para estas fuentes.
8. **Consistencia de la Entidad**: El nombre de la marca, fecha de fundación, liderazgo y datos clave deben ser consistentes a través de Wikipedia, Crunchbase, LinkedIn y el sitio web oficial.
9. **Contenido Exhaustivo**: Las páginas que apuntan a la citación de ChatGPT deben tener **2000+ palabras** con una cobertura exhaustiva del tema. ChatGPT prefiere fuentes únicas y autorizadas en lugar de combinar múltiples páginas delgadas.
10. **Atribución Clara**: Incluye secciones de "Acerca de", descripciones de la empresa e historias de fundación. ChatGPT usa esto para la consolidación (grounding) de entidades.

### Rúbrica de Puntuación (0-100)

| Criterio | Puntos | Cómo Puntuar |
|---|---|---|
| Artículo de Wikipedia existe y es preciso | 20 | 20 si existe, 10 si esbozo (stub), 0 si ninguno |
| Entidad Wikidata con 5+ propiedades | 10 | 10 si completa, 5 si básica, 0 si ninguna |
| Cobertura del índice de Bing en páginas clave | 10 | 10 si completa, 5 si parcial, 0 si pobre |
| Menciones de marca en Reddit (positivas) | 10 | 10 si hay debates activos, 5 si hay menciones, 0 si ninguna |
| Canal de YouTube con contenido relevante | 10 | 10 si activo, 5 si presente pero escaso, 0 si ninguno |
| Backlinks autorizados (.edu, .gov, prensa) | 15 | 3 puntos por categoría de backlink autorizado, máx 15 |
| Consistencia de entidad en las plataformas | 10 | 10 si consistente, 5 si discrepancias menores, 0 si mayores |
| Exhaustividad del contenido (2000+ palabras) | 10 | 10 si exhaustivo, 5 si adecuado, 0 si delgado/pobre |
| Bing Webmaster Tools configurado | 5 | 5 si verificado, 0 si no |

---

## Plataforma 3: Perplexity AI

### Cómo Perplexity Selecciona Fuentes
- Principales fuentes de citación: **Reddit (46.7%)**, Wikipedia, YouTube, principales publicaciones
- Perplexity pone el **mayor énfasis en la validación de la comunidad** de todas las plataformas de búsqueda de IA
- Favorece fuertemente los **hilos de discusión** donde las afirmaciones son debatidas, validadas o ampliadas por múltiples participantes
- Prefiere contenido reciente — la fecha de publicación es una fuerte señal de clasificación
- Cita **múltiples fuentes por respuesta** (típicamente 5-15), por lo que hay más oportunidades de que aparezcan sitios de autoridad media
- Usa su propia infraestructura de rastreo además de las APIs de búsqueda

### Lista de Verificación de Optimización

1. **Presencia Activa en Reddit**: La marca o sus representantes deben participar auténticamente en discusiones de subreddits relevantes. No promocional — útil, específico y orientado a la comunidad.
2. **AMAs e Hilos de Reddit**: Fomenta o participa en AMAs (Ask Me Anything), hilos de discusión detallados y preguntas/respuestas de la comunidad. Perplexity trata estos como contenido de alta señal.
3. **Presencia en Foros y Comunidades**: Más allá de Reddit, revisa Hacker News, Stack Overflow, Quora y foros de la industria del nicho. Perplexity los indexa fuertemente.
4. **Contenido Abierto al Debate**: Publica contenido que invite a la discusión — artículos de opinión, hallazgos de investigación, opiniones contrarias, datos originales. El contenido que se comparte y debate en las comunidades clasifica más alto.
5. **Señales de Frescura**: Publica contenido con fechas claras. Actualiza el contenido regularmente. Perplexity resta prioridad al contenido obsoleto más agresivamente que otras plataformas.
6. **Validación de Múltiples Fuentes**: Las afirmaciones en tu contenido deben estar respaldadas por otras fuentes. Perplexity cruza referencias y prefiere afirmaciones que puede verificar desde múltiples orígenes.
7. **Contenido de Video de YouTube**: Crea contenido de video que Perplexity pueda referenciar. Asegúrate de que los títulos, descripciones y transcripciones de los videos contengan la información objetivo.
8. **Pasajes Directos y Citables**: Escribe párrafos que puedan funcionar solos como citas. Cada párrafo debe plantear un punto claro con evidencia de apoyo.
9. **Datos e Investigación Originales**: Publica encuestas originales, benchmarks, casos de estudio o conjuntos de datos. Perplexity favorece enormemente las fuentes primarias.
10. **Páginas de Perplexity**: Comprueba si Perplexity ha creado una "Página" (Page) sobre tu tema/marca. Estos son resúmenes seleccionados que influyen en futuras citas.

### Rúbrica de Puntuación (0-100)

| Criterio | Puntos | Cómo Puntuar |
|---|---|---|
| Presencia activa en subreddits relevantes | 20 | 20 si es contribuidor activo, 10 si mencionado, 0 si ausente |
| Menciones en foros/comunidades (HN, SO, Quora)| 10 | 10 si en múltiples plataformas, 5 si en una, 0 si ninguna |
| Frescura de contenido (actualizado en los últimos 6 meses) | 10 | 10 si reciente, 5 si en el último año, 0 si más antiguo |
| Investigación/datos originales publicados | 15 | 15 si inv. original, 10 si casos estudio, 5 si algunos datos, 0 si nada |
| Contenido de YouTube con transcripciones | 10 | 10 si canal activo, 5 si algunos videos, 0 si ninguno |
| Párrafos citables independientes | 10 | 2 puntos por párrafo citable bien estructurado, máx 10 |
| Validación de afirmaciones multifuente | 10 | 10 si afirmaciones bien documentadas, 5 si algo documentadas, 0 si nada |
| Contenido que genera discusión | 10 | 10 si se comparte/debate, 5 si hay algo de interacción, 0 si ninguna |
| Presencia en Wikipedia/Wikidata | 5 | 5 si presente, 0 si ausente |

---

## Plataforma 4: Google Gemini

### Cómo Gemini Selecciona Fuentes
- Usa **el índice de búsqueda de Google** con un fuerte peso hacia las **propiedades propiedad de Google**
- El contenido de YouTube tiene un peso significativamente mayor que en la Búsqueda de Google estándar
- Los datos del Perfil de Empresa de Google (Google Business Profile) son accesibles directamente para Gemini
- Gemini usa directamente el Google Knowledge Graph — la presencia de entidades en el Knowledge Graph es una gran ventaja
- Los datos estructurados (Schema.org) son consumidos directamente por Gemini para entender entidades
- Gemini es multi-modal: puede referenciar imágenes, videos y texto juntos

### Lista de Verificación de Optimización

1. **Panel de Conocimiento de Google (Knowledge Panel)**: Comprueba si la marca tiene un Panel de Conocimiento. Si no, reclámalo a través del Perfil de Empresa de Google o con datos estructurados. Asegúrate de que toda la información sea precisa.
2. **Perfil de Empresa de Google (GBP)**: Completa y optimiza el GBP con todos los campos: horarios, servicios, fotos, publicaciones, preguntas y respuestas. Gemini extrae información directamente del GBP para consultas locales.
3. **Estrategia de YouTube**: Crea contenido en YouTube para cada tema clave. Optimiza títulos, descripciones, marcas de tiempo y subtítulos. Gemini cita a YouTube más que cualquier otra plataforma de IA.
4. **Capítulos y Marcas de Tiempo en YouTube**: Usa capítulos (marcas de tiempo en la descripción) para que Gemini pueda referenciar segmentos específicos de los videos.
5. **Google Merchant Center**: Para e-commerce, asegúrate de que los productos estén en Google Merchant Center. Gemini hace referencia directa a los datos de productos.
6. **Datos Estructurados (Schema.org)**: Implementa marcado completo de Schema.org. Gemini usa esto para la comprensión de entidades más agresivamente que otras plataformas.
7. **Ecosistema de Sitios de Google**: Asegura presencia en el ecosistema de Google: Google Scholar (para investigación), Google News (para publicadores), Google Maps (para locales).
8. **Optimización de Imágenes**: Gemini es multi-modal. Usa texto alternativo descriptivo (alt text), nombres de archivo de imagen estructurados e imágenes de alta calidad. Incluye imágenes relevantes en cada contenido.
9. **Señales E-E-A-T de Google**: Se aplican todas las señales E-E-A-T estándar de Google con peso extra. Páginas de autor, páginas de "acerca de", políticas editoriales y demostraciones de conocimiento.
10. **Chrome Web Store / Google Workspace Marketplace**: Para empresas de software, la presencia en las plataformas de Google añade señales a la entidad.

### Rúbrica de Puntuación (0-100)

| Criterio | Puntos | Cómo Puntuar |
|---|---|---|
| Panel de Conocimiento de Google existe | 15 | 15 si completo, 10 si parcial, 0 si ninguno |
| Perfil de Empresa de Google completo | 10 | 10 si totalmente optimizado, 5 si básico, 0 si ninguno |
| Canal YouTube con contenido relevante al tema | 20 | 20 si activo con capítulos, 10 si presente, 0 si ninguno |
| Datos estructurados Schema.org implementados | 15 | 15 si exhaustivo, 10 si básico, 5 si mínimo, 0 si ninguno |
| Presencia en el ecosistema de Google (Scholar, News, Maps) | 10 | 10 si 3+, 5 si 1-2, 0 si ninguna |
| Optimización de imágenes (alt text, archivos) | 10 | 10 si todas optimizadas, 5 si parcial, 0 si ninguna |
| Señales E-E-A-T (autor, acerca de, editorial) | 10 | 10 si fuertes, 5 si parcial, 0 si débiles |
| Google Merchant Center (si es e-commerce) | 5 | 5 si aplica y activo, N/A de otro modo |
| Contenido multi-modal (texto + fotos + video) | 5 | 5 si es rico multi-modal, 3 si algo, 0 si solo texto |

---

## Plataforma 5: Bing Copilot

### Cómo Copilot Selecciona Fuentes
- Usa **el índice de búsqueda de Bing** (infraestructura compartida con ChatGPT pero con clasificación/selección diferente)
- Soporta el **protocolo IndexNow** para la indexación casi instantánea de contenido nuevo y actualizado
- Copilot tiende a citar **menos fuentes por respuesta** (típicamente 3-5) pero da una atribución más prominente
- Integración con el ecosistema de Microsoft: se pondera el contenido de LinkedIn, GitHub, Microsoft Learn
- Copilot prefiere páginas con marcado claro y estructurado, y tiempos de carga rápidos

### Lista de Verificación de Optimización

1. **Bing Webmaster Tools**: Registra y verifica el sitio. Envía el sitemap XML. Revisa y soluciona cualquier problema de rastreo.
2. **Implementación de IndexNow**: Implementa el protocolo IndexNow para notificar a Bing sobre cambios de contenido en tiempo real. Envía un archivo clave en `/.well-known/indexnow-key.txt` y haz ping a la API IndexNow al publicar/actualizar contenido.
3. **Página de Empresa de LinkedIn**: Asegúrate de que la página de la empresa en LinkedIn esté completa con descripción precisa, conexiones de empleados y publicaciones regulares. Copilot indexa el contenido de LinkedIn.
4. **Presencia en GitHub**: Para empresas tecnológicas, mantén una presencia activa en GitHub. Copilot referencia repositorios, documentación y archivos README de GitHub.
5. **Microsoft Learn / Documentación**: Si es relevante, contribuye a Microsoft Learn o asegúrate de que tu documentación sea compatible con los estándares de documentación de Microsoft.
6. **Bing Places for Business**: Equivalente al Perfil de Empresa de Google. Completa todos los campos para la visibilidad en búsquedas locales en Copilot.
7. **Meta Descripciones Claras**: Bing/Copilot pondera las meta descripciones más fuertemente que Google. Escribe meta descripciones persuasivas y ricas en palabras clave para cada página.
8. **Señales Sociales**: Bing ha ponderado históricamente las señales sociales (compartidos, me gusta, interacción) más que Google. Mantén una presencia activa en redes sociales.
9. **Palabras Clave de Coincidencia Exacta**: El algoritmo de Bing es más literal sobre la coincidencia de palabras clave que Google. Incluye frases objetivo exactas en títulos, encabezados y contenido del cuerpo.
10. **Carga de Página Rápida**: Copilot resta prioridad a páginas lentas. Apunta a un tiempo de carga inferior a 2 segundos. Optimiza imágenes, habilita compresión, minimiza recursos que bloquean el renderizado.

### Rúbrica de Puntuación (0-100)

| Criterio | Puntos | Cómo Puntuar |
|---|---|---|
| Bing Webmaster Tools verificado + sitemap | 15 | 15 si verificado, 5 si parcial, 0 si no |
| Protocolo IndexNow implementado | 15 | 15 si activo, 0 si no |
| Cobertura del índice de Bing de páginas clave | 10 | 10 si completa, 5 si parcial, 0 si pobre |
| Página de empresa de LinkedIn (completa) | 10 | 10 si completa, 5 si básica, 0 si ninguna |
| Presencia en GitHub (si aplica) | 5 | 5 si activa, N/A si no aplica |
| Meta descripciones optimizadas | 10 | 10 si todas las páginas clave, 5 si parcial, 0 si falta |
| Señales de interacción en redes sociales | 10 | 10 si interacción activa, 5 si presente, 0 si ninguna |
| Palabras clave de coincidencia exacta en títulos/encabezados | 10 | 10 si bien optimizado, 5 si parcial, 0 si no |
| Velocidad de carga < 2 segundos | 10 | 10 si < 2s, 5 si < 4s, 0 si > 4s |
| Bing Places configurado (si es local) | 5 | 5 si completo, N/A si no es local |

---

## Resumen Multi-plataforma

### Acciones de Optimización Universales (ayudan a TODAS las plataformas)
1. Presencia de entidad en Wikipedia/Wikidata
2. Canal de YouTube con contenido relevante
3. Contenido exhaustivo y bien estructurado con encabezados claros
4. Datos estructurados Schema.org (especialmente Organization + sameAs)
5. Carga de página rápida y HTML limpio
6. Páginas de autor con credenciales y enlaces sameAs
7. Actualizaciones regulares de contenido con fechas visibles

### Prioridades Específicas de Plataforma
| Prioridad | Google AIO | ChatGPT | Perplexity | Gemini | Copilot |
|---|---|---|---|---|---|
| #1 | Ranking Top-10 | Wikipedia | Presencia en Reddit | YouTube | IndexNow |
| #2 | Estructura Q&A | Grafo de Entidades | Investigación original | Knowledge Panel | Bing WMT |
| #3 | Tablas/Listas | SEO Bing | Frescura | Schema.org | LinkedIn |
| #4 | Featured snippets | Reddit | Foros de comunidad | GBP | Meta descripciones |

---

## Formato de Salida

Genera **GEO-PLATFORM-OPTIMIZATION.md** con la siguiente estructura:

```markdown
# Reporte de Optimización de Plataformas GEO — [Dominio]
Fecha: [Fecha]

## Preparación General de Plataforma
- Puntuación GEO Combinada: XX/100 (promedio de todas las puntuaciones de plataforma)

## Puntuaciones de Plataforma
| Plataforma | Puntuación | Estado |
|---|---|---|
| Google AI Overviews | XX/100 | [Fuerte/Moderado/Débil] |
| ChatGPT Web Search | XX/100 | [Fuerte/Moderado/Débil] |
| Perplexity AI | XX/100 | [Fuerte/Moderado/Débil] |
| Google Gemini | XX/100 | [Fuerte/Moderado/Débil] |
| Bing Copilot | XX/100 | [Fuerte/Moderado/Débil] |

Umbrales de estado: Fuerte = 70+, Moderado = 40-69, Débil = 0-39

## Detalles de Plataforma
[Desglose por plataforma con puntuación, brechas encontradas y acciones específicas]

## Plan de Acción Priorizado
### Victorias Rápidas (esta semana)
[Acciones que mejoran múltiples puntuaciones de plataforma con mínimo esfuerzo]

### A Medio Plazo (este mes)
[Acciones que requieren creación de contenido o cambios técnicos]

### Estratégico (este trimestre)
[Acciones que requieren construcción de entidades, desarrollo de comunidad o presencia en plataformas]
```
