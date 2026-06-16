# Template lucrare numerologie

Acest template este folosit pentru generarea unei lucrari numerologice pe baza
documentatiei finisate din `knowledge_base/`.

## Regula de redactare

Lucrarea trebuie sa fie clara pentru un cititor obisnuit, dar formulata ingrijit.
Descrierile ample se folosesc doar acolo unde apare un concept, un calcul sau o
metoda care are nevoie de explicatie: vibratii, karma, matrice, scara bunastarii,
nume, punti, pinacluri, cicluri, ezoterism si aplicabilitate.

Nu se adauga descrieri ample la date simple de intrare, liste administrative sau
rubrici evidente. Tabelele sunt suport de calcul; dupa tabelele importante se
scrie interpretare cursiva, in paragrafe firesti. Tonul trebuie sa fie academic
si accesibil: ideile se explica limpede, cu legaturi intre concepte, iar unde se
potriveste se poate folosi o formulare discret poetica, legata de viata de zi cu
zi.

Toate tabelele din lucrare trebuie incadrate si asezate cu grija. Textul din
celule, mai ales din capul de tabel, nu trebuie rupt sau despartit in mod
nefiresc. Daca o coloana poate fi redusa fara sa intrerupa textul, se reduce;
daca o coloana are nevoie de mai mult spatiu, se mareste si se ajusteaza
celelalte coloane. Prioritatea este lizibilitatea: denumirile, formulele si
observatiile trebuie sa ramana clare, compacte si usor de urmarit.

Interpretarea nu trebuie sa fie o insiruire mecanica de semnificatii. Fiecare
rezultat se leaga de restul lucrarii si se traduce in termeni practici: cum se
vede in relatii, munca, decizii, ritm personal, maturizare si directie de viata.

## Regula de indexare editoriala

Fiecare lucrare trebuie sa poata fi citata ca un document de norme. De aceea,
fiecare element important primeste un cod de index vizibil si stabil, astfel incat
se poate face trimitere exacta la un capitol, subtitlu, paragraf, tabel, grafic
sau interpretare.

Formatul obligatoriu este indexul afisat pe linia separata de dinaintea
elementului.
Indexul nu se scrie niciodata pe acelasi rand cu titlul, subtitlul, paragraful,
tabelul, graficul, interpretarea, lista sau blocul de calcul:

```text
Index: COD-LUCRARE-TIP-NNN

```

Unde:

- `COD-LUCRARE` identifica persoana si versiunea lucrarii, de exemplu
  `SAB-19840417-V3`.
- `TIP` identifica elementul: `CAP` pentru capitol, `SUB` pentru subtitlu,
  `P` pentru paragraf, inclusiv interpretare, `T` pentru tabel, `G` pentru
  grafic, `L` pentru lista, `C` pentru bloc de cod sau calcul.
- `NNN` este numarul curent al elementului in lucrare, cu trei cifre:
  `001`, `002`, `003`.

Reguli de aplicare:

- Titlul principal al lucrarii primeste index de tip `CAP` pe linie separata,
  cu o linie goala intre index si titlu.
- Fiecare capitol `##` primeste index de tip `CAP` pe linia imediat anterioara
  capitolului, cu o linie goala intre index si capitol.
- Fiecare subtitlu `###` primeste index de tip `SUB` pe linia imediat anterioara
  subtitlului, cu o linie goala intre index si subtitlu.
- Fiecare paragraf cursiv primeste index de tip `P` pe linia imediat anterioara
  paragrafului, cu o linie goala intre index si paragraf, cu exceptia liniilor
  din tabele si a listelor scurte.
- Fiecare tabel primeste o linie de index imediat inaintea tabelului, de tip
  `T`.
- Fiecare grafic sau reprezentare vizuala primeste index de tip `G`.
- Fiecare bloc de calcul sau bloc de cod primeste index de tip `C`.
- Fiecare interpretare explicita de dupa tabel primeste index de tip `P`, ca
  orice paragraf interpretativ. Nu se foloseste un tip separat pentru
  interpretare.
- Indexurile nu inlocuiesc titlurile si nu schimba continutul interpretarii; ele
  sunt repere de citare si raman intotdeauna pe rand separat, ca bloc propriu.

## Regula pentru exprimari reutilizabile

Cand se interpreteaza un calcul, o vibratie sau un termen numerologic recurent,
se verifica mai intai `knowledge_base/exprimari/`. Daca exista deja o exprimare
potrivita pentru rezultatul calculat, aceasta se foloseste ca baza si se adapteaza
la persoana analizata, la nivelul de detaliere si la stilul cerut in prompt.

Pot exista mai multe exprimari pentru acelasi rezultat, acelasi stil, acelasi
nivel de detaliere si acelasi context scurt. Cand se lucreaza cu mai multe
persoane apropiate, de exemplu membri ai aceleiasi familii, se evita repetarea
aceleiasi exprimari la fiecare persoana. Se alege o varianta diferita, daca
exista, sau se genereaza o formulare noua cand biblioteca nu are destula
varietate.

Se genereaza o exprimare noua daca variantele existente nu se potrivesc
contextului, stilului, nivelului de detaliere, legaturii cu restul lucrarii sau
nevoii de varietate intre lucrari apropiate. Daca noua formulare este valoroasa
si poate fi refolosita, ea se salveaza in fisierul temei potrivite din
`knowledge_base/exprimari/`.

Fiecare exprimare salvata trebuie sa aiba index numeric, stil, nivel de
detaliere, context scurt si lista lucrarilor in care a fost folosita. Formatul
minim este:

