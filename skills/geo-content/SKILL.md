---
name: geo-content
description: Evaluación de calidad de contenido y E-E-A-T para citabilidad por IA — evalúa experiencia, conocimiento, autoridad, confiabilidad y estructura de contenido
version: 1.0.0
author: geo-seo-claude
tags: [geo, content-quality, eeat, citability, ai-content, topical-authority]
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# Calidad de Contenido GEO y Evaluación E-E-A-T

## Propósito

Las plataformas de búsqueda con IA no solo encuentran contenido — evalúan si el contenido merece ser citado. El marco principal para esta evaluación es **E-E-A-T** (Experiencia, Conocimiento, Autoridad, Confiabilidad), que según la actualización de las Pautas de Calificadores de Calidad de Google de diciembre de 2025 ahora se aplica a **TODAS las consultas competitivas**, no solo a los temas YMYL (Your Money Your Life). El contenido que obtiene una puntuación alta en E-E-A-T tiene drásticamente más probabilidades de ser citado por plataformas de IA.

Esta habilidad evalúa el contenido a través de dos lentes:
1. **Señales E-E-A-T** — ¿El contenido demuestra conocimiento y confianza real?
2. **Citabilidad por IA** — ¿El contenido está estructurado para que las plataformas de IA puedan extraer y citar afirmaciones específicas?

## Cómo Usar Esta Habilidad

1. Obtén la(s) página(s) objetivo — inicio, publicaciones clave de blog, páginas de servicios/productos
2. Evalúa E-E-A-T a través de las 4 dimensiones (25% cada una)
3. Evalúa las métricas de calidad de contenido (estructura, legibilidad, profundidad)
4. Revisa las señales de calidad de contenido de IA
5. Evalúa la autoridad temática en todo el sitio
6. Puntúa y genera GEO-CONTENT-ANALYSIS.md

---

## Marco E-E-A-T (100 puntos en total)

### Experiencia — 25 puntos
Conocimiento de primera mano e involucramiento directo con el tema. Las plataformas de IA distinguen cada vez más entre el contenido que informa sobre un tema y el contenido de alguien que lo ha HECHO.

**Señales a evaluar:**

| Señal | Puntos | Cómo Puntuar |
|---|---|---|
| Relatos en primera persona ("Probé...", "Implementamos...") | 5 | 5 si presente y específico, 3 si genérico, 0 si ausente |
| Investigación o datos originales no disponibles en otros lugares | 5 | 5 si datos originales, 3 si referencia trabajo original, 0 si ninguno |
| Casos de estudio con resultados específicos | 4 | 4 si detallado con números, 2 si general, 0 si ninguno |
| Capturas de pantalla, fotos o evidencia de uso directo | 3 | 3 si evidencia auténtica, 1 si de stock/genérica, 0 si ninguna |
| Ejemplos específicos de experiencia personal | 4 | 4 si específico y único, 2 si algo específico, 0 si genérico |
| Demostraciones del proceso (no solo el resultado) | 4 | 4 si paso a paso desde la experiencia, 2 si parcial, 0 si ninguna |

**Qué marcar como Experiencia débil:**
- Contenido que solo resume lo que dicen otras fuentes sin añadir una nueva perspectiva
- Consejos genéricos que podrían aplicarse a cualquier situación ("Depende de tus necesidades")
- Sin mención de uso real, pruebas o involucramiento directo
- Lenguaje evasivo que sugiere falta de conocimiento directo ("supuestamente", "se dice", "algunos dicen")

### Conocimiento (Expertise) — 25 puntos
Profundidad de conocimiento demostrada y competencia profesional en la materia.

**Señales a evaluar:**

