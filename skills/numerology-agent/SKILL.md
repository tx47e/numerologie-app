---
name: numerology-agent
description: Generate Romanian numerology Markdown reports from person data using this repository's template, knowledge_base, examples, and calculation scripts. Use when the user asks to generate, create, draft, continue, revise, or standardize a numerology report, lucrare numerologica, profil numerologic, or Romanian numerology Markdown document in this project.
---

# Numerology Agent

Use this skill to generate or update Romanian numerology reports inside this
repository. This skill is the complete generation instruction source.

## Core Sources

Before generating a report, read these files from the repository root:

1. `examples/Template-lucrare-numerologie.md`
2. Relevant files from `knowledge_base/`
3. Relevant reusable wording from `knowledge_base/exprimari/`
4. One recent comparable report from `examples/`, preferably the latest matching
   style and detail level.

Use `bibliography/` only when `knowledge_base/` is not developed enough for a
rubric.

## Ask For Person Data

If the user has not provided all required inputs, ask for the missing values in
this form:

```text
Date persoana:
- Nume complet:
- Nume de familie:
- Prenume:
- Prenume activ, daca este cunoscut:
- Gen persoana: masculin / feminin
- Data nasterii:
- Nume anterior / schimbat, daca exista:
- Intrebare personala sau tema principala, daca exista:
- Nivel de detaliere dorit: scurt / mediu / amplu / foarte amplu
- Stil de adresare dorit: conversational / formal
```

`Nume anterior / schimbat` includes any former name that should be analyzed
alongside the current name.

If optional information is missing, continue with `de completat` where
appropriate.

## Generation Workflow

Follow this workflow:

1. Parse and normalize the person data.
2. Choose a report code from initials, birth date, and version, for example
   `SOC-19800604-V1`.
3. Run the calculation scripts when possible:
   - `scripts/calcule_numerologice.py`
   - `scripts/patratul_lui_pitagora.py`
4. Use the template structure and the rules in this skill.
5. Use the relevant `knowledge_base/` documentation before writing each rubric.
6. Use reusable wording from `knowledge_base/exprimari/` when it fits the
   calculated result, style, detail level, and context.
7. Explain concepts and calculations richly, but do not over-explain
   administrative fields.
8. Link the results together: birth date, karma, matrix, wellbeing scale, name,
   pinnacles, cycles, esotericism, optional relationship analysis, and
   conclusion.
   If the user provides a loved person / compatibility person, include the
   optional relationship chapter and use
   `knowledge_base/calcule/relatii/omuletul-relatiilor/`.
9. Add `Rubrici incomplete si date de confirmat` as practical refinement
   suggestions when useful. Do not write it as a technical list of missing work.

## Working Sources

- Use the template from `examples/Template-lucrare-numerologie.md`.
- Use primarily the consolidated documentation from `knowledge_base/`.
- Check `knowledge_base/exprimari/` for validated recurring interpretations. If
  there is wording suitable for the calculated result, use it as a base and adapt
  it to the analyzed person.
- Use `bibliography/` only as a primary verification source when the information
  is not sufficiently developed in `knowledge_base/`.

## Writing Rules

- Do not turn the report into a mechanical list of calculations.
- Do not add long explanations to administrative data or obvious rubrics.
- Respect the requested detail level. If it is not specified, use `amplu`, with
  rich explanations only for concepts, calculations, and important
  interpretations.
- When a numerological concept or calculation appears, explain it richly,
  academically, and in a way that an ordinary reader can understand. The
  explanation should help the person recognize the idea in daily life.
- After every important table, write a flowing interpretation in natural
  paragraphs.
- Arrange tables carefully. Text in cells, especially headers, should not break
  unnaturally. Narrow columns that can be narrowed, widen columns that need
  space, and keep the table clear and easy to read.
- On the wellbeing scale, explain both box values and each vector: digit
  quantity, total value formula, obtained value, and practical meaning.
- The wellbeing scale table must contain all 17 steps: the 8 vectors and the 9
  individual boxes from the Pythagorean matrix. Sort all 17 rows by total value
  descending. In `Cantitate`, show the actual repeated digits for every vector
  or box, using `-` only for missing digits. Do not publish a wellbeing scale
  with only the 8 vectors.
- In the wellbeing scale table, the `Denumire` column must name every vector by
  code plus label: `123 - Energie`, `456 - Vointa`, `789 - Creativitate`,
  `147 - Spiritualitate`, `258 - Social`, `369 - Bunastare materiala`,
  `159 - Cariera`, and `357 - Scopuri`. For box rows, use the box digit.
- In yearly cycle tables with columns `An`, `Varsta`, `An personal`, `Lectie`,
  and `Interpretare`, keep `Interpretare` short and include both the personal
  year and the lesson in meaning, without displaying labels such as `AP` or
  `L`. For example, for personal year `9` and lesson `3`, write `incheiere prin
  exprimare`, not `AP 9 + L 3: incheiere prin exprimare`. Reserve longer
  explanation for the paragraph after the table.
- After the 9-year cycle table and its interpretation, include the `Ani
  importanti` subchapter in review versions. Use one chronological table with
  `Important interior` and `Important exterior` columns; mark both when the same
  year appears in both sequences.
