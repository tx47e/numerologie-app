from __future__ import annotations

import argparse
import html
import json
import re
import unicodedata
import subprocess
import sys
from datetime import datetime
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
APP_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = APP_DIR / "output"
PYTHON = Path(sys.executable)


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFD", value.strip().lower())
    value = "".join(ch for ch in normalized if unicodedata.category(ch) != "Mn")
    value = re.sub(r"[^a-z0-9]+", "-", value, flags=re.IGNORECASE)
    value = value.strip("-")
    return value or "persoana"


def parse_birth_date(value: str) -> tuple[int, int, int]:
    parts = re.split(r"[.\-/\s]+", value.strip())
    if len(parts) != 3:
        raise ValueError("Data nasterii trebuie sa fie in format ZZ.LL.AAAA.")
    zi, luna, an = [int(part) for part in parts]
    return zi, luna, an


def run_script(*args: str) -> str:
    completed = subprocess.run(
        [str(PYTHON), *args],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip())
    return completed.stdout.strip()


def extract_value(pattern: str, text: str, default: str = "de completat") -> str:
    match = re.search(pattern, text, flags=re.MULTILINE)
    return match.group(1).strip() if match else default


def calculation_summary(calc_output: str) -> str:
    soarta = extract_value(r"Soarta grafica:\s+(.+)", calc_output)
    destin = extract_value(r"Destin grafic:\s+(.+)", calc_output)
    tema = extract_value(r"Tema vietii:\s+(.+)", calc_output)
    return "\n".join([
        "Calcul Soarta si Destin:",
        f"Soarta grafica: {soarta}",
        f"Destin grafic: {destin}",
        f"Tema vietii: {tema}",
    ])


def report_code(data: dict, an: int, luna: int, zi: int) -> str:
    initials = "".join(part[:1].upper() for part in data["nume_complet"].split() if part)
    return f"{initials}-{an:04d}{luna:02d}{zi:02d}-V1"


def output_suffix(data: dict) -> str:
    style = data.get("stil_adresare") or "formal"
    detail = data.get("nivel_detaliere") or "amplu"
    style_code = "c" if style == "conversational" else "f"
    detail_code = {
        "scurt": "s",
        "mediu": "m",
        "amplu": "a",
        "foarte amplu": "fa",
    }.get(detail, "a")
    return f"v1{style_code}{detail_code}"


def indexer(code: str):
    counters: dict[str, int] = {}

    def make(kind: str) -> str:
        counters[kind] = counters.get(kind, 0) + 1
        return f"Index: {code}-{kind}-{counters[kind]:03d}"

    return make


def find_existing_report(data: dict, zi: int, luna: int, an: int) -> Path | None:
    folder_name = f"{an:04d}-{luna:02d}-{zi:02d}-{slugify(data['nume_complet'])}"
    folder = ROOT / "examples" / folder_name
    if not folder.exists():
        return None
    reports = sorted(
        folder.glob("*.md"),
        key=lambda path: (
            int(re.search(r"-v(\d+)", path.name, flags=re.IGNORECASE).group(1))
            if re.search(r"-v(\d+)", path.name, flags=re.IGNORECASE)
            else 0,
            path.stat().st_mtime,
        ),
        reverse=True,
    )
    return reports[0] if reports else None


def version_from_path(path: Path | None, fallback: str) -> str:
    if not path:
        return fallback
    match = re.search(r"-(v\d+[a-z]+)\.md$", path.name, flags=re.IGNORECASE)
    return match.group(1) if match else fallback


def normalize_report_metadata(markdown: str, data: dict, version: str) -> str:
    zi, luna, an = parse_birth_date(data["data_nasterii"])
    title = f"# {data['nume_complet']} - {zi:02d}.{luna:02d}.{an:04d}"
    markdown = re.sub(r"^# .+$", title, markdown, count=1, flags=re.MULTILINE)
    markdown = re.sub(
        r"^- Status: .+$",
        f"- Status: de revizuit, {version}",
        markdown,
        count=1,
        flags=re.MULTILINE,
    )
    return markdown