```markdown
### Varianta 001

- Stil: formal / conversational
- Nivel de detaliere: scurt / mediu / amplu / foarte amplu
- Context scurt:
- Lucrari unde a fost folosita:
  - `cale/catre/lucrare.md` - persoana / data / observatie scurta
- Data adaugarii: AAAA-LL-ZZ

Textul interpretarii...
```

## Cuprins

1. Sinteza scurta
2. Date de baza si calcule initiale
3. Karma din data nasterii
4. Matricea numerologica
5. Scara bunastarii
6. Numele
7. Pinacluri, oportunitati si provocari
8. Soarta si destinul
9. Lectii de viata si cicluri
10. Ezoterism si aplicabilitate
11. Concluzie finala
12. Rubrici de test
13. Nota despre persoane
14. Harta documentatie folosita

## Date lucrare

- Persoana analizata:
- Gen persoana: masculin / feminin
- Data nasterii:
- Nume complet folosit in analiza:
- Nume de familie folosit in analiza:
- Prenume folosit in analiza:
- Nume anterior / schimbat, daca exista: nu este cazul / de completat
- Intrebare personala sau tema principala:
- Data adaugarii in lista de persoane:
- Tip template folosit: template complet / maxim
- Nivel de detaliere: amplu / mediu / scurt
- Stil de adresare: formal / conversational
- Data realizarii lucrarii: `AAAA-LL-ZZ HH:MM`
- Status: de revizuit

## 1. Sinteza scurta

Scrie 3-5 paragrafe care prezinta firul principal al lucrarii. Sinteza nu trebuie
sa enumere toate calculele, ci sa arate ce se repeta, ce se intareste si ce tema
pare sa organizeze viata persoanei.

### Teme dominante

-
-
-

Dupa lista, explica in cateva paragrafe de ce aceste teme sunt dominante si cum
se pot vedea in viata de zi cu zi.

### Atentionari principale

-
-
-

Formuleaza atentionarile ca directii de constientizare, nu ca verdict. Arata ce
se poate dezechilibra si ce ajuta la maturizare.

## 2. Date de baza si calcule initiale

Datele de baza stabilesc fundatia numerica a lucrarii. Aici se extrage structura
de baza din data nasterii: interiorul, exteriorul, componenta cosmica, destinul
si puntile dintre ele.

### Vibratii esentiale

Vibratiile esentiale sunt primele repere ale lucrarii. Ele functioneaza ca o
harta de baza: ziua arata nucleul interior, luna arata modul de manifestare in
relatie cu lumea, iar anul adauga fundalul mai larg in care persoana isi traieste
drumul. Destinul si calea destinului arata directia in care aceste forte tind sa
se adune.

| Vibratie | Formula | Calcul | Rezultat | Descriere scurta |
| --- | --- | --- | --- | --- |
| Vibratia interioara | ziua redusa |  |  | Caracterul, lumea interioara, lutul. |
| Vibratia exterioara | luna redusa |  |  | Comportamentul, rolul social, vasul. |
| Vibratia cosmica fixa | primele doua cifre ale anului |  |  | Componenta subtila si constanta. |
| Vibratia cosmica variabila | ultimele doua cifre ale anului, reduse |  |  | Ce poate face omul concret in viata. |
| Vibratia cosmica totala | toate cifrele anului, reduse |  |  | Raportarea la totalitate/univers. |
| Vibratia globala | vibratia interioara + vibratia exterioara |  |  | Contextul de crestere si tensiunile. |
| Vibratia destinului | suma cifrelor datei, redusa |  |  | Vocatia, menirea, rezultatul. |
| Calea destinului | suma tuturor cifrelor datei, neredusa |  |  | Ce si cum are de facut. |

Dupa tabel, scrie cate o descriere ampla pentru fiecare vibratie calculata in
tabel: 8 descrieri in total. Fiecare descriere trebuie sa aiba minimum 100 de
cuvinte si sa explice atat rezultatul final, cat si treptele de calcul care au
dus la el. Daca, de exemplu, vibratia interioara se calculeaza `1 + 7 = 8`,
descrierea nu vorbeste doar despre `8`, ci si despre contributia lui `1`,
contributia lui `7` si felul in care ele se aduna in `8`.

Pentru fiecare vibratie, urmareste aceasta ordine:

1. numeste calculul si treptele lui;
2. explica pe scurt semnificatia fiecarei trepte;
3. explica rezultatul final;
4. arata cum se poate vedea aceasta vibratie in viata de zi cu zi;
5. leaga vibratia de restul profilului, fara sa repeti mecanic aceleasi idei.

La finalul celor 8 descrieri, scrie o interpretare integrata a vibratiilor. Arata
cum lucreaza impreuna ziua, luna si anul, unde exista armonie si unde apare
tensiune.

Pentru `Calea destinului`, foloseste regula `ce` si `cum`. Calea destinului
povesteste ce si cum are omul de facut prin viata ca sa isi realizeze destinul.
Inainte de interpretarea celor doua cifre, citeste categoria mare a caii
destinului: `4-9` cu `0` implicit in fata, `10-19` cu `1` in fata, `20-29` cu
`2` in fata, `30-39` cu `3` in fata, `40-48` cu `4` in fata. Explica pe scurt ce
tip de sanse, ajutoare, obstacole sau antrenament interior sugereaza categoria.
Nu prezenta categoria ca scara ierarhica; un numar mai mare nu inseamna
superioritate, ci alta proportie intre antrenament, sanse si obstacole.

Daca rezultatul este format din doua cifre, prima cifra raspunde la intrebarea
`ce are de facut?`, iar a doua cifra raspunde la intrebarea `cum face?`. Pentru
intrebarea `ce`, explica ce calitati ale primei cifre trebuie cultivate si ce
aspecte negative ale acelei cifre trebuie invinse. Pentru intrebarea `cum`,
explica polaritatea pozitiva a celei de-a doua cifre, fara caracteristicile de
polaritate minus. Daca rezultatul are o singura cifra, aceeasi cifra raspunde si
la `ce`, si la `cum`.

