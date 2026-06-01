#!/usr/bin/env python3
"""
Puntuador de Citabilidad — Analiza bloques de contenido para preparación de citas por IA.
Puntúa pasajes basado en qué tan probable es que los modelos de IA los citen.

Basado en investigaciones que muestran que los pasajes óptimos citados por IA son:
- de 134-167 palabras de largo
- Auto-contenidos (extraíbles sin contexto)
- Ricos en hechos con estadísticas específicas
- Estructurados con patrones de respuesta claros
"""

import sys
import json
import re
from typing import Optional

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: Paquetes requeridos no instalados. Ejecuta: pip install -r requirements.txt")
    sys.exit(1)


def score_passage(text: str, heading: Optional[str] = None) -> dict:
    """Puntúa un solo pasaje para citabilidad de IA (0-100)."""
    words = text.split()
    word_count = len(words)

    scores = {
        "answer_block_quality": 0,
        "self_containment": 0,
        "structural_readability": 0,
        "statistical_density": 0,
        "uniqueness_signals": 0,
    }

    # === 1. Calidad del Bloque de Respuesta (30%) ===
    abq_score = 0

    # Comprueba patrones de definición ("X es...", "X se refiere a...", "X significa...")
    definition_patterns = [
        r"\b\w+\s+is\s+(?:a|an|the)\s",
        r"\b\w+\s+refers?\s+to\s",
        r"\b\w+\s+means?\s",
        r"\b\w+\s+(?:can be |are )?defined\s+as\s",
        r"\bin\s+(?:simple|other)\s+(?:terms|words)\s*,",
    ]
    for pattern in definition_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            abq_score += 15
            break

    # Comprueba si la respuesta aparece temprano (primeras 60 palabras)
    first_60_words = " ".join(words[:60])
    if any(
        re.search(p, first_60_words, re.IGNORECASE)
        for p in [
            r"\b(?:is|are|was|were|means?|refers?)\b",
            r"\d+%",
            r"\$[\d,]+",
            r"\d+\s+(?:million|billion|thousand)",
        ]
    ):
        abq_score += 15

    # Bonus por encabezado basado en pregunta
    if heading and heading.endswith("?"):
        abq_score += 10

    # Estructura de oración clara y directa
    sentences = re.split(r"[.!?]+", text)
    short_clear_sentences = sum(
        1 for s in sentences if 5 <= len(s.split()) <= 25
    )
    if sentences:
        clarity_ratio = short_clear_sentences / len(sentences)
        abq_score += int(clarity_ratio * 10)

    # Tiene una afirmación específica y citable
    if re.search(
        r"(?:according to|research shows|studies? (?:show|indicate|suggest|found)|data (?:shows|indicates|suggests))",
        text,
        re.IGNORECASE,
    ):
        abq_score += 10

    scores["answer_block_quality"] = min(abq_score, 30)

    # === 2. Auto-contención (25%) ===
    sc_score = 0

    # Recuento de palabras óptimo (134-167 palabras)
    if 134 <= word_count <= 167:
        sc_score += 10
    elif 100 <= word_count <= 200:
        sc_score += 7
    elif 80 <= word_count <= 250:
        sc_score += 4
    elif word_count < 30 or word_count > 400:
        sc_score += 0
    else:
        sc_score += 2

    # Baja densidad de pronombres (menos pronombres = más auto-contenido)
    pronoun_count = len(
        re.findall(
            r"\b(?:it|they|them|their|this|that|these|those|he|she|his|her)\b",
            text,
            re.IGNORECASE,
        )
    )
    if word_count > 0:
        pronoun_ratio = pronoun_count / word_count
        if pronoun_ratio < 0.02:
            sc_score += 8
        elif pronoun_ratio < 0.04:
            sc_score += 5
        elif pronoun_ratio < 0.06:
            sc_score += 3

    # Contiene entidades nombradas (nombres propios, marcas, términos específicos)
    proper_nouns = len(re.findall(r"\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b", text))
    if proper_nouns >= 3:
        sc_score += 7
    elif proper_nouns >= 1:
        sc_score += 4

    scores["self_containment"] = min(sc_score, 25)

    # === 3. Legibilidad Estructural (20%) ===
    sr_score = 0

    # Distribución de conteo y longitud de oraciones
    if sentences:
        avg_sentence_length = word_count / len(sentences)
        if 10 <= avg_sentence_length <= 20:
            sr_score += 8
        elif 8 <= avg_sentence_length <= 25:
            sr_score += 5
        else:
            sr_score += 2

    # Contiene estructuras tipo lista
    if re.search(r"(?:first|second|third|finally|additionally|moreover|furthermore)", text, re.IGNORECASE):
        sr_score += 4

    # Contiene elementos numerados o contenido tipo viñeta
    if re.search(r"(?:\d+[\.\)]\s|\b(?:step|tip|point)\s+\d+)", text, re.IGNORECASE):
        sr_score += 4

    # Saltos de párrafo (indica estructura)
    if "\n" in text:
        sr_score += 4

    scores["structural_readability"] = min(sr_score, 20)

    # === 4. Densidad Estadística (15%) ===
    sd_score = 0

    # Porcentajes
    pct_count = len(re.findall(r"\d+(?:\.\d+)?%", text))
    sd_score += min(pct_count * 3, 6)

    # Cantidades en dólares
    dollar_count = len(re.findall(r"\$[\d,]+(?:\.\d+)?(?:\s*(?:million|billion|M|B|K))?", text))
    sd_score += min(dollar_count * 3, 5)

    # Otros números con contexto
    number_count = len(re.findall(r"\b\d+(?:,\d{3})*(?:\.\d+)?\s+(?:users|customers|pages|sites|companies|businesses|people|percent|times|x\b)", text, re.IGNORECASE))
    sd_score += min(number_count * 2, 4)

    # Referencias de años (indica actualidad)
    year_count = len(re.findall(r"\b20(?:2[3-6]|1\d)\b", text))
    if year_count > 0:
        sd_score += 2

    # Fuentes nombradas
    source_patterns = [
        r"(?:according to|per|from|by)\s+[A-Z]",
        r"(?:Gartner|Forrester|McKinsey|Harvard|Stanford|MIT|Google|Microsoft|OpenAI|Anthropic)",
        r"\([A-Z][a-z]+(?:\s+\d{4})?\)",
    ]
    for pattern in source_patterns:
        if re.search(pattern, text):
            sd_score += 2

    scores["statistical_density"] = min(sd_score, 15)

    # === 5. Señales de Unicidad (10%) ===
    us_score = 0

    # Indicadores de datos originales
    if re.search(
        r"(?:our (?:research|study|data|analysis|survey|findings)|we (?:found|discovered|analyzed|surveyed|measured))",
        text,
        re.IGNORECASE,
    ):
        us_score += 5

    # Indicadores de caso de estudio o ejemplo
    if re.search(
        r"(?:case study|for example|for instance|in practice|real-world|hands-on)",
        text,
        re.IGNORECASE,
    ):
        us_score += 3

    # Menciones específicas de herramientas/productos (muestra experiencia práctica)
    if re.search(r"(?:using|with|via|through)\s+[A-Z][a-z]+", text):
        us_score += 2

    scores["uniqueness_signals"] = min(us_score, 10)

    # === Calcular total ===
    total = sum(scores.values())

    # Determinar grado/calificación
    if total >= 80:
        grade = "A"
        label = "Altamente Citable"
    elif total >= 65:
        grade = "B"
        label = "Buena Citabilidad"
    elif total >= 50:
        grade = "C"
        label = "Citabilidad Moderada"
    elif total >= 35:
        grade = "D"
        label = "Baja Citabilidad"
    else:
        grade = "F"
        label = "Pobre Citabilidad"

    return {
        "heading": heading,
        "word_count": word_count,
        "total_score": total,
        "grade": grade,
        "label": label,
        "breakdown": scores,
        "preview": " ".join(words[:30]) + ("..." if word_count > 30 else ""),
    }


