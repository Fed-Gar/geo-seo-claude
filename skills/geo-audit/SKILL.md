---
name: geo-audit
description: Auditoría GEO+SEO completa de un sitio web con delegación paralela a subagentes. Orquesta una auditoría exhaustiva de Optimización para Motores Generativos (GEO) a través de citabilidad por IA, análisis de plataformas, infraestructura técnica, calidad de contenido y marcado de esquema. Produce una Puntuación GEO compuesta (0-100) con un plan de acción priorizado.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Habilidad de Orquestación de Auditoría GEO

## Propósito

Esta habilidad realiza una auditoría exhaustiva de Optimización para Motores Generativos (GEO) de cualquier sitio web. GEO es la práctica de optimizar contenido web para que los sistemas de IA (ChatGPT, Claude, Perplexity, Gemini, etc.) puedan descubrirlo, entenderlo, citarlo y recomendarlo. Esta auditoría mide qué tan bien se desempeña un sitio en todas las dimensiones de GEO y produce un plan de mejora accionable.

## Idea Clave

El SEO tradicional optimiza para clasificar en motores de búsqueda. GEO optimiza para la citación y recomendación por IA. Los sitios que obtienen puntuaciones altas en métricas GEO ven un 30-115% más de visibilidad en respuestas generadas por IA (Estudio Georgia Tech / Princeton / IIT Delhi 2024). Las dos disciplinas se superponen pero tienen requisitos distintos.

---

## Flujo de Trabajo de la Auditoría

### Fase 1: Descubrimiento y Reconocimiento

**Paso 1: Obtener la Página de Inicio y Detectar el Tipo de Negocio**

1. Usa WebFetch para recuperar la página de inicio en la URL proporcionada.
2. Extrae las siguientes señales:
   - Título de la página, meta descripción, encabezado H1
   - Elementos del menú de navegación (revela la estructura del sitio)
   - Contenido del pie de página (revela info del negocio, ubicación, páginas legales)
   - Marcado Schema.org en la página de inicio (Organization, LocalBusiness, etc.)
   - Enlace a la página de precios (indicador de SaaS)
   - Patrones de listado de productos (indicador de E-commerce)
   - Sección de Blog/recursos (indicador de Publicador)
   - Páginas de servicios (indicador de Agencia)
   - Dirección/teléfono/mapa de Google integrado (indicador de Negocio Local)

3. Clasifica el tipo de negocio usando estos patrones:

| Tipo de Negocio | Señales de Detección |
|---|---|
| **SaaS** | Página de precios, botones de "Regístrate" / "Prueba gratis", subdominio app.domain.com, tablas comparativas de funciones, páginas de integraciones |
| **Negocio Local** | Dirección física en la página de inicio, mapa de Google integrado, contenido "cerca de mí", schema LocalBusiness, páginas de áreas de servicio |
| **E-commerce** | Listados de productos, carrito de compras, schema Product, páginas de categoría, precios mostrados, botones de "Añadir al carrito" |
| **Publicador** | Navegación enfocada en blog, schema Article, páginas de autor, archivos basados en fechas, feeds RSS, alto volumen de contenido |
| **Agencia/Servicios** | Casos de estudio, portafolio, sección "Nuestro Trabajo", página del equipo, logos de clientes, descripciones de servicios |
| **Híbrido** | Combinación de las señales anteriores -- clasificar por el patrón dominante |

**Paso 2: Rastrear Sitemap y Enlaces Internos**

1. Intenta obtener `/sitemap.xml` y `/sitemap_index.xml`.
2. Si el sitemap existe, extrae hasta 50 URLs de páginas únicas priorizadas por:
   - Página de inicio (incluir siempre)
   - Páginas de navegación de nivel superior
   - Páginas de alto valor (precios, acerca de, contacto, páginas clave de servicios/productos)
   - Entradas de blog (muestra de las 5-10 más recientes)
   - Páginas de categoría/aterrizaje (landing pages)
3. Si no existe sitemap, rastrea enlaces internos desde la página de inicio:
   - Extrae todos los enlaces `<a href>` que apunten al mismo dominio
   - Sigue hasta 2 niveles de profundidad
   - Prioriza páginas enlazadas desde la navegación principal
