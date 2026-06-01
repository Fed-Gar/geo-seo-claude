---
name: geo-crawlers
description: Análisis de acceso de rastreadores de IA. Revisa robots.txt, meta etiquetas y cabeceras HTTP para determinar qué rastreadores de IA pueden acceder al sitio. Proporciona un mapa de acceso completo y recomendaciones para maximizar la visibilidad de IA mientras se mantiene el control adecuado.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Habilidad de Análisis de Acceso de Rastreadores de IA

## Propósito

Esta habilidad analiza la accesibilidad de un sitio web para los rastreadores de IA (los bots que las empresas de IA utilizan para descubrir, indexar y entrenarse con contenido web). Si los rastreadores de IA están bloqueados, el contenido del sitio no puede aparecer en las respuestas generadas por IA, independientemente de su calidad. El acceso de los rastreadores es el requisito técnico fundamental para GEO.

## Idea Clave

A principios de 2026, muchos sitios web bloquean inadvertidamente los rastreadores de IA a través de reglas de robots.txt demasiado agresivas, heredadas de configuraciones SEO antiguas. Un estudio de Originality.ai de 2025 descubrió que más del 35% de los 1.000 sitios web principales bloquean al menos a un rastreador de IA importante, y el 5-10% bloquea todos los rastreadores de IA. Bloquear los rastreadores de IA es la forma más rápida de volverse invisible en los resultados de búsqueda generados por IA.

---

## Referencia Completa de Rastreadores de IA

### Nivel 1: Críticos para Visibilidad en Búsqueda por IA (RECOMENDACIÓN: PERMITIR)

Estos rastreadores impulsan los productos de búsqueda de IA donde los usuarios buscan respuestas activamente. Bloquearlos reduce directamente tu visibilidad en las respuestas generadas por IA.

#### GPTBot
- **Operador:** OpenAI
- **User-Agent:** `GPTBot`
- **Cadena Completa User-Agent:** `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; GPTBot/1.2; +https://openai.com/gptbot)`
- **Propósito:** Obtiene contenido para la navegación web, plugins y funciones de búsqueda de ChatGPT. El contenido accedido por GPTBot puede usarse para mejorar los modelos de OpenAI.
- **Impacto de Bloquear:** El contenido NO aparecerá en los resultados de Búsqueda de ChatGPT ni será accesible cuando los usuarios pidan a ChatGPT que navegue por la web. Este es el rastreador de IA de mayor impacto a permitir.
- **Recomendación:** **PERMITIR** -- ChatGPT tiene más de 300M de usuarios activos semanales en 2025. Bloquear GPTBot elimina tu contenido de una de las superficies de búsqueda de IA más grandes.

#### OAI-SearchBot
- **Operador:** OpenAI
- **User-Agent:** `OAI-SearchBot`
- **Cadena Completa User-Agent:** `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; OAI-SearchBot/1.0; +https://docs.openai.com/bots/overview)`
- **Propósito:** Específicamente impulsa la función de búsqueda de ChatGPT. A diferencia de GPTBot, el contenido accedido por OAI-SearchBot NO se usa para entrenamiento del modelo -- solo para resultados de búsqueda en vivo.
- **Impacto de Bloquear:** El contenido no aparecerá en los resultados de búsqueda de ChatGPT, incluso si se permite GPTBot.
- **Recomendación:** **PERMITIR** -- Este es un rastreador exclusivo para búsqueda sin implicaciones de entrenamiento. No hay razón estratégica para bloquearlo.

#### ChatGPT-User
- **Operador:** OpenAI
- **User-Agent:** `ChatGPT-User`
- **Cadena Completa User-Agent:** `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; ChatGPT-User/1.0; +https://openai.com/bot)`
- **Propósito:** Se usa cuando un usuario de ChatGPT pide explícitamente al modelo visitar una URL específica. Actúa como un agente de navegador en nombre del usuario.
- **Impacto de Bloquear:** ChatGPT no puede visitar tus páginas cuando los usuarios piden leerlas o resumirlas. Esto previene el tráfico directo iniciado por el usuario.
- **Recomendación:** **PERMITIR** -- Bloquear este bot impide que los usuarios que intentan interactuar activamente con tu contenido accedan a él a través de ChatGPT.

#### ClaudeBot
- **Operador:** Anthropic
- **User-Agent:** `ClaudeBot`
- **Cadena Completa User-Agent:** `ClaudeBot/1.0; +https://www.anthropic.com/claude-bot`
- **Propósito:** Obtiene contenido web para las características de Claude, incluyendo búsqueda web, citas y herramientas de análisis.
- **Impacto de Bloquear:** El contenido no será accesible para Claude en búsquedas web o cuando los usuarios pidan a Claude analizar URLs específicas.
- **Recomendación:** **PERMITIR** -- Claude es un asistente de IA principal con una cuota de mercado en crecimiento. Bloquear ClaudeBot reduce tu huella en búsquedas de IA.

