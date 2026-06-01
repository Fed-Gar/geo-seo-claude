---
name: geo-llmstxt
description: Analiza y genera archivos llms.txt -- el estándar emergente para ayudar a los sistemas de IA a entender la estructura y contenido de un sitio web. Puede validar archivos llms.txt existentes o generar nuevos desde cero rastreando el sitio.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
  - Write
---

# Habilidad de Análisis y Generación del Estándar llms.txt

## Propósito

Esta habilidad maneja todo lo relacionado con el estándar `llms.txt` -- una convención emergente (propuesta por Jeremy Howard en septiembre de 2024, ganando adopción durante 2025-2026) que permite a los sitios web proporcionar orientación estructurada a los sistemas de IA sobre su contenido, estructura e información clave. Es análogo a `robots.txt` (que le dice a los rastreadores a qué NO acceder) pero en su lugar le dice a los sistemas de IA qué ES más útil entender sobre el sitio.

## Por Qué Importa llms.txt

Los modelos de lenguaje de IA enfrentan un desafío fundamental al procesar sitios web: deben determinar qué páginas son más importantes, de qué trata el sitio y cómo está organizado el contenido -- típicamente rastreando muchas páginas e infiriendo la estructura. `llms.txt` resuelve esto proporcionando un resumen explícito legible por máquinas (y por humanos).

**Beneficios de tener un llms.txt bien elaborado:**

1. **Comprensión más rápida por la IA:** Los sistemas de IA pueden entender el propósito y la estructura de tu sitio desde un solo archivo en lugar de rastrear docenas de páginas.
2. **Narrativa controlada:** Tú eliges qué páginas y hechos ven primero los sistemas de IA, moldeando cómo representan tu marca.
3. **Mayor precisión de citación:** Los sistemas de IA que consultan llms.txt pueden citar la página correcta y con autoridad para cada tema.
4. **Menos tergiversación:** Los datos clave (precios, características, ubicaciones) se declaran explícitamente, reduciendo las alucinaciones de la IA sobre tu negocio.
5. **Ventaja de adoptante temprano:** A principios de 2026, menos del 5% de los sitios web tienen un archivo llms.txt, lo que lo convierte en un diferenciador.

---

## La Especificación de llms.txt

### Ubicación del Archivo

El archivo DEBE ubicarse en la raíz del dominio:
```
https://example.com/llms.txt
```

### Especificación del Formato

El archivo usa formato Markdown con convenciones específicas:

```markdown
# [Nombre del Sitio]

> [Descripción de una oración sobre lo que hace el sitio/negocio. Mantener bajo 200 caracteres.]

## Docs

- [Título de la Página](https://example.com/url-pagina): Descripción concisa de lo que cubre esta página y por qué importa.
- [Otra Página](https://example.com/otra-pagina): Descripción del contenido.

## Optional

- [Página Menos Crítica](https://example.com/pagina-opcional): Descripción.
```

### Reglas Detalladas de Formato

**1. Título (Requerido)**
```markdown
# Nombre del Sitio
```
- Debe ser la primera línea del archivo.
- Debe ser el nombre oficial del negocio/sitio.
- Usa el formato de encabezado H1 (un solo `#`).

**2. Descripción (Requerido)**
```markdown
> Breve descripción del sitio/negocio
```
- Debe aparecer inmediatamente después del título.
- Usa formato de cita en bloque Markdown (`>`).
- Mantenla bajo 200 caracteres.
- Debe establecer claramente lo que hace el negocio y a quién sirve.
- Evita lenguaje puramente de marketing (fluff) -- sé factual y específico.

**3. Secciones Principales (Requerido -- al menos una)**

Usa encabezados H2 (`##`) para organizar las páginas por categoría. Nombres comunes de secciones:

| Nombre de Sección | Propósito | Ejemplo de Contenido |
|---|---|---|
| `## Docs` | Documentación principal o páginas clave | Páginas de productos, descripciones de servicios, contenido central |
| `## Optional` | Páginas secundarias que vale la pena conocer | Publicaciones de blog, recursos suplementarios |
| `## API` | Documentación de la API | Referencia de la API, guías de autenticación |
| `## Blog` | Contenido de blog o noticias | Artículos recientes/populares |
| `## Products` | Catálogo de productos | Páginas de productos, precios |
| `## Services` | Ofertas de servicios | Descripciones de servicios, páginas de procesos |
| `## About` | Información de la empresa | Página Acerca de, equipo, misión |
| `## Resources` | Contenido educativo/de referencia | Guías, tutoriales, libros blancos |
| `## Legal` | Documentos legales | Términos de servicio, política de privacidad |
| `## Contact` | Información de contacto | Página de contacto, canales de soporte |

**4. Entradas de Página (Requerido)**

Cada entrada sigue el formato:
```markdown
- [Título de la Página](URL): Descripción del contenido de la página
```

