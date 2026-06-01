---
name: geo-schema
description: Auditoría de datos estructurados de Schema.org y generación optimizada para la descubribilidad por IA — detecta, valida y genera marcado JSON-LD
version: 1.0.0
author: geo-seo-claude
tags: [geo, schema, structured-data, json-ld, entity-recognition, ai-discoverability]
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# Esquema GEO y Datos Estructurados

## Propósito

Los datos estructurados son la principal señal legible por máquina que dice a los sistemas de IA qué ES una entidad, qué hace y cómo se conecta con otras entidades. Aunque el marcado de esquema tradicionalmente se ha tratado de conseguir resultados enriquecidos en Google, su papel en GEO es fundamentalmente diferente: **los datos estructurados son la forma en que los modelos de IA entienden y confían en tu entidad**. Un grafo de entidades completo en datos estructurados aumenta dramáticamente la probabilidad de citación en todas las plataformas de búsqueda por IA.

## Cómo Usar Esta Habilidad

1. Obtén el HTML de la página objetivo usando `fetch_page.py` (ver nota abajo)
2. Detecta todos los datos estructurados existentes (JSON-LD, Microdatos, RDFa)
3. Valida los esquemas detectados frente a las especificaciones de Schema.org
4. Identifica esquemas recomendados faltantes según el tipo de negocio
5. Genera bloques de código JSON-LD listos para usar
6. Produce GEO-SCHEMA-REPORT.md

---

## Paso 1: Detección

**IMPORTANTE:** WebFetch convierte HTML a markdown y elimina el contenido del `<head>`, lo que elimina los bloques JSON-LD. Usa `fetch_page.py` en su lugar:
```bash
python3 ~/.claude/skills/geo/scripts/fetch_page.py <url> page
```
La salida incluye un array `structured_data` con todos los bloques JSON-LD extraídos de la página.

### Escanear en busca de JSON-LD
Busca bloques `<script type="application/ld+json">` en el HTML. Analiza cada bloque como JSON. Una página puede contener múltiples bloques JSON-LD — recógelos todos.

### Escanear en busca de Microdatos
Busca elementos con atributos `itemscope`, `itemtype` e `itemprop`. Mapea la jerarquía de elementos anidados. Nota: Los microdatos son más difíciles de analizar para los rastreadores de IA que JSON-LD. Marca una recomendación para migrar a JSON-LD si los Microdatos son el único formato encontrado.

### Escanear en busca de RDFa
Busca elementos con atributos `typeof`, `property` y `vocab`. Similar a los microdatos — recomienda migrar a JSON-LD.

### Orden de Prioridad
JSON-LD es el **formato fuertemente recomendado** para GEO. Google, Bing y las plataformas de IA procesan JSON-LD de manera más confiable. Si el sitio usa Microdatos o RDFa exclusivamente, marca esto como una migración de alta prioridad.

---

## Paso 2: Validación

Para cada bloque de esquema detectado, valida:

1. **JSON Válido**: ¿Es el JSON-LD sintácticamente válido? Comprueba que no haya comas al final (trailing commas), claves sin comillas o cadenas malformadas.
2. **@type Válido**: ¿Coincide el `@type` con un tipo reconocido por Schema.org? Comprueba en https://schema.org/docs/full.html.
3. **Propiedades Requeridas**: ¿Incluye el esquema todas las propiedades requeridas para su tipo? (Ver requisitos por tipo abajo).
4. **Propiedades Recomendadas**: ¿Incluye el esquema propiedades recomendadas que aumenten la descubribilidad por IA?
5. **Enlaces sameAs**: ¿Incluye el esquema propiedades `sameAs` enlazando a presencias en otras plataformas?
6. **Validez de URL**: ¿Se resuelven todas las URLs en el esquema (no devuelven 404)?
7. **Anidamiento**: ¿Está el esquema anidado correctamente (ej., author dentro de Article, address dentro de Organization)?
8. **Método de Renderizado**: ¿Está el JSON-LD en el HTML renderizado por el servidor o se inyecta vía JavaScript? Según la guía de Google de diciembre de 2025, **los datos estructurados inyectados por JavaScript pueden enfrentar un procesamiento retrasado**. Señala cualquier esquema que requiera ejecución JS.

---

## Paso 3: Tipos de Esquema para GEO

### Organization (CRÍTICO — todo sitio de negocio)
Esencial para el reconocimiento de entidades a través de todas las plataformas de IA. Esta es la forma en que los modelos de IA identifican QUÉ es el negocio.