def build_markdown(data: dict, calc_output: str, matrix_output: str) -> str:
    zi, luna, an = parse_birth_date(data["data_nasterii"])
    code = report_code(data, an, luna, zi)
    idx = indexer(code)
    today = datetime.now().strftime("%Y-%m-%d %H:%M")

    vibratie_interioara = extract_value(r"Vibratia interioara:\s+(.+)", calc_output)
    vibratie_exterioara = extract_value(r"Vibratia exterioara:\s+(.+)", calc_output)
    destin_data = extract_value(r"Vibratia datei / destin:\s+(.+)", calc_output)
    exprimare = extract_value(r"Numar de exprimare / destin:\s+(.+)", calc_output)
    intim = extract_value(r"Numar intim:\s+(.+)", calc_output)
    realizare = extract_value(r"Numar de realizare:\s+(.+)", calc_output)
    activ = extract_value(r"Numar activ:\s+(.+)", calc_output)
    ereditar = extract_value(r"Numar ereditar:\s+(.+)", calc_output)
    neam = extract_value(r"Numar ereditar karmic:\s+(.+)", calc_output)
    soarta = extract_value(r"Soarta grafica:\s+(.+)", calc_output)
    destin_grafic = extract_value(r"Destin grafic:\s+(.+)", calc_output)
    tema_vietii = extract_value(r"Tema vietii:\s+(.+)", calc_output)
    an_personal = extract_value(r"Vibratia anului personal \d+:\s+(.+)", calc_output)

    def chart_parts(value: str) -> tuple[str, str, str]:
        match = re.match(r"(\d+)\s+\((.*?),\s+zona\s+([0-9.,]+)\)", value)
        if not match:
            return "de completat", value, "de completat"
        return match.group(2), match.group(1), match.group(3)

    soarta_formula, soarta_digits, soarta_zone = chart_parts(soarta)
    destin_formula, destin_digits, destin_zone = chart_parts(destin_grafic)

    lines = [
        idx("CAP"),
        "",
        f"# Lucrare numerologica - {data['nume_complet']}",
        "",
        idx("P"),
        "",
        "Aceasta lucrare este generata din formularul local `test HTML`, folosind "
        "skill-ul `numerology-agent` ca referinta de structura si scripturile "
        "existente ale proiectului pentru calcule.",
        "",
        idx("CAP"),
        "",
        "## Date lucrare",
        "",
        idx("L"),
        "",
        f"- Persoana analizata: {data['nume_complet']}",
        f"- Gen persoana: {data['gen_persoana']}",
        f"- Data nasterii: {zi:02d}.{luna:02d}.{an:04d}",
        f"- Nume complet folosit in analiza: {data['nume_complet']}",
        f"- Nume de familie folosit in analiza: {data['nume_familie']}",
        f"- Prenume folosit in analiza: {data['prenume']}",
        f"- Prenume activ: {data.get('prenume_activ') or 'de completat'}",
        f"- Nume anterior / schimbat: {data.get('nume_anterior') or 'de completat'}",
        f"- Intrebare personala sau tema principala: {data.get('tema') or 'de completat'}",
        f"- Nivel de detaliere: {data.get('nivel_detaliere') or 'amplu'}",
        f"- Stil de adresare: {data.get('stil_adresare') or 'formal'}",
        f"- Data realizarii lucrarii: {today}",
        "- Status: generat automat, de revizuit",
        "",
        idx("CAP"),
        "",
        "## 1. Sinteza scurta",
        "",
        idx("P"),
        "",
        "Aceasta versiune HTML construieste o lucrare de lucru pe baza calculelor "
        "numerologice generate automat. Pentru interpretarea finala ampla, textul "
        "poate fi extins ulterior conform regulilor din skill-ul `numerology-agent`, "
        "pastrand structura, indexarea si legatura dintre capitole.",
        "",
        idx("CAP"),
        "",
        "## 2. Date de baza si calcule initiale",
        "",
        idx("T"),
        "",
        "| Element | Rezultat |",
        "| --- | --- |",
        f"| Vibratia interioara | {vibratie_interioara} |",
        f"| Vibratia exterioara | {vibratie_exterioara} |",
        f"| Vibratia datei / destin | {destin_data} |",
        f"| Numar de exprimare / destin pe nume | {exprimare} |",
        f"| Tema vietii | {tema_vietii} |",
        f"| An personal | {an_personal} |",
        "",
        idx("CAP"),
        "",
        "## 3. Numele",
        "",
        idx("T"),
        "",
        "| Numar | Rezultat |",
        "| --- | --- |",
        f"| Numar intim | {intim} |",
        f"| Numar de realizare | {realizare} |",
        f"| Numar activ | {activ} |",
        f"| Numar ereditar | {ereditar} |",
        f"| Numarul neamului | {neam} |",
        "",
        idx("CAP"),
        "",
        "## 4. Soarta si destinul",
        "",
        idx("T"),
        "",
        "| Linie | Formula | Sir grafic | Zona de confort |",
        "| --- | --- | --- | --- |",
        f"| Soarta grafica | {soarta_formula} | {soarta_digits} | {soarta_zone} |",
        f"| Destin grafic | {destin_formula} | {destin_digits} | {destin_zone} |",
        "",
        idx("CAP"),
        "",
        "## 5. Rezultate brute din scripturi",
        "",
        idx("SUB"),
        "",
        "### Calcule numerologice",
        "",
        idx("C"),
        "",
        "```text",
        calc_output,
        "```",
        "",
        idx("SUB"),
        "",
        "### Patratul lui Pitagora",
        "",
        idx("C"),
        "",
        "```text",
        matrix_output,
        "```",
        "",
        idx("CAP"),
        "",
        "## Rubrici incomplete si date de confirmat",
        "",
        idx("L"),
        "",
        "- Tema personala principala: daca exista o intrebare concreta, lucrarea poate fi rafinata in jurul ei.",
        "- Context profesional: domeniul de lucru sau directia profesionala actuala pot nuanta aplicabilitatea numerologica.",
        "- Relatii si familie: daca exista o tema activa aici, interpretarile despre sensibilitate, grija, limite sau karma pot fi adaptate.",
        "- Perioada curenta: evenimentele deja simtite in anul analizat pot lega mai bine anul personal si lectia de viata de realitatea imediata.",
        "- Nume folosit social: daca numele complet, prenumele activ sau numele folosit public difera, analiza numelui poate fi ajustata.",
    ]
    return "\n".join(lines) + "\n"


