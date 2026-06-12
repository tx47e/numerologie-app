# Structura de date

Acest document descrie modelul initial pentru baza de informatii numerologice.

## Entitate: vibratie

Campuri propuse:

- `numar`: valoare intre 1 si 9 sau numar maestru, de exemplu 11, 22, 33.
- `titlu`: titlul afisat, de exemplu `Vibratia 1`.
- `slug`: identificator stabil, de exemplu `vibratia-1`.
- `capitole`: lista de capitole disponibile.

## Entitate: capitol

Campuri propuse:

- `ordine`: ordinea capitolului in afisare.
- `slug`: identificator stabil, de exemplu `esenta`.
- `titlu`: titlul capitolului.
- `fisier`: calea catre fisierul Markdown.
- `continut`: continutul incarcat din Markdown.

## Capitole initiale

| Ordine | Slug | Titlu | Fisier |
| --- | --- | --- | --- |
| 1 | `esenta` | Esenta | `01-esenta.md` |
| 2 | `arhetip` | Arhetip | `02-arhetip.md` |
| 3 | `lumina` | Lumina | `03-lumina.md` |
| 4 | `umbra` | Umbra | `04-umbra.md` |
| 5 | `lectii` | Lectii | `05-lectii.md` |
| 6 | `directii-de-dezvoltare` | Directii de dezvoltare | `06-directii-de-dezvoltare.md` |
| 7 | `exemple` | Exemple | `07-exemple.md` |

## Cale continut

Exemplu pentru vibratia 1:

```text
knowledge_base/vibratii/vibratia-1/
  README.md
  01-esenta.md
  02-arhetip.md
  03-lumina.md
  04-umbra.md
  05-lectii.md
  06-directii-de-dezvoltare.md
  07-exemple.md
```

## Observatii

Structura este gandita pentru editare manuala in Markdown si conversie automata
in JSON. Contractul detaliat este documentat in `docs/model-date.md`, iar
artefactul consumabil de aplicatie se genereaza in `generated/index.json`.

## Director: knowledge_base

`knowledge_base/` este sursa principala de continut numerologic.

Include:

- `knowledge_base/vibratii/`: interpretari pentru vibratiile 1-9 si numerele maestre.
- `knowledge_base/calcule/`: metode, formule, semnificatii si exemple de calcul.
- `knowledge_base/tarot/`: interpretari pentru Arcanele Majore si analogii simbolice.

Acest director trebuie tratat ca baza de cunoastere a aplicatiei, separata de
documentatia de management a proiectului din `docs/`.

## Entitate: calcul

Campuri propuse:

- `slug`: identificator stabil, de exemplu `vibratia-interioara`.
- `titlu`: titlul afisat.
- `categorie`: gruparea calculului, de exemplu `nume` sau `timp-si-cicluri`.
- `inputuri`: datele necesare pentru calcul.
- `metoda`: calea catre fisierul care descrie formula.
- `semnificatii`: calea catre interpretarea rezultatelor.
- `exemple`: calea catre exemplele de calcul.
- `observatii`: reguli speciale sau exceptii.

## Entitate: arcana majora

Campuri propuse:

- `numar`: numarul arcanei.
- `titlu_en`: numele in engleza, de exemplu `The Hierophant`.
- `titlu_ro`: numele in romana, de exemplu `Marele Preot`.
- `slug`: identificator stabil, de exemplu `05-marele-preot`.
- `plusuri`: expresii constructive ale arcanei.
- `minusuri`: expresii dezechilibrate sau imature.
- `cheie_de_integrare`: directia de lucru cu simbolul.

## Entitate: arcana minora

Campuri propuse:

- `suita`: una dintre `bate`, `cupe`, `sabii`, `monede`.
- `element`: foc, apa, aer sau pamant.
- `rang`: As, 2-10, Paj, Cavaler, Regina sau Rege.
- `titlu`: titlul afisat.
- `slug`: identificator stabil.
- `plusuri`: expresii constructive ale cartii.
- `minusuri`: expresii dezechilibrate sau imature.
- `cheie_de_integrare`: directia de lucru cu simbolul.

## Cale continut tarot

Exemplu pentru Marele Preot:

```text
knowledge_base/tarot/arcane-majore/
  README.md
  05-marele-preot.md
```

Exemplu pentru Arcanele Minore:

```text
knowledge_base/tarot/arcane-minore/
  README.md
  bate/
    README.md
  cupe/
    README.md
  sabii/
    README.md
  monede/
    README.md
```

## Calcule de timp si cicluri

Calcule documentate initial:

- `vibratia-anului-personal`: vibratia numerologica asociata unui an calendaristic pentru o persoana.
- `ani-importanti-interiori`: ani cu accent pe procese personale si interioare.
- `ani-importanti-exteriori`: ani cu accent pe manifestari vizibile si contexte exterioare.
- `cicluri-7-ani`: cicluri recurente de sapte ani.
- `cicluri-9-ani`: cicluri recurente de noua ani.
- `cicluri-12-ani`: cicluri recurente de doisprezece ani.
- `karma-zilei-de-nastere`: program karmic din ziua nasterii.
- `karma-lunii-de-nastere`: datorie karmica din luna nasterii.
- `karma-din-calea-destinului`: suma cifrelor datei citita karmic.
- `numarul-ereditar-karmic`: numarul neamului 1-22; termenul `karma
  neamului` este doar alias pentru acest calcul.

## Entitate: exemplu de calcul

Campuri propuse:

- `titlu`: numele exemplului.
- `input`: datele initiale.
- `pasi`: lista de pasi intermediari.
- `rezultat`: rezultatul final.
- `interpretare`: textul explicativ asociat rezultatului.