### Aspecte de indreptat si solutia

Aspectele de indreptat indica o zona de lucru constient. Nu arata o greseala a
persoanei, ci o tema care cere rafinare. Vibratia solutiei arata prin ce calitate
poate fi transformata tensiunea.

| Element | Calcul | Rezultat |
| --- | --- | --- |
| Calea destinului | suma tuturor cifrelor din data nasterii |  |
| Prima cifra din ziua nasterii |  |  |
| Aspecte de indreptat | calea destinului - 2 x prima cifra din zi |  |
| Vibratia solutiei | reducerea rezultatului |  |

Dupa tabel, scrie descrieri ample doar pentru aceste 3 elemente: calea destinului,
aspectele de indreptat si vibratia solutiei. Fiecare descriere trebuie sa aiba
minimum 100 de cuvinte. La calea destinului, repeta explicit interpretarea prin
categoria mare si prin intrebarile `ce?` si `cum?`, folosind regula de mai sus.

Prima cifra din ziua nasterii nu primeste descriere separata. Ea este doar element
tehnic folosit in formula pentru aspectele de indreptat.

Pentru aspectele de indreptat, explica trecerea completa: calea destinului,
scaderea dublului primei cifre din zi si rezultatul obtinut. Pentru vibratia
solutiei, explica reducerea rezultatului si felul in care solutia poate deveni
comportament practic, nu doar idee simbolica.

### Punti

Puntile arata distanta dintre straturi ale persoanei. Ele nu separa omul in
bucati, ci arata ce calitate poate impaca interiorul cu exteriorul, firea cu
destinul si valorile cu directia de viata.

In tabel, completeaza calculul numeric explicit si rezultatul obtinut. Puntea se
calculeaza ca diferenta dintre cele doua vibratii, citita ca valoare absoluta
atunci cand prima cifra este mai mica decat a doua. In coloana `Calcul` se scrie
operatia simpla cu cifrele persoanei, fara apostrofuri, backticks sau bare de
valoare absoluta, dupa modelul `2 - 7` sau `8 - 4`. In coloana `Rezultat` se
scrie cifra obtinuta din diferenta absoluta dintre cele doua valori; aceasta este
cifra care se interpreteaza.

| Punte | Calcul | Rezultat |
| --- | --- | --- |
| Interior - exterior | cifra interioara - cifra exterioara | cifra rezultata |
| Interior - destin | cifra interioara - cifra destinului | cifra rezultata |
| Exterior - destin | cifra exterioara - cifra destinului | cifra rezultata |
| Cosmic - destin | cifra cosmica totala - cifra destinului | cifra rezultata |

Dupa tabel, scrie cate o interpretare ampla pentru fiecare punte din tabel: 4
interpretari in total. Metoda de interpretare este aceeasi pentru toate puntile:
puntea nu inlocuieste cele doua vibratii comparate si nu le anuleaza, ci arata
calitatea prin care ele pot fi armonizate. Mai intai explica ce reprezinta prima
vibratie, apoi ce reprezinta a doua vibratie, apoi arata ca cifra rezultata prin
scadere este energia prin care cele doua concepte pot colabora.

Pentru fiecare punte, foloseste aceasta logica:

1. Interior - exterior: explica felul in care cine este omul in interior se
   armonizeaza cu felul in care se manifesta in exterior, prin cifra puntii.
2. Interior - destin: explica felul in care cine este omul la interior se
   armonizeaza cu ceea ce are de devenit, prin cifra puntii.
3. Exterior - destin: explica felul in care comportamentul exterior si imaginea
   sociala se armonizeaza cu ceea ce are omul de devenit, prin cifra puntii.
4. Cosmic - destin: explica felul in care vibratia cosmica, adica ceea ce cere
   Universul sau fundalul mai larg al vietii, se armonizeaza cu ceea ce are omul
   de devenit, prin cifra puntii.

Nu adauga o sectiune separata de interpretare integrata a puntilor.

## 3. Karma din data nasterii

Karma din data nasterii se citeste ca tema de transformare. Ea nu se formuleaza
ca pedeapsa sau verdict, ci ca memorie, lectie si directie de maturizare.

### Karma zilei de nastere

| Zi / Arcana | Tema karmica | Ce trebuie transformat | Solutie |
| --- | --- | --- | --- |
|  |  |  |  |

### Karma lunii de nastere

| Luna | Tema karmica | Relatie-cheie | Directie de lucru |
| --- | --- | --- | --- |
|  |  |  |  |

### Karma din calea destinului

| Calea karmica | Categorie | Ajutoare / obstacole | Recomandare |
| --- | --- | --- | --- |
|  |  |  |  |

Dupa tabele, scrie o sinteza karmica. Leaga ziua, luna si calea destinului intr-o
idee coerenta: ce se cere vindecat, maturizat, dus mai departe sau folosit mai
constient.

## 4. Matricea numerologica

Matricea numerologica organizeaza cifrele in pozitii simbolice. Ea arata unde
energia este concentrata, unde lipseste sprijinul si cum se poate compensa un gol
prin constienta, ritm si exercitiu.

### Cod numerologic personal

| Operatie | Formula | Calcul | Rezultat | Descriere scurta |
| --- | --- | --- | --- | --- |
| Operatia 1 | suma tuturor cifrelor datei |  |  | Baza codului numerologic personal. |
| Operatia 2 | reducerea Operatiei 1 |  |  | Esenta redusa a primei sume. |
| Operatia 3 | Operatia 1 - 2 x prima cifra nenula din zi |  |  | Aspecte de indreptat / corectat in matrice. |
| Operatia 4 | reducerea Operatiei 3 |  |  | Vibratia solutiei sau a corectarii. |

