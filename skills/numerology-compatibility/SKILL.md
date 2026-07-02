---
name: numerology-compatibility
description: Generate Romanian numerology compatibility comparisons between two people using existing numerology reports, birth-date matrices, name matrices, vectors, and the local HTML output workflow. Use when the user asks for compatibilitate, comparatie, relatie numerologica, cuplu, potrivire, or "persoana A vs persoana B" in this repository.
---

# Numerology Compatibility

Use this skill to create Romanian compatibility comparisons between two people
inside this repository. It complements `numerology-agent`: use existing
individual reports when available, then compare the two profiles.

## Core Sources

Work from the repository root.

- Individual reports: `examples/YYYY-MM-DD-nume-prenume/*.md`
- Relationship method:
  `knowledge_base/calcule/relatii/omuletul-relatiilor/`
- Calculations:
  - `scripts/calcule_numerologice.py`
  - `scripts/patratul_lui_pitagora.py`
- Output directory: `test HTML/output/comparatie/`
- Optional HTML conversion: `test HTML/server.py`, function `markdown_to_html`
- Useful structure examples:
  - `examples/1984-11-06-szabo-mihai-gabriel/1984-11-06-Szabo-Mihai-Gabriel-v4ca.md`
  - recent reports for the two people being compared

## Required Inputs

If the user does not provide enough information to identify both people, ask for:

```text
Date comparatie:
- Persoana 1:
- Persoana 2:
- Tema comparatiei, daca exista: relatie / familie / profesional / general
- Nivel de detaliere: scurt / mediu / amplu
- Stil: conversational / formal
```

If both people already have reports in `examples/`, use those reports as the
source of truth for full names, birth dates, active names, matrices, and existing
interpretations.

## Workflow

1. Identify the two latest relevant individual reports in `examples/`.
2. Extract or verify:
   - full names;
   - active first names;
   - birth dates;
   - essential vibrations;
   - birth-date Pythagorean matrix;
   - name matrix;
   - wellbeing-scale vectors.
   - relationship-man digit counts for the birth-date matrix, including `0`.
3. If a matrix or calculation is missing or unclear, rerun:
   - `scripts/calcule_numerologice.py`
   - `scripts/patratul_lui_pitagora.py`
4. Create `test HTML/output/comparatie/` if it does not exist.
5. Generate a Markdown comparison named:

```text
Persoana-1-vs-Persoana-2.md
```

Use short display names, normally `Nume-Prenume-vs-Nume-Prenume.md`.

6. If the user asks for HTML, or if the request includes a presentation output,
   also generate:

```text
Persoana-1-vs-Persoana-2.html
```

through `markdown_to_html`.

## Comparison Method

Compare both matrices separately:

### Birth-Date Matrix vs Birth-Date Matrix

Read this as native structure: what each person brings by birth.

Compare:

- repeated digits and missing digits;
- dominant boxes;
- shared strengths;
- complementary digits;
- shared absences;
- potential friction where one profile has excess and the other has absence.

For HTML or presentation outputs, display the two completed birth-date matrices
side by side, using the same 3x3 color treatment as individual reports.

### Name Matrix vs Name Matrix

Read this as social identity and active expression.

Compare:

- how each name reinforces or softens the birth-date matrix;
- digits one person brings through name that the other lacks by date;
- whether the name matrix supports communication, emotional stability, career,
  social life, or shared goals.

For HTML or presentation outputs, display the two completed name matrices side
by side, using the same 3x3 color treatment as individual reports.

### Cross-Activation

Add two short subchapters:

- What person 1 activates in person 2.
- What person 2 activates in person 1.

Use concrete digit/vector language, for example:

- `5` can bring center, freedom, rhythm, and choice;
- `6` can bring harmony, responsibility, family, repair, and warmth;
- `7` can bring analysis, depth, study, and intuition;
- excess `1` can bring initiative but also pressure;
- excess `9` can bring vision but also idealization or unfinished endings.

### Vectors

Compare these 8 vectors for both people:

- `123 - Energie`
- `456 - Vointa`
- `789 - Creativitate`
- `147 - Spiritualitate`
- `258 - Social`
- `369 - Bunastare materiala`
- `159 - Cariera`
- `357 - Scopuri`

For each vector, explain:

- who has the stronger native vector;
- whether the other person complements it through name;
- how it may feel in daily life;
- what practical rule helps the relation.

When requested, include a separate wellbeing-scale-by-vectors table for the
birth-date matrices. Sort vectors descending for each person and display the two
birth-date vector scales side by side in HTML. Use name-vector scales only if the
user explicitly asks for name-based wellbeing scales.

### Omuletul Relatiilor

Always include `Omuletul relatiilor` in compatibility reports. Use
`knowledge_base/calcule/relatii/omuletul-relatiilor/01-metoda.md`.

For general compatibility, use each person's complete birth-date numerological
code as the digit source, including `0`. Add:

- `ce se poate realiza impreuna`;
- `ce este de rezolvat impreuna`;
- digit distribution on the pentagram positions;
- element synthesis;
- practical interpretation of dominant, absent, and imbalanced digits.

## Report Structure

Use this structure for the Markdown comparison:

1. Date comparatie
2. Sinteza compatibilitatii
3. Datele celor doua persoane
4. Matricea datei de nastere: comparatie
5. Matricea numelui: comparatie
6. Activari reciproce
7. Vectori de compatibilitate
8. Omuletul relatiilor
9. Zone de armonie
10. Zone de tensiune si lucru constient
11. Recomandari practice
12. Concluzie
13. Surse folosite

Use tables where they make comparison easier, then write natural interpretive
paragraphs after each important table.

## Writing Rules

- Write in Romanian.
- Keep the tone warm, clear, practical, and non-fatalistic.
- For conversational style, address both people by active first name.
- Do not declare that two people are "compatibili" or "incompatibili" as a
  fixed verdict. Speak in terms of patterns, resources, friction, and practices.
- Distinguish clearly between native structure from birth date and social/active
  expression from name.
- Avoid turning the comparison into a mechanical digit list.
- Mention missing or assumed data in a final `Date de confirmat` section when
  useful.

## Quality Check

Before finishing:

1. Confirm the output directory exists.
2. Confirm the Markdown file exists and is non-empty.
3. If HTML is generated, confirm the HTML file exists, is non-empty, has the
   expected title, and has no stray Markdown backticks.
4. Confirm both people are named in the title and comparison metadata.
5. Confirm the comparison includes both birth-date matrices and name matrices.
6. Confirm `Omuletul relatiilor` is included with digit and element tables.
