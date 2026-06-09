# Structura de date

Acest document descrie modelul initial pentru baza de informatii numerologice.

## Entitate: vibratie

Campuri propuse:

- `numar`: valoare intre 1 si 9.
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
vibratii/vibratia-1/
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