### Sir complet de cifre - data nasterii

Se noteaza sirul complet folosit pentru matrice. Cifra `0` se pastreaza in sirul
explicativ, dar nu se introduce in matrice.

```text

```

### Matricea datei de nastere

| 1 | 4 | 7 |
| --- | --- | --- |
|  |  |  |
| 2 | 5 | 8 |
|  |  |  |
| 3 | 6 | 9 |
|  |  |  |

### Citirea matricei

- Casute dominante:
- Casute lipsa:
- Element predominant:
- Elemente slabe:
- Trasee informationale importante:
- Observatii despre paritate:

### Interpretare

Scrie interpretarea matricei ca sistem. Explica pe intelesul cititorului ce
inseamna cifrele dominante, ce inseamna cifrele lipsa si cum se pot vedea aceste
lucruri in ritmul zilnic, in relatii, munca si decizii.

## 5. Scara bunastarii

Scara bunastarii se asaza imediat dupa matricea numerologica, pentru ca foloseste
valorile casutelor si vectorilor din matrice. Ea arata unde persoana are resurse
naturale si unde apar goluri care cer grija, exercitiu sau sprijin.

### Valorile casutelor

| Casuta | Cantitatea cifrelor | Formula valorii totale | Valoare totala | Explicatie simpla |
| --- | --- | --- | --- | --- |
| 1 |  | 1 x cantitatea |  |  |
| 2 |  | 2 x cantitatea |  |  |
| 3 |  | 3 x cantitatea |  |  |
| 4 |  | 4 x cantitatea |  |  |
| 5 |  | 5 x cantitatea |  |  |
| 6 |  | 6 x cantitatea |  |  |
| 7 |  | 7 x cantitatea |  |  |
| 8 |  | 8 x cantitatea |  |  |
| 9 |  | 9 x cantitatea |  |  |

Dupa tabel, scrie o explicatie cursiva pentru valorile casutelor. Explica pe
scurt cantitatea fiecarei cifre importante, valoarea totala care rezulta si ce
inseamna diferenta dintre o casuta goala, o casuta prezenta discret si o casuta
dominanta. Interpretarea trebuie sa fie simpla si aplicabila: ce resursa arata
casuta, unde poate aparea excesul si ce poate face persoana in viata de zi cu zi
pentru a folosi echilibrat acea energie.

### Valorile vectorilor

| Vector | Casute incluse | Cantitatea cifrelor pe casute | Formula valorii totale | Valoare totala | Sens |
| --- | --- | --- | --- | --- | --- |
| 123 | 1, 2, 3 |  | valoare 1 + valoare 2 + valoare 3 |  | Bunastare energetica |
| 456 | 4, 5, 6 |  | valoare 4 + valoare 5 + valoare 6 |  | Bunastare volutiva |
| 789 | 7, 8, 9 |  | valoare 7 + valoare 8 + valoare 9 |  | Bunastare creativa |
| 147 | 1, 4, 7 |  | valoare 1 + valoare 4 + valoare 7 |  | Bunastare spirituala |
| 258 | 2, 5, 8 |  | valoare 2 + valoare 5 + valoare 8 |  | Bunastare sociala |
| 369 | 3, 6, 9 |  | valoare 3 + valoare 6 + valoare 9 |  | Bunastare materiala |
| 159 | 1, 5, 9 |  | valoare 1 + valoare 5 + valoare 9 |  | Bunastare in cariera |
| 357 | 3, 5, 7 |  | valoare 3 + valoare 5 + valoare 7 |  | Atingerea scopurilor |

Dupa tabel, scrie cate o interpretare mai ampla pentru fiecare vector: 8
interpretari in total. Pentru fiecare vector, explica mai intai cantitatea
cifrelor din casutele care il formeaza, apoi valoarea totala rezultata si sensul
ei. Arata daca vectorul este sustinut de toate cele trei casute sau daca se
sprijina mai mult pe una singura, pentru ca aceasta diferenta schimba felul in
care se traieste bunastarea respectiva. Interpretarea trebuie sa lege calculul
de comportamente concrete: energie, vointa, creativitate, relatii, munca,
materialitate, cariera si atingerea scopurilor.

### Scara rezultata

```text
```

### Scara bunastarii

In coloana `Cantitate`, nu trece doar numarul de aparitii. Afiseaza cifrele
prezente efectiv in fiecare vector sau casuta: `77 / 8 / 9`, `444 / 5 / -`,
`33 / - / 9`. Cifrele repetate se scriu lipit, fara minus intre ele. Foloseste
`-` numai acolo unde o cifra lipseste.

| Ordine | Tip | Denumire | Cantitate | Valoare totala | Observatie |
| --- | --- | --- | --- | --- | --- |
| 1 | vector / casuta |  |  |  |  |
| 2 | vector / casuta |  |  |  |  |
| 3 | vector / casuta |  |  |  |  |
| 4 | vector / casuta |  |  |  |  |
| 5 | vector / casuta |  |  |  |  |
| 6 | vector / casuta |  |  |  |  |
| 7 | vector / casuta |  |  |  |  |
| 8 | vector / casuta |  |  |  |  |
| 9 | vector / casuta |  |  |  |  |
| 10 | vector / casuta |  |  |  |  |
| 11 | vector / casuta |  |  |  |  |
| 12 | vector / casuta |  |  |  |  |
| 13 | vector / casuta |  |  |  |  |
| 14 | vector / casuta |  |  |  |  |
| 15 | vector / casuta |  |  |  |  |
| 16 | vector / casuta |  |  |  |  |
| 17 | vector / casuta |  |  |  |  |