**Propiedades requeridas:**
- `@type`: "Organization" (o subtipo: Corporation, LocalBusiness, etc.)
- `name`: Nombre oficial del negocio
- `url`: URL oficial del sitio web
- `logo`: URL de la imagen del logotipo (se prefiere ImageObject)

**Propiedades recomendadas para GEO:**
- `sameAs`: Array de TODAS las URLs de plataformas (ver estrategia sameAs abajo)
- `description`: Descripción de 1-2 oraciones de la organización
- `foundingDate`: Fecha en ISO 8601
- `founder`: Esquema Person
- `address`: Esquema PostalAddress
- `contactPoint`: ContactPoint con teléfono, email, contactType
- `areaServed`: Área geográfica
- `numberOfEmployees`: QuantitativeValue
- `industry`: Texto o DefinedTerm
- `award`: Array de premios recibidos
- `knowsAbout`: Array de temas en los que la organización es experta (fuerte señal GEO)

### LocalBusiness (para negocios con ubicaciones físicas)
Extiende Organization. Crítico para resultados de búsqueda locales de IA y Google Gemini.

**Propiedades requeridas adicionales:**
- `address`: PostalAddress completo
- `telephone`: Número de teléfono
- `openingHoursSpecification`: Horario de operación

**Recomendadas para GEO:**
- `geo`: GeoCoordinates (latitud, longitud)
- `priceRange`: Indicador de precios
- `aggregateRating`: Esquema AggregateRating
- `review`: Array de esquemas Review
- `hasMap`: URL a Google Maps

### Article + Author (CRÍTICO para publicadores)
El esquema Author es una de las señales E-E-A-T más fuertes para las plataformas de IA.

**Article requerido:**
- `@type`: "Article" (o NewsArticle, BlogPosting, TechArticle)
- `headline`: Título del artículo
- `datePublished`: ISO 8601
- `dateModified`: ISO 8601 (crítico para señales de frescura)
- `author`: Esquema Person u Organization
- `publisher`: Esquema Organization con logo
- `image`: Imagen representativa

**Author (Person) requerido para GEO:**
- `name`: Nombre completo
- `url`: URL de la página de autor en el sitio
- `sameAs`: LinkedIn, Twitter, sitio personal, Google Scholar, ORCID
- `jobTitle`: Título profesional
- `worksFor`: Esquema Organization
- `knowsAbout`: Array de áreas de especialización
- `alumniOf`: Instituciones educativas
- `award`: Premios profesionales

### Product (para e-commerce)
**Requerido:**
- `name`, `description`, `image`
- `offers`: Offer con price, priceCurrency, availability
- `brand`: Esquema Brand
- `sku` o `gtin`/`mpn`

**Recomendado para GEO:**
- `aggregateRating`: AggregateRating
- `review`: Array de reseñas individuales
- `category`: Categoría del producto
- `material`, `weight`, `width`, `height` (donde aplique)

### FAQPage
**Estado a partir de 2024**: Google restringe los resultados enriquecidos de FAQ a sitios gubernamentales y de salud. Sin embargo, el esquema FAQPage aún cumple propósitos GEO — las plataformas de IA analizan los datos estructurados de FAQ para extracción de preguntas y respuestas. Impleméntalo para legibilidad por IA incluso si no aparecen resultados enriquecidos.

**Estructura:**
- `@type`: "FAQPage"
- `mainEntity`: Array de esquemas Question, cada uno con `acceptedAnswer` conteniendo un esquema Answer

### SoftwareApplication (para SaaS)
**Requerido:**
- `name`, `description`
- `applicationCategory`: ej., "BusinessApplication"
- `operatingSystem`: Plataformas soportadas
- `offers`: Precios

**Recomendado para GEO:**
- `aggregateRating`: Valoraciones de usuarios
- `featureList`: Array de características (fuerte señal de citación)
- `screenshot`: Capturas de pantalla
- `softwareVersion`: Versión actual
- `releaseNotes`: Enlace al registro de cambios (changelog)

