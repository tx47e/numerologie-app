# Omuletul relatiilor - metoda

Omuletul relatiilor este o diagrama comparativa construita din cifrele deja
calculate pentru persoanele analizate. Nu inlocuieste matricea datei de nastere,
matricea numelui sau scara bunastarii, ci le reorganizeaza relational: cine ce
aduce, cine ce sustine si ce ramane de construit constient.

## Cand se foloseste

Se foloseste in analize relationale, de compatibilitate, cuplu, familie,
colaborare sau dinamica intre doua ori trei persoane.

In lucrarile individuale, rubrica este optionala si se include numai daca exista
o persoana iubita, partener, persoana de comparat sau o tema explicita de
compatibilitate.

## Sursa cifrelor

Sursa cifrelor trebuie aleasa explicit si pastrata identic pentru toate
persoanele comparate.

Surse permise:

- matricea datei de nastere, cu sirul complet al codului numerologic personal;
- matricea numelui;
- un set de rezultate ales explicit pentru relatia analizata.

Pentru compatibilitatea generala din acest proiect, sursa recomandata este
matricea datei de nastere, folosind sirul complet al codului numerologic
personal, inclusiv cifra `0` pentru pozitia de potential.

## Pozitiile pentagramei

Pentagrama are zece puncte de citire: cinci exterioare si cinci interioare. Pe
aceste puncte se aseaza cifrele de la `1` la `0`.

| Cifra | Pozitie in diagrama |
| --- | --- |
| 1 | varful de sus al pentagramei |
| 2 | coltul interior din dreapta sus |
| 3 | coltul exterior din dreapta |
| 4 | coltul interior din dreapta jos |
| 5 | coltul exterior de jos |
| 6 | centrul pentagramei, punctul de intersectie |
| 7 | coltul exterior din stanga jos |
| 8 | coltul interior din stanga jos |
| 9 | coltul exterior din stanga |
| 0 | coltul interior din stanga sus |

## Sinteza relatiei

### Ce se poate realiza impreuna

Pentru doua persoane:

```text
realizare_impreuna =
  reducere_numerologica(vibratia_interioara_A + vibratia_interioara_B)
```

Pentru trei persoane:

```text
realizare_impreuna =
  reducere_numerologica(vibratia_interioara_A + vibratia_interioara_B + vibratia_interioara_C)
```

Rezultatul arata ce pot construi, manifesta sau duce la implinire impreuna
persoanele implicate. Se citeste ca directie comuna, nu ca garantie automata.

### Ce este de rezolvat impreuna

Pentru doua persoane:

```text
de_rezolvat_impreuna =
  valoare_absoluta(vibratia_interioara_A - vibratia_interioara_B)
```

Pentru trei persoane, se calculeaza diferentele dintre fiecare pereche:

```text
diferenta_A_B = valoare_absoluta(vibratia_interioara_A - vibratia_interioara_B)
diferenta_A_C = valoare_absoluta(vibratia_interioara_A - vibratia_interioara_C)
diferenta_B_C = valoare_absoluta(vibratia_interioara_B - vibratia_interioara_C)
```

Rezultatul arata zona de tensiune, ajustare sau maturizare comuna. Nu indica
incompatibilitate, ci locul in care relatia cere dialog si lucru constient.

## Formula de citire

Pentru fiecare cifra/pozitie se noteaza:

- elementul cifrei;
- cate aparitii are fiecare persoana;
- totalul relatiei pe cifra;
- cine sustine cel mai mult cifra;
- cine are lipsa sau prezenta slaba pe cifra;
- ce poate oferi fiecare persoana relatiei prin cifra respectiva.

## Elemente

| Element | Cifre | Tema relationala |
| --- | --- | --- |
| Foc | 1, 5, 9 | initiativa, centru, vointa, sens, directie |
| Apa | 2, 6 | emotie, apropiere, grija, responsabilitate afectiva |
| Aer | 3, 7 | comunicare, inspiratie, perspectiva, spiritualitate |
| Pamant | 4, 8 | stabilitate, corp, organizare, limite, concretizare |
| Potential | 0 | spatiu, resetare, gol fertil, camp de posibilitate |

## Totaluri pe elemente

Pentru fiecare persoana si pentru intreaga relatie:

```text
foc = cantitate(1) + cantitate(5) + cantitate(9)
apa = cantitate(2) + cantitate(6)
aer = cantitate(3) + cantitate(7)
pamant = cantitate(4) + cantitate(8)
potential = cantitate(0)
```

Interpretarea observa elementul dominant, elementele slabe, complementaritatea
si dezechilibrul, mai ales cand o persoana sustine aproape singura o zona.

## Tabele obligatorii

### Sinteza relatiei

| Calcul | Formula | Rezultat | Citire |
| --- | --- | --- | --- |
| Ce se poate realiza impreuna | suma vibratiilor interioare reduse |  |  |
| Ce este de rezolvat impreuna | diferenta vibratiilor interioare reduse |  |  |

### Distributia cifrelor pe pentagrama

| Cifra | Element | Pozitie in pentagrama | Persoana A | Persoana B | Total relatie | Cine sustine | Citire |
| --- | --- | --- | ---: | ---: | ---: | --- | --- |
| 1 | Foc | varf sus |  |  |  |  |  |
| 2 | Apa | colt interior dreapta sus |  |  |  |  |  |
| 3 | Aer | colt exterior dreapta |  |  |  |  |  |
| 4 | Pamant | colt interior dreapta jos |  |  |  |  |  |
| 5 | Foc | colt exterior jos |  |  |  |  |  |
| 6 | Apa | centru / punct de intersectie |  |  |  |  |  |
| 7 | Aer | colt exterior stanga jos |  |  |  |  |  |
| 8 | Pamant | colt interior stanga jos |  |  |  |  |  |
| 9 | Foc | colt exterior stanga |  |  |  |  |  |
| 0 | Potential | colt interior stanga sus |  |  |  |  |  |

### Sinteza pe elemente

| Element | Persoana A | Persoana B | Total relatie | Citire |
| --- | ---: | ---: | ---: | --- |
| Foc |  |  |  |  |
| Apa |  |  |  |  |
| Aer |  |  |  |  |
| Pamant |  |  |  |  |
| Potential / 0 |  |  |  |  |

## Surse bibliografice interne

- `bibliography/Omuletul Relatiilor.md`