Dupa scara bunastarii, treci direct la interpretare, fara subtitlu separat.
Interpreteaza fiecare pozitie din tabel independent, in ordinea descrescatoare a
treptelor. Textul trebuie sa fie conversational, adresat direct persoanei. Prima
pozitie arata unde omul se simte cel mai bine si cel mai fericit in aceasta
viata. Explica apoi de ce are nevoie acea treapta pentru a se manifesta: fiecare
vector sau casuta de mai jos sustine treapta de deasupra. Arata interdependenta
progresiva a scarii, dar pastreaza si citirea separata a fiecarui rand.

## 6. Numele

Numele arata felul in care persoana se exprima in lume si cum primeste o anumita
forma sociala. In lucrare, numele nu se trateaza ca simpla eticheta, ci ca strat
de manifestare: ce se arata, ce se mosteneste, ce se activeaza prin prenume si ce
se duce mai departe prin neam.

### Nume analizat

- Nume complet:
- Nume de familie:
- Prenume:
- Nume folosit curent:
- Context lingvistic:
- Nume anterior / schimbat, daca exista:
- Nume actual diferit, daca exista:
- Data aproximativa a schimbarii numelui, daca exista:

### Regula de lucru pentru nume

- Foloseste exact forma din fisa persoanei.
- Daca fisa foloseste `Nume, Prenume`, pastreaza forma aceea in lucrare.
- Calculeaza separat numele de familie, prenumele si numele complet.
- Nu folosi o forma scurta sau prescurtata daca nu apare explicit in fisa persoanei.
- Daca numele s-a schimbat, se analizeaza in paralel numele anterior si numele actual.
- Pentru numarul neamului, se pastreaza atentia pe numele de familie de la nastere, daca documentatia cere linia de sange.
- Daca exista un nume anterior / schimbat si un nume actual, pastreaza ambele
  nume in analiza. Explica faptul ca numele anterior poate pastra linia de
  origine, iar numele actual poate arata linia sociala si familiala activa;
  numarul ereditar karmic de sange ramane prezent intreaga viata.

### Numarul de exprimare

Numarul de exprimare se citeste ca personalitatea formata prin nume si ca
echivalent pe nume al vibratiei destinului din data de nastere. Dupa calcul,
compara rezultatul cu vibratia destinului deja calculata in capitolul de vibratii
esentiale: ideal este sa fie aceeasi cifra. Daca sunt cifre diferite, observa
daca ambele sunt pare sau ambele impare; aceasta arata o compatibilitate de ritm.
Daca una este para si cealalta impara, noteaza ca armonizarea dintre nume si
directia de destin poate cere mai mult efort constient.

| Calcul | Rezultat | Interpretare |
| --- | --- | --- |
|  |  |  |

### Analiza paralela pentru nume schimbat (optional)

Se include numai daca exista nume anterior / schimbat, adoptie, divort sau alta
schimbare explicita de nume.

| Strat analizat | Nume anterior / schimbat | Nume actual | Diferenta observata |
| --- | --- | --- | --- |
| Numarul de exprimare |  |  |  |
| Numarul intim |  |  |  |
| Numarul de realizare |  |  |  |
| Numarul activ |  |  |  |
| Numarul ereditar |  |  |  |
| Numarul neamului |  |  |  |

### Comparatie intre cele doua nume (optional)

- Ce intareste numele inainte de schimbare:
- Ce intareste numele dupa schimbare:
- Ce se pierde sau se slabeste:
- Ce se activeaza nou:
- Cum se raporteaza numele actual la matricea de baza:

### Numere derivate din nume

| Numar | Calcul | Rezultat | Interpretare |
| --- | --- | --- | --- |
| Numarul intim | vocale |  |  |
| Numarul de realizare | consoane |  |  |
| Numarul activ | prenume folosit |  |  |
| Numarul ereditar | nume de familie |  |  |
| Numarul neamului | nume ereditar karmic |  |  |

Pentru numarul intim, interpretarea se face intotdeauna in concordanta cu
vibratia interioara calculata din ziua nasterii. Compara ce isi doreste omul in
structura lui nativa cu ce amplifica numarul intim prin vocalele numelui. Arata
daca numele modifica, mentine sau amplifica eul ascuns, aspiratiile intime si
dorinte profunde ale persoanei.

Pentru numarul de realizare, interpretarea se face intotdeauna in concordanta cu
vibratia exterioara calculata din luna nasterii. Compara felul in care omul se
manifesta in exterior prin structura lui nativa cu felul in care numele sustine
sau franeaza realizarea concreta prin consoanele numelui. Arata daca numele
amplifica, mentine, modifica sau franeaza eul exterior si realizarile sociale sau
profesionale.

Pentru numarul neamului / numarul ereditar karmic, foloseste interpretarile din
`knowledge_base/calcule/nume/numarul-ereditar-karmic/03-interpretari-neam.md` ca
baza traditionala, dar cand scrii analiza persoanei adapteaza ocupatiile si
rolurile la societatea actuala. Nu modifica definitia traditionala, ci traduce-o
in forme moderne: de exemplu, mestesugar poate deveni specialist tehnic, designer,
producator, creator, artizan modern sau profesionist practic, dupa context.

Dupa tabel, scrie cate o descriere ampla pentru fiecare dintre cele 5 numere
derivate din nume: numarul intim, numarul de realizare, numarul activ, numarul
ereditar si numarul neamului. Fiecare descriere trebuie sa aiba minimum 100 de
cuvinte si sa explice calculul, treptele de reducere si sensul rezultatului.