### WebSite + SearchAction (para caja de búsqueda de sitelinks)
**Estructura:**
```json
{
  "@type": "WebSite",
  "name": "Nombre del Sitio",
  "url": "https://example.com",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://example.com/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

### Person (independiente — para marcas personales, autores, líderes de pensamiento)
Úsalo como un esquema independiente en páginas Acerca de/Bio. Esto construye el grafo de entidades para la experiencia individual.

**Requerido:** `name`, `url`
**Recomendado para GEO:** `sameAs`, `jobTitle`, `worksFor`, `knowsAbout`, `alumniOf`, `award`, `description`, `image`

### Propiedad speakable (para asistentes de voz/IA)
La propiedad `speakable` marca secciones específicas de contenido como particularmente adecuadas para el consumo de asistentes de voz e IA. Añádela a esquemas Article o WebPage.

```json
{
  "@type": "Article",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".article-summary", ".key-takeaway"]
  }
}
```
Esto indica a los asistentes de IA qué pasajes son los mejores candidatos para citar o leer en voz alta.

---

## Paso 4: Esquemas Obsoletos/Modificados a Señalar

| Esquema | Estado | Nota |
|---|---|---|
| HowTo | Resultados enriquecidos deprecados Ago 2023 | Sigue siendo útil para análisis IA, pero no promete resultados enriquecidos |
| FAQPage | Restringido a gob/salud Ago 2023 | Sigue siendo útil para análisis IA (ver arriba) |
| SpecialAnnouncement | Deprecado 2023 | Fue para el COVID; elimínalo si sigue presente |
| CourseInfo | Reemplazado por actualizaciones de Course 2024 | Usa propiedades de esquema Course actualizadas |
| VideoObject `contentUrl` | Comportamiento modificado 2024 | Debe apuntar al archivo de video real, no a la URL de la página |
| Review snippet | Ejecución más estricta 2024 | Reseñas auto-promocionales en páginas de productos pueden no mostrarse |

Señala cualquier esquema obsoleto (deprecated) encontrado y recomienda reemplazos.

---

## Paso 5: Estrategia sameAs (CRÍTICA para Reconocimiento de Entidades)

La propiedad `sameAs` es la propiedad de datos estructurados más importante para GEO. Les dice a los sistemas de IA: "Esta entidad en mi sitio web es la MISMA entidad que estos perfiles en otros lugares". Esto crea el grafo de entidades que las plataformas de IA usan para verificar, confiar y citar fuentes.

### Enlaces sameAs Recomendados (en orden de prioridad)

1. **Artículo de Wikipedia** — enlace de entidad de mayor autoridad
2. **Elemento Wikidata** — identificador de entidad legible por máquina (ej., `https://www.wikidata.org/wiki/Q12345`)
3. **LinkedIn** — página de empresa o perfil personal
4. **YouTube** — URL del canal
5. **Twitter/X** — URL del perfil
6. **Facebook** — URL de la página
7. **Crunchbase** — perfil de empresa (para startups/tech)
8. **GitHub** — organización o perfil personal (para tech)
9. **Google Scholar** — perfil de autor (para investigadores/académicos)
10. **ORCID** — identificador de investigador (para académicos)
11. **Instagram** — URL del perfil
12. **Apple App Store / Google Play** — listados de aplicaciones (para software)
13. **BBB** — listado de Better Business Bureau (para negocios de EE.UU.)
14. **Directorios de la industria** — directorios verticales relevantes

### Proceso de Auditoría sameAs
1. Recopila todas las presencias web conocidas para la entidad
2. Comprueba que cada URL se resuelva (no 404 o redirigida)
3. Verifica que el esquema Organization/Person las incluye TODAS
4. Comprueba que la información en cada plataforma sea consistente (nombre, descripción, fecha de fundación, etc.)
5. Señala cualquier plataforma donde la entidad debería tener presencia pero no la tiene

---

## Paso 6: Generación de JSON-LD

Basado en el tipo de negocio detectado, genera bloques JSON-LD listos para pegar. Siempre genera:

1. **Organization o Person** (dependiendo del tipo de entidad) — siempre
2. **WebSite con SearchAction** — siempre para la página de inicio
3. **Específico del tipo de negocio** — Article para publicadores, Product para e-commerce, LocalBusiness para local, SoftwareApplication para SaaS
4. **BreadcrumbList** — para cualquier página más profunda que la página de inicio

### Reglas de Generación
- Usa el patrón `@graph` para incluir múltiples esquemas en un solo bloque JSON-LD
- Todas las URLs deben ser absolutas (no relativas)
- Incluye propiedades `@id` para referencias cruzadas entre esquemas
- Usa ISO 8601 para todas las fechas
- Incluye `speakable` en esquemas Article con selectores CSS apuntando a secciones clave del contenido
- Coloca JSON-LD en la sección `<head>` — NO inyectado vía JavaScript

