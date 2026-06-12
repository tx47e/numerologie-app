from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_BASE = ROOT / "knowledge_base"
OUTPUT = ROOT / "generated" / "index.json"

MASTER_REDUCTIONS = {11: 2, 22: 4, 33: 6}

INPUTS_BY_CALC = {
    "numarul-de-exprimare": ["nume_complet"],
    "destin": ["nume_complet"],
    "vibratia-interioara": ["zi_nastere"],
    "vibratia-exterioara": ["luna_nastere"],
    "vibratia-cosmica": ["an_nastere"],
    "vibratia-globala": ["zi_nastere", "luna_nastere"],
    "vibratia-destinului": ["zi_nastere", "luna_nastere", "an_nastere"],
    "calea-destinului": ["data_nasterii"],
    "soarta": ["data_nasterii"],
    "tema-vietii": ["data_nasterii", "nume_complet"],
    "vibratia-anului-personal": ["zi_nastere", "luna_nastere", "an_analizat"],
    "ani-importanti-interiori": ["zi_nastere", "luna_nastere", "interval_ani"],
    "ani-importanti-exteriori": ["zi_nastere", "luna_nastere", "interval_ani"],
    "lectii-de-viata": ["data_nasterii", "an_de_viata"],
    "cicluri-7-ani": ["varsta"],
    "cicluri-9-ani": ["varsta"],
    "cicluri-12-ani": ["varsta"],
    "pinacluri": ["data_nasterii"],
    "karma-zilei-de-nastere": ["zi_nastere"],
    "karma-lunii-de-nastere": ["luna_nastere"],
    "karma-din-calea-destinului": ["data_nasterii"],
    "patratul-lui-pitagora": ["data_nasterii"],
}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def slug_to_title(slug: str) -> str:
    words = slug.replace("-", " ").split()
    return " ".join(word.capitalize() for word in words)


def first_heading(path: Path) -> str | None:
    if not path.exists():
        return None
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def chapter_from_file(path: Path) -> dict:
    match = re.match(r"^(\d+)-(.+)\.md$", path.name)
    if not match:
        raise ValueError(f"Nume capitol invalid: {path}")
    order = int(match.group(1))
    slug = match.group(2)
    return {
        "ordine": order,
        "slug": slug,
        "titlu": first_heading(path) or slug_to_title(slug),
        "fisier": rel(path),
        "continut": path.read_text(encoding="utf-8-sig").strip(),
        "metadate": {
            "cuvinte_cheie": [],
            "teme_principale": [],
            "recomandari": [],
            "avertismente": [],
            "exemple": [],
        },
    }


def build_vibrations() -> list[dict]:
    vibrations_dir = KNOWLEDGE_BASE / "vibratii"
    vibrations = []

    for directory in vibrations_dir.glob("vibratia-*"):
        if not directory.is_dir():
            continue
        number = int(directory.name.removeprefix("vibratia-"))
        chapter_files = sorted(
            path for path in directory.glob("*.md")
            if re.match(r"^\d+-", path.name)
        )
        vibrations.append(
            {
                "numar": number,
                "titlu": first_heading(directory / "README.md") or f"Vibratia {number}",
                "slug": directory.name,
                "tip": "maestru" if number in MASTER_REDUCTIONS else "baza",
                "reduce_la": MASTER_REDUCTIONS.get(number),
                "cale": rel(directory),
                "capitole": [chapter_from_file(path) for path in chapter_files],
            }
        )

    return sorted(vibrations, key=lambda item: item["numar"])


def calculation_files(directory: Path) -> dict:
    keys = [
        "README",
        "metoda",
        "semnificatii",
        "exemple",
        "observatii",
        "oportunitati",
        "provocari",
        "scara-bunastarii",
        "semnificatii-frecvente",
        "semnificatii-pozitii",
    ]
    files = {}
    for key in keys:
        direct_path = directory / f"{key}.md"
        prefixed_paths = sorted(directory.glob(f"[0-9][0-9]-{key}.md"))
        if direct_path.exists():
            files[key] = rel(direct_path)
        elif prefixed_paths:
            files[key] = rel(prefixed_paths[0])
    return files


def build_calculations() -> list[dict]:
    calculations_dir = KNOWLEDGE_BASE / "calcule"
    calculations = []

    for category_dir in sorted(path for path in calculations_dir.iterdir() if path.is_dir()):
        direct_files = calculation_files(category_dir)
        if "metoda" in direct_files:
            slug = category_dir.name
            calculations.append(
                {
                    "slug": slug,
                    "titlu": first_heading(category_dir / "README.md")
                    or first_heading(category_dir / "01-metoda.md")
                    or slug_to_title(slug),
                    "categorie": category_dir.name,
                    "cale": rel(category_dir),
                    "inputuri": INPUTS_BY_CALC.get(slug, []),
                    "fisiere": direct_files,
                }
            )

        for calc_dir in sorted(path for path in category_dir.iterdir() if path.is_dir()):
            files = calculation_files(calc_dir)
            if not files:
                continue
            slug = calc_dir.name
            calculations.append(
                {
                    "slug": slug,
                    "titlu": first_heading(calc_dir / "README.md")
                    or first_heading(calc_dir / "01-metoda.md")
                    or slug_to_title(slug),
                    "categorie": category_dir.name,
                    "cale": rel(calc_dir),
                    "inputuri": INPUTS_BY_CALC.get(slug, []),
                    "fisiere": files,
                }
            )

    return calculations


def build_index() -> dict:
    return {
        "versiune": 1,
        "sursa": rel(KNOWLEDGE_BASE),
        "decizie_model": "Markdown ca sursa editoriala, JSON generat pentru aplicatie",
        "vibratii": build_vibrations(),
        "calcule": build_calculations(),
    }


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    index = build_index()
    OUTPUT.write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Generat {rel(OUTPUT)}")
    print(f"Vibratii: {len(index['vibratii'])}")
    print(f"Calcule: {len(index['calcule'])}")


if __name__ == "__main__":
    main()