Pentru fiecare numar, arata ce strat al persoanei descrie: interiorul dorintelor,
felul de realizare, energia prenumelui activ, mostenirea numelui de familie sau
tema de neam. Leaga rezultatul de numarul de exprimare, de vibratiile din data
nasterii si de matricea numelui, fara sa repeti mecanic aceeasi interpretare.

### Matricea numelui

Sir complet de cifre din nume:

```text

```

| 1 | 4 | 7 |
| --- | --- | --- |
|  |  |  |
| 2 | 5 | 8 |
|  |  |  |
| 3 | 6 | 9 |
|  |  |  |

### Comparare matricea numelui - matricea datei de nastere

Comparatia dintre matricea datei de nastere si matricea numelui se face dupa
metoda de citire comparativa din Patratul lui Pitagora. Se pastreaza separat
matricea datei si matricea numelui. Nu se mai calculeaza o a treia matrice.

Pentru fiecare cifra, compara casuta din matricea numelui cu aceeasi casuta din
matricea datei. In coloanele `Data` si `Nume`, nu scrie doar cantitatea numerica,
ci cifrele efective prezente in casuta: `1111`, `44`, `9`; daca cifra lipseste,
scrie `-`. Diferenta ramane numerica si se calculeaza ca nume minus data.

Daca numele depaseste data cu doua sau mai multe unitati, cifra este in exces in
nume. Excesul arata ca posesorul numelui isi poate dori, in interior, sa fie mai
mult pe tema acelei cifre decat ii este dat prin datele native. Daca cifra exista
in matricea datei, dar lipseste din matricea numelui, ea se noteaza ca lipsa in
nume; aceasta arata impresia interioara ca omul are mai putin din acea
caracteristica decat ii este dat prin datele native.

| Cifra | Data | Nume | Diferenta | Status comparativ | Observatie |
| --- | --- | --- | ---: | --- | --- |
| 1 |  |  |  | exces / sustinuta / lipsa in nume / potential de nume / absenta |  |
| 2 |  |  |  | exces / sustinuta / lipsa in nume / potential de nume / absenta |  |
| 3 |  |  |  | exces / sustinuta / lipsa in nume / potential de nume / absenta |  |
| 4 |  |  |  | exces / sustinuta / lipsa in nume / potential de nume / absenta |  |
| 5 |  |  |  | exces / sustinuta / lipsa in nume / potential de nume / absenta |  |
| 6 |  |  |  | exces / sustinuta / lipsa in nume / potential de nume / absenta |  |
| 7 |  |  |  | exces / sustinuta / lipsa in nume / potential de nume / absenta |  |
| 8 |  |  |  | exces / sustinuta / lipsa in nume / potential de nume / absenta |  |
| 9 |  |  |  | exces / sustinuta / lipsa in nume / potential de nume / absenta |  |

### Interpretare comparativa

- Cifre dominante in data si in nume:
- Casute sustinute, prezente in ambele matrici:
- Casute in exces, unde numele depaseste data cu doua sau mai multe unitati:
- Casute lipsa in nume, prezente in data dar absente in nume:
- Casute potential de nume, prezente in nume dar absente in data:
- Vectori activi in data fata de vectori activi in nume:
- Influenta generala a numelui asupra structurii de baza:

Scrie o concluzie despre relatia dintre nume si data nasterii: ce completeaza
numele, ce apare in exces, ce lipseste din nume si ce ramane potential fara suport
nativ. Nu formula comparatia ca verdict; explica felul in care numele poate crea
dorinte, impresii de lipsa, presiuni sau directii de exprimare fata de structura
primita prin data nasterii.

In concluzie, formuleaza explicit diferenta dintre exces si lipsa: cifrele in
exces arata ca persoana isi poate dori sa fie mai mult pe tema acelei cifre decat
poate sustine in realitate prin structura nativa, iar cifrele lipsa in nume arata
doar senzatia ca persoana are mai putin din acea caracteristica decat are de fapt.
Cand cifra exista in matricea datei, calitatea exista nativ; numele doar o face
mai putin vizibila sau mai greu de accesat interior.

## 7. Pinacluri, oportunitati si provocari

Pinaclurile descriu etape de viata, nu intamplari fixe. Ele arata ce tip de
energie devine mai vizibil intr-o perioada si ce calitate trebuie exersata pentru
ca acea etapa sa fie traita matur.

Valorile folosite pentru calcul sunt: zi ``, luna ``, an ``, vibratia
destinului ``.

### Calculul oportunitatilor si provocarilor

Oportunitatile arata resursa de crestere din fiecare etapa, iar provocarile
arata lectia care trebuie maturizata in aceeasi perioada.

| Etapa | Calcul oportunitate | Rezultat | Calcul provocare | Rezultat |
| --- | --- | --- | --- | --- |
| O1 / P1 | `luna + zi = ...` |  | `|zi - luna| = ...` |  |
| O2 / P2 | `zi + an = ...` |  | `|zi - an| = ...` |  |
| O3 / P3 | `O1 + O2 = ...` |  | `|P1 - P2| = ...` |  |
| O4 / P4 | `luna + an = ...` |  | `|luna - an| = ...` |  |

### Calculul pinaclurilor

Perioadele pinaclurilor se stabilesc pornind de la vibratia destinului.

| Pinaclu | Calcul perioada | Perioada rezultata | Oportunitate | Provocare |
| --- | --- | --- | --- | --- |
| Pinaclul 1 | `36 - vibratia destinului = ...` |  |  |  |
| Pinaclul 2 | `sfarsit pinaclu 1 + 9 = ...` |  |  |  |
| Pinaclul 3 | `sfarsit pinaclu 2 + 9 = ...` |  |  |  |
| Pinaclul 4 | dupa finalul pinaclului 3 |  |  |  |