#### PerplexityBot
- **Operador:** Perplexity AI
- **User-Agent:** `PerplexityBot`
- **Cadena Completa User-Agent:** `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)`
- **Propósito:** Impulsa el motor de búsqueda de IA de Perplexity, el cual proporciona respuestas documentadas con citas directas y enlaces a las páginas de origen.
- **Impacto de Bloquear:** El contenido no aparecerá en los resultados de búsqueda de Perplexity. Perplexity es una de las mejores fuentes de tráfico referido entre los productos de búsqueda de IA porque siempre muestra los enlaces a las fuentes.
- **Recomendación:** **PERMITIR** -- Perplexity impulsa tráfico referido real y siempre atribuye las fuentes. Es un rastreador de IA de alto valor para publicadores y negocios.

---

### Nivel 2: Importantes para Ecosistema IA Más Amplio (RECOMENDACIÓN: PERMITIR)

Estos rastreadores sirven a grandes plataformas de IA o ecosistemas de búsqueda. Permitirlos aumenta el alcance de tu contenido.

#### Google-Extended
- **Operador:** Google
- **User-Agent:** `Google-Extended`
- **Propósito:** Controla si Google usa tu contenido para entrenamiento de modelos Gemini y para mejorar los Resúmenes de IA (AI Overviews). **NOTA CRÍTICA:** Bloquear Google-Extended NO afecta tus clasificaciones en Google Search ni tu aparición en los resultados de Búsqueda de Google. Eso está controlado por el Googlebot estándar.
- **Impacto de Bloquear:** El contenido no podrá usarse para entrenamiento de Gemini o para mejorar AI Overviews. Sin embargo, tu contenido todavía puede aparecer en AI Overviews basándose en la indexación de búsqueda estándar.
- **Recomendación:** **PERMITIR** -- Bloquear ofrece un beneficio mínimo de protección de contenido mientras que reduce tu presencia en funciones de IA de Google. Como no afecta el ranking estándar, la única razón para bloquear es una objeción filosófica al uso de datos de entrenamiento.

#### GoogleOther
- **Operador:** Google
- **User-Agent:** `GoogleOther`
- **Propósito:** Usado por Google para varios propósitos ajenos a la clasificación en búsqueda, incluyendo investigación, rastreos únicos y recolección de datos relacionados con la IA.
- **Impacto de Bloquear:** Impacto mínimo en clasificaciones de búsqueda. Puede reducir la presencia en funciones de investigación y experimentales de IA de Google.
- **Recomendación:** **PERMITIR** -- Bajo riesgo, beneficio potencial moderado para inclusión en funciones de IA.

#### Applebot-Extended
- **Operador:** Apple
- **User-Agent:** `Applebot-Extended`
- **Propósito:** Usado por Apple para entrenar y mejorar características de Apple Intelligence, Siri y los productos de IA de Apple. Separado del Applebot estándar (que impulsa búsqueda de Siri y Spotlight).
- **Impacto de Bloquear:** El contenido no podrá usarse en funciones de Apple Intelligence. Las funciones estándar de Siri y Spotlight no se ven afectadas (controladas por Applebot).
- **Recomendación:** **PERMITIR** -- Apple Intelligence está integrada en todos los dispositivos Apple (2B+ dispositivos activos). La presencia en las funciones de IA de Apple tiene valor estratégico creciente.

#### Amazonbot
- **Operador:** Amazon
- **User-Agent:** `Amazonbot`
- **Cadena Completa User-Agent:** `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (compatible; Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot)`
- **Propósito:** Indexa contenido para respuestas de Alexa y funciones de IA de Amazon.
- **Impacto de Bloquear:** El contenido no aparecerá en las respuestas de voz de Alexa o en funciones de búsqueda impulsadas por IA de Amazon.
- **Recomendación:** **PERMITIR** -- Relevante para optimización de búsqueda por voz. Prioridad más baja que los rastreadores de Nivel 1, pero no hay desventaja en permitirlo.

#### FacebookBot
- **Operador:** Meta
- **User-Agent:** `FacebookBot`
- **Propósito:** Usado por Meta para funciones de IA en Facebook, Instagram, WhatsApp y el asistente Meta AI.
- **Impacto de Bloquear:** El contenido puede no ser accesible para Meta AI. Las vistas previas de enlaces en Facebook/Instagram son manejadas por un rastreador diferente y no se ven afectadas.
- **Recomendación:** **PERMITIR** -- Meta AI está integrado en aplicaciones con 3B+ de usuarios combinados. Importancia creciente para visibilidad de IA.