| Señal | Puntos | Cómo Puntuar |
|---|---|---|
| Credenciales del autor visibles (bio, grados, certificaciones) | 5 | 5 si credenciales completas, 3 si bio básica, 0 si no hay autor |
| Profundidad técnica adecuada al tema | 5 | 5 si tratamiento técnico exhaustivo, 3 si adecuado, 0 si superficial |
| Explicación de la metodología (cómo se llegó a las conclusiones) | 4 | 4 si metodología clara, 2 si alguna explicación, 0 si ninguna |
| Afirmaciones respaldadas por datos (estadísticas, citas a investigaciones) | 4 | 4 si bien documentado, 2 si algunos datos, 0 si afirmaciones sin respaldo |
| Terminología específica de la industria usada correctamente | 3 | 3 si lenguaje especializado preciso, 1 si básico, 0 si hay errores |
| Página de autor con perfil profesional detallado | 4 | 4 si página dedicada al autor, 2 si bio breve, 0 si ninguna |

**Qué marcar como Conocimiento débil:**
- Afirmaciones sin evidencia de respaldo o fuentes
- Cobertura superficial de temas complejos
- Mal uso de terminología técnica
- Sin autor visible o autor sin credenciales relevantes
- Contenido amplio y genérico en lugar de profundo y específico

### Autoridad — 25 puntos
Reconocimiento por parte de otros como una fuente creíble en el tema.

**Señales a evaluar:**

| Señal | Puntos | Cómo Puntuar |
|---|---|---|
| Citas entrantes de fuentes autorizadas | 5 | 5 si citado por fuentes principales, 3 si algunas citas, 0 si ninguna |
| Autor citado o mencionado en prensa/medios | 4 | 4 si menciones en medios, 2 si menciones en la industria, 0 si ninguna |
| Premios o reconocimientos de la industria mencionados | 3 | 3 si premios relevantes, 1 si tangenciales, 0 si ninguno |
| Credenciales como ponente (conferencias, eventos) | 3 | 3 si están listados, 0 si ninguno |
| Publicado en medios revisados por pares o respetados | 4 | 4 si publicaciones nivel 1, 2 si medios de la industria, 0 si ninguno |
| Cobertura exhaustiva del tema (autoridad temática) | 3 | 3 si el sitio cubre el tema a fondo, 1 si alguna cobertura, 0 si aislado |
| Marca mencionada en Wikipedia o referencias autorizadas | 3 | 3 si Wikipedia, 2 si otras referencias enciclopédicas, 0 si ninguna |

**Qué marcar como Autoridad débil:**
- Sitio de un solo tema sin profundidad de cobertura
- Sin validación externa de afirmaciones de conocimiento
- Sin backlinks de fuentes autorizadas
- Afirmaciones de autoridad sin evidencia (autoproclamado "experto")

### Confiabilidad (Trustworthiness) — 25 puntos
Señales de que el contenido y su editor son confiables y transparentes.

**Señales a evaluar:**

| Señal | Puntos | Cómo Puntuar |
|---|---|---|
| Información de contacto visible (dirección, teléfono, correo) | 4 | 4 si info de contacto completa, 2 si solo correo, 0 si ninguna |
| Política de privacidad presente y enlazada | 2 | 2 si presente, 0 si ausente |
| Términos de servicio presentes | 1 | 1 si presentes, 0 si ausentes |
| HTTPS con certificado válido | 2 | 2 si HTTPS válido, 0 si no |
| Estándares editoriales o política de correcciones | 3 | 3 si está documentada, 1 si implícita, 0 si ninguna |
| Transparencia sobre el modelo de negocio y conflictos | 3 | 3 si hay divulgación clara, 1 si alguna, 0 si ninguna |
| Reseñas y testimonios de clientes reales | 3 | 3 si reseñas verificadas, 1 si testimonios, 0 si ninguno |
| Afirmaciones precisas (no se detecta desinformación) | 4 | 4 si todas son precisas, 2 si mayormente precisas, 0 si hay errores |
| Divulgación clara de afiliados/patrocinios | 3 | 3 si está debidamente divulgado, 0 si no se divulga o está ausente |

**Qué marcar como Confiabilidad débil:**
- Sin información de contacto ni dirección física
- Falta de política de privacidad o términos
- Enlaces de afiliados o contenido patrocinado no divulgados
- Afirmaciones verificablemente falsas o engañosas
- Sin forma de contactar al editor para correcciones

