---
name: geo-update
description: Obtiene las últimas actualizaciones de la habilidad GEO-SEO desde el repositorio principal (upstream). Compara los archivos instalados con la última versión, muestra qué cambió, y actualiza todas las habilidades, agentes, scripts y plantillas de esquema en el lugar.
allowed-tools:
  - Bash
  - Read
  - Write
---

# Habilidad de Actualización GEO-SEO

## Propósito

Actualiza las habilidades, agentes, scripts y plantillas de esquema GEO-SEO instalados localmente a la última versión del repositorio original (upstream). Muestra un resumen de qué cambió antes y después de la actualización.

---

## Flujo de Trabajo de Actualización

### Paso 1: Determinar Ubicación de Instalación

El conjunto de herramientas GEO-SEO se instala en estas ubicaciones bajo `~/.claude/`:

| Componente | Ruta de Instalación |
|-----------|-------------|
| Habilidad principal | `~/.claude/skills/geo/` |
| Sub-habilidades | `~/.claude/skills/geo-*/` |
| Agentes | `~/.claude/agents/geo-*.md` |
| Scripts | `~/.claude/skills/geo/scripts/` |
| Plantillas de esquema | `~/.claude/skills/geo/schema/` |
| Hooks (Ganchos) | `~/.claude/skills/geo/hooks/` |

Verifica que la instalación existe buscando `~/.claude/skills/geo/SKILL.md`. Si no existe, informa al usuario que GEO-SEO no está instalado y sugiere ejecutar el instalador en su lugar.

### Paso 2: Clonar Última Versión desde Upstream

```bash
TEMP_DIR=$(mktemp -d)
git clone --depth 1 https://github.com/joanby/geo-seo-claude.git "$TEMP_DIR/repo"
```

Si la clonación falla, reporta el error y detente. No modifiques ningún archivo instalado.

### Paso 3: Comparar Instalación Local vs Última Versión

Antes de copiar archivos, genera un resumen de diferencias (diff) para que el usuario sepa qué cambiará:

1. Para cada directorio de componente, compara los archivos instalados contra los archivos clonados usando `diff --recursive --brief`.
2. Categoriza los cambios como:
   - **Archivos nuevos** — existen en upstream pero no localmente
   - **Archivos modificados** — existen en ambos pero difieren
   - **Archivos eliminados** — existen localmente pero no en upstream (estos NO se eliminan automáticamente)
3. Presenta el resumen al usuario.

### Paso 4: Aplicar Actualizaciones

Copia archivos desde el repositorio clonado sobre las ubicaciones de instalación:

```bash
CLAUDE_DIR="${HOME}/.claude"
SOURCE_DIR="$TEMP_DIR/repo"

# Habilidad principal
cp -r "$SOURCE_DIR/geo/"* "$CLAUDE_DIR/skills/geo/"

# Sub-habilidades
for skill_dir in "$SOURCE_DIR/skills"/*/; do
    skill_name=$(basename "$skill_dir")
    mkdir -p "$CLAUDE_DIR/skills/${skill_name}"
    cp -r "$skill_dir"* "$CLAUDE_DIR/skills/${skill_name}/"
done

# Agentes
for agent_file in "$SOURCE_DIR/agents/"*.md; do
    cp "$agent_file" "$CLAUDE_DIR/agents/"
done

# Scripts
if [ -d "$SOURCE_DIR/scripts" ]; then
    cp -r "$SOURCE_DIR/scripts/"* "$CLAUDE_DIR/skills/geo/scripts/"
    chmod +x "$CLAUDE_DIR/skills/geo/scripts/"*.py 2>/dev/null || true
fi

# Plantillas de esquema
if [ -d "$SOURCE_DIR/schema" ]; then
    cp -r "$SOURCE_DIR/schema/"* "$CLAUDE_DIR/skills/geo/schema/"
fi

# Hooks
if [ -d "$SOURCE_DIR/hooks" ] && [ "$(ls -A "$SOURCE_DIR/hooks" 2>/dev/null)" ]; then
    mkdir -p "$CLAUDE_DIR/skills/geo/hooks"
    cp -r "$SOURCE_DIR/hooks/"* "$CLAUDE_DIR/skills/geo/hooks/"
    chmod +x "$CLAUDE_DIR/skills/geo/hooks/"* 2>/dev/null || true
fi
```

### Paso 5: Actualizar Dependencias Python

Si `requirements.txt` existe en el repo upstream y difiere de la versión instalada:

```bash
python3 -m pip install -r "$SOURCE_DIR/requirements.txt" --quiet
```

Reporta cualquier falla pero no la trates como fatal.

### Paso 6: Limpieza

```bash
rm -rf "$TEMP_DIR"
```

### Paso 7: Reportar Resultados

Presenta un resumen:

```
Actualización de GEO-SEO Completada
=======================
Archivos nuevos:      [cantidad]
Archivos modificados: [cantidad]
Sin cambios:          [cantidad]
Eliminados en upstream (mantenidos localmente): [cantidad]

Dependencias: [actualizadas / sin cambios / fallidas]
```

Si hubo archivos eliminados en upstream, enúmeralos y sugiere que el usuario revise si debe eliminarlos manualmente.

---

## Notas Importantes

- **Nunca elimines archivos instalados localmente** que ya no existan en el upstream. El usuario puede haberlos personalizado. Enúmeralos y deja que el usuario decida.
- **Nunca modifiques `~/.claude/settings.json` ni `~/.claude/settings.local.json`** — estos son archivos de configuración del usuario, no parte del conjunto de herramientas GEO-SEO.
- **Si ya está actualizado** (sin diferencias), repórtalo y omite el paso de copiado.
- **Aviso de reinicio:** Recuerda al usuario que los cambios de habilidades surten efecto en nuevas sesiones de Claude Code. Deberían reiniciar su sesión para usar las habilidades actualizadas.