def markdown_to_html(markdown: str, title: str) -> str:
    body: list[str] = []
    toc: list[tuple[str, str]] = []
    heading_count = 0
    in_code = False
    code_lines: list[str] = []
    in_ul = False
    table_lines: list[str] = []
    current_section = ""
    current_subsection = ""
    pending_index = ""

    DIACRITICS = {
        "aceasta": "această",
        "aceleasi": "aceleași",
        "acelasi": "același",
        "acolo": "acolo",
        "adancime": "adâncime",
        "adanc": "adânc",
        "adevar": "adevăr",
        "adevarul": "adevărul",
        "alegeri": "alegeri",
        "ampla": "amplă",
        "amplu": "amplu",
        "ani": "ani",
        "anul": "anul",
        "aplicabilitate": "aplicabilitate",
        "apropiere": "apropiere",
        "aprofundare": "aprofundare",
        "arata": "arată",
        "atentie": "atenție",
        "atitudinea": "atitudinea",
        "baza": "bază",
        "bunastarii": "bunăstării",
        "calcul": "calcul",
        "calcule": "calcule",
        "calea": "calea",
        "capitol": "capitol",
        "cariera": "carieră",
        "casuta": "căsuță",
        "casute": "căsuțe",
        "cautare": "căutare",
        "cautarea": "căutarea",
        "catre": "către",
        "cat": "cât",
        "centrata": "centrată",
        "cicluri": "cicluri",
        "cifra": "cifră",
        "cifre": "cifre",
        "claritate": "claritate",
        "colaborare": "colaborare",
        "comparare": "comparare",
        "concluzie": "concluzie",
        "constient": "conștient",
        "constienta": "conștientă",
        "constiente": "conștiente",
        "conversational": "conversațional",
        "creativitate": "creativitate",
        "crestere": "creștere",
        "date": "date",
        "destin": "destin",
        "destinul": "destinul",
        "directia": "direcția",
        "directie": "direcție",
        "discernamant": "discernământ",
        "diferenta": "diferența",
        "dupa": "după",
        "emotionala": "emoțională",
        "energie": "energie",
        "esenta": "esența",
        "exterioara": "exterioară",
        "exterior": "exterior",
        "fara": "fără",
        "feminin": "feminin",
        "fortata": "forțată",
        "fortate": "forțate",
        "grafica": "grafică",
        "grafic": "grafic",
        "implinire": "împlinire",
        "importanta": "importantă",
        "important": "important",
        "importanti": "importanți",
        "inainte": "înainte",
        "incheieri": "încheieri",
        "incredere": "încredere",
        "indica": "indică",
        "indreptat": "îndreptat",
        "influenta": "influență",
        "informatie": "informație",
        "informatii": "informații",
        "initiale": "inițiale",
        "interioara": "interioară",
        "interior": "interior",
        "intalnire": "întâlnire",
        "intre": "între",
        "intreaga": "întreagă",
        "intrebare": "întrebare",
        "invat": "învăț",
        "invatare": "învățare",
        "lectii": "lecții",
        "legatura": "legătură",
        "legaturi": "legături",
        "lucrarii": "lucrării",
        "lucrare": "lucrare",
        "matricea": "matricea",
        "masculin": "masculin",
        "nastere": "naștere",
        "nasterii": "nașterii",
        "nevoie": "nevoie",
        "nuanta": "nuanță",
        "numar": "număr",
        "nume": "nume",
        "ocazii": "ocazii",
        "oportunitati": "oportunități",
        "pamant": "pământ",
        "perioada": "perioadă",
        "persoana": "persoană",
        "peste": "peste",
        "pinacluri": "pinacluri",
        "practica": "practică",
        "principal": "principal",
        "principala": "principală",
        "provocari": "provocări",
        "prudenta": "prudență",
        "recomandare": "recomandare",
        "relatie": "relație",
        "relatii": "relații",
        "rezultat": "rezultat",
        "scara": "scară",
        "schimbare": "schimbare",
        "scurta": "scurtă",
        "sectiune": "secțiune",
        "sensibilitate": "sensibilitate",
        "simbol": "simbol",
        "sinteza": "sinteză",
        "sir": "șir",
        "soarta": "soartă",
        "sortii": "sorții",
        "spirituala": "spirituală",
        "stiintific": "științific",
        "subtila": "subtilă",
        "subtile": "subtile",
        "tabel": "tabel",
        "tarot": "Tarot",
        "tema": "temă",
        "test": "test",
        "totala": "totală",
        "transformare": "transformare",
        "vibratia": "vibrația",
        "vibratii": "vibrații",
        "esentiale": "esențiale",
        "viata": "viață",
        "vietii": "vieții",
        "vointa": "voință",
        "varsta": "vârstă",
        "varstelor": "vârstelor",
        "zona": "zonă",
        "si": "și",
        "in": "în",
        "iti": "îți",
        "tau": "tău",
        "poti": "poți",
        "sa": "să",
        "daca": "dacă",
        "fata": "față",
        "forta": "forță",
        "forte": "forțe",
        "responsabilitatii": "responsabilității",
        "semnificatia": "semnificația",
        "naturala": "naturală",
        "spatiu": "spațiu",
        "reactie": "reacție",
        "metoda": "metodă",
        "perfecta": "perfectă",
        "potrivita": "potrivită",
        "inteles": "înțeles",
        "intamplarii": "întâmplării",
        "functie": "funcție",
        "calitatea": "calitatea",
    }

    PHRASE_DIACRITICS = {
        "Data nasterii": "Data nașterii",
        "data nasterii": "data nașterii",
        "Luna nasterii": "Luna nașterii",
        "luna nasterii": "luna nașterii",
        "data de nastere": "data de naștere",
        "Data de nastere": "Data de naștere",
        "Matricea datei de nastere": "Matricea datei de naștere",
        "matricea datei de nastere": "matricea datei de naștere",
        "data sustinuta": "data susținută",
        "Data sustinuta": "Data susținută",
    }

    def with_diacritics(text: str) -> str:
        for source, replacement in PHRASE_DIACRITICS.items():
            text = text.replace(source, replacement)

        def replace(match: re.Match[str]) -> str:
            word = match.group(0)
            replacement = DIACRITICS.get(word.lower())
            if not replacement:
                return word
            if word.isupper():
                return replacement.upper()
            if word[0].isupper():
                return replacement[0].upper() + replacement[1:]
            return replacement

        return re.sub(r"\b[A-Za-z]+\b", replace, text)

    def inline_markup(text: str) -> str:
        escaped = html.escape(with_diacritics(text))
        escaped = re.sub(r"`([^`]+)`", r"\1", escaped)
        escaped = escaped.replace("`", "")
        escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
        return escaped

    def normalize_wrapped_paragraphs(source: str) -> list[str]:
        normalized: list[str] = []
        paragraph: list[str] = []
        in_fence = False

        def flush_paragraph() -> None:
            nonlocal paragraph
            if paragraph:
                normalized.append(" ".join(part.strip() for part in paragraph))
                paragraph = []

        for raw in source.splitlines():
            stripped = raw.rstrip()
            marker = stripped.lstrip()
            if marker.startswith("```"):
                flush_paragraph()
                normalized.append(stripped)
                in_fence = not in_fence
                continue
            if in_fence:
                normalized.append(stripped)
                continue
            if not stripped.strip():
                flush_paragraph()
                normalized.append("")
                continue
            if (
                marker.startswith("#")
                or marker.startswith("Index: ")
                or marker.startswith("|")
                or marker.startswith("- ")
            ):
                flush_paragraph()
                normalized.append(stripped)
                continue
            paragraph.append(stripped)

        flush_paragraph()
        return normalized

    def split_table_row(line: str) -> list[str]:
        stripped = line.strip()
        if stripped.startswith("|"):
            stripped = stripped[1:]
        if stripped.endswith("|"):
            stripped = stripped[:-1]

        cells: list[str] = []
        current: list[str] = []
        in_backtick = False
        escaped = False
        for char in stripped:
            if escaped:
                current.append(char)
                escaped = False
                continue
            if char == "\\":
                escaped = True
                current.append(char)
                continue
            if char == "`":
                in_backtick = not in_backtick
                current.append(char)
                continue
            if char == "|" and not in_backtick:
                cells.append("".join(current).strip())
                current = []
                continue
            current.append(char)
        cells.append("".join(current).strip())
        return cells

    vector_label_map = {
        "Creativitate": "Creativitate - vector 789",
        "Bunastare materiala": "Bunastare materiala - vector 369",
        "Cariera": "Cariera - vector 159",
        "Spiritualitate": "Spiritualitate - vector 147",
        "Scopuri": "Scopuri - vector 357",
        "Vointa": "Vointa - vector 456",
        "Energie": "Energie - vector 123",
        "Social": "Social - vector 258",
    }

    def clean_table_cell(cell: str) -> str:
        cell = cell.strip()
        cell = re.sub(r"`\|([^`]+)\|`", r"\1", cell)
        cell = re.sub(r"`([^`]+)`", r"\1", cell)
        cell = cell.replace("|", "")
        cell = vector_label_map.get(cell, cell)
        return cell

    def table_class_for(rows: list[list[str]]) -> str:
        if not rows:
            return ""
        headers = [clean_table_cell(cell).lower() for cell in rows[0]]
        if headers == ["vibratie", "formula", "calcul", "rezultat", "descriere scurta"]:
            return "table-vibratii-esentiale"
        if headers == ["ordine", "tip", "denumire", "cantitate", "valoare totala", "observatie"]:
            return "table-scara-bunastarii"
        if headers == ["an", "varsta", "an personal", "lectie", "interpretare"]:
            return "table-ciclu-9-ani"
        return ""

    def is_matrix_table(rows: list[list[str]]) -> bool:
        cleaned = [[clean_table_cell(cell) for cell in row] for row in rows]
        return (
            len(cleaned) >= 7
            and cleaned[0] == ["1", "4", "7"]
            and cleaned[3] == ["2", "5", "8"]
            and cleaned[5] == ["3", "6", "9"]
        )

    def render_matrix_table(rows: list[list[str]]) -> str:
        cleaned = [[clean_table_cell(cell) for cell in row] for row in rows]
        matrix_rows = [
            (cleaned[0], cleaned[2]),
            (cleaned[3], cleaned[4]),
            (cleaned[5], cleaned[6]),
        ]
        element_by_digit = {
            "1": "foc",
            "5": "foc",
            "9": "foc",
            "2": "apa",
            "4": "pamant",
            "3": "aer",
            "7": "aer",
            "6": "apa",
            "8": "pamant",
        }
        html_rows = ["<div class=\"matrix-grid\">"]
        for headers, values in matrix_rows:
            for label, value in zip(headers, values):
                display_value = value if value else "-"
                element = element_by_digit.get(label, "aer")
                html_rows.append(
                    f"<div class=\"matrix-cell element-{element}\">"
                    f"<div class=\"matrix-value\"><span>{html.escape(label)}</span>{inline_markup(display_value)}</div>"
                    "</div>"
                )
        html_rows.append("</div>")
        return "\n".join(html_rows)

    def digits_for_chart(value: str) -> list[int]:
        digits = [int(char) for char in re.sub(r"\D", "", value)]
        if not digits:
            return []
        while len(digits) < 10:
            digits.append(digits[len(digits) % len(re.sub(r"\D", "", value))])
        return digits[:10]

    def render_destiny_chart(rows: list[list[str]]) -> str:
        data_rows = [[clean_table_cell(cell) for cell in row] for row in rows[2:]]
        soarta_row = next((row for row in data_rows if row and row[0].lower().startswith("soarta")), None)
        destin_row = next((row for row in data_rows if row and row[0].lower().startswith("destin")), None)
        if not soarta_row or not destin_row or len(soarta_row) < 4 or len(destin_row) < 4:
            return ""

        soarta_values = digits_for_chart(soarta_row[2])
        destin_values = digits_for_chart(destin_row[2])
        if not soarta_values or not destin_values:
            return ""

        def parse_zone(value: str) -> float:
            matches = re.findall(r"([0-9]+(?:[,.][0-9]+)?)", value)
            if not matches:
                return 0.0
            return float(matches[-1].replace(",", "."))

        soarta_zone = parse_zone(soarta_row[3])
        destin_zone = parse_zone(destin_row[3])

        width, height = 920, 430
        left, right, top, bottom = 64, 24, 28, 58
        chart_w = width - left - right
        chart_h = height - top - bottom

        def point(index: int, value: float) -> tuple[float, float]:
            x = left + chart_w * (index / 9)
            y = top + chart_h * ((9 - value) / 9)
            return x, y

        def polyline(values: list[int], y_offset: float = 0) -> str:
            return " ".join(
                f"{x:.1f},{y + y_offset:.1f}"
                for x, y in (point(i, val) for i, val in enumerate(values))
            )

        grid = []
        for y_val in range(0, 10):
            _, y = point(0, y_val)
            grid.append(f"<line x1=\"{left}\" y1=\"{y:.1f}\" x2=\"{width - right}\" y2=\"{y:.1f}\" />")
            grid.append(f"<text x=\"{left - 18}\" y=\"{y + 4:.1f}\">{y_val}</text>")
        for index, age in enumerate(range(0, 100, 10)):
            x, _ = point(index, 0)
            grid.append(f"<line x1=\"{x:.1f}\" y1=\"{top}\" x2=\"{x:.1f}\" y2=\"{height - bottom}\" />")
            grid.append(f"<text x=\"{x - 8:.1f}\" y=\"{height - 24}\">{age}</text>")

        def circles(values: list[int], klass: str, y_offset: float = 0) -> str:
            return "\n".join(
                f"<circle class=\"{klass}\" cx=\"{point(i, val)[0]:.1f}\" cy=\"{point(i, val)[1] + y_offset:.1f}\" r=\"5\" />"
                for i, val in enumerate(values)
            )

        zone_overlap = abs(soarta_zone - destin_zone) < 0.03
        line_width = 4
        soarta_zone_offset = -(line_width / 2) if zone_overlap else 0
        destin_zone_offset = line_width / 2 if zone_overlap else 0
        soarta_zone_y = point(0, soarta_zone)[1] + soarta_zone_offset
        destin_zone_y = point(0, destin_zone)[1] + destin_zone_offset
        soarta_zone_points = f"{left},{soarta_zone_y:.1f} {width - right},{soarta_zone_y:.1f}"
        destin_zone_points = f"{left},{destin_zone_y:.1f} {width - right},{destin_zone_y:.1f}"
        line_overlap = soarta_values == destin_values
        soarta_line_points = polyline(soarta_values, -line_width / 2 if line_overlap else 0)
        destin_line_points = polyline(destin_values, line_width / 2 if line_overlap else 0)
        soarta_dot_offset = -line_width / 2 if line_overlap else 0
        destin_dot_offset = line_width / 2 if line_overlap else 0

        diffs = [abs(a - b) for a, b in zip(soarta_values, destin_values)]
        closest = [str(i * 10) for i, diff in enumerate(diffs) if diff == min(diffs)]
        farthest = [str(i * 10) for i, diff in enumerate(diffs) if diff == max(diffs)]
        high_effort = [str(i * 10) for i, (s, d) in enumerate(zip(soarta_values, destin_values)) if s < soarta_zone or d < destin_zone]

        return f"""
<section class="destiny-chart">
  <div class="chart-heading">
    <span>Grafic Soarta si Destin</span>
    <strong>{html.escape(soarta_row[2])} / {html.escape(destin_row[2])}</strong>
  </div>
  <svg viewBox="0 0 {width} {height}" role="img" aria-label="Grafic Soarta si Destin">
    <g class="grid">{''.join(grid)}</g>
    <polyline class="comfort soarta-comfort" points="{soarta_zone_points}" />
    <polyline class="comfort destin-comfort" points="{destin_zone_points}" />
    <polyline class="line soarta-line" points="{soarta_line_points}" />
    <polyline class="line destin-line" points="{destin_line_points}" />
    {circles(soarta_values, "soarta-dot", soarta_dot_offset)}
    {circles(destin_values, "destin-dot", destin_dot_offset)}
  </svg>
  <div class="chart-legend">
    <span><i class="legend-soarta"></i>Soarta</span>
    <span><i class="legend-destin"></i>Destin</span>
    <span><i class="legend-soarta-comfort"></i>Zona de confort pentru soarta</span>
    <span><i class="legend-destin-comfort"></i>Zona de confort pentru destin</span>
  </div>
  <div class="chart-interpretation">
    <p><strong>Puncte de apropiere:</strong> liniile se apropie cel mai mult in jurul varstelor {", ".join(closest)} ani. Acolo cadrul primit si directia de implinire pot colabora mai usor.</p>
    <p><strong>Puncte de departare:</strong> diferenta cea mai mare apare in jurul varstelor {", ".join(farthest)} ani. Acolo poate fi nevoie de alegeri mai constiente, pentru ca directia interioara si contextul exterior nu merg automat in acelasi ritm.</p>
    <p><strong>Zona de confort:</strong> Soarta are zona {soarta_zone:.2f}, iar Destinul are zona {destin_zone:.2f}. Linia punctata arata nivelul la care energia se simte familiara; sub ea apar efort, invatare si reglaj, peste ea apare activare mai vizibila.</p>
    <p><strong>Zone de efort:</strong> varstele {", ".join(high_effort) if high_effort else "de completat"} cer mai multa atentie la centru, limite si adaptare.</p>
  </div>
</section>
"""

    def flush_ul():
        nonlocal in_ul
        if in_ul:
            body.append("</ul>")
            in_ul = False

    def flush_pending_index():
        nonlocal pending_index
        if pending_index:
            body.append(f"<div class=\"index\">{html.escape(pending_index)}</div>")
            pending_index = ""

    def heading_with_index(tag: str, text: str, anchor: str | None = None) -> str:
        nonlocal pending_index
        index_html = ""
        if pending_index:
            index_html = f"<span class=\"heading-index\">{html.escape(pending_index)}</span>"
            pending_index = ""
        anchor_attr = f" id=\"{anchor}\"" if anchor else ""
        return f"<{tag}{anchor_attr}>{index_html}<span>{inline_markup(text)}</span></{tag}>"

    def flush_table():
        nonlocal table_lines
        if not table_lines:
            return
        rows = [split_table_row(line) for line in table_lines]
        if is_matrix_table(rows):
            body.append(render_matrix_table(rows))
            table_lines = []
            return
        table_class = table_class_for(rows)
        class_attr = f' class="{table_class}"' if table_class else ""
        body.append(f'<div class="table-wrap"><table{class_attr}>')
        for index, row in enumerate(rows):
            if index == 1 and all(set(cell.strip()) <= {"-", ":", " "} for cell in row):
                continue
            tag = "th" if index == 0 else "td"
            cells = "".join(f"<{tag}>{inline_markup(clean_table_cell(cell))}</{tag}>" for cell in row)
            body.append(f"<tr>{cells}</tr>")
        body.append("</table></div>")
        if "soarta si destinul" in current_section.lower():
            chart = render_destiny_chart(rows)
            if chart:
                body.append(chart)
        table_lines = []

    for raw_line in normalize_wrapped_paragraphs(markdown):
        line = raw_line.rstrip()
        if line.startswith("```"):
            flush_ul()
            flush_table()
            if in_code:
                body.append(f"<pre>{html.escape(chr(10).join(code_lines))}</pre>")
                code_lines = []
                in_code = False
            else:
                flush_pending_index()
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if line.startswith("|"):
            flush_ul()
            if not table_lines:
                flush_pending_index()
            table_lines.append(line)
            continue
        flush_table()
        if not line:
            flush_ul()
            continue
        if line.startswith("Index: "):
            flush_ul()
            pending_index = line
        elif line.startswith("# "):
            flush_ul()
            body.append(heading_with_index("h1", title))
        elif line.startswith("## "):
            flush_ul()
            heading_count += 1
            anchor = f"sectiune-{heading_count}"
            title_text = line[3:]
            current_section = title_text
            current_subsection = ""
            toc.append((anchor, title_text))
            body.append(heading_with_index("h2", title_text, anchor))
        elif line.startswith("### "):
            flush_ul()
            current_subsection = line[4:]
            body.append(heading_with_index("h3", current_subsection))
        elif line.startswith("- "):
            flush_pending_index()
            if not in_ul:
                body.append("<ul>")
                in_ul = True
            body.append(f"<li>{inline_markup(line[2:])}</li>")
        else:
            flush_ul()
            flush_pending_index()
            body.append(f"<p>{inline_markup(line)}</p>")

    flush_ul()
    flush_table()

    toc_html = ""
    if toc:
        toc_items = "\n".join(
            f"<a href=\"#{anchor}\">{html.escape(text)}</a>" for anchor, text in toc
        )
        toc_html = f"<nav class=\"toc\"><div>Cuprins</div>{toc_items}</nav>"

    return f"""<!doctype html>
<html lang="ro">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    :root {{
      --ink: #061c1d;
      --deep: #0b2b2c;
      --teal: #0f5a56;
      --aqua: #239f98;
      --cream: #f4e5d4;
      --paper: #fffaf3;
      --gold: #8a632f;
      --sand: #c9a479;
    }}
    body {{
      margin: 0;
      background: var(--cream);
      color: var(--ink);
      font-family: "Segoe UI", Arial, sans-serif;
      line-height: 1.65;
    }}
    .topbar {{
      background: linear-gradient(135deg, var(--deep), var(--teal) 62%, var(--aqua));
      color: white;
      padding: 22px 32px;
      border-bottom: 8px solid var(--sand);
    }}
    .topbar strong {{
      display: block;
      font-size: 18px;
    }}
    .topbar span {{
      color: #f7ead8;
      font-size: 14px;
    }}
    main {{
      width: 1040px;
      max-width: min(1040px, calc(100% - 32px));
      margin: 28px auto;
      background: var(--paper);
      border-radius: 8px;
      padding: clamp(20px, 4vw, 42px);
      box-shadow: 0 18px 44px rgba(11, 43, 44, 0.08);
    }}
    .table-wrap {{
      width: 100%;
      overflow-x: auto;
      overflow-y: hidden;
      margin: 18px 0;
      -webkit-overflow-scrolling: touch;
    }}
    .toc {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 8px;
      margin: 18px 0 34px;
      padding: 18px;
      border: 1px solid rgba(11, 43, 44, 0.14);
      border-left: 6px solid var(--aqua);
      background: #fffdf8;
      border-radius: 8px;
    }}
    .toc div {{
      grid-column: 1 / -1;
      color: var(--gold);
      font-weight: 800;
      text-transform: uppercase;
      font-size: 13px;
    }}
    .toc a {{
      color: var(--teal);
      text-decoration-color: var(--sand);
      font-weight: 650;
    }}
    h1, h2, h3 {{ line-height: 1.18; }}
    h1, h2, h3 {{
      display: grid;
      gap: 7px;
    }}
    h1 {{
      font-size: clamp(30px, 4vw, 46px);
      color: var(--deep);
      margin-bottom: 18px;
    }}
    h2 {{
      margin: 42px 0 22px;
      color: white;
      background: linear-gradient(135deg, var(--deep) 0%, #0d4745 58%, var(--teal) 100%);
      border-top: 0;
      border-left: 8px solid var(--gold);
      padding: 16px 22px;
      border-radius: 6px;
      width: 100%;
      box-sizing: border-box;
    }}
    h3 {{ color: var(--teal); }}
    .heading-index {{
      color: var(--gold);
      font-size: 12px;
      font-weight: 700;
      line-height: 1.2;
    }}
    p {{
      margin: 12px 0;
      max-width: none;
      width: 100%;
      text-wrap: pretty;
      color: var(--teal);
    }}
    code {{
      background: rgba(35, 159, 152, 0.12);
      color: var(--deep);
      padding: 1px 5px;
      border-radius: 4px;
    }}
    .index {{
      color: var(--gold);
      font-size: 12px;
      font-weight: 700;
      margin-top: 18px;
    }}
    table {{
      min-width: 100%;
      border-collapse: collapse;
      margin: 0;
      background: white;
      table-layout: fixed;
    }}
    th, td {{
      border: 1px solid rgba(11, 43, 44, 0.16);
      padding: 10px;
      vertical-align: top;
      overflow-wrap: anywhere;
      word-break: break-word;
    }}
    th {{
      background: var(--teal);
      color: white;
      text-align: left;
      overflow-wrap: normal;
      word-break: normal;
      hyphens: none;
    }}
    .table-vibratii-esentiale th:nth-child(1),
    .table-vibratii-esentiale td:nth-child(1) {{
      width: 18%;
    }}
    .table-vibratii-esentiale th:nth-child(2),
    .table-vibratii-esentiale td:nth-child(2) {{
      width: 22%;
    }}
    .table-vibratii-esentiale th:nth-child(3),
    .table-vibratii-esentiale td:nth-child(3) {{
      width: 17%;
    }}
    .table-vibratii-esentiale th:nth-child(4),
    .table-vibratii-esentiale td:nth-child(4) {{
      width: 12%;
    }}
    .table-vibratii-esentiale th:nth-child(5),
    .table-vibratii-esentiale td:nth-child(5) {{
      width: 31%;
    }}
    .table-scara-bunastarii th:nth-child(1),
    .table-scara-bunastarii td:nth-child(1) {{
      width: 8%;
    }}
    .table-scara-bunastarii th:nth-child(2),
    .table-scara-bunastarii td:nth-child(2) {{
      width: 11%;
      white-space: nowrap;
      overflow-wrap: normal;
      word-break: normal;
    }}
    .table-scara-bunastarii th:nth-child(3),
    .table-scara-bunastarii td:nth-child(3) {{
      width: 20%;
    }}
    .table-scara-bunastarii th:nth-child(4),
    .table-scara-bunastarii td:nth-child(4) {{
      width: 19%;
    }}
    .table-scara-bunastarii th:nth-child(5),
    .table-scara-bunastarii td:nth-child(5) {{
      width: 10%;
    }}
    .table-scara-bunastarii th:nth-child(6),
    .table-scara-bunastarii td:nth-child(6) {{
      width: 32%;
    }}
    .table-ciclu-9-ani th:nth-child(1),
    .table-ciclu-9-ani td:nth-child(1) {{
      width: 11%;
    }}
    .table-ciclu-9-ani th:nth-child(2),
    .table-ciclu-9-ani td:nth-child(2) {{
      width: 11%;
    }}
    .table-ciclu-9-ani th:nth-child(3),
    .table-ciclu-9-ani td:nth-child(3) {{
      width: 15%;
    }}
    .table-ciclu-9-ani th:nth-child(4),
    .table-ciclu-9-ani td:nth-child(4) {{
      width: 11%;
    }}
    .table-ciclu-9-ani th:nth-child(5),
    .table-ciclu-9-ani td:nth-child(5) {{
      width: 52%;
    }}
    tr:nth-child(even) td {{
      background: rgba(244, 229, 212, 0.42);
    }}
    pre {{
      background: #dcc39b;
      color: var(--deep);
      border-left: 6px solid var(--sand);
      padding: 16px;
      border-radius: 6px;
      overflow: auto;
      white-space: pre-wrap;
    }}
    .matrix-grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 6px;
      margin: 18px 0 28px;
      max-width: 420px;
    }}
    .matrix-cell {{
      min-height: 58px;
      border: 1px solid rgba(11, 43, 44, 0.18);
      border-radius: 6px;
      display: grid;
      overflow: hidden;
    }}
    .matrix-value {{
      display: grid;
      place-items: center;
      min-height: 58px;
      color: var(--deep);
      font-weight: 800;
      font-size: 17px;
      padding: 8px;
      gap: 2px;
    }}
    .matrix-value span {{
      font-size: 11px;
      opacity: 0.82;
    }}
    .element-aer {{
      background: #fffaf3;
      color: var(--deep);
    }}
    .element-apa {{
      background: #b8d9e7;
      color: var(--deep);
    }}
    .element-pamant {{
      background: #d8c1a2;
      color: var(--deep);
    }}
    .element-foc {{
      background: #e6b4a9;
      color: var(--deep);
    }}
    .destiny-chart {{
      margin: 26px 0 30px;
      padding: 18px;
      border: 1px solid rgba(11, 43, 44, 0.16);
      border-radius: 8px;
      background: #fffdf8;
    }}
    .chart-heading {{
      display: flex;
      justify-content: space-between;
      gap: 16px;
      color: var(--gold);
      font-weight: 800;
      margin-bottom: 10px;
    }}
    .chart-heading strong {{
      color: var(--teal);
    }}
    .destiny-chart svg {{
      width: 100%;
      height: auto;
      background: #fffaf3;
      border-radius: 6px;
    }}
    .grid line {{
      stroke: rgba(11, 43, 44, 0.22);
      stroke-dasharray: 5 5;
    }}
    .grid text {{
      fill: var(--deep);
      font-size: 13px;
      font-weight: 700;
    }}
    .line {{
      fill: none;
      stroke-width: 4;
      stroke-linejoin: round;
      stroke-linecap: round;
    }}
    .soarta-line {{ stroke: var(--aqua); }}
    .destin-line {{ stroke: var(--gold); }}
    .comfort {{
      fill: none;
      stroke-width: 4;
      stroke-dasharray: 12 8;
      opacity: 1;
    }}
    .soarta-comfort {{ stroke: var(--aqua); }}
    .destin-comfort {{ stroke: var(--gold); }}
    .soarta-dot {{ fill: var(--aqua); }}
    .destin-dot {{ fill: var(--gold); }}
    .chart-legend {{
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      margin: 12px 0;
      color: var(--deep);
      font-weight: 700;
    }}
    .chart-legend i {{
      display: inline-block;
      width: 20px;
      height: 4px;
      border-radius: 99px;
      margin-right: 7px;
      vertical-align: middle;
    }}
    .legend-soarta {{ background: var(--aqua); }}
    .legend-destin {{ background: var(--gold); }}
    .legend-soarta-comfort {{
      background: repeating-linear-gradient(
        90deg,
        var(--aqua) 0 10px,
        transparent 10px 16px
      );
    }}
    .legend-destin-comfort {{
      background: repeating-linear-gradient(
        90deg,
        var(--gold) 0 10px,
        transparent 10px 16px
      );
    }}
    .chart-interpretation {{
      border-left: 5px solid var(--sand);
      padding-left: 14px;
    }}
    ul, li {{
      color: var(--teal);
    }}
    li {{ margin: 6px 0; }}
    @media (max-width: 1100px) {{
      body {{
        overflow-x: auto;
      }}
      main {{
        width: 1040px;
        max-width: none;
      }}
    }}
    @media print {{
      body {{ background: white; }}
      .topbar, .toc {{ break-inside: avoid; }}
      main {{ box-shadow: none; margin: 0; width: auto; }}
      h2, h3, table, pre {{ break-inside: avoid; }}
    }}
  </style>
</head>
<body>
  <header class="topbar">
    <strong>{html.escape(title)}</strong>
    <span>Lucrare numerologica completa, transpusă din Markdown in HTML</span>
  </header>
  <main>
    {toc_html}
    {chr(10).join(body)}
  </main>
</body>
</html>
"""


