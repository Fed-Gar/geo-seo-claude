# Guía de Inicio

## Requisitos Previos

| Requisito | Por qué es necesario |
|---|---|
| Python 3.8+ | Ejecuta los scripts de utilidad (obtención de páginas, puntuación de citabilidad, generación de PDF, etc.) |
| Claude Code CLI | Las habilidades y agentes se cargan y se invocan a través de Claude Code |
| Git | Utilizado por el instalador para clonar el repositorio |
| Playwright (opcional) | Permite la captura de pantallas; se instala por separado después de la instalación principal |

Instala Claude Code si aún no lo has hecho:

```bash
npm install -g @anthropic-ai/claude-code
```

---

## Instalación

### Mac / Linux (Recomendado)

La forma más fácil es usando nuestro script de instalación de una sola línea:

```bash
curl -fsSL https://raw.githubusercontent.com/joanby/geo-seo-claude/main/install.sh | bash
```

O si prefieres clonarlo manualmente:

```bash
git clone https://github.com/joanby/geo-seo-claude.git
cd geo-seo-claude
./install.sh
```

### Windows (PowerShell o Git Bash)

Usa el instalador de Windows:

```bash
curl -fsSL https://raw.githubusercontent.com/joanby/geo-seo-claude/main/install-win.sh | bash
```
O manual:
```bash
git clone https://github.com/joanby/geo-seo-claude.git
cd geo-seo-claude
./install-win.sh
```

Haz clic derecho en la carpeta clonada y elige "Open Git Bash here", o navega hasta ella dentro de una sesión existente de Git Bash.

### Qué hace el instalador

- Copia la habilidad orquestadora `geo` a `~/.claude/skills/geo/`
- Copia 13 subhabilidades a `~/.claude/skills/geo-*/`
- Copia 5 definiciones de subagentes a `~/.claude/agents/`
- Instala las dependencias de Python vía `pip install --user`
- Opcionalmente instala el navegador Chromium de Playwright para capturas de pantalla

---

## Verificar la Instalación

Después de la instalación, abre Claude Code en cualquier directorio de proyecto y ejecuta:

```
/geo quick https://example.com
```

Si la habilidad está conectada correctamente, Claude Code iniciará una instantánea de visibilidad GEO de 60 segundos. Si ves "comando desconocido" o no sucede nada, reinicia Claude Code — este lee las habilidades y agentes al inicio.

Para confirmar que los archivos llegaron al lugar correcto:

```bash
ls ~/.claude/skills/geo/
ls ~/.claude/skills/ | grep geo
ls ~/.claude/agents/ | grep geo
```

---

## Tu Primera Auditoría

### Ruta rápida — Instantánea de 60 segundos

```
/geo quick https://tusitio.com
```

Devuelve una puntuación de visibilidad GEO de alto nivel y los principales problemas. Ideal para un primer vistazo o una revisión rápida del cliente.

### Ruta completa — Auditoría completa

```
/geo audit https://tusitio.com
```

Lanza 5 subagentes en paralelo cubriendo visibilidad de IA, optimización de plataforma, SEO técnico, calidad del contenido y datos estructurados. Produce un plan de acción priorizado con una puntuación GEO compuesta (0–100).

La auditoría completa tarda varios minutos dependiendo del sitio. Consulta [scoring-methodology.md](scoring-methodology.md) para ver cómo se calcula la puntuación y [commands-reference.md](commands-reference.md) para todos los comandos disponibles.

---

## Solución de Problemas

**Python no se encontró durante la instalación**
- Síntoma: el instalador se cierra con `Python 3.8+ is required but not found`
- Causa: Python no está instalado o no está en el `PATH`
- Solución: instálalo desde [python.org](https://www.python.org/downloads/); en Windows asegúrate de marcar "Add Python to PATH" durante la configuración; luego vuelve a abrir tu terminal

**Claude Code CLI no se encontró**
- Síntoma: el instalador advierte `Claude Code CLI not found in PATH`
- Causa: `claude` no está instalado o no está en el `PATH`
- Solución: `npm install -g @anthropic-ai/claude-code`; confirma con `claude --version`

**Las habilidades no aparecen en Claude Code**
- Síntoma: `/geo quick` produce "comando desconocido" o no hay respuesta
- Causa: Claude Code lee las habilidades al iniciar; no verá los archivos añadidos después de abrirse
- Solución: cierra por completo y vuelve a abrir Claude Code

**Permiso denegado en `./install.sh`**
- Síntoma: `bash: ./install.sh: Permission denied`
- Causa: el bit de ejecución no está configurado
- Solución: `chmod +x install.sh && ./install.sh`

**Terminal incorrecto en Windows**
- Síntoma: `curl` no reconocido, o errores de sintaxis en el script
- Causa: ejecutando `install-win.sh` en PowerShell o el Símbolo del sistema
- Solución: usa solo Git Bash — haz clic derecho en la carpeta, "Open Git Bash here"

**Playwright no disponible / capturas de pantalla faltantes**
- Síntoma: los pasos relacionados con capturas de pantalla se saltan silenciosamente o dan error
- Causa: Playwright se omitió durante la instalación (no interactiva o se respondió no)
- Solución: instálalo manualmente:
  ```bash
  python3 -m playwright install chromium
  ```

**Las dependencias de Python fallaron durante la instalación**
- Síntoma: el instalador imprime `Some Python dependencies failed to install`
- Causa: error de pip (red, permisos o conflicto de entorno virtual)
- Solución: ejecuta manualmente desde el repositorio clonado o desde `~/.claude/skills/geo/`:
  ```bash
  python3 -m pip install --user -r requirements.txt
  ```

---

## Desinstalar

### Con script

Ejecuta desde el directorio del repositorio clonado:

```bash
./uninstall.sh
```

Esto elimina `~/.claude/skills/geo/`, todas las subhabilidades `~/.claude/skills/geo-*/`, y todos los archivos de agentes `~/.claude/agents/geo-*.md`. Los paquetes de Python no se eliminan.

### Manual

```bash
rm -rf ~/.claude/skills/geo ~/.claude/skills/geo-* ~/.claude/agents/geo-*.md
```

### Datos de tiempo de ejecución

El directorio `~/.geo-prospects/` (utilizado por `/geo prospect`, `/geo proposal` y `/geo compare`) **no** es eliminado por el desinstalador. Bórralo manualmente si ya no necesitas los datos:

```bash
rm -rf ~/.geo-prospects
```

---

Ver también: [architecture.md](architecture.md) | [commands-reference.md](commands-reference.md) | [scoring-methodology.md](scoring-methodology.md) | [skills-and-agents.md](skills-and-agents.md)