---

## Métricas de Calidad de Contenido

### Puntos de Referencia de Recuento de Palabras
Estos son **pisos, no objetivos**. Más palabras no significan mejor contenido. El punto de referencia es la longitud mínima para cubrir adecuadamente un tema para la citabilidad de la IA.

| Tipo de Página | Palabras Mínimas | Rango Ideal | Notas |
|---|---|---|---|
| Inicio | 500 | 500-1,500 | Propuesta de valor clara, no un muro de texto |
| Post de Blog | 1,500 | 1,500-3,000 | Exhaustivo pero enfocado |
| Contenido Pilar / Guía definitiva | 2,000 | 2,500-5,000 | Cobertura integral del tema |
| Página de producto | 300 | 500-1,500 | Descripciones, especificaciones, casos de uso |
| Página de servicio | 500 | 800-2,000 | Qué, cómo, por qué, para quién |
| Página Acerca de | 300 | 500-1,000 | Historia de la empresa/persona y credenciales |
| Página FAQ | 500 | 1,000-2,500 | Respuestas exhaustivas, no de una sola línea |

### Evaluación de Legibilidad
- **Facilidad de Lectura de Flesch (Objetivo)**: 60-70 (Nivel de 8vo-9no grado)
- Esto NO es un factor directo de ranking pero afecta la citabilidad — las plataformas de IA prefieren contenido que sea claro y sin ambigüedades
- La escritura demasiado académica (puntuación < 30) reduce la citabilidad para consultas generales
- La escritura demasiado simple (puntuación > 80) puede carecer de la profundidad necesaria para señales de conocimiento

**Cómo estimar sin una herramienta:**
- Longitud promedio de oración: 15-20 palabras es ideal
- Longitud promedio de párrafo: 2-4 oraciones
- Presencia de jerga: debe definirse al usarse por primera vez
- Voz pasiva: < 15% de las oraciones

### Estructura de Párrafo para Procesamiento IA
Las plataformas de IA extraen contenido a nivel de párrafo. Cada párrafo debe ser una unidad de significado autosuficiente.

**Estructura óptima del párrafo:**
- **2-4 oraciones** por párrafo (párrafos de 1 oración son débiles; de 5+ oraciones son difíciles de extraer)
- **Una idea por párrafo** — no mezcles temas dentro del mismo párrafo
- **Lidera con la afirmación clave** — la primera oración debe contener el punto principal
- **Apoya con evidencia** — las oraciones restantes proporcionan datos, ejemplos o contexto
- **Citable de forma independiente** — cada párrafo debe tener sentido si se extrae de forma aislada

### Estructura de Encabezados
- **Un H1 por página** — el tema/título principal
- **H2 para secciones principales** — deben representar subtemas distintos
- **H3 para subsecciones** — anidadas bajo el H2 relevante
- **Sin niveles omitidos** — no pases de un H1 a un H3 sin un H2
- **Encabezados descriptivos** — "Cómo Optimizar para Búsqueda por IA" en lugar de "Sección 2"
- **Encabezados basados en preguntas** donde sea apropiado — mapean directamente a consultas de IA

### Enlazado Interno
- Cada página de contenido debe enlazar a 3-5 páginas relacionadas en el mismo sitio
- Los enlaces deben usar texto de anclaje (anchor text) descriptivo (no "clic aquí")
- Crear una estructura de agrupamiento temático (topic cluster): página pilar enlazada a/desde todas las páginas de subtemas relacionadas
- Las páginas huérfanas (sin enlaces internos apuntando a ellas) rara vez son citadas por la IA

---

## Evaluación de Contenido IA

### Política de Contenido Generado por IA
El contenido generado por IA es **aceptable** según las directrices de Google (aclaración de marzo de 2024) siempre que demuestre señales E-E-A-T genuinas y tenga supervisión humana. La preocupación no es CÓMO se crea el contenido sino SI aporta valor.

