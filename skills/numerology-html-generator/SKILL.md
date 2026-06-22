---
name: numerology-html-generator
description: Generate, update, restyle, and verify local HTML numerology reports from Romanian Markdown numerology works in this repository. Use when the user asks to create a HTML site/form/report, convert a numerology Markdown report to HTML, regenerate `test HTML/output/*.html`, adjust table/matrix/chart styling, fix HTML rendering issues, or continue the browser-based numerology presentation workflow.
---

# Numerology HTML Generator

Use this skill for the repository's local HTML workflow that turns a Romanian
numerology report into a polished browser document. This skill complements
`numerology-agent`: use `numerology-agent` for report content and calculations,
then use this skill for HTML generation, styling, rendering fixes, and output
verification.

## Core Files

Work from the repository root.

- Form UI: `test HTML/index.html`, `test HTML/styles.css`, `test HTML/app.js`
- Generator and converter: `test HTML/server.py`
- Generated outputs: `test HTML/output/`
- Source reports: `examples/YYYY-MM-DD-nume-prenume/*.md`
- Report template: `examples/Template-lucrare-numerologie.md`
- Calculation scripts: `scripts/calcule_numerologice.py`,
  `scripts/patratul_lui_pitagora.py`
- Relevant knowledge base: `knowledge_base/calcule/`

When the task touches report correctness, read the relevant source from
`examples/`, the template section, and the matching `knowledge_base/calcule/`
method before changing HTML.

## Workflow

1. Identify the target person and output HTML file.
2. If a complete report exists in `examples/`, use the latest matching `.md`
   report as the source.
3. If no complete report exists, use `test HTML/server.py` to generate a
   calculation-based draft from the form fields.
4. Preserve the Markdown source and regenerate HTML through `markdown_to_html`.
5. Verify the generated HTML file exists, is non-empty, and contains the expected
   sections, tables, matrices, calculation blocks, and charts.
6. If the user has the in-app browser open, ask them to refresh or use browser
   tooling when available to inspect the rendered page.

## Regenerating Casiana's Test HTML

For the current test person, use this pattern from the repository root:

```powershell
@'
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("test_server", Path("test HTML/server.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

data = {
    "nume_complet": "Comaniciu Casiana Teodora",
    "nume_familie": "Comaniciu",
    "prenume": "Casiana Teodora",
    "prenume_activ": "Casiana",
    "gen_persoana": "feminin",
    "data_nasterii": "11.07.1989",
    "nume_anterior": "",
    "tema": "",
    "nivel_detaliere": "amplu",
    "stil_adresare": "conversational",
}

zi, luna, an = mod.parse_birth_date(data["data_nasterii"])
existing = mod.find_existing_report(data, zi, luna, an)
version = mod.version_from_path(existing, mod.output_suffix(data))
md = mod.normalize_report_metadata(existing.read_text(encoding="utf-8"), data, version)
html = mod.markdown_to_html(md, f"{data['nume_complet']} - {zi:02d}.{luna:02d}.{an:04d}")

out = Path("test HTML/output")
out.mkdir(exist_ok=True)
(out / "test-casiana-complet.md").write_text(md, encoding="utf-8")
(out / "test-casiana-complet.html").write_text(html, encoding="utf-8")
print(len(html))
'@ | C:\Users\Mihai\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -
```

Adapt `data` and output filenames for other people.

## Rendering Rules

- The page title must be only `Nume complet - data nasterii`.
- Put version/status in the report metadata, not in the page title.
- Display chapter indexes inside the heading, below the visual heading line or
  inside the chapter box.
- Keep paragraph text fluid and responsive; do not lock paragraphs to a fixed
  width that fails to follow the viewport.
- Strip literal Markdown backticks from rendered paragraph and table text.
- Render special Pythagorean matrix tables as true 3x3 grids, not ordinary
  Markdown tables.
- Matrix element mapping:
  - `1, 5, 9`: foc
  - `2, 6`: apa
  - `3, 7`: aer
  - `4, 8`: pamant
- Use calm, palette-compatible matrix colors; `aer` should be near white.
- Render `Soarta si destinul` as a SVG line chart when the table is present.
  Include separate dashed comfort lines for Soarta and Destin. If the values are
  identical, offset the two dashed lines slightly so both remain visible.
- For ezoterism, if the first division gives code `0`, stop the calculation
  there. Do not render or interpret the second division.
- Render the wellbeing scale table with all 17 rows: 8 vectors and 9 individual
  boxes. In the `Denumire` column, vector rows must include code plus label,
  for example `123 - Energie`, `456 - Vointa`, `789 - Creativitate`,
  `147 - Spiritualitate`, `258 - Social`, `369 - Bunastare materiala`,
  `159 - Cariera`, and `357 - Scopuri`. Keep box rows as the box digit.
- In yearly cycle tables such as `T020`, use the header `Lectie` for the
  lesson column and write the digit calculated from the life-lessons sequence
  shown in `T019`, not the personal-year digit. Compute it from the person's
  year of life (`age + 1`) and cycle through the `T019` sequence. Do not include
  a `Vibratie cosmica` column in `T020`; keep only `An`, `Varsta`,
  `An personal`, `Lectie`, and `Interpretare`. Keep lesson meanings or short
  text only in the interpretation column. The `Interpretare` cell must be short
  and combine the personal year with the lesson in meaning, without labels such
  as `AP` or `L`; for example, write `incheiere prin exprimare`.
- Review-version HTML should include the `Ani importanti` subchapter after the
  9-year cycle table and its interpretation when the source report contains or
  requires important interior/exterior years.
- For the first essential-vibrations table (`T001`), keep the `Rezultat` header
  on one line. In HTML, slightly narrow the calculation column and widen the
  result column when needed so headers do not split words.
- Render bullet lists in the same text color as normal paragraphs. They should
  feel like part of the report body, not a secondary or muted note.
- For review versions, preserve indexes and all rubrics in the generated HTML so
  the user can revise by exact reference. Do not create or render a `final`
  variant unless the user has already approved the indexed review version.

## Visual Palette

Use the established cream, teal, turquoise, gold, and brown palette.

- Main text: dark teal.
- Chapter boxes: deep green/teal with white text, full width of the content area.
- Table headers: a lighter green/teal than chapter boxes, with white text.
- Code/calculation blocks: light brown/gold with dark teal text.
- Avoid strong saturated matrix blocks that distract from the report palette.

## Verification Checklist

Before finishing:

1. Search the generated HTML for stray backticks.
2. Search for obsolete or incorrect calculations mentioned by the user.
3. Confirm matrix colors and dimensions appear in CSS.
4. Confirm `Soarta` and `Destin` chart lines and comfort lines are present.
5. Confirm table headers and chapter boxes use the requested palette.
6. Confirm wellbeing scale vector labels use `cod - denumire` and the table has
   17 rows when the source contains the full scale.
7. Confirm the HTML file was regenerated after source or converter changes.

Use `Select-String` or `rg` for targeted verification. If browser tooling is
available, inspect the open local file visually after regeneration.
