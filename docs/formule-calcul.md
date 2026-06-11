# Formule de calcul adoptate

Acest document centralizeaza formulele numerologice adoptate in proiect.

## Nume

- `numarul de exprimare`: fiecare componenta a numelui
  complet se transforma in valori numerologice, se reduce separat la o cifra,
  apoi componentele reduse se aduna si se reduc din nou la 1-9.
- `numarul intim`: vocalele din numele complet se transforma in valori
  numerologice, se aduna si se reduc la o cifra.
- `numarul de realizare`: consoanele din numele complet se transforma in valori
  numerologice, se aduna si se reduc la o cifra.
- `numarul activ`: prenumele se transforma in valori numerologice, se aduna si
  se reduce la o singura cifra.
- `numarul ereditar`: numele de familie se transforma in valori numerologice,
  se aduna si se reduce la o singura cifra.
- `numarul ereditar karmic`: numele de familie se transforma in valori
  numerologice, valorile se aduna, iar daca rezultatul este mai mare de 22 se
  scade 22 pana cand ramane un numar intre 1 si 22.
- `destin`: aceeasi formula ca numarul de exprimare, folosita ca axa a numelui complet.
- `nume inainte/dupa casatorie`: se calculeaza separat, apoi se compara
  numarul de exprimare, matricea numelui, karma numelui si karma neamului.

## Data nasterii

- `vibratia interioara`: ziua nasterii redusa la 1-9.
- `vibratia exterioara`: luna nasterii redusa la 1-9.
- `vibratia cosmica`: anul nasterii redus la 1-9.
- `vibratia globala`: ziua + luna, reduse la 1-9.
- `vibratia destinului`: ziua + luna + anul, reduse la 1-9.
- `calea destinului`: suma tuturor cifrelor datei, pastrata neredusa complet.
- `soarta`: calcul istoric din proiect, echivalent operational cu reducerea
  caii destinului; de revizuit fata de denumirea `vibratia destinului`.
- `tema vietii`: suma dintre soarta si destin, redusa la 1-9.

## Timp si cicluri

- `vibratia anului personal`: `reducere_numerologica(ziua nasterii + luna
  nasterii + anul analizat)`. Rezultatul descrie energia anului calendaristic
  pentru persoana si nu se confunda cu anul personal din ciclul de 9 ani, care
  se citeste intre doua aniversari.
- `ani importanti interiori`: secventa porneste din anul nasterii; fiecare an
  important interior se obtine prin `an_curent + reducere_numerologica(an_curent)`.
- `ani importanti exteriori`: secventa porneste din anul nasterii; fiecare an
  important exterior se obtine prin `an_curent + suma_cifrelor(an_curent)`,
  fara reducerea sumei la o singura cifra.
- `lectii de viata`: `zi x luna x an`; cifrele produsului se aplica ciclic peste anii de viata.
- `cicluri de 7 ani`: formula operationala pentru ritm secundar de praguri de
  varsta, sustinuta de referinte web generale, dar fara sursa bibliografica
  interna explicita; `floor(varsta / 7) + 1`, pozitie `varsta % 7 + 1`.
- `cicluri de 9 ani`: ciclul se construieste de la data nasterii, pe perioade
  dintre doua aniversari; anul personal 1 incepe la nastere, apoi urmeaza anii
  personali 2-9, dupa care ciclul se reia. Calcul rapid dupa varsta implinita:
  `floor(varsta / 9) + 1`, pozitie `varsta % 9 + 1`.
- `cicluri de 12 ani`: ritm larg pentru graficul sortii si destinului, ales
  cand predomina energia feminina; calcul rapid dupa varsta:
  `floor(varsta / 12) + 1`, pozitie `varsta % 12 + 1`.

## Pinacluri

- `oportunitate 1`: luna redusa + zi redusa.
- `oportunitate 2`: zi redusa + an redus.
- `oportunitate 3`: oportunitate 1 + oportunitate 2.
- `oportunitate 4`: luna redusa + an redus.
- `provocare 1`: diferenta absoluta dintre ziua redusa si luna redusa.
- `provocare 2`: diferenta absoluta dintre ziua redusa si anul redus.
- `provocare 3`: diferenta absoluta dintre provocare 1 si provocare 2.
- `provocare 4`: diferenta absoluta dintre luna redusa si anul redus.
- `sfarsit pinaclu 1`: `36 - soarta`.
- `sfarsit pinaclu 2`: `sfarsit pinaclu 1 + 9`.
- `sfarsit pinaclu 3`: `sfarsit pinaclu 2 + 9`.
- pinaclul 4 incepe dupa finalul pinaclului 3 si ramane activ pana la finalul vietii.

## Karma

- `lectii karmice`: numerele 1-9 absente din valorile literelor numelui.
- `datorii karmice`: aparitia numerelor 13, 14, 16 sau 19 in totaluri importante.
- `karma neamului`: aceeasi analiza karmica, aplicata pe numele de familie.
- `karma neamului inainte/dupa casatorie`: analiza separata pe numele de familie
  purtat inainte si dupa schimbarea numelui.

## Patratul lui Pitagora

- se foloseste metoda cu patru numere de lucru din
  `knowledge_base/calcule/patratul-lui-pitagora/01-metoda.md`;
- matricea datei se construieste din data nasterii si cele patru numere de lucru;
- matricea numelui se construieste separat din valorile literelor numelui complet,
  plus numarul final de exprimare;
- cele doua matrici se compara, dar nu se combina automat;
- vectorii se calculeaza ca total de aparitii pe fiecare linie;
- vectorii se sorteaza descrescator dupa valoare si se analizeaza la comun.

## Surse externe consultate

Sursele externe au fost folosite doar pentru completarea formulelor care nu erau
inca stabilite in proiect:

- World Numerology: pinacluri, varsta `36 - Life Path` si cicluri de cate 9 ani.
- Numerologist.com: confirmare pentru durata pinaclurilor.
- World Numerology si Numerologist.com: lectii karmice ca numere lipsa din numele complet.
- Seventh Life Path si World Numerology: numar de expresie / destin din numele complet.
- Astrology Future Eye, Almanac si alte surse de numerologie generala: vibratia anului personal din zi, luna si anul analizat.
- Formula `lectii de viata = zi x luna x an` este formula de lucru adoptata
  intern in proiect si trebuie tratata separat de formulele clasice pentru
  calea vietii / soarta.

Formulele marcate ca `formula de lucru` trebuie validate editorial inainte de
publicarea finala.
