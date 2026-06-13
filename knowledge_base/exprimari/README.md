# Exprimari validate pentru interpretari

Acest director pastreaza formulari generate si validate pentru interpretarile
care se repeta in lucrarile numerologice. Scopul este sa construim treptat o
baza de texte reutilizabile, astfel incat interpretarile mature sa poata fi
preluate din `knowledge_base/exprimari/`, nu regenerate de fiecare data.

## Regula de lucru

Cand intr-o lucrare apare o interpretare buna pentru o tema recurenta, textul se
salveaza in fisierul temei potrivite. Daca exista deja o formulare pentru aceeasi
tema si acelasi rezultat numeric, nu se sterge varianta veche; se adauga o
varianta noua, cu index propriu, stilul in care a fost scrisa, nivelul de
detaliere, context scurt si lista lucrarilor in care a fost folosita.

Pot exista mai multe variante pentru acelasi rezultat numeric, acelasi stil,
acelasi nivel de detaliere si acelasi context scurt. Acest lucru este dorit,
pentru ca lucrarile apropiate intre ele, cum ar fi analizele pentru membrii unei
familii, au nevoie de varietate de limbaj si nu trebuie sa repete aceeasi
exprimare la fiecare persoana.

Fisierele sunt numerotate in ordinea in care apar calculele in template. README-ul
ramane fara prefix numeric. Numerotarea incepe de la `00`.

## Ordine fisiere

- `00-vibratie-interioara.md`
- `01-vibratie-exterioara.md`
- `02-vibratie-cosmica-fixa.md`
- `03-vibratie-cosmica-variabila.md`
- `04-vibratie-cosmica-totala.md`
- `05-vibratie-globala.md`
- `06-destin.md`
- `07-calea-destinului.md`
- `08-aspecte-de-indreptat.md`
- `09-punti.md`
- `10-karma-din-data-nasterii.md`
- `11-matrice-numerologica.md`
- `12-scara-bunastarii.md`
- `13-nume.md`
- `14-vibratii-esentiale-integrat.md`

## Format obligatoriu pentru fiecare intrare

Fiecare fisier poate contine mai multe rezultate numerice si mai multe variante
pentru acelasi rezultat. Fiecare varianta trebuie indexata numeric in ordine
crescatoare: `Varianta 001`, `Varianta 002`, `Varianta 003` si asa mai departe.

```markdown
## Rezultat 3

### Varianta 001

- Stil: formal / conversational
- Nivel de detaliere: scurt / mediu / amplu / foarte amplu
- Context scurt: cand se potriveste aceasta varianta
- Lucrari unde a fost folosita:
  - `cale/catre/lucrare.md` - persoana / data / observatie scurta
- Data adaugarii: AAAA-LL-ZZ

Textul interpretarii...

### Varianta 002

- Stil:
- Nivel de detaliere:
- Context scurt:
- Lucrari unde a fost folosita:
  -
- Data adaugarii:

Textul interpretarii...
```

## Reguli de folosire in lucrari

1. Inainte de a genera o interpretare noua pentru un calcul sau o tema
   recurenta, se verifica fisierul potrivit din acest director.
2. Cand exista mai multe formulari potrivite pentru rezultatul calculat, se alege
   varianta care aduce cea mai buna potrivire cu persoana si cea mai buna
   varietate fata de lucrarile apropiate.
3. Intr-un grup de lucrari legate intre ele, de exemplu o familie, se evita
   refolosirea aceleiasi variante pentru acelasi rezultat. Se alege o alta
   varianta potrivita sau se genereaza o formulare noua daca biblioteca nu are
   destula varietate.
4. Se genereaza o formulare noua daca exprimarile existente nu se potrivesc
   stilului, nivelului de detaliere, contextului persoanei, legaturii cu restul
   lucrarii sau nevoii de varietate intre lucrari apropiate.
5. Textul poate fi adaptat usor la persoana analizata, la stilul cerut si la
   restul lucrarii, dar sensul numerologic nu se schimba.
6. Cand se genereaza o formulare noua si este valoroasa, se adauga ca varianta
   noua in fisierul temei, cu index, stil, nivel de detaliere, context scurt si
   lista lucrarilor unde a fost folosita.
7. Cand aceeasi exprimare este refolosita intr-o alta lucrare, nu se creeaza
   automat o varianta noua; se adauga noua lucrare in lista `Lucrari unde a fost
   folosita`.
8. Daca doua variante spun acelasi lucru aproape identic, dar au limbaj diferit
   si pot ajuta la varietate intre lucrari, se pot pastra ambele. Se elimina doar
   variantele care sunt redundante fara sa aduca o diferenta reala de formulare,
   ton sau aplicabilitate.
9. Exprimarile validate nu inlocuiesc metoda de calcul; ele completeaza metoda
   cu formulari umane, fluide si reutilizabile.