---

### Nivel 3: Rastreadores Solo para Entrenamiento (PERMITIR o BLOQUEAR según Estrategia)

Estos rastreadores se usan principalmente para entrenamiento de modelos de IA en lugar de funciones de búsqueda en vivo. Bloquearlos no afecta la visibilidad en búsqueda de IA.

#### CCBot
- **Operador:** Common Crawl (organización sin fines de lucro)
- **User-Agent:** `CCBot`
- **Cadena Completa User-Agent:** `CCBot/2.0 (https://commoncrawl.org/faq/)`
- **Propósito:** Construye el conjunto de datos de Common Crawl, el cual es usado como dato de entrenamiento por muchas empresas de IA (Google, Meta, Stability AI, y otras).
- **Impacto de Bloquear:** El contenido no aparecerá en futuros conjuntos de datos de Common Crawl. NO afecta ningún producto de búsqueda IA en vivo.
- **Recomendación:** **DEPENDE DEL CONTEXTO** -- Permitir si deseas la máxima presencia de entrenamiento IA a largo plazo. Bloquear si deseas controlar el uso de datos de entrenamiento. Sin impacto en visibilidad de búsqueda.

#### anthropic-ai
- **Operador:** Anthropic
- **User-Agent:** `anthropic-ai`
- **Propósito:** Usado por Anthropic para investigación en seguridad de IA y entrenamiento de modelo Claude. Separado de ClaudeBot (que impulsa características en vivo).
- **Impacto de Bloquear:** El contenido no será usado para entrenamiento de Claude. NO afecta a las funciones de búsqueda en vivo o navegación web de Claude (controlado por ClaudeBot).
- **Recomendación:** **DEPENDE DEL CONTEXTO** -- Similar a CCBot. Permitir para presencia en entrenamiento, bloquear para controlar datos de entrenamiento. Sin impacto en búsqueda de IA en vivo.

#### Bytespider
- **Operador:** ByteDance
- **User-Agent:** `Bytespider`
- **Propósito:** Usado por ByteDance para varios productos de IA incluyendo las funciones de IA de TikTok y Doubao (su competidor de ChatGPT en China).
- **Impacto de Bloquear:** El contenido no se usará para productos de IA de ByteDance. Impacto mínimo para negocios en el mercado occidental.
- **Recomendación:** **BLOQUEAR** para la mayoría de negocios occidentales (comportamiento de rastreo agresivo reportado, mínimo beneficio de visibilidad de búsqueda). **PERMITIR** si se dirige al mercado asiático/chino.

#### cohere-ai
- **Operador:** Cohere
- **User-Agent:** `cohere-ai`
- **Propósito:** Usado por Cohere para entrenamiento de modelos. Cohere provee soluciones de IA empresarial y el producto de chat Coral.
- **Impacto de Bloquear:** El contenido no será usado para el entrenamiento de modelos Cohere. Mínimo impacto directo de cara al consumidor.
- **Recomendación:** **DEPENDE DEL CONTEXTO** -- Baja prioridad. Permitir o bloquear basado en postura general sobre datos de entrenamiento.

---

## Resumen de Matriz de Recomendación

| Rastreador | Nivel | Recomendación | Razón |
|---|---|---|---|
| GPTBot | 1 | **PERMITIR** | Impulsa ChatGPT Search (300M+ usuarios) |
| OAI-SearchBot | 1 | **PERMITIR** | Solo búsqueda, no usa para entrenamiento |
| ChatGPT-User | 1 | **PERMITIR** | Navegación iniciada por el usuario |
| ClaudeBot | 1 | **PERMITIR** | Búsqueda web de Claude y análisis |
| PerplexityBot | 1 | **PERMITIR** | El mejor tráfico referido en búsqueda de IA |
| Google-Extended | 2 | **PERMITIR** | Funciones Gemini; sin impacto en rank de búsqueda |
| GoogleOther | 2 | **PERMITIR** | Investigación IA de Google |
| Applebot-Extended | 2 | **PERMITIR** | Apple Intelligence (2B+ dispositivos) |
| Amazonbot | 2 | **PERMITIR** | Alexa e IA de Amazon |
| FacebookBot | 2 | **PERMITIR** | Meta AI (3B+ usuarios de app) |
| CCBot | 3 | Contexto | Solo para datos de entrenamiento |
| anthropic-ai | 3 | Contexto | Solo para datos de entrenamiento |
| Bytespider | 3 | **BLOQUEAR** | Rastreador agresivo, bajo beneficio |
| cohere-ai | 3 | Contexto | Solo para datos de entrenamiento |

