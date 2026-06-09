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
  index.md
  01-esenta.md
  02-arhetip.md
  03-lumina.md
  04-umbra.md
  05-lectii.md
  06-directii-de-dezvoltare.md
  07-exemple.md
```

## Observatii

Structura este gandita pentru editare manuala acum si conversie automata ulterior.
Cand aplicatia va avea nevoie de continut programatic, putem genera un index JSON
din fisierele Markdown.

## Director: knowledge_base

`knowledge_base/` este sursa principala de continut numerologic.

Include:

- `knowledge_base/vibratii/`: interpretari pentru vibratiile 1-9 si numerele maestre.
- `knowledge_base/calcule/`: metode, formule, semnificatii si exemple de calcul.

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

## Calcule de timp si cicluri

Calcule documentate initial:

- `vibratia-anului`: vibratia numerologica asociata unui an.
- `tema-anului`: lectia sau accentul principal al unei perioade anuale.
- `ani-importanti-interiori`: ani cu accent pe procese personale si interioare.
- `ani-importanti-exteriori`: ani cu accent pe manifestari vizibile si contexte exterioare.
- `cicluri-7-ani`: cicluri recurente de sapte ani.
- `cicluri-9-ani`: cicluri recurente de noua ani.
- `cicluri-12-ani`: cicluri recurente de doisprezece ani.

## Entitate: exemplu de calcul

Campuri propuse:

- `titlu`: numele exemplului.
- `input`: datele initiale.
- `pasi`: lista de pasi intermediari.
- `rezultat`: rezultatul final.
- `interpretare`: textul explicativ asociat rezultatului.
