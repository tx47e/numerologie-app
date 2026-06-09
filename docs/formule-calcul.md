# Formule de calcul adoptate

Acest document centralizeaza formulele numerologice adoptate in proiect.

## Nume

- `vibratia numelui`: suma valorilor literelor din numele complet, redusa la 1-9.
- `destin`: aceeasi formula ca vibratia numelui, folosita ca axa a numelui complet.

## Data nasterii

- `vibratia interioara`: ziua nasterii redusa la 1-9.
- `vibratia exterioara`: luna nasterii redusa la 1-9.
- `soarta`: suma cifrelor din data completa de nastere, redusa la 1-9.
- `tema vietii`: suma dintre soarta si destin, redusa la 1-9.

## Timp si cicluri

- `vibratia anului`: ziua + luna + anul analizat, reduse la 1-9.
- `tema anului`: interpretarea vibratiei anului.
- `ani importanti interiori`: ani in care vibratia anului este egala cu vibratia interioara.
- `ani importanti exteriori`: ani in care vibratia anului este egala cu vibratia exterioara.
- `cicluri de 7 ani`: `floor(varsta / 7) + 1`, pozitie `varsta % 7 + 1`.
- `cicluri de 9 ani`: `floor(varsta / 9) + 1`, pozitie `varsta % 9 + 1`.
- `cicluri de 12 ani`: `floor(varsta / 12) + 1`, pozitie `varsta % 12 + 1`.

## Pinacluri

- `pinaclu 1`: luna redusa + zi redusa.
- `pinaclu 2`: zi redusa + an redus.
- `pinaclu 3`: pinaclu 1 + pinaclu 2.
- `pinaclu 4`: luna redusa + an redus.
- `provocarile`: diferente absolute intre aceleasi baze.
- `sfarsit pinaclu 1`: `36 - soarta`.
- urmatoarele doua pinacluri dureaza cate 9 ani.

## Karma

- `lectii karmice`: numerele 1-9 absente din valorile literelor numelui.
- `datorii karmice`: aparitia numerelor 13, 14, 16 sau 19 in totaluri importante.
- `karma neamului`: aceeasi analiza karmica, aplicata pe numele de familie.

## Patratul lui Pitagora

- se foloseste metoda cu patru numere de lucru din
  `knowledge_base/calcule/patratul-lui-pitagora/metoda.md`;
- vectorii se calculeaza ca total de aparitii pe fiecare linie;
- vectorii se sorteaza descrescator dupa valoare si se analizeaza la comun.

## Surse externe consultate

Sursele externe au fost folosite doar pentru completarea formulelor care nu erau
inca stabilite in proiect:

- World Numerology: pinacluri, varsta `36 - Life Path` si cicluri de cate 9 ani.
- Numerologist.com: confirmare pentru durata pinaclurilor.
- World Numerology si Numerologist.com: lectii karmice ca numere lipsa din numele complet.
- Seventh Life Path si World Numerology: numar de expresie / destin din numele complet.
- Astrology Future Eye, Almanac si alte surse de numerologie generala: an personal din zi, luna si anul analizat.

Formulele marcate ca `formula de lucru` trebuie validate editorial inainte de
publicarea finala.
