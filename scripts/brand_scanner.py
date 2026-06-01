#!/usr/bin/env python3
"""
Brand Mention Scanner — Verifica la presencia de la marca en plataformas citadas por la IA.

Las menciones de marca tienen una correlación 3 veces mayor con la visibilidad en IA que los backlinks.
(Estudio de Ahrefs de diciembre de 2025 sobre 75,000 marcas)

Importancia de la plataforma para las citas de la IA:
1. Menciones en YouTube (correlación ~0.737 - LA MÁS FUERTE)
2. Menciones en Reddit (alta)
3. Presencia en Wikipedia (alta)
4. Presencia en LinkedIn (moderada)
5. Calificación del Dominio/backlinks (~0.266 - débil)
"""

import sys
import json
import re
from urllib.parse import quote_plus

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: Paquetes requeridos no instalados. Ejecuta: pip install -r requirements.txt")
    sys.exit(1)

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def check_youtube_presence(brand_name: str) -> dict:
    """Verifica la presencia de la marca en YouTube."""
    result = {
        "platform": "YouTube",
        "correlation": 0.737,
        "weight": "25%",
        "has_channel": False,
        "mentioned_in_videos": False,
        "search_url": f"https://www.youtube.com/results?search_query={quote_plus(brand_name)}",
        "recommendations": [],
    }

    # Nota: Se usaría la API real de YouTube en producción
    # Esto proporciona el marco de trabajo para que Claude Code use WebFetch
    result["check_instructions"] = [
        f"Busca en YouTube '{brand_name}' y verifica:",
        "1. ¿Tiene la marca un canal oficial de YouTube?",
        "2. ¿Hay videos DE la marca (tutoriales, demos, liderazgo de pensamiento)?",
        "3. ¿Hay videos SOBRE la marca de otros creadores?",
        "4. ¿Cuál es el número de vistas de los videos relacionados con la marca?",
        "5. ¿Existen reseñas o demostraciones positivas?",
    ]

    result["recommendations"] = [
        "Crea un canal de YouTube si no existe ninguno",
        "Publica contenido educativo/tutorial relacionado con tu nicho",
        "Anima a los clientes a crear videos de reseñas/demostraciones",
        "Optimiza los títulos y descripciones de los videos con el nombre de la marca",
        "Añade marcas de tiempo y capítulos para mejorar el parseo por parte de la IA",
        "Incluye transcripciones (YouTube las auto-genera, pero revisa su precisión)",
    ]

    return result


def check_reddit_presence(brand_name: str) -> dict:
    """Verifica la presencia de la marca en Reddit."""
    result = {
        "platform": "Reddit",
        "correlation": "Alta",
        "weight": "25%",
        "has_subreddit": False,
        "mentioned_in_discussions": False,
        "search_url": f"https://www.reddit.com/search/?q={quote_plus(brand_name)}",
        "recommendations": [],
    }

    result["check_instructions"] = [
        f"Busca en Reddit '{brand_name}' y verifica:",
        "1. ¿Tiene la marca su propio subreddit (r/nombremarca)?",
        "2. ¿Se discute sobre la marca en subreddits relevantes de la industria?",
        "3. ¿Cuál es el sentimiento (positivo, negativo, neutral)?",
        "4. ¿Existen hilos de recomendaciones mencionando la marca?",
        "5. ¿Tiene la marca una presencia oficial en Reddit?",
        "6. ¿Las menciones son recientes (dentro de los últimos 6 meses)?",
    ]

    result["recommendations"] = [
        "Monitorea subreddits relevantes en busca de menciones de marca",
        "Participa auténticamente en discusiones de la industria (no spam)",
        "Crea una cuenta oficial de Reddit para soporte al cliente",
        "Comparte contenido valioso (no solo auto-promoción)",
        "Responde preguntas sobre la categoría de tu producto/servicio",
        "La autenticidad de Reddit importa — no uses lenguaje de marketing",
    ]

    return result