- After the birth-date matrix and name matrix, do the comparative reading using
  the Pythagorean Square method: supported boxes, digits in excess in the name,
  digits missing from the name, and name potential without native support. Do not
  calculate a third resulting matrix.
- If there is a former/changed name and a current name, keep both names in the
  karmic hereditary number analysis. Explain that the former name preserves the
  origin line, while the current name shows the active social and family line;
  the blood-line karmic hereditary number remains present throughout life.
- In the ezoterism rubric, if the first division yields code `0`, stop there.
  Do not write or interpret a second division; explain only the principal `0`.
- When interpreting the karmic hereditary number / number of the lineage, keep
  the traditional definition from the documentation, but adapt the analysis to
  current society. Translate old occupations into suitable modern equivalents
  for the person: for example, `mestesugar` may become technical specialist,
  designer, producer, creator, modern artisan, or practical professional.
- Connect the results: birth date, karma, matrix, wellbeing scale, name,
  pinnacles, cycles, esotericism, and conclusion.
- The tone must be friendly, warm, clear, and gently poetic where appropriate,
  but practical and applicable. The reader should feel guided through the report,
  not lost in concepts or judgments.
- Respect the requested address style. For `conversational`, write as a direct
  conversation with the analyzed person, using the active first name if known and
  second person singular: `Mihai, aceasta vibratie iti arata...`. For `formal`,
  write about the person in third person, keeping the tone warm, clear, and
  respectful. If style is not specified, use `formal`.
- Avoid fatalistic verdicts. Present results as directions for awareness,
  maturity, and practical work.
- If information is missing, mark it discreetly as `de completat` and continue
  with what can be calculated correctly.
- Include `Omuletul relatiilor` only when a loved person, compatibility person,
  or explicit relationship theme is provided. Do not add it mechanically to every
  individual report.
- In `Rubrici incomplete si date de confirmat`, give concrete suggestions the
  reader can act on: personal theme, professional context, relationship/family
  context, current-year events, socially used name, and optional graph/cycle
  refinements. Each bullet should explain why confirming that detail would make
  the report more precise.
- For each recurring interpretation, first check whether a suitable wording
  already exists in `knowledge_base/exprimari/`. If there are several suitable
  variants, choose one that brings variety compared with nearby reports,
  especially when analyzing people from the same family or group.
- Generate new wording if the existing variants do not fit the result, style,
  detail level, report context, or need for variety between nearby reports.
- If you generate a valuable new interpretation for a recurring theme, note it
  as text worth saving in `knowledge_base/exprimari/`, in the appropriate theme
  file. When saved, the wording must have numeric index, style (`formal` or
  `conversational`), detail level (`scurt`, `mediu`, `amplu`, or `foarte amplu`),
  short context, and list of reports where it was used. If you reuse an existing
  wording in a new report, add the new report to that variant's usage list; do
  not automatically create a new variant.

## Indexing

For review versions, index the report as a reference document: every chapter,
subtitle, paragraph, table, graph, and calculation block must have a code
displayed on the separate line before the element, in this form:

```text
Index: COD-LUCRARE-TIP-NNN
```

Add a blank line after the index. Do not put the index on the same line as the
title, paragraph, table, or any other indexed element. Interpretations are
indexed as paragraphs, with type `P`; do not use a separate `I` type. Follow the
complete rule in `examples/Template-lucrare-numerologie.md`, section `Regula de
indexare editoriala`.

Keep indexes in every review version so the user can revise by exact reference.
Do not remove previously omitted rubrics from the review version; keep the work
complete and fully structured. Only after the user confirms the indexed review
version is approved should a second final report be generated. For that final
report, create a separate final template in `examples/` with suffix `final`,
based on the reviewed version and the validated editorial decisions.

## Report Structure

Use this structure:

1. Date lucrare
2. Sinteza scurta
3. Date de baza si calcule initiale
4. Karma din data nasterii
5. Matricea numerologica
6. Scara bunastarii
7. Numele
8. Oportunitati, provocari si pinacluri
9. Soarta si destinul
10. Lectii de viata si cicluri
11. Ezoterism si aplicabilitate
12. Relatii, persoana iubita si compatibilitate optionala
13. Concluzie finala
14. Harta documentatie folosita

## File Output

Save generated reports in:

```text
examples/YYYY-MM-DD-nume-prenume/
```

Use this filename pattern:

```text
YYYY-MM-DD-Nume-Prenume-vNxx.md
```

Where:

- `vN` is the version number.
- Use review versions such as `v2ca` for indexed review work. Reserve the
  `final` suffix for the separate final template/report created only after the
  user has reviewed and approved the indexed version.
- `fa` means formal amplu.
- `ca` means conversational amplu.
- Adapt the suffix for other style/detail combinations if needed.

After creating a new report, update `examples/README.md` with a link to it.

## Final Requirements

- Mention which rubrics or data can refine a final version, but phrase them as
  useful suggestions in `Rubrici incomplete si date de confirmat`.
- Keep the report in Markdown format.

## Quality Check

Before finishing:

1. Search the generated report for conflict markers and unfinished TODOs.
2. Check that indexes follow the repository template.
3. Check that the wellbeing scale table has exactly 17 rows: 8 vectors and 9
   individual boxes.
4. Check that the report path and README link are correct.
5. Summarize what was generated and mention any missing input data.
