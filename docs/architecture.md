# Arquitectura y Diseño

El repositorio está estructurado para proporcionar un soporte integral de GEO+SEO utilizando las capacidades de herramientas de Claude junto con agentes y scripts de utilidad en Python.

```
geo-seo-claude/
├── geo/                          # Orquestador principal de habilidades
│   └── SKILL.md                  # Archivo principal de habilidades con comandos y enrutamiento
├── skills/                       # 13 subhabilidades especializadas
│   ├── geo-audit/                # Orquestación de auditoría completa y puntuación
│   ├── geo-citability/           # Puntuación de preparación para citación por IA
│   ├── geo-crawlers/             # Análisis de acceso de rastreadores de IA
│   ├── geo-llmstxt/              # Análisis y generación del estándar llms.txt
│   ├── geo-brand-mentions/       # Presencia de marca en plataformas citadas por IA
│   ├── geo-platform-optimizer/   # Optimización de búsqueda por IA específica por plataforma
│   ├── geo-schema/               # Datos estructurados para descubribilidad por IA
│   ├── geo-technical/            # Bases de SEO técnico
│   ├── geo-content/              # Calidad de contenido y E-E-A-T
│   ├── geo-report/               # Generación de reportes en markdown listos para clientes
│   ├── geo-report-pdf/           # Reporte profesional en PDF con gráficos
│   ├── geo-prospect/             # Gestión de pipeline de prospectos estilo CRM
│   ├── geo-proposal/             # Autogeneración de propuestas para clientes
│   └── geo-compare/              # Seguimiento de diferencias mensuales y reportes de progreso
├── agents/                       # 5 subagentes en paralelo
│   ├── geo-ai-visibility.md      # Auditoría GEO, citabilidad, rastreadores, marcas
│   ├── geo-platform-analysis.md  # Optimización específica por plataforma
│   ├── geo-technical.md          # Análisis técnico de SEO
│   ├── geo-content.md            # Análisis de contenido y E-E-A-T
│   └── geo-schema.md             # Análisis de marcado de esquema (Schema markup)
├── scripts/                      # Utilidades en Python
│   ├── fetch_page.py             # Extracción y análisis de páginas
│   ├── citability_scorer.py      # Motor de puntuación de citabilidad por IA
│   ├── brand_scanner.py          # Detección de menciones de marca
│   ├── llmstxt_generator.py      # Validación y generación de llms.txt
│   └── generate_pdf_report.py    # Generador de reportes PDF (ReportLab)
├── schema/                       # Plantillas JSON-LD
│   ├── organization.json         # Esquema de Organización (con sameAs)
│   ├── local-business.json       # Esquema de Negocio Local (LocalBusiness)
│   ├── article-author.json       # Esquema de Artículo + Persona (E-E-A-T)
│   ├── software-saas.json        # Esquema de Aplicación de Software
│   ├── product-ecommerce.json    # Esquema de Producto con ofertas
│   └── website-searchaction.json # Esquema de Sitio Web + Acción de Búsqueda
├── install.sh                    # Instalador de un comando
├── uninstall.sh                  # Desinstalador
├── requirements.txt              # Dependencias de Python
└── README.md                     # Vista principal del proyecto
```

### Flujo de Auditoría Completa

Cuando ejecutas `/geo audit https://example.com`:

1. **Descubrimiento** — Obtiene la página de inicio, detecta el tipo de negocio, rastrea el mapa del sitio (sitemap)
2. **Análisis en Paralelo** — Lanza 5 subagentes simultáneamente:
   - Visibilidad de IA (citabilidad, rastreadores, llms.txt, menciones de marca)
   - Análisis de Plataforma (preparación para ChatGPT, Perplexity, Google AIO)
   - SEO Técnico (Core Web Vitals, SSR, seguridad, móvil)
   - Calidad de Contenido (E-E-A-T, legibilidad, frescura)
   - Marcado de Esquema (detección, validación, generación)
3. **Síntesis** — Agrega puntuaciones, genera Puntuación GEO compuesta (0-100)
4. **Reporte** — Produce un plan de acción priorizado con victorias rápidas (quick wins)

### Almacenamiento de Datos

Las habilidades de CRM y reportes (`/geo prospect`, `/geo proposal`, `/geo compare`) almacenan datos de tiempo de ejecución fuera del directorio de Claude Code:

```
~/.geo-prospects/
├── prospects.json              # Datos del pipeline de clientes/prospectos
├── proposals/                  # Documentos de propuestas generadas
│   └── <domain>-proposal-<date>.md
└── reports/                    # Reportes de diferencias mensuales
    └── <domain>-monthly-<YYYY-MM>.md
```

Este directorio **no se elimina** con el desinstalador — bórralo manualmente si ya no necesitas los datos de tus prospectos.