4. Respeta las directivas de `robots.txt` -- no obtengas rutas no permitidas (disallowed).
5. Impón un máximo de 50 páginas y un tiempo de espera de 30 segundos por obtención (fetch).

**Paso 3: Recopilar Datos a Nivel de Página**

Para cada página en el conjunto de rastreo, registra:
- URL, título, meta descripción, URL canónica
- Estructura de encabezados H1-H6
- Recuento de palabras del contenido principal
- Tipos de Schema.org presentes
- Recuentos de enlaces internos/externos
- Imágenes con/sin texto alternativo (alt text)
- Meta etiquetas de Open Graph y Twitter Card
- Código de estado de respuesta
- Si la página tiene datos estructurados

---

### Fase 2: Delegación a Subagentes Paralelos

Delega el análisis a 5 subagentes especializados. Cada subagente opera sobre los datos de página recopilados y produce una puntuación de categoría (0-100) más hallazgos.

**Subagente 1: Análisis de Visibilidad por IA (geo-ai-visibility)**
- Analizar bloques de contenido por su capacidad de ser citados por sistemas de IA (puntuación de citabilidad)
- Comprobar acceso de rastreadores de IA vía robots.txt y presencia de llms.txt
- Escanear presencia de marca a través de YouTube, Reddit, Wikipedia, LinkedIn
- Puntuar señales de autoridad de marca que los modelos de IA usan para el reconocimiento de entidades

**Subagente 2: Optimización de Plataformas (geo-platform-analysis)**
- Evaluar la preparación para Google AI Overviews, ChatGPT, Perplexity, Gemini, Bing Copilot
- Comprobar factores de ranking específicos por plataforma y oportunidades de optimización

**Subagente 3: Infraestructura Técnica GEO (geo-technical)**
- Analizar robots.txt para el acceso de rastreadores de IA
- Verificar meta etiquetas, cabeceras y accesibilidad técnica para sistemas de IA
- Comprobar velocidad de página, renderizado en servidor (SSR) y Core Web Vitals
- Evaluar cabeceras de seguridad y optimización móvil

**Subagente 4: Calidad de Contenido E-E-A-T (geo-content)**
- Evaluar señales de Experiencia, Conocimiento, Autoridad, Confiabilidad
- Comprobar biografías de autores, credenciales, citas a fuentes
- Evaluar frescura del contenido, profundidad y originalidad
- Verificar calidad de la página "Acerca de" y credenciales del equipo

**Subagente 5: Esquema y Datos Estructurados (geo-schema)**
- Validar todo el marcado schema.org
- Comprobar tipos de esquema críticos para GEO (FAQ, HowTo, Organization, Product, Article)
- Evaluar integridad y precisión del esquema
- Identificar oportunidades de esquemas faltantes

---

### Fase 3: Agregación de Puntuación y Generación de Reporte

#### Cálculo de Puntuación GEO Compuesta

La Puntuación GEO general (0-100) es un promedio ponderado de seis puntuaciones de categoría:

| Categoría | Peso | Qué Mide |
|---|---|---|
| **Citabilidad por IA** | 25% | Qué tan citable/extraíble es el contenido para los sistemas de IA |
| **Autoridad de Marca** | 20% | Menciones de terceros, señales de reconocimiento de entidades |
| **E-E-A-T de Contenido** | 20% | Experiencia, Conocimiento, Autoridad, Confiabilidad |
| **GEO Técnico** | 15% | Acceso de rastreadores de IA, llms.txt, renderizado, velocidad |
| **Esquema y Datos Estructurados** | 10% | Calidad e integridad del marcado Schema.org |
| **Optimización de Plataformas** | 10% | Presencia en plataformas donde los modelos de IA entrenan y citan |

**Fórmula:**
```
Puntuacion_GEO = (Citabilidad * 0.25) + (Marca * 0.20) + (EEAT * 0.20) + (Tecnico * 0.15) + (Esquema * 0.10) + (Plataforma * 0.10)
```

#### Interpretación de Puntuación