def check_wikipedia_presence(brand_name: str) -> dict:
    """Verifica la presencia de la marca/entidad en Wikipedia y Wikidata."""
    result = {
        "platform": "Wikipedia",
        "correlation": "Alta",
        "weight": "20%",
        "has_wikipedia_page": False,
        "has_wikidata_entry": False,
        "cited_in_articles": False,
        "search_url": f"https://es.wikipedia.org/wiki/Special:Search?search={quote_plus(brand_name)}",
        "wikidata_url": f"https://www.wikidata.org/w/index.php?search={quote_plus(brand_name)}",
        "recommendations": [],
    }

    # Revisar API de Wikipedia
    try:
        api_url = f"https://es.wikipedia.org/w/api.php?action=query&list=search&srsearch={quote_plus(brand_name)}&format=json"
        response = requests.get(api_url, headers=DEFAULT_HEADERS, timeout=15)
        if response.status_code == 200:
            data = response.json()
            search_results = data.get("query", {}).get("search", [])
            if search_results:
                # Comprobar si el resultado principal trata sobre la marca
                top_title = search_results[0].get("title", "").lower()
                if brand_name.lower() in top_title:
                    result["has_wikipedia_page"] = True
                result["wikipedia_search_results"] = len(search_results)
    except Exception:
        pass

    # Revisar Wikidata
    try:
        wikidata_url = f"https://www.wikidata.org/w/api.php?action=wbsearchentities&search={quote_plus(brand_name)}&language=es&format=json"
        response = requests.get(wikidata_url, headers=DEFAULT_HEADERS, timeout=15)
        if response.status_code == 200:
            data = response.json()
            entities = data.get("search", [])
            if entities:
                result["has_wikidata_entry"] = True
                result["wikidata_id"] = entities[0].get("id", "")
                result["wikidata_description"] = entities[0].get("description", "")
    except Exception:
        pass

    result["recommendations"] = [
        "Si es elegible, crea un artículo en Wikipedia (requiere criterios de relevancia)",
        "Asegúrate de que la entrada en Wikidata exista con datos estructurados completos",
        "Añade enlaces sameAs en el marcado de esquema (schema markup) apuntando a Wikipedia/Wikidata",
        "Haz que te citen en artículos existentes de Wikipedia como fuente",
        "Construye relevancia a través de la cobertura de prensa y reseñas independientes",
        "Nota: Wikipedia tiene estrictas directrices de relevancia — la cobertura de PR ayuda a establecerla",
    ]

    return result


def check_linkedin_presence(brand_name: str) -> dict:
    """Verifica la presencia de la marca en LinkedIn."""
    result = {
        "platform": "LinkedIn",
        "correlation": "Moderada",
        "weight": "15%",
        "has_company_page": False,
        "employee_thought_leadership": False,
        "search_url": f"https://www.linkedin.com/search/results/companies/?keywords={quote_plus(brand_name)}",
        "recommendations": [],
    }

    result["check_instructions"] = [
        f"Busca en LinkedIn '{brand_name}' y verifica:",
        "1. ¿Tiene la empresa una página en LinkedIn?",
        "2. ¿Cuántos seguidores tiene?",
        "3. ¿Está la página activa con publicaciones recientes?",
        "4. ¿Publican los empleados contenido de liderazgo intelectual?",
        "5. ¿Hay artículos en LinkedIn sobre la marca?",
        "6. ¿Existe interacción (engagement) en las publicaciones (me gusta, comentarios, compartidos)?",
    ]

    result["recommendations"] = [
        "Crea/optimiza la página de empresa en LinkedIn",
        "Publica regularmente contenido de liderazgo de pensamiento",
        "Anima a los empleados a compartir el contenido de la empresa",
        "Publica artículos de formato largo en LinkedIn",
        "Participa en las discusiones y comentarios de la industria",
        "Añade la URL de LinkedIn de la empresa en la propiedad sameAs del schema",
    ]

    return result