Reglas para las entradas de página:
- **Título:** Usa el título real de la página o un título descriptivo claro.
- **URL:** Debe ser una URL absoluta completa (no rutas relativas).
- **Descripción:** 10-30 palabras describiendo lo que cubre la página. Sé específico sobre la información disponible.
- **Orden:** Enumera las páginas en orden de importancia dentro de cada sección.
- **Límite:** Incluye de 10-30 entradas de página en total. Prioriza tus páginas más autorizadas y útiles.

**5. Sección de Datos Clave (Recomendado)**

```markdown
## Key Facts
- Founded in [año] by [fundador(es)]
- Headquarters: [Ciudad, País]
- [X] customers/users in [Y] countries
- Key products: [Producto A], [Producto B], [Producto C]
- Industry: [Clasificación de la industria]
```

Esta sección proporciona datos de referencia rápida que los sistemas de IA frecuentemente necesitan para responder consultas de usuarios sobre tu negocio.

**6. Sección de Contacto (Recomendado)**

```markdown
## Contact
- Website: https://example.com
- Email: hola@example.com
- Support: soporte@example.com
- Phone: +1-555-123-4567
- Address: 123 Calle Principal, Ciudad, Estado, Código Postal, País
```

---

## llms-full.txt (Versión Extendida)

Además de `llms.txt`, los sitios pueden proporcionar `/llms-full.txt` -- una versión extendida con más detalles.

**Diferencias con llms.txt:**

| Característica | llms.txt | llms-full.txt |
|---|---|---|
| **Longitud** | Conciso (50-150 líneas) | Exhaustivo (150-500+ líneas) |
| **Entradas de página** | 10-30 páginas clave | 30-100+ páginas |
| **Descripciones** | 10-30 palabras por entrada | 30-100 palabras por entrada, puede incluir datos clave de cada página |
| **Audiencia** | Comprensión rápida de la IA | Análisis profundo de la IA |
| **Secciones** | 3-6 secciones | 8-15 secciones |
| **Datos clave** | Datos a nivel negocio | Datos a nivel de página y puntos de información |

Ambos archivos pueden coexistir. Los sistemas de IA buscan `llms.txt` primero, y luego pueden opcionalmente cargar `llms-full.txt` para un entendimiento más profundo.

---

## Modo de Análisis

Al revisar un archivo llms.txt existente:

### Paso 1: Obtener el Archivo

1. Usa WebFetch para recuperar `[dominio]/llms.txt`.
2. También revisa `[dominio]/llms-full.txt`.
3. Registra el código de estado HTTP:
   - **200:** El archivo existe -- procede a la validación.
   - **404:** El archivo no existe -- recomienda generación.
   - **403:** El archivo existe pero está bloqueado -- márcalo como mala configuración.
   - **301/302:** Redirección -- síguela y anota la redirección.

### Paso 2: Validar Formato

Revisa cada elemento estructural:

| Elemento | Comprobación | Severidad si falta |
|---|---|---|
| Título H1 | Presente, coincide con nombre del negocio | Crítica |
| Descripción en Blockquote | Presente, < 200 caracteres, factual | Alta |
| Al menos una sección H2 | Presente | Crítica |
| Entradas de página con URLs | Al menos 5 entradas presentes | Alta |
| Las URLs son absolutas | Todas las URLs usan rutas https:// completas | Alta |
| Las URLs son válidas | Todas las URLs devuelven estado 200 | Media |
| Descripciones presentes | Toda entrada tiene descripción después de los dos puntos | Media |
| Sección de Datos Clave (Key Facts) | Presente con información del negocio | Media |
| Sección de Contacto | Presente con al menos un correo | Baja |
| Longitud razonable | 30-200 líneas | Baja |
| Markdown sin errores | Formato adecuado en todo el archivo | Media |

### Paso 3: Evaluar la Calidad del Contenido

Califica el llms.txt en estas dimensiones:

**Exhaustividad (0-100):**
- ¿Cubre todas las secciones principales del sitio visibles en la navegación?
- ¿Están incluidas las páginas más importantes/de mayor tráfico?
- ¿Está presente la sección de Datos Clave con datos de negocio precisos?
- ¿Incluye contenido reciente/actualizado?

**Precisión (0-100):**
- ¿Las descripciones reflejan con precisión el contenido de la página?
- ¿Las URLs son válidas y apuntan a las páginas correctas?
- ¿Los Datos Clave son verificables y actuales?
- ¿La descripción del negocio es precisa?

**Utilidad (0-100):**
- ¿Un sistema de IA entendería el propósito del sitio solo a partir de este archivo?
- ¿Son las descripciones lo suficientemente específicas para diferenciar las páginas?
- ¿Están destacadas las páginas más dignas de citación?
- ¿Es la organización lógica e intuitiva?