def analyze_page_citability(url: str) -> dict:
    """Analiza todos los bloques de contenido en una página para citabilidad."""
    try:
        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
            },
            timeout=30,
        )
        response.raise_for_status()
    except Exception as e:
        return {"error": f"Falló al obtener la página: {str(e)}"}

    soup = BeautifulSoup(response.text, "lxml")

    # Eliminar elementos que no son contenido
    for element in soup.find_all(
        ["script", "style", "nav", "footer", "header", "aside", "form"]
    ):
        element.decompose()

    # Extraer bloques de contenido
    blocks = []
    current_heading = "Introduction"
    current_paragraphs = []

    for element in soup.find_all(["h1", "h2", "h3", "h4", "p", "ul", "ol", "table"]):
        if element.name.startswith("h"):
            # Guardar sección anterior
            if current_paragraphs:
                combined = " ".join(current_paragraphs)
                if len(combined.split()) >= 20:
                    blocks.append(
                        {"heading": current_heading, "content": combined}
                    )
            current_heading = element.get_text(strip=True)
            current_paragraphs = []
        else:
            text = element.get_text(strip=True)
            if text and len(text.split()) >= 5:
                current_paragraphs.append(text)

    # Último bloque
    if current_paragraphs:
        combined = " ".join(current_paragraphs)
        if len(combined.split()) >= 20:
            blocks.append({"heading": current_heading, "content": combined})

    # Puntuar cada bloque
    scored_blocks = []
    for block in blocks:
        score = score_passage(block["content"], block["heading"])
        scored_blocks.append(score)

    # Calcular métricas a nivel de página
    if scored_blocks:
        avg_score = sum(b["total_score"] for b in scored_blocks) / len(scored_blocks)
        top_blocks = sorted(scored_blocks, key=lambda x: x["total_score"], reverse=True)[:5]
        bottom_blocks = sorted(scored_blocks, key=lambda x: x["total_score"])[:5]

        # Recuento óptimo de pasajes (134-167 palabras)
        optimal_count = sum(
            1 for b in scored_blocks if 134 <= b["word_count"] <= 167
        )
    else:
        avg_score = 0
        top_blocks = []
        bottom_blocks = []
        optimal_count = 0

    # Distribución de grados
    grade_dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for block in scored_blocks:
        grade_dist[block["grade"]] += 1

    return {
        "url": url,
        "total_blocks_analyzed": len(scored_blocks),
        "average_citability_score": round(avg_score, 1),
        "optimal_length_passages": optimal_count,
        "grade_distribution": grade_dist,
        "top_5_citable": top_blocks,
        "bottom_5_citable": bottom_blocks,
        "all_blocks": scored_blocks,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python citability_scorer.py <url>")
        print("Devuelve JSON con análisis de citabilidad para todos los bloques de contenido.")
        sys.exit(1)

    url = sys.argv[1]
    result = analyze_page_citability(url)
    print(json.dumps(result, indent=2, default=str))
