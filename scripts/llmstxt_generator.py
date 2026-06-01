#!/usr/bin/env python3
"""
Generador de llms.txt — Crea y valida archivos llms.txt para guiar a los rastreadores de IA.

El estándar llms.txt es una especificación emergente que ayuda a los rastreadores de IA a
entender la estructura de tu sitio y encontrar tu contenido más importante.

Ubicación: /llms.txt (raíz del dominio)
Extendido: /llms-full.txt (versión detallada)
"""

import sys
import json
import re
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: Paquetes requeridos no instalados. Ejecuta: pip install -r requirements.txt")
    sys.exit(1)

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def validate_llmstxt(url: str) -> dict:
    """Comprobar si llms.txt existe y validar su formato."""
    parsed = urlparse(url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    llms_url = f"{base_url}/llms.txt"
    llms_full_url = f"{base_url}/llms-full.txt"

    result = {
        "url": llms_url,
        "exists": False,
        "format_valid": False,
        "has_title": False,
        "has_description": False,
        "has_sections": False,
        "has_links": False,
        "section_count": 0,
        "link_count": 0,
        "content": "",
        "issues": [],
        "suggestions": [],
        "full_version": {
            "url": llms_full_url,
            "exists": False,
        },
    }

    # Comprobar llms.txt
    try:
        response = requests.get(llms_url, headers=DEFAULT_HEADERS, timeout=15)
        if response.status_code == 200:
            result["exists"] = True
            result["content"] = response.text
            content = response.text

            # Validar formato
            lines = content.strip().split("\n")

            # Comprobar si hay título (# al inicio)
            if lines and lines[0].startswith("# "):
                result["has_title"] = True
            else:
                result["issues"].append("Falta el título (debe comenzar con '# Nombre del Sitio')")

            # Comprobar si hay descripción (> blockquote)
            for line in lines:
                if line.startswith("> "):
                    result["has_description"] = True
                    break
            if not result["has_description"]:
                result["issues"].append("Falta la descripción (usa '> Breve descripción')")

            # Comprobar si hay secciones (## encabezados)
            sections = [l for l in lines if l.startswith("## ")]
            result["section_count"] = len(sections)
            result["has_sections"] = len(sections) > 0
            if not result["has_sections"]:
                result["issues"].append("No se encontraron secciones (usa '## Nombre de la Sección')")

            # Comprobar si hay enlaces
            link_pattern = r"- \[.+\]\(.+\)"
            links = re.findall(link_pattern, content)
            result["link_count"] = len(links)
            result["has_links"] = len(links) > 0
            if not result["has_links"]:
                result["issues"].append("No se encontraron enlaces de página (usa '- [Título de la Página](url): Descripción')")

            # Validez general del formato
            result["format_valid"] = (
                result["has_title"]
                and result["has_description"]
                and result["has_sections"]
                and result["has_links"]
            )

            # Sugerencias
            if result["link_count"] < 5:
                result["suggestions"].append("Considera añadir más páginas clave (apunta a 10-20)")
            if result["section_count"] < 2:
                result["suggestions"].append("Añade más secciones para organizar los tipos de contenido")
            if "contact" not in content.lower():
                result["suggestions"].append("Añade una sección de Contacto con correo y ubicación")
            if "key fact" not in content.lower() and "about" not in content.lower():
                result["suggestions"].append("Añade datos clave sobre tu negocio/servicio")

        else:
            result["issues"].append(f"llms.txt devolvió el estado {response.status_code}")
    except Exception as e:
        result["issues"].append(f"Error al obtener llms.txt: {str(e)}")

    # Comprobar llms-full.txt
    try:
        response = requests.get(llms_full_url, headers=DEFAULT_HEADERS, timeout=15)
        if response.status_code == 200:
            result["full_version"]["exists"] = True
    except Exception:
        pass

    return result


def generate_llmstxt(url: str, max_pages: int = 30) -> dict:
    """Generar un archivo llms.txt rastreando el sitio."""
    parsed = urlparse(url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"

    result = {
        "generated_llmstxt": "",
        "generated_llmstxt_full": "",
        "pages_analyzed": 0,
        "sections": {},
    }

    # Obtener página de inicio
    try:
        response = requests.get(url, headers=DEFAULT_HEADERS, timeout=30)
        soup = BeautifulSoup(response.text, "lxml")
    except Exception as e:
        result["error"] = f"Falló al obtener la página de inicio: {str(e)}"
        return result

    # Extraer nombre y descripción del sitio
    title = soup.find("title")
    site_name = title.get_text(strip=True).split("|")[0].split("-")[0].strip() if title else parsed.netloc
    meta_desc = soup.find("meta", attrs={"name": "description"})
    site_description = meta_desc.get("content", "") if meta_desc else f"Sitio web oficial de {site_name}"

    # Descubrir y categorizar páginas
    pages = {
        "Páginas Principales": [],
        "Productos y Servicios": [],
        "Recursos y Blog": [],
        "Compañía": [],
        "Soporte": [],
    }

    # Rastrear enlaces internos
    seen_urls = set()
    for link in soup.find_all("a", href=True):
        href = urljoin(base_url, link["href"])
        link_text = link.get_text(strip=True)

        if not link_text or len(link_text) < 2:
            continue

        parsed_href = urlparse(href)
        if parsed_href.netloc != parsed.netloc:
            continue
        if href in seen_urls:
            continue
        if any(ext in href for ext in [".pdf", ".jpg", ".png", ".gif", ".css", ".js"]):
            continue
        if "#" in href and href.split("#")[0] in seen_urls:
            continue

        seen_urls.add(href)
        path = parsed_href.path.lower()

        # Categorizar
        page_entry = {"url": href, "title": link_text}

        if any(kw in path for kw in ["/pricing", "/feature", "/product", "/solution", "/demo"]):
            pages["Productos y Servicios"].append(page_entry)
        elif any(kw in path for kw in ["/blog", "/article", "/resource", "/guide", "/learn", "/docs", "/documentation"]):
            pages["Recursos y Blog"].append(page_entry)
        elif any(kw in path for kw in ["/about", "/team", "/career", "/contact", "/press", "/partner"]):
            pages["Compañía"].append(page_entry)
        elif any(kw in path for kw in ["/help", "/support", "/faq", "/status"]):
            pages["Soporte"].append(page_entry)
        elif path in ["/", ""] or any(kw in path for kw in ["/home", "/index"]):
            if href != base_url and href != base_url + "/":
                pages["Páginas Principales"].append(page_entry)
        else:
            pages["Páginas Principales"].append(page_entry)

        if len(seen_urls) >= max_pages:
            break

    result["pages_analyzed"] = len(seen_urls)

    # Generar llms.txt (versión concisa)
    llms_lines = [
        f"# {site_name}",
        f"> {site_description}",
        "",
    ]

    for section, section_pages in pages.items():
        if section_pages:
            llms_lines.append(f"## {section}")
            # Limitar a los 10 primeros por sección para la versión concisa
            for page in section_pages[:10]:
                llms_lines.append(f"- [{page['title']}]({page['url']})")
            llms_lines.append("")

    # Añadir marcador de posición para la sección de contacto
    llms_lines.extend([
        "## Contacto",
        f"- Sitio web: {base_url}",
        f"- Correo: contact@{parsed.netloc}",
        "",
    ])

    result["generated_llmstxt"] = "\n".join(llms_lines)

    # Generar llms-full.txt (versión detallada con descripciones)
    full_lines = [
        f"# {site_name}",
        f"> {site_description}",
        "",
    ]

    for section, section_pages in pages.items():
        if section_pages:
            full_lines.append(f"## {section}")
            for page in section_pages:
                # Omitir URLs de origen cruzado para prevenir SSRF a través de cadenas de redirección
                if urlparse(page["url"]).netloc != parsed.netloc:
                    full_lines.append(f"- [{page['title']}]({page['url']})")
                    continue

                # Intentar obtener la descripción de la página
                try:
                    page_resp = requests.get(page["url"], headers=DEFAULT_HEADERS, timeout=10)
                    page_soup = BeautifulSoup(page_resp.text, "lxml")
                    page_meta = page_soup.find("meta", attrs={"name": "description"})
                    page_desc = page_meta.get("content", "") if page_meta else ""
                    if page_desc:
                        full_lines.append(f"- [{page['title']}]({page['url']}): {page_desc}")
                    else:
                        full_lines.append(f"- [{page['title']}]({page['url']})")
                except Exception:
                    full_lines.append(f"- [{page['title']}]({page['url']})")
            full_lines.append("")

    full_lines.extend([
        "## Contacto",
        f"- Sitio web: {base_url}",
        f"- Correo: contact@{parsed.netloc}",
        "",
    ])

    result["generated_llmstxt_full"] = "\n".join(full_lines)
    result["sections"] = {k: len(v) for k, v in pages.items()}

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python llmstxt_generator.py <url> [modo]")
        print("Modos: validate (por defecto), generate")
        sys.exit(1)

    target_url = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "validate"

    if mode == "validate":
        data = validate_llmstxt(target_url)
    elif mode == "generate":
        data = generate_llmstxt(target_url)
    else:
        print(f"Modo desconocido: {mode}. Usa 'validate' o 'generate'.")
        sys.exit(1)

    print(json.dumps(data, indent=2, default=str))
