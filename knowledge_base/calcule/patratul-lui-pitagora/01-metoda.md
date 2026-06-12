# Patratul lui Pitagora - metoda

Metoda porneste de la data nasterii si genereaza o serie de cifre care se aseaza
in matricea 3x3.

## Date necesare pentru matricea datei

- ziua nasterii;
- luna nasterii;
- anul nasterii.

Data se scrie numeric, fara separatori, in forma:

```text
ZZLLAAAA
```

Exemplu:

```text
24.04.1982 -> 24041982
```

## Cifre brute

Se iau toate cifrele din data nasterii, cu exceptia cifrei 0.

Exemplu:

```text
24041982 -> 2, 4, 4, 1, 9, 8, 2
```

Zero nu se introduce in matrice, dar ramane important in data ca loc, gol,
potential sau absenta explicita.

## Numere de lucru

Pentru proiect folosim patru numere de lucru.

### Numarul 1 de lucru

Se aduna toate cifrele datei de nastere.

```text
2 + 4 + 0 + 4 + 1 + 9 + 8 + 2 = 30
```

### Numarul 2 de lucru

Se reduce numarul 1 de lucru prin adunarea cifrelor sale.

```text
3 + 0 = 3
```

### Numarul 3 de lucru

Din numarul 1 de lucru se scade dublul primei cifre nenule din ziua nasterii.

Pentru ziua 24, prima cifra este 2.

```text
30 - (2 x 2) = 26
```

Pentru o zi de forma 07, prima cifra nenula este 7.

### Numarul 4 de lucru

Se reduce numarul 3 de lucru prin adunarea cifrelor sale.

```text
2 + 6 = 8
```

## Sirul complet de lucru

Se noteaza:

```text
data nasterii + numarul 1 + numarul 2 + numarul 3 + numarul 4
```

Exemplu:

```text
24041982 + 30 + 3 + 26 + 8
```

Cifrele care intra in matrice sunt:

```text
2, 4, 4, 1, 9, 8, 2, 3, 3, 2, 6, 8
```

Cifra 0 se elimina.

## Matricea

Folosim aceasta pozitionare:

```text
1 | 4 | 7
2 | 5 | 8
3 | 6 | 9
```

Pentru fiecare cifra aparuta, se adauga acea cifra in casuta corespunzatoare.
Daca cifra apare de mai multe ori, se repeta in aceeasi casuta.

Exemplu:

```text
1  | 44 |
222|    | 88
33 | 6  | 9
```

## Formula pentru implementare

```text
functie patratul_lui_pitagora(zi, luna, an):
  data = cifrele(zi, luna, an)
  n1 = suma(data)
  n2 = suma_cifrelor_pana_la_o_cifra(n1)
  prima_cifra_zi = prima_cifra_nenula(zi)
  n3 = n1 - 2 * prima_cifra_zi
  n4 = suma_cifrelor_pana_la_o_cifra(n3)

  sir = data + cifrele(n1) + cifrele(n2) + cifrele(n3) + cifrele(n4)
  sir_fara_zero = elimina_zero(sir)

  matrice = grupeaza_dupa_cifra(sir_fara_zero, 1..9)
  return matrice
```

## Reguli importante

- Zero nu se pune in matrice.
- Repetitia conteaza: `111` se interpreteaza diferit de `1`.
- Absenta conteaza: lipsa unei cifre nu este defect, ci tema de dezvoltare.
- Numerele de lucru se interpreteaza prin cifrele lor, nu ca numere independente.
- Matricea este instrument de citire simbolica, nu diagnostic psihologic.

## Matricea numelui

Matricea numelui se calculeaza separat fata de matricea datei de nastere.
Ea arata distributia expresiei prin nume, nu structura extrasa din data.

Date necesare:

- numele complet;
- alfabetul numerologic pitagoreic documentat in
  `knowledge_base/calcule/nume/01-alfabet-numerologic.md`.

Regula:

1. Se preia numele complet.
2. Se normalizeaza numele:
   - se transforma literele cu diacritice in litere de baza;
   - se ignora spatiile, cratimele si semnele de punctuatie;
   - se pastreaza doar literele.
3. Fiecare litera se transforma in valoarea numerologica 1-9.
4. Se calculeaza numarul de exprimare: fiecare componenta a numelui se reduce
   separat, apoi componentele reduse se aduna si se reduc la o cifra.
5. In matrice se introduc:
   - valorile literelor din nume si prenume;
   - numarul final de exprimare.

Cifrele intermediare ale componentelor reduse se folosesc doar pentru calculul
numarului de exprimare. Ele nu se introduc separat in matrice.

Valorile obtinute se aseaza in aceeasi matrice 3x3:

```text
1 | 4 | 7
2 | 5 | 8
3 | 6 | 9
```

Exemplu scurt:

```text
ANA POPESCU

ANA -> A=1, N=5, A=1 -> 7
POPESCU -> P=7, O=6, P=7, E=5, S=1, C=3, U=3 -> 32 -> 5
numar de exprimare -> 7 + 5 = 12 -> 3
```

Matricea numelui:

```text
111 |   | 77
    | 55|
333 | 6 |
```

## Citire comparativa

In profilul complet se pastreaza doua matrici:

- matricea datei de nastere;
- matricea numelui.

Ele se compara prin:

- cifre dominante in data si in nume;
- cifre absente in data, dar prezente in nume;
- cifre prezente in data, dar absente in nume;
- vectori activi in data fata de vectori activi in nume.

Nu combinam automat cifrele datei cu cifrele numelui intr-o singura matrice,
pentru ca ar amesteca doua surse simbolice diferite: structura nasterii si
expresia prin nume.

## Metoda pentru scara bunastarii

Scara bunastarii foloseste valorile casutelor si valorile vectorilor din matrice.

### Valoarea casutei

Valoarea unei casute se calculeaza ca suma cifrelor repetate in acea casuta.

```text
111 -> 1 + 1 + 1 = 3
66 -> 6 + 6 = 12
99999 -> 9 + 9 + 9 + 9 + 9 = 45
```

### Valoarea vectorului

Valoarea unui vector este suma valorilor celor trei casute care il formeaza.

```text
vectorul 3-6-9 = valoare(3) + valoare(6) + valoare(9)
```

### Ordinea de lucru

1. Se calculeaza valoarea fiecarei casute.
2. Se calculeaza valoarea fiecarui vector.
3. Se ordoneaza valorile de la cea mai mare la cea mai mica, cu zero separat.
4. Se citeste scara de sus in jos si de jos in sus.
5. Valorile egale se citesc ca teme care se sustin intre ele.
6. Valorile de jos determina valorile urmatoare.
7. Diferentele mari intre trepte se trec greu; diferentele mici se trec usor.