| Rango de Puntuación | Calificación | Interpretación |
|---|---|---|
| 90-100 | Excelente | Optimización GEO de primer nivel; el sitio tiene altas probabilidades de ser citado por la IA |
| 75-89 | Bueno | Sólida base GEO con margen de mejora |
| 60-74 | Justo | Presencia GEO moderada; existen oportunidades significativas de optimización |
| 40-59 | Pobre | Señales GEO débiles; los sistemas de IA pueden tener dificultades para citar o recomendar |
| 0-39 | Crítico | Optimización GEO mínima; el sitio es en gran medida invisible a los sistemas de IA |

---

## Clasificación de Severidad de Problemas

Cada problema encontrado durante la auditoría se clasifica por severidad:

### Crítico (Solucionar Inmediatamente)
- Todos los rastreadores de IA bloqueados en robots.txt
- Sin contenido indexable (solo renderizado por JavaScript sin SSR)
- Directiva noindex a nivel de dominio
- El sitio devuelve errores 5xx en páginas clave
- Ausencia completa de cualquier dato estructurado
- La marca no es reconocida como una entidad por ningún sistema de IA

### Alto (Solucionar en 1 Semana)
- Rastreadores de IA clave (GPTBot, ClaudeBot, PerplexityBot) bloqueados
- Sin archivo llms.txt presente
- Cero bloques de contenido de preguntas y respuestas en páginas clave
- Falta esquema Organization o LocalBusiness
- Sin atribución de autor en páginas de contenido
- Todo el contenido detrás de login/muro de pago sin vista previa

### Medio (Solucionar en 1 Mes)
- Bloqueo parcial de rastreadores de IA (algunos permitidos, otros bloqueados)
- llms.txt existe pero está incompleto o malformado
- Bloques de contenido con un promedio por debajo de 50 en puntuación de citabilidad
- Falta esquema FAQ en páginas con contenido de Preguntas Frecuentes
- Biografías de autores escasas sin credenciales
- Sin presencia de marca en Wikipedia o Reddit

### Bajo (Optimizar Cuando Sea Posible)
- Errores menores de validación de esquema
- Algunas imágenes sin texto alternativo (alt text)
- Problemas de frescura de contenido en páginas no críticas
- Faltan etiquetas Open Graph
- Jerarquía de encabezados subóptima en algunas páginas
- La página de empresa en LinkedIn existe pero está incompleta

---

## Formato de Salida

Genera un archivo llamado `GEO-AUDIT-REPORT.md` con la siguiente estructura:

```markdown
# Reporte de Auditoría GEO: [Nombre del Sitio]

**Fecha de Auditoría:** [Fecha]
**URL:** [URL]
**Tipo de Negocio:** [Tipo Detectado]
**Páginas Analizadas:** [Recuento]

---

## Resumen Ejecutivo

**Puntuación GEO General: [X]/100 ([Calificación])**

[Resumen de 2-3 oraciones sobre la salud GEO del sitio, las mayores fortalezas y las brechas más críticas.]

### Desglose de Puntuación

| Categoría | Puntuación | Peso | Puntuación Ponderada |
|---|---|---|---|
| Citabilidad por IA | [X]/100 | 25% | [X] |
| Autoridad de Marca | [X]/100 | 20% | [X] |
| E-E-A-T de Contenido | [X]/100 | 20% | [X] |
| GEO Técnico | [X]/100 | 15% | [X] |
| Esquema y Datos Estructurados | [X]/100 | 10% | [X] |
| Optimización de Plataformas | [X]/100 | 10% | [X] |
| **Puntuación GEO General** | | | **[X]/100** |

---

## Problemas Críticos (Solucionar Inmediatamente)

[Lista cada problema crítico con URLs de páginas específicas y solución recomendada]

## Problemas de Alta Prioridad

[Lista cada problema de alta prioridad con detalles]

## Problemas de Media Prioridad

[Lista cada problema de media prioridad]

## Problemas de Baja Prioridad

[Lista cada problema de baja prioridad]

---

## Inmersión Profunda por Categoría

### Citabilidad por IA ([X]/100)
[Hallazgos detallados, ejemplos de buenos/malos pasajes, sugerencias de reescritura]

### Autoridad de Marca ([X]/100)
[Mapa de presencia en plataformas, volumen de menciones, sentimiento]

### E-E-A-T de Contenido ([X]/100)
[Calidad del autor, citas a fuentes, frescura, profundidad]

### GEO Técnico ([X]/100)
[Acceso de rastreadores, llms.txt, renderizado, cabeceras]

### Esquema y Datos Estructurados ([X]/100)
[Tipos de esquema encontrados, resultados de validación, oportunidades faltantes]

### Optimización de Plataformas ([X]/100)
[Presencia en YouTube, Reddit, Wikipedia, etc.]

---

## Victorias Rápidas (Implementar Esta Semana)

1. [Victoria rápida específica y accionable con impacto esperado]
2. [Otra victoria rápida]
3. [Otra victoria rápida]
4. [Otra victoria rápida]
5. [Otra victoria rápida]

## Plan de Acción de 30 Días

### Semana 1: [Tema]
- [ ] Elemento de acción 1
- [ ] Elemento de acción 2

### Semana 2: [Tema]
- [ ] Elemento de acción 1
- [ ] Elemento de acción 2

### Semana 3: [Tema]
- [ ] Elemento de acción 1
- [ ] Elemento de acción 2

### Semana 4: [Tema]
- [ ] Elemento de acción 1
- [ ] Elemento de acción 2

---

## Apéndice: Páginas Analizadas

| URL | Título | Problemas GEO |
|---|---|---|
| [url] | [título] | [recuento de problemas] |
```

