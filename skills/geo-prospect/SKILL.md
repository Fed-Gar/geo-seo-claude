---
name: geo-prospect
description: >
  CRM ligero para gestionar prospectos y clientes de agencia GEO. Rastrea leads a través
  del flujo completo de ventas: Lead → Calificado → Propuesta Enviada → Ganado → Perdido.
  Almacena historial de auditorías, notas, valores de los tratos y genera resúmenes del embudo de ventas.
  Usar cuando el usuario diga "prospect", "lead", "client", "pipeline", "crm", "nuovo prospect",
  "aggiungi cliente", o cuando administre el lado comercial de los servicios GEO.
version: 1.0.0
tags: [geo, business, crm, prospect, pipeline, sales]
allowed-tools: Read, Write, Bash, Glob
---

# Gestor de Prospectos GEO

## Propósito

Gestionar los prospectos y clientes de una agencia GEO a través del ciclo completo de ventas.
Todos los datos se almacenan en `~/.geo-prospects/prospects.json` (persiste entre sesiones).

---

## Comandos

| Comando | Qué Hace |
|---------|-------------|
| `/geo prospect new <domain>` | Crear nuevo prospecto (indicaciones interactivas) |
| `/geo prospect list` | Mostrar todos los prospectos con estado en el pipeline |
| `/geo prospect list <status>` | Filtrar: lead, qualified, proposal, won, lost |
| `/geo prospect show <id-or-domain>` | Detalle completo del prospecto con historial |
| `/geo prospect audit <id-or-domain>` | Ejecutar auditoría GEO rápida y guardar en registro del prospecto |
| `/geo prospect note <id-or-domain> "<text>"` | Añadir nota de interacción con marca de tiempo |
| `/geo prospect status <id-or-domain> <new-status>` | Mover a través del pipeline |
| `/geo prospect won <id-or-domain> <monthly-value>` | Marcar como ganado, establecer valor de contrato |
| `/geo prospect lost <id-or-domain> "<reason>"` | Marcar como perdido con motivo |
| `/geo prospect pipeline` | Resumen visual del pipeline con previsión de ingresos |

---

## Estructura de Datos

Cada prospecto se almacena como un registro JSON:

```json
{
  "id": "PRO-001",
  "company": "Electron Srl",
  "domain": "electron-srl.com",
  "contact_email": "info@electron-srl.com",
  "contact_name": "",
  "industry": "Educational Equipment Manufacturing",
  "country": "Italy",
  "status": "qualified",
  "geo_score": 32,
  "audit_date": "2026-03-12",
  "audit_file": "~/.geo-prospects/audits/electron-srl.com-2026-03-12.md",
  "proposal_file": "~/.geo-prospects/proposals/electron-srl.com-proposal.md",
  "monthly_value": 0,
  "contract_start": null,
  "contract_months": 0,
  "notes": [
    {
      "date": "2026-03-12",
      "text": "Escaneo rápido inicial GEO. Puntuación 32/100 - Nivel crítico. Fuerte candidato para servicios GEO."
    }
  ],
  "created_at": "2026-03-12",
  "updated_at": "2026-03-12"
}
```

---

## Instrucciones de Orquestación

### `/geo prospect new <domain>`

1. Verifica si `~/.geo-prospects/prospects.json` existe, crea uno si no (array vacío)
2. Autodetecta el nombre de la empresa a partir del dominio (ej., `electron-srl.com` → `Electron Srl`)
3. Asigna siguiente ID secuencial: `PRO-001`, `PRO-002`, etc.
4. Pide al usuario:
   - Nombre del contacto (opcional)
   - Correo electrónico del contacto
   - Estimación de valor mensual del contrato (opcional)
5. Establece estado (status) en `lead`
6. Guarda en archivo JSON
7. Sugiere siguiente paso: "Ejecuta `/geo prospect audit electron-srl.com` para puntuar a este prospecto"

### `/geo prospect list`

Lee `~/.geo-prospects/prospects.json` y renderiza una tabla resumen:

```
Pipeline de Prospectos GEO — Marzo 2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ID       Dominio                 Empresa           Estado      Puntaje  Valor
───────  ──────────────────────  ────────────────  ──────────  ─────  ──────
PRO-001  electron-srl.com        Electron Srl      Qualified   32/100  €4.5K
PRO-002  acme.com                ACME Corp         Lead        —       —
PRO-003  bigshop.it              BigShop           Won         41/100  €6.0K

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pipeline: 1 lead | 1 calificado | 0 propuestas | 1 ganado | 0 perdidos
MRR (Ingresos Recurrentes) Comprometidos: €6,000 | Valor en Pipeline: €4,500
```

### `/geo prospect audit <id-or-domain>`

1. Ejecuta `/geo quick <domain>` para obtener instantánea de la puntuación GEO
2. Guarda la puntuación en el registro del prospecto: `geo_score`, `audit_date`
3. Guarda la salida de la auditoría en `~/.geo-prospects/audits/<domain>-<date>.md`
4. Actualiza la ruta `audit_file` en el registro del prospecto
5. Añade nota automática: "Auditoría rápida ejecutada. Puntuación GEO: XX/100."
6. Si la puntuación es < 55: sugiere "La puntuación indica fuerte oportunidad de venta. Ejecuta `/geo proposal <domain>` para generar propuesta."

### `/geo prospect note <id-or-domain> "<text>"`

1. Encuentra prospecto por ID o dominio
2. Añade nota con la fecha ISO actual
3. Guarda de vuelta en JSON
4. Confirma: "Nota añadida a Electron Srl (PRO-001)"

### `/geo prospect status <id-or-domain> <status>`

Estados válidos: `lead`, `qualified`, `proposal`, `won`, `lost`

1. Actualiza el campo status
2. Añade nota automática: "Estado cambiado a <status>"
3. Guarda y confirma

### `/geo prospect pipeline`

Resumen visual del pipeline enfocado en ingresos:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESUMEN DEL PIPELINE AGENCIA GEO — Marzo 2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ETAPA          CANT.   VALOR POTENCIAL   NOTAS
─────────────  ─────   ───────────────   ─────────────────────
Lead             2      €8,000/mes       Nuevos descubrimientos
Calificado       1      €4,500/mes       Listo para propuesta
Prop. Enviada    1      €6,000/mes       A la espera de firma
Ganado           3      €18,500/mes      Clientes activos (MRR)
Perdido          1      —                Congelación presupuesto

MRR COMPROMETIDO:        €18,500
PIPELINE (calificado+):  €10,500
POTENCIAL TOTAL:         €29,000/mes → €348,000/año

Próximas acciones:
→ PRO-003 (acme.com): Enviar propuesta — puntuación 38/100 (caso fuerte)
→ PRO-007 (shop.it): Seguimiento — propuesta enviada hace 8 días
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Ubicación de Almacenamiento

Todos los datos se guardan en `~/.geo-prospects/`:
```
~/.geo-prospects/
├── prospects.json          # Base de datos CRM principal
├── audits/                 # Instantáneas de auditorías rápidas
│   └── electron-srl.com-2026-03-12.md
└── proposals/              # Propuestas generadas
    └── electron-srl.com-proposal.md
```

Crea el directorio si no existe: `mkdir -p ~/.geo-prospects/audits ~/.geo-prospects/proposals`

---

## Definiciones de Etapas del Pipeline

| Estado | Significado | Acción Siguiente Típica |
|--------|---------|---------------------|
| `lead` | Descubierto, aún no contactado | Ejecutar auditoría rápida, evaluar oportunidad |
| `qualified` | Auditoría hecha, confirmación de puntos de dolor | Generar propuesta |
| `proposal` | Propuesta enviada, a la espera de decisión | Hacer seguimiento, responder dudas |
| `won` | Contrato firmado, cliente activo | Ejecutar auditoría completa, inicio onboarding |
| `lost` | Trato cerrado perdido | Registrar motivo para futura referencia |

---

## Salida

- Todos los comandos imprimen confirmación + estado actual del prospecto en la terminal
- No generar archivos externos a menos que se guarden explícitamente auditorías/propuestas
- La base de datos JSON es la única fuente de verdad