### Señales de Contenido IA de Baja Calidad (marcar estas)

| Señal | Descripción |
|---|---|
| Fraseo genérico | "En el mundo acelerado de hoy...", "Es importante notar que...", "Al final del día..." |
| Sin aportación original | Contenido que solo reformula información ampliamente disponible |
| Falta de experiencia de primera mano | Sin anécdotas personales, casos de estudio o ejemplos específicos |
| Estructura perfecta pero vacía | Encabezados bien formateados con contenido superficial debajo |
| Sin ejemplos específicos | Usa explicaciones abstractas sin instancias concretas |
| Conclusiones repetitivas | Cada sección termina con una variación del mismo punto |
| Exceso de evasivas | "En términos generales", "En la mayoría de los casos", "Depende de varios factores" sin especificar cuáles |
| Voz humana ausente | Sin opiniones, preferencias o juicio profesional expresado |
| Contenido de relleno | Párrafos que podrían eliminarse sin perder información |
| Sin datos o fuentes | Afirmaciones presentadas como hechos sin atribución o evidencia |

### Señales de Contenido de Alta Calidad (sin importar método de producción)

| Señal | Descripción |
|---|---|
| Datos originales | Encuestas, experimentos, benchmarks, análisis propietario |
| Ejemplos específicos | Nombres de productos, empresas, fechas, números |
| Visiones matizadas o contrarias | Desacuerdo con la sabiduría convencional, respaldado por razonamiento |
| Experiencia en primera persona | "Cuando probé esto..." o "Nuestro equipo encontró..." |
| Información actualizada | Referencias a eventos recientes, datos actuales |
| Opinión experta | Juicio profesional claro, no solo hechos |
| Recomendaciones prácticas | Consejos específicos y accionables, no guías vagas |
| Reconocimiento de compensaciones (Trade-offs) | "Este enfoque funciona bien para X pero no para Y porque..." |

---

## Evaluación de Frescura de Contenido

### Fechas de Publicación
- Comprueba si `datePublished` y `dateModified` son visibles tanto en el contenido como en los datos estructurados
- El contenido sin fechas es tratado como menos confiable por las plataformas de IA
- Las fechas deben ser específicas (15 de enero de 2026) no vagas ("recientemente")

### Puntuación de Frescura

| Criterio | Puntuación |
|---|---|
| Actualizado en los últimos 3 meses | Excelente — actual y relevante |
| Actualizado en los últimos 6 meses | Bueno — todavía razonablemente actual |
| Actualizado en los últimos 12 meses | Aceptable — puede necesitar actualización |
| Actualizado hace 12-24 meses | Advertencia — revisar precisión |
| Sin fecha o más de 24 meses de antigüedad | Crítico — plataformas de IA pueden restar prioridad |

### Indicadores Atemporales (Evergreen)
Algún contenido sigue siendo relevante sin importar la edad. Marca el contenido como atemporal si:
- Cubre conceptos fundamentales que no cambian (física, matemáticas básicas, definiciones legales)
- Está claramente etiquetado como una referencia/guía para conceptos duraderos
- No contiene afirmaciones dependientes del tiempo ("lo último", "actualmente", "en 2024")

---

## Evaluación de Autoridad Temática

### Qué Es
La autoridad temática mide si un sitio cubre de manera integral un tema en lugar de abordarlo superficialmente. Las plataformas de IA prefieren citar sitios que son autoridades reconocidas en sus temas.

### Cómo Evaluar
1. **Amplitud de contenido**: ¿El sitio tiene múltiples páginas cubriendo diferentes aspectos de su tema central?
2. **Profundidad de contenido**: ¿Las páginas individuales profundizan en los subtemas?
3. **Agrupación temática (Clustering)**: ¿Están las páginas organizadas en grupos lógicos con enlazado interno?
4. **Brechas de contenido**: ¿Existen subtemas obvios que el sitio debería cubrir pero no lo hace?
5. **Comparación de competidores**: ¿Los competidores cubren subtemas que este sitio omite?