**Puntuación General llms.txt** = (Exhaustividad * 0.40) + (Precisión * 0.35) + (Utilidad * 0.25)

### Paso 4: Comparar con el Contenido del Sitio

1. Rastrea la navegación principal y el sitemap del sitio.
2. Identifica páginas importantes NO listadas en llms.txt.
3. Comprueba si alguna URL listada está rota o redirigida.
4. Verifica que la descripción del negocio coincida con el mensaje actual de la página de inicio.
5. Señala entradas obsoletas (páginas que han sido actualizadas significativamente desde que se escribió el llms.txt).

---

## Modo de Generación

Al crear un nuevo archivo llms.txt desde cero:

### Paso 1: Descubrimiento del Sitio

1. Obtén la página de inicio y extrae:
   - Nombre del sitio (desde `<title>`, `<meta property="og:site_name">`, o H1)
   - Descripción del negocio (desde la meta description o sección hero)
   - Enlaces principales de navegación
   - Enlaces del pie de página
2. Obtén `/sitemap.xml` para descubrir todas las páginas públicas.
3. Identifica el tipo de negocio principal del sitio (SaaS, E-commerce, Local, Publicador, Agencia).

### Paso 2: Priorización de Páginas

Categoriza todas las páginas descubiertas y selecciona las más importantes:

**Incluir Siempre:**
- Página de Inicio (Homepage)
- Página Acerca de / Compañía
- Página de Precios (si existe)
- Páginas de productos/servicios principales (top 3-5)
- Página de Contacto
- Página de inicio de documentación (si existe)

**Incluir si es de Alta Calidad:**
- Top publicaciones de blog (por importancia aparente, recencia o exhaustividad)
- Casos de estudio o historias de clientes
- Páginas clave de recursos/guías
- Página de Preguntas Frecuentes (FAQ)
- Página de Carreras (para empresas grandes)

**Omitir:**
- Páginas delgadas de categorías/etiquetas
- Páginas de paginación
- Páginas de inicio de sesión/registro
- Texto legal estándar (a menos que sea específicamente relevante)
- Contenido duplicado o casi duplicado
- Páginas con contenido único mínimo

### Paso 3: Escribir Descripciones

Para cada página seleccionada:

1. Obtén el contenido de la página usando WebFetch.
2. Lee el H1, meta description y los primeros 2-3 párrafos.
3. Escribe una descripción que:
   - Tenga entre 10-30 palabras
   - Declare qué información hay en la página
   - Mencione temas específicos, datos o características cubiertas
   - Evite el lenguaje de marketing ("mejor", "líder", "revolucionario")
   - Use lenguaje factual e informativo

**Ejemplos de descripciones buenas:**
- `Explica los tres niveles de precios (Free, Pro, Enterprise) con comparación de características y costos anuales/mensuales.`
- `Detalla la fundación de la empresa en 2018, equipo de 45 empleados y ubicaciones de oficinas en Austin y Londres.`
- `Cubre la configuración de integración para Slack, Salesforce y HubSpot con guías paso a paso y endpoints de API.`

**Ejemplos de descripciones malas:**
- `¡Nuestra increíble página de precios!` (lenguaje de marketing, sin detalles)
- `Conozca más sobre nuestra empresa.` (demasiado vago)
- `Haga clic aquí para más detalles.` (no descriptivo)

### Paso 4: Recopilar Datos Clave

Reúne hechos comerciales clave del sitio:

- Año de fundación
- Nombre(s) del/los fundador(es)
- Ubicación de la sede
- Número de empleados (si es público)
- Número de clientes/usuarios (si es público)
- Productos o servicios clave (enumera el top 3-5)
- Clasificación de la industria
- Clientes notables o asociaciones (si son públicos)
- Diferenciadores clave (qué hace a este negocio único)
- Hitos o logros recientes (últimos 12 meses)

### Paso 5: Ensamblar el Archivo

Construye el llms.txt siguiendo esta plantilla:

```markdown
# [Nombre del Sitio]

> [Una oración clara: qué hace el negocio, a quién sirve y su propuesta de valor principal. Menos de 200 caracteres.]

## Docs

- [Página Más Importante](https://example.com/pagina): Descripción cubriendo el contenido clave en esta página.
- [Segunda Página](https://example.com/pagina-2): Descripción del contenido de esta página y su valor.
- [Tercera Página](https://example.com/pagina-3): Lo que los usuarios y los sistemas de IA encontrarán aquí.

## Products

- [Producto A](https://example.com/producto-a): Características principales, usuarios objetivo y modelo de precios para Producto A.
- [Producto B](https://example.com/producto-b): Lo que hace Producto B y cómo se diferencia de Producto A.

## Resources

- [Título de la Guía](https://example.com/guia): Guía exhaustiva cubriendo [tema] con [X] secciones y ejemplos prácticos.
- [Publicación de Blog](https://example.com/blog/post): Análisis de [tema] con datos originales de [fuente].

## Key Facts

- Founded in [año] by [nombre(s)]
- Headquartered in [Ciudad, País]
- [Métrica específica: ej., "Serves 10,000+ businesses in 40 countries"]
- [Diferenciador clave: ej., "Only platform offering real-time X and Y integration"]
- Industry: [Clasificación]

## Contact

- Website: https://example.com
- Email: [correo de contacto principal]
- Support: [URL de soporte o correo]
```