### Configuración Máxima de Visibilidad de IA (robots.txt)

Para sitios que quieren máxima visibilidad en búsquedas por IA:

```
# Rastreadores IA - PERMITIDOS para visibilidad en búsqueda IA
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: GoogleOther
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: Amazonbot
Allow: /

User-agent: FacebookBot
Allow: /

# Rastreadores IA - BLOQUEADOS (agresivos/bajo valor)
User-agent: Bytespider
Disallow: /

User-agent: CCBot
Disallow: /
```

---

## Procedimiento de Análisis

### Paso 1: Obtener y Analizar robots.txt

1. Usa WebFetch para recuperar `[dominio]/robots.txt`.
2. Analiza todas las directivas de User-agent y sus reglas Allow/Disallow asociadas.
3. Para cada rastreador de IA en la lista de referencia anterior:
   - Revisa si hay un bloque User-agent específico para ese rastreador
   - Revisa si hay un bloque comodín (`User-agent: *`) que aplicaría
   - Determina el acceso efectivo: **Permitido**, **Bloqueado** o **No Mencionado** (hereda reglas del comodín)
4. Toma nota de cualquier directiva `Crawl-delay` que pueda ralentizar el acceso de rastreadores IA.
5. Revisa directivas `Sitemap` (los rastreadores IA las usan para descubrimiento).

### Paso 2: Revisar Etiquetas Meta Robots

1. Para una muestra de 5-10 páginas clave, obtiene el HTML y busca:
   - `<meta name="robots" content="noindex">` -- bloquea a todos los bots
   - `<meta name="robots" content="nofollow">` -- impide seguir enlaces
   - `<meta name="robots" content="noai">` -- etiqueta emergente para bloquear uso por IA
   - `<meta name="robots" content="noimageai">` -- bloquea entrenamiento con imágenes para IA
   - Meta etiquetas específicas de bots: `<meta name="GPTBot" content="noindex">`
2. Registra cualquier invalidación (override) a nivel de página de las directivas del robots.txt.

### Paso 3: Revisar Cabeceras HTTP

1. Para las mismas páginas de muestra, revisa las cabeceras de respuesta en busca de:
   - `X-Robots-Tag: noindex` -- Equivalente en cabecera HTTP de meta noindex
   - `X-Robots-Tag: noai` -- Cabecera HTTP para bloquear uso de IA
   - `X-Robots-Tag: noimageai` -- Bloquea entrenamiento IA de imágenes
   - Cabeceras específicas de bots: `X-Robots-Tag: GPTBot: noindex`
2. Toma en cuenta que las cabeceras HTTP anulan las meta etiquetas y también aplican a recursos no-HTML.

### Paso 4: Revisar Archivos Específicos de IA

1. Busca `/llms.txt` (estándar emergente para orientación a rastreadores de IA).
2. Busca `/.well-known/ai-plugin.json` (manifiesto de plugin de OpenAI).
3. Busca `/ai.txt` (estándar propuesto, similar a ads.txt para IA).
4. Registra la presencia/ausencia y calidad de cada archivo.

### Paso 5: Evaluar Requisitos de Renderizado JavaScript

1. Verifica si el sitio es una Aplicación de una Sola Página (SPA) o altamente dependiente de renderizado JavaScript.
2. Los rastreadores de IA varían en sus capacidades de renderizar JavaScript:
   - GPTBot: Renderizado JS limitado
   - ClaudeBot: Renderizado JS limitado
   - PerplexityBot: Renderizado JS limitado
   - Googlebot: Renderizado JS completo (pero Google-Extended lo hereda)
3. Si el contenido crítico requiere renderizado JS, marca esto como un problema potencial.
4. Verifica si hay renderizado en el servidor (SSR) o Generación de Sitios Estáticos (SSG) como mitigación.

### Paso 6: Analizar Señales de Contenido (Content Signals)

Usando el robots.txt que ya se obtuvo en el Paso 1, escanea por directivas `Content-Signal:` (borrador IETF `draft-romm-aipref-contentsignals`).

1. Escanea cada línea buscando aquellas que comiencen por `Content-Signal:` (insensible a mayúsculas/minúsculas).
2. Si se encuentra:
   - Parsea todos los pares clave=valor (divide por `,` y luego por `=`).
   - Valida claves contra el conjunto conocido: `ai-train`, `search`, `ai-personalization`, `ai-retrieval`.
   - Valida valores: solo `yes` y `no` son válidos.
   - Señala cualquier clave desconocida o valor inválido como una advertencia — la especificación aún es un borrador IETF.
   - Registra el resultado como **Aprobado** (Pass) y expone los valores parseados con un significado en lenguaje simple.