### Plantilla: Organización con Señales GEO Completas
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://example.com/#organization",
  "name": "Nombre de Empresa",
  "url": "https://example.com",
  "logo": {
    "@type": "ImageObject",
    "url": "https://example.com/logo.png",
    "width": 600,
    "height": 60
  },
  "description": "Descripción concisa de lo que hace la empresa.",
  "foundingDate": "2020-01-15",
  "founder": {
    "@type": "Person",
    "name": "Nombre del Fundador",
    "sameAs": "https://www.linkedin.com/in/fundador"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Calle Principal",
    "addressLocality": "Ciudad",
    "addressRegion": "Estado",
    "postalCode": "12345",
    "addressCountry": "US"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-555-555-5555",
    "contactType": "servicio al cliente",
    "email": "soporte@example.com"
  },
  "sameAs": [
    "https://en.wikipedia.org/wiki/Nombre_de_Empresa",
    "https://www.wikidata.org/wiki/Q12345",
    "https://www.linkedin.com/company/nombre-empresa",
    "https://www.youtube.com/@nombreempresa",
    "https://twitter.com/nombreempresa",
    "https://github.com/nombreempresa",
    "https://www.crunchbase.com/organization/nombre-empresa"
  ],
  "knowsAbout": [
    "Tema 1",
    "Tema 2",
    "Tema 3"
  ]
}
```

---

## Rúbrica de Puntuación (0-100)

| Criterio | Puntos | Cómo Puntuar |
|---|---|---|
| Esquema Organization/Person presente y completo | 15 | 15 si completo, 10 si básico, 0 si no hay |
| Enlaces sameAs (5+ plataformas) | 15 | 3 por enlace sameAs válido, máx 15 |
| Esquema Article con detalles de autor | 10 | 10 si esquema autor completo, 5 si solo nombre, 0 si no hay |
| Esquema específico del negocio presente | 10 | 10 si completo, 5 si parcial, 0 si falta |
| WebSite + SearchAction | 5 | 5 si presente, 0 si no |
| BreadcrumbList en páginas internas | 5 | 5 si presente, 0 si no |
| Formato JSON-LD (no Microdatos/RDFa) | 5 | 5 si JSON-LD, 3 si mixto, 0 si solo Microdatos/RDFa |
| Renderizado en servidor (no inyectado JS) | 10 | 10 si en fuente HTML, 5 si JS pero en head, 0 si JS dinámico |
| Propiedad speakable en artículos | 5 | 5 si presente, 0 si no |
| JSON Válido + tipos Schema.org válidos | 10 | 10 si sin errores, 5 si problemas menores, 0 si errores mayores |
| Propiedad knowsAbout en Organization/Person | 5 | 5 si presente con 3+ temas, 0 si falta |
| Sin esquemas obsoletos (deprecated) presentes | 5 | 5 si limpio, 0 si se encuentran esquemas obsoletos |

---

## Formato de Salida

Genera **GEO-SCHEMA-REPORT.md** con:

```markdown
# Reporte de Esquema GEO y Datos Estructurados — [Dominio]
Fecha: [Fecha]

## Puntuación de Esquema: XX/100

## Esquemas Detectados
| Página | Tipo de Esquema | Formato | Estado | Problemas |
|---|---|---|---|---|
| / | Organization | JSON-LD | Válido | Falta sameAs |
| /blog/post-1 | Article | JSON-LD | Válido | Sin esquema de autor |

## Resultados de Validación
[Enumera cada esquema con aprobado/fallo por propiedad]

## Esquemas Recomendados Faltantes
[Enumera esquemas que deberían estar presentes según tipo de negocio pero no lo están]

## Auditoría sameAs
| Plataforma | URL | Estado |
|---|---|---|
| Wikipedia | [URL o "No encontrada"] | Presente/Ausente |
| LinkedIn | [URL o "No encontrada"] | Presente/Ausente |
[Continuar para todas las plataformas recomendadas]

## Código JSON-LD Generado
[Bloques JSON-LD listos para pegar para cada esquema faltante o incompleto]

## Notas de Implementación
- Dónde colocar cada bloque JSON-LD
- Requisitos de renderizado en servidor
- Pruebas con Prueba de Resultados Enriquecidos de Google (Rich Results Test) y Validador Schema.org
```
