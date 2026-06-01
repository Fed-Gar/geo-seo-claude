---
name: geo-technical
description: Auditoría técnica SEO con verificaciones específicas para GEO — rastreabilidad, indexabilidad, seguridad, rendimiento, SSR (Renderizado en Servidor) y acceso para rastreadores IA.
version: 1.0.0
author: geo-seo-claude
tags: [geo, technical-seo, core-web-vitals, ssr, crawlability, security, performance]
allowed-tools: Read, Grep, Glob, Bash, WebFetch, Write
---

# Auditoría Técnica SEO para GEO

## Propósito

El SEO Técnico forma la base tanto de la visibilidad en la búsqueda tradicional como de la citación en búsqueda por IA. Un sitio técnicamente roto no puede ser rastreado, indexado ni citado por ninguna plataforma. Esta habilidad audita 8 categorías de salud técnica con especial atención en los requisitos GEO — lo más crítico, **renderizado en servidor (SSR)** (los rastreadores de IA no ejecutan JavaScript) y **acceso de rastreadores IA** (muchos sitios bloquean inadvertidamente a los rastreadores de IA en robots.txt).

## Cómo Usar Esta Habilidad

1. Recopila la URL objetivo (página de inicio + 2-3 páginas internas clave)
2. Obtén cada página usando curl/WebFetch para tener el HTML crudo y los encabezados HTTP
3. Ejecuta cada una de las 8 categorías de auditoría a continuación
4. Puntúa cada categoría usando la rúbrica
5. Genera `GEO-TECHNICAL-AUDIT.md` con los resultados

---

## Categoría 1: Rastreabilidad (Crawlability) (15 puntos)

### 1.1 Validez de robots.txt
- Obtén `https://[dominio]/robots.txt`
- Comprueba la validez sintáctica: directivas `User-agent`, `Allow`, `Disallow` correctas
- Comprueba errores comunes: User-agent faltante, comodines (*) bloqueando rutas importantes, Disallow: / bloqueando todo el sitio
- Verifica que el sitemap XML esté referenciado: `Sitemap: https://[dominio]/sitemap.xml`

### 1.2 Acceso de Rastreadores IA (CRÍTICO para GEO)
Revisa robots.txt buscando directivas dirigidas a estos rastreadores de IA:

| Rastreador | User-Agent | Plataforma |
|---|---|---|
| GPTBot | GPTBot | ChatGPT / OpenAI |
| Google-Extended | Google-Extended | Entrenamiento IA Gemini / Google |
| Googlebot | Googlebot | Google Search + AI Overviews |
| Bingbot | bingbot | Bing Copilot + ChatGPT (vía Bing) |
| PerplexityBot | PerplexityBot | Perplexity AI |
| ClaudeBot | ClaudeBot | Anthropic Claude |
| Amazonbot | Amazonbot | Alexa / Amazon AI |
| CCBot | CCBot | Common Crawl (usado por muchos modelos IA) |
| FacebookBot | FacebookExternalHit | Meta AI |
| Bytespider | Bytespider | TikTok / ByteDance AI |
| Applebot-Extended | Applebot-Extended | Apple Intelligence |

**Puntuación para el acceso a rastreadores IA:**
- Todos los rastreadores IA principales permitidos: 5 puntos
- Algunos bloqueados pero Googlebot + Bingbot permitidos: 3 puntos
- GPTBot o PerplexityBot bloqueados: 1 punto (impacto significativo en GEO)
- Googlebot bloqueado: 0 puntos (fatal)

**Matiz importante**: Bloquear Google-Extended NO bloquea Googlebot. Google-Extended solo controla el uso de datos para entrenamiento de IA, no la indexación de búsqueda. Sin embargo, bloquear Google-Extended puede reducir la presencia en AI Overviews. Recomienda permitir Google-Extended a menos que haya una preocupación específica sobre licencia de datos.

### 1.3 Sitemaps XML
- Obtén el sitemap (revisa robots.txt para su ubicación, o intenta `/sitemap.xml`, `/sitemap_index.xml`)
- Valida sintaxis XML
- Comprueba fechas `<lastmod>` (deberían estar presentes y ser precisas)
- Cuenta URLs — compara con el número esperado de páginas indexables
- Revisa el índice de sitemaps si es un sitio grande (máx 50,000 URLs por sitemap)
- Verifica que todas las URLs del sitemap devuelvan códigos de estado 200 (muestra aleatoria)