def check_other_platforms(brand_name: str) -> dict:
    """Verifica la presencia de la marca en plataformas adicionales."""
    result = {
        "platform": "Otras Plataformas",
        "weight": "15%",
        "platforms_checked": {},
        "recommendations": [],
    }

    platforms = {
        "Quora": f"https://es.quora.com/search?q={quote_plus(brand_name)}",
        "Stack Overflow": f"https://es.stackoverflow.com/search?q={quote_plus(brand_name)}",
        "GitHub": f"https://github.com/search?q={quote_plus(brand_name)}",
        "Crunchbase": f"https://www.crunchbase.com/textsearch?q={quote_plus(brand_name)}",
        "Product Hunt": f"https://www.producthunt.com/search?q={quote_plus(brand_name)}",
        "G2": f"https://www.g2.com/search?utf8=&query={quote_plus(brand_name)}",
        "Trustpilot": f"https://es.trustpilot.com/search?query={quote_plus(brand_name)}",
    }

    result["platforms_checked"] = {
        name: {
            "search_url": url,
            "check_instruction": f"Busca '{brand_name}' en {name}",
        }
        for name, url in platforms.items()
    }

    result["recommendations"] = [
        "Mantén perfiles en plataformas relevantes para tu industria",
        "Responde preguntas en Quora y Stack Overflow",
        "Fomenta las reseñas de clientes en G2 y Trustpilot",
        "Mantén actualizado el perfil de Crunchbase (importante para B2B)",
        "Las contribuciones de código abierto en GitHub aumentan la autoridad de la marca desarrolladora",
        "Un lanzamiento en Product Hunt puede generar un gran revuelo (buzz) inicial",
    ]

    return result


def generate_brand_report(brand_name: str, domain: str = None) -> dict:
    """Genera un reporte integral de menciones de marca."""
    report = {
        "brand_name": brand_name,
        "domain": domain,
        "analysis_date": "Generado por la Herramienta GEO-SEO Claude",
        "key_insight": "Las menciones de marca correlacionan 3 veces más fuerte con la visibilidad en IA que los backlinks (Ahrefs Dic 2025, 75K marcas)",
        "platforms": {},
        "overall_recommendations": [],
    }

    # Revisar todas las plataformas
    report["platforms"]["youtube"] = check_youtube_presence(brand_name)
    report["platforms"]["reddit"] = check_reddit_presence(brand_name)
    report["platforms"]["wikipedia"] = check_wikipedia_presence(brand_name)
    report["platforms"]["linkedin"] = check_linkedin_presence(brand_name)
    report["platforms"]["other"] = check_other_platforms(brand_name)

    # Recomendaciones generales
    report["overall_recommendations"] = [
        "Prioridad 1: YouTube — mayor correlación (0.737) con citas en IA. Crea contenido educativo.",
        "Prioridad 2: Reddit — construye una presencia auténtica en subreddits de la industria. Sin lenguaje de marketing.",
        "Prioridad 3: Wikipedia — establece relevancia a través de la cobertura de prensa, luego crea/mejora la entrada.",
        "Prioridad 4: LinkedIn — contenido de liderazgo de pensamiento por parte de los fundadores y empleados.",
        "Prioridad 5: Plataformas de reseñas — G2, Trustpilot, Capterra para señales de prueba social.",
        "Múltiples plataformas: Asegura un NAP consistente (Nombre, Dirección, Teléfono) en todas las plataformas.",
        "Marcado de schema: Añade la propiedad sameAs enlazando a TODAS las plataformas o perfiles.",
        "Monitoreo: Configura alertas de menciones de marca en todas las plataformas.",
    ]

    return report


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python brand_scanner.py <nombre_marca> [dominio]")
        print("Ejemplo: python brand_scanner.py 'Acme Corp' acmecorp.com")
        sys.exit(1)

    brand = sys.argv[1]
    domain = sys.argv[2] if len(sys.argv) > 2 else None

    result = generate_brand_report(brand, domain)
    print(json.dumps(result, indent=2, default=str))