class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path: str) -> str:
        path = unquote(path.split("?", 1)[0])
        if path.startswith("/output/"):
            return str(APP_DIR / path.lstrip("/"))
        return str(APP_DIR / path.lstrip("/"))

    def do_POST(self) -> None:
        if self.path != "/generate":
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            data = json.loads(self.rfile.read(length).decode("utf-8"))
            zi, luna, an = parse_birth_date(data["data_nasterii"])
            OUTPUT_DIR.mkdir(exist_ok=True)

            calc_output = run_script(
                "scripts/calcule_numerologice.py",
                "--zi", str(zi),
                "--luna", str(luna),
                "--an", str(an),
                "--nume", data["nume_complet"],
                "--nume-familie", data["nume_familie"],
                "--an-analizat", str(datetime.now().year),
                "--start", str(an),
                "--stop", str(datetime.now().year + 10),
            )
            matrix_output = run_script(
                "scripts/patratul_lui_pitagora.py",
                str(zi),
                str(luna),
                str(an),
                "--nume", data["nume_complet"],
            )

            slug = f"{an:04d}-{luna:02d}-{zi:02d}-{slugify(data['nume_complet'])}"
            markdown_name = f"{slug}.md"
            html_name = f"{slug}.html"
            existing_report = find_existing_report(data, zi, luna, an)
            if existing_report:
                version = version_from_path(existing_report, output_suffix(data))
                markdown = normalize_report_metadata(
                    existing_report.read_text(encoding="utf-8"),
                    data,
                    version,
                )
                source_note = f"Lucrarea completa a fost preluata din {existing_report.relative_to(ROOT)} si transpusa in HTML."
            else:
                version = output_suffix(data)
                markdown = normalize_report_metadata(
                    build_markdown(data, calc_output, matrix_output),
                    data,
                    version,
                )
                source_note = "A fost generata o lucrare de lucru automata si transpusa in HTML."
            html_title = f"{data['nume_complet']} - {zi:02d}.{luna:02d}.{an:04d}"
            html_text = markdown_to_html(markdown, html_title)
            (OUTPUT_DIR / markdown_name).write_text(markdown, encoding="utf-8")
            (OUTPUT_DIR / html_name).write_text(html_text, encoding="utf-8")

            payload = {
                "markdown_name": markdown_name,
                "html_name": html_name,
                "markdown_url": f"/output/{markdown_name}",
                "html_url": f"/output/{html_name}",
                "summary": (
                    f"Au fost rulate scripturile de calcul. {source_note}\n\n"
                    f"{calculation_summary(calc_output)}"
                ),
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(payload).encode("utf-8"))
        except Exception as exc:
            payload = {"error": str(exc)}
            self.send_response(500)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(payload).encode("utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8787)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("localhost", args.port), Handler)
    print(f"Server pornit: http://localhost:{args.port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