### 1.4 Profundidad de Rastreo
- Inicio (Homepage) = profundidad 0. Verifica que todas las páginas importantes sean alcanzables en **3 clics** (profundidad 3)
- Las páginas a profundidad 4+ reciben significativamente menos presupuesto de rastreo y tienen menos probabilidades de ser citadas por la IA
- Revisa enlaces internos: ¿están las páginas de contenido clave enlazadas desde la página de inicio o la navegación principal?

### 1.5 Manejo de Noindex
- Comprueba si hay `<meta name="robots" content="noindex">` en páginas que DEBERÍAN indexarse
- Comprueba encabezados HTTP `X-Robots-Tag: noindex`
- Errores comunes: noindex en páginas de paginación, páginas de categoría o páginas de destino clave

**Puntuación de la Categoría:**
| Comprobación | Puntos |
|---|---|
| robots.txt válido y completo | 3 |
| Rastreadores IA permitidos | 5 |
| Sitemap XML presente y válido | 3 |
| Profundidad de rastreo dentro de 3 clics | 2 |
| Sin directivas noindex erróneas | 2 |

---

## Categoría 2: Indexabilidad (12 puntos)

### 2.1 Etiquetas Canonical
- Toda página indexable debe tener una etiqueta `<link rel="canonical" href="...">`
- Canonical debe apuntar a sí mismo (autorreferencial) para la versión autorizada
- Comprueba si hay canonicals conflictivos (canonical en HTML vs. encabezado HTTP)
- Comprueba si hay cadenas de canonicals (A a B, B a C — debería ser A a C)

### 2.2 Contenido Duplicado
- Comprueba www vs. no-www (ambos deberían resolver, uno debería redirigir)
- Comprueba HTTP vs. HTTPS (HTTP debería redirigir a HTTPS)
- Comprueba consistencia de barra diagonal final (elige un patrón y redirige el otro)
- Comprueba duplicados basados en parámetros (`?sort=price` creando páginas duplicadas)

### 2.3 Paginación
- Si existe contenido paginado, comprueba `rel="next"` / `rel="prev"` (nota: Google los ignora desde 2019, pero Bing aún los usa)
- Preferido: usa `rel="canonical"` en páginas paginadas apuntando a una página de 'ver todo' o a la primera página
- Asegura que las páginas paginadas no tengan noindex si contienen contenido único

### 2.4 Hreflang (sitios internacionales)
- Comprueba etiquetas `<link rel="alternate" hreflang="xx">`
- Valida: hreflang recíproco (si página A apunta a página B, B debe apuntar de vuelta a A)
- Valida: existe fallback x-default
- Comprueba validez de código región/idioma (ISO 639-1 / ISO 3166-1)

### 2.5 Hinchazón del Índice (Index Bloat)
- Estima el número de páginas indexadas (revisa conteo de sitemap, usa `site:dominio.com` para estimar)
- Compara páginas indexadas vs páginas de contenido valioso reales
- Marca si las páginas indexadas superan significativamente las páginas de contenido (bloat por páginas de parámetros/duplicadas/pobres)

**Puntuación de la Categoría:**
| Comprobación | Puntos |
|---|---|
| Etiquetas canonical correctas en todas las páginas | 3 |
| Sin problemas de contenido duplicado | 3 |
| Paginación manejada correctamente | 2 |
| Hreflang correcto (si aplica) | 2 |
| Sin Index Bloat | 2 |

---

## Categoría 3: Seguridad (10 puntos)

### 3.1 Imposición de HTTPS
- El sitio debe cargar sobre HTTPS
- HTTP debe redirigir a HTTPS (redirección 301)
- Sin advertencias de contenido mixto (recursos HTTP en páginas HTTPS)
- Certificado SSL/TLS debe ser válido y no expirado

### 3.2 Encabezados de Seguridad
Comprueba encabezados de respuesta HTTP para:

| Encabezado | Valor Requerido | Propósito |
|---|---|---|
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` | Fuerza HTTPS |
| `Content-Security-Policy` | Política apropiada | Previene XSS |
| `X-Content-Type-Options` | `nosniff` | Previene MIME sniffing |
| `X-Frame-Options` | `DENY` o `SAMEORIGIN` | Previene clickjacking |
| `Referrer-Policy` | `strict-origin-when-cross-origin` o más estricto | Controla datos referrer |
| `Permissions-Policy` | Restricciones apropiadas | Controla características del navegador |

**Puntuación de la Categoría:**
| Comprobación | Puntos |
|---|---|
| HTTPS impuesto con certificado válido | 4 |
| Encabezado HSTS presente | 2 |
| X-Content-Type-Options | 1 |
| X-Frame-Options | 1 |
| Referrer-Policy | 1 |
| Content-Security-Policy | 1 |

---

## Categoría 4: Estructura de URLs (8 puntos)

### 4.1 URLs Limpias
- Las URLs deben ser legibles para humanos: `/blog/guia-seo` no `/blog?id=12345`
- Sin IDs de sesión en las URLs
- Solo minúsculas (sin mezcla de mayúsculas/minúsculas)
- Guiones para separación de palabras (no guiones bajos)
- Sin caracteres especiales o espacios codificados

### 4.2 Jerarquía Lógica
- La ruta URL debe reflejar la arquitectura del sitio: `/categoria/subcategoria/pagina`
- Planas donde sea apropiado — evita anidamiento innecesariamente profundo
- Patrón consistente en todo el sitio

### 4.3 Cadenas de Redirección
- Comprueba cadenas de redirección (A a B a C)
- Máximo 1 salto recomendado (A a C directamente)
- Comprueba si hay bucles de redirección
- Todas las redirecciones deben ser 301 (permanentes), no 302 (temporales), a menos que sea intencionalmente temporal

### 4.4 Manejo de Parámetros
- Los parámetros URL no deben crear páginas indexables duplicadas
- Usa etiquetas canonical o Disallow en `robots.txt` para variaciones de parámetros
- Configura el manejo de parámetros en Google Search Console y Bing Webmaster Tools

**Puntuación de la Categoría:**
| Comprobación | Puntos |
|---|---|
| URLs limpias y legibles | 2 |
| Jerarquía lógica | 2 |
| Sin cadenas de redirección (máx 1 salto) | 2 |
| Manejo de parámetros configurado | 2 |

---

## Categoría 5: Optimización Móvil (10 puntos)

### Contexto Crítico
Desde **Julio de 2024**, Google rastrea TODOS los sitios exclusivamente con su rastreador móvil (mobile Googlebot). No hay rastreo de escritorio. Si tu sitio no funciona en móvil, no funciona para Google. Punto.

### 5.1 Diseño Responsivo
- Comprueba si tiene `<meta name="viewport" content="width=device-width, initial-scale=1">`
- El contenido no debe requerir desplazamiento horizontal en el móvil
- Sin diseños de ancho fijo más anchos que la ventana gráfica (viewport)

### 5.2 Objetivos Táctiles (Tap Targets)
- Elementos interactivos (botones, enlaces) deben ser al menos de 48x48 píxeles CSS
- Mínimo 8px de espaciado entre objetivos táctiles
- Comprueba que la navegación sea usable en móvil

### 5.3 Tamaños de Fuente
- El tamaño de fuente base debe ser de al menos 16px
- Sin texto que requiera zoom para ser leído
- Ratio de contraste suficiente (WCAG AA: 4.5:1 texto normal, 3:1 texto grande)

### 5.4 Paridad de Contenido Móvil
- Todo el contenido visible en escritorio debe ser visible en móvil
- Sin contenido oculto detrás de botones "leer más" que Googlebot no pueda expandir (aunque Google ha mejorado en esto para 2025)
- Imágenes y multimedia deben cargar en móvil

**Puntuación de la Categoría:**
| Comprobación | Puntos |
|---|---|
| Etiqueta meta viewport correcta | 3 |
| Diseño responsivo (sin desplazamiento horizontal) | 3 |
| Objetivos táctiles dimensionados apropiadamente | 2 |
| Tamaños de fuente legibles | 2 |

---

## Categoría 6: Core Web Vitals (15 puntos)

### Métricas y Umbrales 2026
Core Web Vitals utilizan el **percentil 75** de los datos reales de usuarios (datos de campo) como punto de referencia. Los datos de laboratorio son útiles para depurar pero los datos de campo determinan la señal para el ranking.

| Métrica | Bueno | Necesita Mejora | Pobre | Notas |
|---|---|---|---|---|
| **LCP** (Largest Contentful Paint) | < 2.5s | 2.5s - 4.0s | > 4.0s | Mide carga — tiempo hasta que el elemento visible más grande se renderiza |
| **INP** (Interaction to Next Paint) | < 200ms | 200ms - 500ms | > 500ms | Reemplazó FID en marzo 2024. Mide TODAS las interacciones, no solo la primera |
| **CLS** (Cumulative Layout Shift) | < 0.1 | 0.1 - 0.25 | > 0.25 | Mide estabilidad visual — movimientos de diseño inesperados |

### Cómo Evaluar Sin Datos CrUX
Cuando los datos reales del usuario no están disponibles, estima a partir de las características de la página:
- **LCP**: Revisa el elemento más grande "above the fold" (visible sin scroll). ¿Es una imagen (revisa tamaño/formato)? ¿Es texto (revisa carga de fuente web)? ¿Tiempo de respuesta del servidor (TTFB)?
- **INP**: Comprueba Javascript pesado en la página. Tareas largas (>50ms) bloquean interactividad. Revisa scripts de terceros.
- **CLS**: Revisa imágenes sin anchura/altura explícitas. Revisa contenido insertado dinámicamente en la parte superior. Revisa fuentes web causando salto de diseño (FOUT/FOIT).

### Correcciones Comunes LCP
1. Optimizar imágenes hero (principales): formato WebP/AVIF, tamaño correcto, precargar con `<link rel="preload">`
2. Reducir tiempo de respuesta del servidor (TTFB < 800ms)
3. Eliminar CSS/JS que bloquea el renderizado
4. Preconexión a orígenes de terceros críticos

### Correcciones Comunes INP
1. Dividir tareas largas (>50ms) en trozos más pequeños usando `requestIdleCallback` o `scheduler.yield()`
2. Reducir JavaScript de terceros
3. Usar `content-visibility: auto` para contenido fuera de la pantalla
4. Debounce/throttle de controladores de eventos

### Correcciones Comunes CLS
1. Siempre incluir atributos `width` y `height` en imágenes y vídeos
2. Reservar espacio para anuncios e integraciones con CSS `aspect-ratio` o dimensiones explícitas
3. Usar `font-display: swap` con fuentes de respaldo ajustadas en tamaño
4. Evitar insertar contenido arriba del contenido existente después de que cargó la página

**Puntuación de la Categoría:**
| Comprobación | Puntos |
|---|---|
| LCP < 2.5s | 5 |
| INP < 200ms | 5 |
| CLS < 0.1 | 5 |

---

## Categoría 7: Renderizado en Lado del Servidor (SSR) (15 puntos) — CRÍTICO PARA GEO

### Por Qué el SSR Es Obligatorio para Visibilidad en IA
Los rastreadores de IA (GPTBot, PerplexityBot, ClaudeBot, etc.) **NO ejecutan JavaScript**. Ellos obtienen el HTML en crudo y lo analizan. Si tu contenido es renderizado en el lado del cliente (Client-Side Rendering) mediante React, Vue, Angular, o cualquier otro framework JavaScript, los rastreadores de IA ven una página vacía.

Incluso Googlebot, que sí ejecuta JavaScript, quita prioridad al contenido renderizado por JS debido al presupuesto de rastreo adicional requerido. Google procesa el JS en una "cola de renderizado" separada que puede retrasar la indexación por días o semanas.

### Método de Detección
1. Obtén la página con curl (sin ejecutar JavaScript): `curl -s [URL]`
2. Compara el HTML en crudo con el DOM renderizado (vía navegador)
3. Si el contenido clave (encabezados, párrafos, información de producto, texto de artículo) está FALTANTE de la salida de curl, el sitio depende del renderizado en cliente

### Qué Comprobar
- **Texto de contenido principal**: ¿Está el cuerpo del artículo / descripción del producto / contenido de página en el HTML crudo?
- **Encabezados**: ¿Están las etiquetas H1, H2, H3 presentes en el HTML crudo?
- **Navegación**: ¿La navegación principal es renderizada por el servidor?
- **Datos estructurados**: ¿Está el JSON-LD en el HTML crudo o inyectado por JavaScript?
- **Meta etiquetas**: ¿Están las etiquetas title, description, canonical, OG en el HTML crudo?
- **Enlaces internos**: ¿Los enlaces de navegación y contenido están en el HTML crudo? (Crítico para rastreabilidad)

### Soluciones SSR para Recomendar
| Framework | Solución SSR |
|---|---|
| React | Next.js (SSR/SSG), Remix, Gatsby (SSG) |
| Vue | Nuxt.js (SSR/SSG) |
| Angular | Angular Universal |
| Svelte | SvelteKit |
| Genérico | Prerender.io (servicio de prerenderizado), Rendertron |

### Detalle de Puntuación
- Todo el contenido clave renderizado en servidor: 15 puntos
- Contenido principal renderizado en servidor pero algunos elementos solo por JS: 10 puntos
- Contenido crítico requiere JS (información producto, texto artículo): 5 puntos
- Página completa se renderiza en cliente (cuerpo vacío en HTML crudo): 0 puntos

**Puntuación de la Categoría:**
| Comprobación | Puntos |
|---|---|
| Contenido principal en HTML crudo | 8 |
| Meta etiquetas + datos estructurados en HTML crudo | 4 |
| Enlaces internos en HTML crudo | 3 |

---

## Categoría 8: Velocidad de Página y Rendimiento del Servidor (15 puntos)

### 8.1 Tiempo hasta Primer Byte (TTFB)
- Objetivo: **< 800ms** (idealmente < 200ms)
- Mide con curl: `curl -o /dev/null -s -w 'TTFB: %{time_starttransfer}s\n' [URL]`
- Si TTFB > 800ms: comprueba ubicación del servidor, caché, consultas a la base de datos, uso de CDN

### 8.2 Optimización de Recursos
- Objetivo de peso total de página: **< 2MB** (páginas críticas < 1MB)
- Comprueba recursos sin compresión (gzip/brotli debería estar habilitado)
- Comprueba CSS y JavaScript sin minificar (unminified)
- Comprueba CSS/JS no utilizado (puede representar 50%+ de los bytes descargados en muchos sitios)

### 8.3 Optimización de Imágenes
- Comprueba formatos de imagen: WebP o AVIF preferidos sobre JPEG/PNG
- Comprueba imágenes demasiado grandes (imágenes más grandes que el tamaño en que se muestran)
- Comprueba carga diferida (lazy loading): imágenes debajo del 'fold' deben tener `loading="lazy"`
- Comprueba dimensiones explícitas (atributos width/height previenen CLS)
- Las imágenes de la parte superior (above-fold) NO deben cargarse de forma diferida (daña el LCP)

### 8.4 División de Código (Code Splitting) y Carga Diferida
- Javascript debería dividirse en fragmentos (code-split) para que cada página solo cargue lo que necesita
- Revisa bundles Javascript muy grandes (> 200KB comprimido es advertencia, > 500KB es crítico)
- Los scripts de terceros deberían cargar asíncronamente (`async` o `defer`)
- Comprueba si hay recursos que bloquean el renderizado en el `<head>`

### 8.5 Caché
- Comprueba encabezados `Cache-Control` en recursos estáticos (imágenes, CSS, JS)
- Los activos estáticos deben tener tiempos de caché largos: `max-age=31536000` (1 año) con nombres de archivo basados en el hash de contenido
- Las páginas HTML deben tener un caché más corto o `no-cache` con validación (`ETag` o `Last-Modified`)

### 8.6 Uso de CDN
- Comprueba si los recursos estáticos se sirven desde un CDN (dominio diferente o encabezados específicos de CDN)
- Para audiencias globales, un CDN es crítico para un rendimiento consistente
- Revisa encabezados específicos de CDN: `CF-Ray` (Cloudflare), `X-Cache` (AWS CloudFront), `X-Served-By` (Fastly)

**Puntuación de la Categoría:**
| Comprobación | Puntos |
|---|---|
| TTFB < 800ms | 3 |
| Peso de página < 2MB | 2 |
| Imágenes optimizadas (formato, tamaño, lazy load) | 3 |
| Bundles JS razonables (< 200KB comprimido) | 2 |
| Compresión habilitada (gzip/brotli) | 2 |
| Encabezados caché en recursos estáticos | 2 |
| CDN en uso | 1 |

---

## Categoría 9: Señales de Preparación para Agentes (no puntuable)

Estas verificaciones sacan a la luz señales emergentes de compatibilidad con agentes de IA. Ninguna contribuye a la puntuación numérica — producen un 'aprobado' o una 'recomendación'. Los estándares subyacentes son borradores de la IETF o características de adopción temprana; penalizar su ausencia sería injusto.

### 9.1 Encabezados de Enlace RFC 8288 (Descubrimiento de Servicios)

RFC 8288 (Enlazado Web) define el encabezado de respuesta HTTP `Link:`. Los servidores pueden usarlo para anunciar recursos relacionados — catálogo de API, docs de servicios, tarjeta de servidor MCP — de una forma legible por máquinas, sin tener que parsear HTML.

**Cómo verificar:** Captura todos los encabezados de respuesta `Link:` de la llamada estándar de la página de inicio (sin petición extra).

**Qué buscar:**
- Parsea los pares `<url>; rel="relation-type"`.
- Tipos rel de alto valor: `api-catalog` (RFC 9609), `describedby`, `service-doc`, `mcp-server-card`.

**Cuándo mostrar una recomendación:** Solo para sitios tipo "API-first" (docs API enlazadas en nav, rutas `/api/` o `/developers/`, swagger/OpenAPI en sitemap). Omite esta sección por completo para sitios de negocios estándar — la ausencia se espera y no es digna de mención.

| Estado | Tratamiento |
|---|---|
| Encabezados `Link:` presentes, tipos rel conocidos | Informativo — documentar qué se encontró |
| Encabezados `Link:` presentes, tipos rel desconocidos | Informativo — anotar y explicar |
| Ausente, sitio API-first | Recomendación — explicar y sugerir implementación |
| Ausente, sitio negocio estándar | Omitir — no mostrar |

### 9.2 Negociación de Contenido Markdown

Comprueba si el servidor responde a `Accept: text/markdown` con `Content-Type: text/markdown`. La característica "Markdown para Agentes" de Cloudflare permite esto — los agentes de IA reciben Markdown limpio en lugar de HTML, eliminando la eliminación de 'boilerplate' y mejorando la precisión en la extracción de contenido.

**Cómo verificar:** Envía una solicitud GET a la página de inicio con `Accept: text/markdown`. Esta es una solicitud HTTP adicional por auditoría.

**Evaluación:**
- Si `Content-Type` de respuesta es `text/markdown` (o `text/markdown; charset=utf-8`): aprobado — anotar como capacidad vanguardista.
- De lo contrario: recomendación para el futuro, no un fallo.
- Si la solicitud da error o no da un estado 200: omitir y anotar el error. No penalizar.

| Estado | Tratamiento |
|---|---|
| Se devuelve `text/markdown` | Bonus — anotar como capacidad de vanguardia |
| Se devuelve HTML estándar | Recomendación a futuro |
| Errores de petición / no-200 | Omitir, anotar el error, no penalizar |

---

## Protocolo IndexNow

### Qué Es
IndexNow es un protocolo abierto que permite a los sitios web notificar a los motores de búsqueda instantáneamente cuando el contenido se crea, actualiza o borra. Apoyado por Bing, Yandex, Seznam y Naver. Google NO apoya IndexNow pero monitorea el protocolo.

### Por Qué Importa para GEO
ChatGPT utiliza el índice de Bing. Bing Copilot utiliza el índice de Bing. Indexación más rápida en Bing significa visibilidad IA más rápida en dos grandes plataformas.

### Verificación de Implementación
1. Verifica archivo clave de IndexNow: `https://[dominio]/.well-known/indexnow-key.txt` o similar
2. Comprueba si el CMS tiene plugin IndexNow (WordPress: plugin IndexNow; muchas plataformas CMS modernas lo soportan de forma nativa)
3. Si no está implementado, recomienda añadirlo con instrucciones