### Tabel sinteza

| Pinaclu | Perioada | Oportunitate | Provocare | Interpretare |
| --- | --- | --- | --- | --- |
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |

Scrie interpretarea ca parcurs, dar incepe cu perioada actuala a persoanei:
calculeaza varsta la data lucrarii, spune explicit in ce pinaclu este acum, in
ce interval de varsta se afla si care sunt oportunitatea si provocarea active.
Apoi explica pe scurt cum primele pinacluri au pregatit etapa prezenta si ce
urmeaza in pinaclul urmator. Textul trebuie sa ramana conversational si aplicat:
ce poate face persoana concret pentru a folosi oportunitatile fara sa fie condusa
de provocari.

## 8. Soarta si destinul

Soarta si destinul se citesc impreuna ca doua linii grafice. Soarta arata cadrul
primit si linia de conditionare, calculata prin `ZZLL x AAAA`. Destinul arata
directia de implinire, calculata din aceeasi structura, dar cu zerourile
inlocuite cu `1`. Intre ele se observa apropierea, departarea, zona de confort,
punctele de intalnire si punctele de rascruce. Aceasta interpretare comparativa
poate fi numita si `tema vietii`, atunci cand in lucrare se formuleaza concluzia
de sinteza dintre cadrul primit si directia de implinire.

Atentie: in aceasta rubrica, soarta si destinul nu se reduc la o cifra si nu se
inlocuiesc cu vibratia destinului din data nasterii. Se pastreaza numarul grafic
de 7 cifre. Daca rezultatul inmultirii are mai putin de 7 cifre, se completeaza
cu zerouri in fata. Zona de confort se calculeaza ca suma cifrelor numarului
grafic impartita la 7.

### Calcul soarta

| Formula | Numar grafic | Zona de confort |
| --- | --- | --- |
| `ZZLL x AAAA` | numar de 7 cifre, fara reducere numerologica | `suma cifrelor / 7` |

### Calcul destin

| Formula | Numar grafic | Zona de confort |
| --- | --- | --- |
| `ZZLL ajustat x AAAA ajustat` | numar de 7 cifre, fara reducere numerologica | `suma cifrelor / 7` |

### Interpretare grafica

- Ciclul folosit: 10 ani / 12 ani
- Puncte de intalnire:
- Puncte de rascruce:
- Zone de confort:
- Zone de efort:

## 9. Lectii de viata si cicluri

Ciclurile arata ritmul in care anumite teme revin. Ele nu inlocuiesc libertatea
omului, ci ofera o harta a momentelor in care viata poate cere inceput, rabdare,
clarificare, incheiere sau reconstructie.

### Lectii de viata

Formula de calcul: `ziua x luna x anul`.

Pastreaza zerourile si repetitiile din sirul rezultat. Daca aceeasi lectie apare
in doi ani consecutivi, mentioneaza ca repetitia poate aduce un plus de cariera,
faima si bani, deoarece persoana sta mai mult in acea lectie si o invata mai
profund.

| Lectie | Perioada / an | Ce verifica viata | Recomandare |
| --- | --- | --- | --- |
|  |  |  |  |

### Ciclul de 9 ani

Regula de calcul pentru anul personal: anul personal `1` incepe la data nasterii
persoanei. De la urmatoarea aniversare incepe anul personal `2`, apoi ciclul
continua pana la `9` si se reia.

Tabelul se completeaza pentru 15 ani in total: 5 ani inainte de anul curent, anul
curent si 9 ani dupa anul curent.

| An | Varsta | An personal | Lectie | Interpretare |
| --- | --- | --- | --- | --- |
| anul curent - 5 |  |  |  |  |
| anul curent - 4 |  |  |  |  |
| anul curent - 3 |  |  |  |  |
| anul curent - 2 |  |  |  |  |
| anul curent - 1 |  |  |  |  |
| anul curent |  |  |  |  |
| anul curent + 1 |  |  |  |  |
| anul curent + 2 |  |  |  |  |
| anul curent + 3 |  |  |  |  |
| anul curent + 4 |  |  |  |  |
| anul curent + 5 |  |  |  |  |
| anul curent + 6 |  |  |  |  |
| anul curent + 7 |  |  |  |  |
| anul curent + 8 |  |  |  |  |
| anul curent + 9 |  |  |  |  |

### Ani importanti

Anii importanti interiori si exteriori se noteaza intr-un singur tabel cronologic
care incepe cu anul nasterii si merge pana la 10 ani peste anul curent al
lucrarii. Pentru fiecare an important rezultat in acest interval, marcheaza daca
este important interior, exterior sau ambele. Anul nasterii se trece ca punct de
pornire pentru ambele siruri.

| An | Varsta | Important interior | Important exterior | Observatie |
| --- | --- | --- | --- | --- |
| anul nasterii | 0 | punct de pornire | punct de pornire | inceputul celor doua siruri |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
| ... |  |  |  |  |

## 10. Ezoterism si aplicabilitate

Rubrica de ezoterism se scrie cu prudenta. Codurile ezoterice indica tipuri de
inclinatie, sensibilitate sau interes, nu certitudini despre persoana. Ele trebuie
legate de restul lucrarii si traduse in directii de studiu, protectie si folosire
responsabila a informatiei.

### Cod ezoteric

Data scrisa ca un singur numar:

Pentru calculul ezoteric, ziua si luna se scriu fara zerourile de completare din
fata. De exemplu, `06.11.1984` devine `6111984`, iar `17.04.1984` devine
`1741984`. Zerourile care fac parte din valoarea reala a zilei, lunii sau anului
se pastreaza.