### Paso 6: Validar el Archivo Generado

Antes de enviar a la salida:
1. Verifica que todas las URLs sean alcanzables (estado 200).
2. Confirma que la cantidad total de entradas esté entre 10-30.
3. Revisa que ninguna descripción exceda las 50 palabras.
4. Verifica que la longitud total del archivo sea de 50-150 líneas.
5. Asegúrate de que el formato Markdown sea limpio y consistente.

---

## Formato de Salida

### Para el Modo de Análisis

Genera `GEO-LLMSTXT-ANALYSIS.md`:

```markdown
# Análisis de llms.txt: [Dominio]

**Fecha de Análisis:** [Fecha]
**Estado llms.txt:** [Encontrado en URL / No Encontrado / Error]
**Estado llms-full.txt:** [Encontrado / No Encontrado]

---

## Puntuación General llms.txt: [X]/100

| Dimensión | Puntuación |
|---|---|
| Exhaustividad | [X]/100 |
| Precisión | [X]/100 |
| Utilidad | [X]/100 |

---

## Validación de Formato

| Elemento | Estado | Notas |
|---|---|---|
| Título H1 | [Pasa/Falla] | [Notas] |
| Descripción blockquote | [Pasa/Falla] | [Notas] |
| Secciones H2 | [Pasa/Falla] | [X secciones encontradas] |
| Entradas de página | [Pasa/Falla] | [X entradas encontradas] |
| Validez de URLs | [Pasa/Falla] | [X URLs rotas] |
| Descripciones de entradas | [Pasa/Falla] | [X descripciones faltantes] |
| Datos Clave (Key Facts) | [Pasa/Falla] | [Notas] |
| Sección de Contacto | [Pasa/Falla] | [Notas] |

---

## Páginas Faltantes

Estas páginas importantes fueron encontradas en el sitio pero no en llms.txt:

1. [Título de Página](URL) -- [Por qué debería estar incluida]
2. [Título de Página](URL) -- [Por qué debería estar incluida]

## Recomendaciones de Mejora

1. [Recomendación específica]
2. [Recomendación específica]
3. [Recomendación específica]

## Sugerencia de llms.txt Actualizado

[Archivo llms.txt completo reescrito si se necesitan mejoras significativas]
```

### Para el Modo de Generación

Imprime el contenido completo del archivo `llms.txt`, listo para ser guardado en el directorio raíz del sitio. También genera un breve informe `GEO-LLMSTXT-GENERATION.md` explicando:
- Cuántas páginas fueron descubiertas y cuántas fueron seleccionadas
- El fundamento de priorización
- Cualquier página que estuvo en el límite (que podría añadirse después)
- Frecuencia de actualización recomendada (ej., mensual para blogs activos, trimestral para sitios estables)

---

## Referencia de Mejores Prácticas

1. **Actualiza regularmente.** Si tu sitio publica artículos de blog semanalmente, actualiza llms.txt mensualmente. Si tu producto cambia trimestralmente, actualiza después de cada lanzamiento.
2. **Lidera con tu contenido más fuerte.** Las primeras entradas de cada sección deberían ser tus páginas más autorizadas y exhaustivas.
3. **Sé específico en las descripciones.** "Guía exhaustiva de 3.000 palabras sobre React Server Components con ejemplos de código" es mucho más útil que "Guía de React".
4. **Incluye tus diferenciadores.** Si tu sitio tiene datos únicos, investigación original o características exclusivas, resáltalos en las descripciones y en Key Facts.
5. **Mantenlo conciso.** El llms.txt debería poder escanearse en menos de 60 segundos. Guarda el detalle para llms-full.txt.
6. **Usa URLs absolutas.** Siempre incluye la URL completa con `https://`, nunca rutas relativas.
7. **Prueba después de implementar.** Después de subirlo, verifica que el archivo sea accesible en `https://tudominio.com/llms.txt` sin redirecciones.
8. **Coordina con robots.txt.** Asegúrate de que las páginas listadas en llms.txt no estén bloqueadas en robots.txt para rastreadores de IA.
9. **Refleja la estructura de tu sitio.** Los nombres de las secciones en llms.txt deberían corresponder aproximadamente a tus categorías principales de navegación.
10. **Evita páginas sensibles.** No incluyas herramientas internas, paneles de administración o páginas con información confidencial.