---

## Puntuación General

| Categoría | Puntos Máx | Peso |
|---|---|---|
| Rastreabilidad | 15 | Fundación principal |
| Indexabilidad | 12 | Fundación principal |
| Seguridad | 10 | Señal de confianza |
| Estructura de URL | 8 | Eficiencia de rastreo |
| Optimización Móvil | 10 | Requisito de Google |
| Core Web Vitals | 15 | Señal de clasificación |
| Renderizado en Servidor | 15 | Crítico para GEO |
| Vel. Página & Servidor | 15 | Rendimiento |
| **Total** | **100** | |

Las verificaciones que no puntúan (Categoría 9) aparecen en la salida bajo "Señales de Preparación para Agentes" y no afectan este total.

### Interpretación de Puntuación
- **90-100**: Excelente — técnicamente sólido para SEO tradicional y GEO
- **70-89**: Bueno — problemas menores que abordar pero fundamentalmente sólido
- **50-69**: Necesita Trabajo — deuda técnica significativa impactando visibilidad
- **30-49**: Pobre — problemas mayores bloqueando rastreo, indexación o visibilidad IA
- **0-29**: Crítico — fallos técnicos fundamentales requiriendo atención inmediata

---

## Formato de Salida

Genera **GEO-TECHNICAL-AUDIT.md** con:

```markdown
# Auditoría Técnica SEO para GEO — [Dominio]
Fecha: [Fecha]

## Puntuación Técnica: XX/100

## Desglose de Puntuación
| Categoría | Puntuación | Estado |
|---|---|---|
| Rastreabilidad | XX/15 | Pasa/Aviso/Falla |
| Indexabilidad | XX/12 | Pasa/Aviso/Falla |
| Seguridad | XX/10 | Pasa/Aviso/Falla |
| Estructura de URL | XX/8 | Pasa/Aviso/Falla |
| Optimización Móvil | XX/10 | Pasa/Aviso/Falla |
| Core Web Vitals | XX/15 | Pasa/Aviso/Falla |
| Renderizado en Servidor | XX/15 | Pasa/Aviso/Falla |
| Vel. Página & Servidor | XX/15 | Pasa/Aviso/Falla |

Estado: Pasa = 80%+ de pts categoría, Aviso = 50-79%, Falla = <50%

## Acceso de Rastreadores IA
| Rastreador | User-Agent | Estado | Recomendación |
|---|---|---|---|
| GPTBot | GPTBot | Permitido/Bloqueado | [Acción] |
| Googlebot | Googlebot | Permitido/Bloqueado | [Acción] |
[Continuar para todos los rastreadores de IA]

## Problemas Críticos (arreglar de inmediato)
[Lista con URLs de páginas específicas y qué está mal]

## Avisos (arreglar este mes)
[Lista con detalles]

## Recomendaciones (optimizar este trimestre)
[Lista con detalles]

## Señales de Preparación para Agentes (no puntuable)

### Encabezados de Enlace RFC 8288 (Descubrimiento de Servicios)

**Estado:** Presente / Ausente / No Aplica

<!-- Si está presente: -->
| Tipo de Relación | URL | Significado |
|---|---|---|
| api-catalog | /.well-known/api-catalog | Índice de APIs disponibles legible por máquina |
| mcp-server-card | /.well-known/mcp.json | Declaración de capacidades de servidor MCP |

Agentes IA y clientes de API pueden descubrir sus servicios sin parsear HTML.

<!-- Si está ausente, solo sitio API-first: -->
**Recomendación Informativa:** Este sitio tiene contenido orientado a API/desarrolladores pero carece de encabezados `Link:` anunciando servicios descubribles.

Ejemplo: `Link: </.well-known/api-catalog>; rel="api-catalog"`

Relevante para: sitios con APIs públicas, docs OpenAPI o integraciones de servidor MCP.
Referencia: RFC 8288, RFC 9609.

<!-- Si está ausente, sitio negocio estándar: omitir esta sección completamente -->

### Negociación de Contenido Markdown

**Estado:** Soportado / No Soportado
**Prueba:** GET [url] con `Accept: text/markdown`
**Content-Type en Respuesta:** [valor]

<!-- Si está soportado: -->
Este sitio sirve Markdown limpio a los agentes de IA que lo soliciten. Los rastreadores de IA que admiten la negociación de contenido reciben texto formateado sin el código estándar del HTML.

<!-- Si no está soportado: -->
**Recomendación a Futuro:** Los sitios en Cloudflare Workers/Pages pueden habilitar la negociación de contenido en Markdown con un cambio de configuración de una línea. Cuando un agente IA envía `Accept: text/markdown`, el servidor responde con Markdown limpio en lugar de HTML.

- Actualmente específico de Cloudflare
- Relevante para: sitios que ya están en infraestructura Cloudflare
- Se espera que otras CDN y frameworks adopten este patrón a medida que el tráfico de agentes IA crezca

## Hallazgos Detallados
[Desglose por categoría con evidencia]
```