3. Si no se encuentra: registra como **Recomendación** — el sitio no ha declarado preferencias de uso para la IA.

No se necesita solicitud HTTP adicional. robots.txt ya se obtiene en el Paso 1.

---

## Formato de Salida

Genera un archivo llamado `GEO-CRAWLER-ACCESS.md`:

```markdown
# Reporte de Acceso a Rastreadores de IA: [Dominio]

**Fecha de Análisis:** [Fecha]
**Dominio:** [Dominio]
**Estado de robots.txt:** [Encontrado/No Encontrado/Error]

---

## Resumen de Acceso de Rastreadores

| Rastreador | Operador | Nivel | Estado | Impacto |
|---|---|---|---|---|
| GPTBot | OpenAI | 1 | [Permitido/Bloqueado/No Mencionado] | [Descripción impacto] |
| OAI-SearchBot | OpenAI | 1 | [Estado] | [Impacto] |
| ChatGPT-User | OpenAI | 1 | [Estado] | [Impacto] |
| ClaudeBot | Anthropic | 1 | [Estado] | [Impacto] |
| PerplexityBot | Perplexity | 1 | [Estado] | [Impacto] |
| Google-Extended | Google | 2 | [Estado] | [Impacto] |
| GoogleOther | Google | 2 | [Estado] | [Impacto] |
| Applebot-Extended | Apple | 2 | [Estado] | [Impacto] |
| Amazonbot | Amazon | 2 | [Estado] | [Impacto] |
| FacebookBot | Meta | 2 | [Estado] | [Impacto] |
| CCBot | Common Crawl | 3 | [Estado] | [Impacto] |
| anthropic-ai | Anthropic | 3 | [Estado] | [Impacto] |
| Bytespider | ByteDance | 3 | [Estado] | [Impacto] |
| cohere-ai | Cohere | 3 | [Estado] | [Impacto] |

## Puntuación de Visibilidad IA: [X]/100

**Acceso Nivel 1:** [X/5 rastreadores permitidos]
**Acceso Nivel 2:** [X/5 rastreadores permitidos]
**Acceso Nivel 3:** [X/4 rastreadores permitidos]

---

## Problemas Críticos

[Enumerar cualquier rastreador Nivel 1 que esté bloqueado]

## Recomendaciones

### Acciones Inmediatas
[Cambios específicos requeridos en robots.txt]

### Recomendación de robots.txt
```
[Contenido recomendado completo de robots.txt para rastreadores de IA]
```

### Hallazgos Técnicos Adicionales
- **Etiquetas Meta Robots:** [Hallazgos]
- **Cabeceras X-Robots-Tag:** [Hallazgos]
- **Renderizado JavaScript:** [Evaluación]
- **llms.txt:** [Presente/Ausente]
- **Accesibilidad de Sitemap:** [Evaluación]

### Señales de Contenido (Borrador IETF)

**Estado:** Presente / Ausente

<!-- Si está presente: -->
| Clave de Señal | Valor | Significado |
|---|---|---|
| ai-train | no | Excluido (opt-out) del entrenamiento de modelo IA |
| search | yes | Permite uso en resultados de búsqueda impulsados por IA |

<!-- Si está ausente: -->
**Recomendación:** Añade una directiva `Content-Signal:` a robots.txt para declarar explícitamente las preferencias de uso por IA. Ejemplo:

`Content-Signal: ai-train=no, search=yes, ai-retrieval=yes`

Ve https://contentsignals.org/ para la especificación completa.
```

---

## Puntuación para Acceso de Rastreadores

La Puntuación de Acceso de Rastreadores de IA se calcula como:

| Componente | Peso | Puntuación |
|---|---|---|
| Rastreadores de Nivel 1 Permitidos | 50% | 20 puntos por rastreador de Nivel 1 permitido (5 rastreadores = 100 puntos máx, escalado a 50) |
| Rastreadores de Nivel 2 Permitidos | 25% | 20 puntos por rastreador de Nivel 2 permitido (5 rastreadores = 100 puntos máx, escalado a 25) |
| Sin Bloqueos Generales a IA | 15% | Puntos completos si no hay `User-agent: *` Disallow: / y sin meta etiquetas noai |
| Archivos Específicos-IA Presentes | 10% | 5 puntos por llms.txt, 5 puntos por sitemap accesible a rastreadores de IA |

Puntuación final = suma de todos los componentes ponderados, con límite de 100.