### Puntuación

| Nivel | Descripción | Impacto en Puntuación |
|---|---|---|
| Autoridad | 20+ páginas cubriendo el tema exhaustivamente, fuerte agrupación | +10 bono |
| En Desarrollo | 10-20 páginas con algo de agrupación | +5 bono |
| Emergente | 5-10 páginas sobre el tema, agrupación limitada | +0 |
| Pobre | < 5 páginas, sin agrupación | -5 penalización |

---

## Puntuación General (0-100)

### Composición de Puntuación
| Componente | Peso | Puntos Máximos |
|---|---|---|
| Experiencia | 25% | 25 |
| Conocimiento | 25% | 25 |
| Autoridad | 25% | 25 |
| Confiabilidad | 25% | 25 |
| **Subtotal** | | **100** |
| Modificador de Autoridad Temática | | +10 a -5 |
| **Puntuación Final** | | **Limitada a 100** |

### Interpretación de Puntuación
- **85-100**: Excepcional — fuerte candidato para citación por IA a través de plataformas
- **70-84**: Bueno — base sólida, mejoras específicas aumentarán la citabilidad
- **55-69**: Promedio — múltiples vacíos en E-E-A-T reduciendo visibilidad por IA
- **40-54**: Por Debajo del Promedio — problemas significativos de calidad y confianza en el contenido
- **0-39**: Pobre — se necesita una revisión fundamental de la estrategia de contenido

---

## Formato de Salida

Genera **GEO-CONTENT-ANALYSIS.md** con:

```markdown
# Calidad de Contenido GEO y Análisis E-E-A-T — [Dominio]
Fecha: [Fecha]

## Puntuación de Contenido: XX/100

## Desglose E-E-A-T
| Dimensión | Puntuación | Hallazgo Clave |
|---|---|---|
| Experiencia | XX/25 | [Resumen de una línea] |
| Conocimiento | XX/25 | [Resumen de una línea] |
| Autoridad | XX/25 | [Resumen de una línea] |
| Confiabilidad | XX/25 | [Resumen de una línea] |

## Modificador de Autoridad Temática: [+10 a -5]

## Páginas Analizadas
| Página | Palabras | Legibilidad | Estructura Encabezados | Clasificación de Citabilidad |
|---|---|---|---|---|
| [URL] | [Recuento] | [Puntuación] | [Pasa/Adv/Falla] | [Alta/Media/Baja] |

## Hallazgos Detallados E-E-A-T

### Experiencia
[Pasajes y páginas específicas con señales fuertes/débiles de experiencia]

### Conocimiento
[Credenciales de autor encontradas, evaluación de profundidad técnica, vacíos específicos]

### Autoridad
[Validación externa encontrada, evaluación de autoridad temática, vacíos]

### Confiabilidad
[Señales de confianza presentes/ausentes, preocupaciones sobre exactitud si las hay]

## Problemas de Calidad de Contenido
[Pasajes específicos marcados con razones y sugerencias de reescritura]

## Preocupaciones de Contenido IA
[Cualquier patrón de contenido de IA de baja calidad detectado, con ejemplos específicos]

## Evaluación de Frescura
| Página | Publicado | Última Actualización | Estado |
|---|---|---|---|
| [URL] | [Fecha] | [Fecha] | [Actual/Obsoleto/Sin Fecha] |

## Evaluación de Citabilidad
### Pasajes Más Citables
[Top 5 pasajes que las plataformas de IA tienen más probabilidades de citar, con razones]

### Páginas Menos Citables
[Páginas con la menor citabilidad, con recomendaciones específicas de mejora]

## Recomendaciones de Mejora
### Victorias Rápidas
[Cambios específicos en el contenido que se pueden hacer inmediatamente]

### Brechas de Contenido
[Temas que el sitio debería cubrir para fortalecer la autoridad temática]

### Mejoras de Autor/E-E-A-T
[Pasos específicos para fortalecer las señales E-E-A-T]
```
