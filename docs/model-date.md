# Model de date

Acest document fixeaza contractul minim de date pentru aplicatie. Sursa
editoriala ramane Markdown in `knowledge_base/`, iar fisierul JSON generat este
un artefact regenerabil pentru consum programatic.

## Decizie

- Continutul se editeaza in continuare in Markdown.
- Aplicatia va consuma initial `generated/index.json`.
- O baza de date poate fi adaugata ulterior doar daca apar nevoi reale de
  cautare avansata, conturi, salvare rapoarte sau administrare de continut.

## Schema: vibratie

```json
{
  "numar": 1,
  "titlu": "Vibratia 1",
  "slug": "vibratia-1",
  "tip": "baza",
  "reduce_la": null,
  "cale": "knowledge_base/vibratii/vibratia-1",
  "capitole": []
}
```

Campuri:

- `numar`: numarul vibratiei, inclusiv 11, 22 sau 33.
- `titlu`: titlul afisat in interfata.
- `slug`: identificator stabil derivat din director.
- `tip`: `baza` pentru 1-9, `maestru` pentru 11, 22, 33.
- `reduce_la`: vibratia de baza asociata numerelor maestre.
- `cale`: directorul sursa.
- `capitole`: lista capitolelor disponibile.

## Schema: capitol

```json
{
  "ordine": 1,
  "slug": "esenta",
  "titlu": "Esenta",
  "fisier": "knowledge_base/vibratii/vibratia-1/01-esenta.md",
  "continut": "...",
  "metadate": {
    "cuvinte_cheie": [],
    "teme_principale": [],
    "recomandari": [],
    "avertismente": [],
    "exemple": []
  }
}
```

Campurile din `metadate` sunt optionale editorial in Markdown, dar sunt prezente
in JSON ca structura stabila pentru dezvoltarea aplicatiei.

## Schema: calcul

```json
{
  "slug": "vibratia-interioara",
  "titlu": "Vibratia interioara",
  "categorie": "vibratii-personale",
  "cale": "knowledge_base/calcule/vibratii-personale/vibratia-interioara",
  "inputuri": ["zi_nastere"],
  "fisiere": {
    "README": "...",
    "metoda": "...",
    "semnificatii": "...",
    "exemple": "...",
    "observatii": "..."
  }
}
```

Campuri:

- `slug`: identificatorul calculului.
- `titlu`: titlul afisat, extras din primul heading Markdown sau derivat din slug.
- `categorie`: directorul functional din `knowledge_base/calcule/`.
- `cale`: directorul sursa sau fisierul sursa pentru calcule simple.
- `inputuri`: lista canonica de inputuri asteptate.
- `fisiere`: fisierele Markdown asociate calculului.

## Schema: exemplu de calcul

Exemplele raman in fisierele `02-exemple.md`, dar structura recomandata pentru
continut este:

```json
{
  "titlu": "Exemplu",
  "input": {},
  "pasi": [],
  "rezultat": {},
  "interpretare": ""
}
```

Cand exemplele vor trebui afisate separat in aplicatie, se poate adauga un
extractor dedicat fara schimbarea continutului sursa.

## Inputuri canonice

- `zi_nastere`
- `luna_nastere`
- `an_nastere`
- `data_nasterii`
- `nume_complet`
- `nume_familie`
- `an_analizat`
- `interval_ani`
- `varsta`

## Reguli de generare

- `generated/index.json` nu se editeaza manual.
- Ordinea vibratiilor este numerica: 1-9, 11, 22, 33.
- Ordinea capitolelor este data de prefixul numeric din numele fisierului.
- Fisierele temporare `_sursa-initiala.md` sunt ignorate.
- Continutul Markdown este inclus integral pentru prototipare si poate fi scos
  ulterior daca aplicatia va incarca fisierele separat.