```text
```

| Calcul | Cod | Tip de ezoterism | Esenta codului |
| --- | --- | --- | --- |
|  |  |  |  |

A doua impartire, doar daca primul cod nu este `0`. Daca primul cod este `0`,
se opreste calculul aici si se interpreteaza doar codul principal:

| Calcul | Cod secundar | Rezultat | Domenii deschise |
| --- | --- | --- | --- |
|  |  |  |  |

### Aplicabilitate profesionala - Tarot

| Aplicabil | Calcul | Arcana Tarot | Valenta constructiva | Valenta de umbra |
| --- | --- | --- | --- | --- |
| Nu |  |  |  |  |
| Da |  |  |  |  |

| Tip directie | Arcana | Profesii / directii |
| --- | --- | --- |
| De evitat ca directie profesionala principala |  |  |
| De aplicat / potrivite personal |  |  |

## 11. Concluzie finala

### Directia principala

Scrie directia de viata care apare cel mai des.

### Ce are de cultivat

-
-
-

### Ce are de evitat

-
-
-

### Recomandare practica

Scrie o recomandare concreta, legata de viata zilnica. Ea trebuie sa rezulte din
intreaga lucrare, nu dintr-un singur calcul.

## 12. Rubrici de test

Pentru prima testare a template-ului, se completeaza doar aceste rubrici:

1. Date de baza si vibratii esentiale.
2. Karma din data nasterii.
3. Matricea numerologica.
4. Scara bunastarii.
5. Numele: numarul de exprimare si numarul neamului.
6. Pinacluri, oportunitati si provocari.
7. Concluzie finala.

Restul rubricilor raman pregatite pentru extindere.

## 13. Nota despre persoane

- Fiecare fisa de persoana trebuie sa includa data adaugarii in lista de persoane.
- In lucrari, numele trebuie preluat din fisa de persoana, nu din memorie.
- Daca apar diferente de ortografie, se corecteaza inainte de calcule.

## 14. Harta documentatie folosita

Se folosesc in primul rand fisierele consolidate din `knowledge_base/`. Fisierele
din `bibliography/` raman surse primare si se consulta doar cand o rubrica nu
este inca detaliata suficient in documentatia de lucru.

Pentru formulari deja validate, se verifica si `knowledge_base/exprimari/`.
Aceste fisiere nu inlocuiesc metoda de calcul, ci ofera texte reutilizabile
pentru interpretari recurente: destin, vibratii, punti, scara bunastarii, nume si
alte rubrici similare.

| Rubrica din lucrare | Documentatie de lucru |
| --- | --- |
| Cifre si interpretari de baza | `knowledge_base/vibratii/`, `knowledge_base/calcule/patratul-lui-pitagora/04-semnificatii-pozitii.md` |
| Formulari validate pentru interpretari recurente | `knowledge_base/exprimari/` |
| Vibratii esentiale, globala, destin | `knowledge_base/calcule/vibratii-personale/` |
| Punti | `knowledge_base/calcule/vibratii-personale/punti/` |
| Aspecte de indreptat | `knowledge_base/calcule/vibratii-personale/aspecte-de-indreptat/`, `knowledge_base/calcule/vibratii-personale/calea-destinului/` |
| Karma zilei | `knowledge_base/calcule/karma/karma-zilei-de-nastere/` |
| Karma lunii | `knowledge_base/calcule/karma/karma-lunii-de-nastere/` |
| Karma caii destinului | `knowledge_base/calcule/karma/karma-din-calea-destinului/` |
| Matrice / patrat / cod personal | `knowledge_base/calcule/patratul-lui-pitagora/` |
| Citire comparativa matrice data - matrice nume | `knowledge_base/calcule/patratul-lui-pitagora/01-metoda.md`, sectiunea `Citire comparativa` |
| Scara bunastarii si vectorii | `knowledge_base/calcule/patratul-lui-pitagora/06-scara-bunastarii.md` |
| Nume, exprimare, matricea numelui | `knowledge_base/calcule/nume/` |
| Oportunitati, provocari, pinacluri | `knowledge_base/calcule/pinacluri/`; pentru oportunitati si provocari, verifica si `bibliography/09 - Oportunitati si provocari.md` |
| Soarta si destin | `knowledge_base/calcule/soarta-si-destin/` |
| Lectii de viata si cicluri | `knowledge_base/calcule/timp-si-cicluri/` |
| Ezoterism | `knowledge_base/calcule/ezoterism/` |
| Aplicabilitate profesionala | `knowledge_base/calcule/aplicabilitate-profesionala/` |

## Rubrici incomplete si date de confirmat

Aceasta rubrica nu trebuie sa sune ca o lista de erori sau lipsuri tehnice. Se
scrie ca o lista de sugestii utile pentru rafinarea lucrarii. Fiecare punct
trebuie sa spuna ce informatie ar merita confirmata si cum ar putea imbunatati
interpretarea.

- Tema personala principala: daca exista o intrebare concreta, lucrarea poate fi rafinata in jurul ei.
- Context profesional: domeniul de lucru sau directia profesionala actuala pot nuanta aplicabilitatea numerologica.
- Relatii si familie: daca exista o tema activa aici, interpretarile despre sensibilitate, grija, limite sau karma pot fi adaptate.
- Perioada curenta: evenimentele deja simtite in anul analizat pot lega mai bine anul personal si lectia de viata de realitatea imediata.
- Nume folosit social: daca numele complet, prenumele activ sau numele folosit public difera, analiza numelui poate fi ajustata.
- Grafice si cicluri: daca se doreste o reprezentare mai precisa, se confirma ciclul vizual folosit si anii care merita dezvoltati.