---

## Controles de Calidad

- **Límite de Páginas:** Nunca rastrees más de 50 páginas por auditoría. Prioriza páginas de alto valor.
- **Tiempo de Espera:** Máximo de 30 segundos por obtención de página. Omite las páginas que superen esto.
- **Robots.txt:** Siempre revisa y respeta el robots.txt antes de rastrear. Nota cualquier directiva específica de IA.
- **Límite de Peticiones:** Espera al menos 1 segundo entre peticiones de página para evitar sobrecargar el servidor.
- **Manejo de Errores:** Registra las peticiones fallidas pero continúa la auditoría. Reporta los fallos de obtención en el apéndice.
- **Tipo de Contenido:** Solo analiza páginas HTML. Omite PDFs, imágenes y otro contenido binario.
- **Desduplicación:** Canonicaliza las URLs antes de rastrear. Omite contenido duplicado (ej., HTTP vs HTTPS, www vs sin-www, barras finales).

---

## Ajustes de Auditoría Específicos por Tipo de Negocio

### Sitios SaaS
- Mayor peso en: Tablas comparativas de funciones (alta citabilidad), páginas de integración, calidad de la documentación
- Comprobar: Estructura de documentación de la API, páginas de registro de cambios (changelog), organización de la base de conocimientos
- Esquema clave: SoftwareApplication, FAQPage, HowTo

### Negocios Locales
- Mayor peso en: Consistencia NAP, señales del Perfil de Empresa de Google, esquema local
- Comprobar: Páginas de áreas de servicio, contenido específico de ubicación, marcado de reseñas
- Esquema clave: LocalBusiness, GeoCoordinates, OpeningHoursSpecification

### Sitios E-commerce
- Mayor peso en: Descripciones de productos (citabilidad), contenido de comparación, guías de compra
- Comprobar: Integridad del esquema de productos, agregación de reseñas, secciones de FAQ en páginas de producto
- Esquema clave: Product, AggregateRating, Offer, BreadcrumbList

### Publicadores
- Mayor peso en: Calidad de los artículos, credenciales del autor, prácticas de citación a fuentes
- Comprobar: Esquema de artículo, páginas de autor, frescura de la fecha de publicación, investigación original
- Esquema clave: Article, NewsArticle, Person (autor), ClaimReview

### Agencia/Servicios
- Mayor peso en: Casos de estudio (citabilidad), demostración de conocimientos, liderazgo de pensamiento
- Comprobar: Esquema de portafolio, credenciales del equipo, señales de conocimiento específico de la industria
- Esquema clave: Organization, Service, Person (equipo), Review
