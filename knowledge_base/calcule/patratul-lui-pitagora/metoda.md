# Patratul lui Pitagora - metoda

Metoda porneste de la data nasterii si genereaza o serie de cifre care se aseaza
in matricea 3x3.

## Date necesare

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
3 | 6 | 9
2 | 5 | 8
1 | 4 | 7
```

Pentru fiecare cifra aparuta, se adauga acea cifra in casuta corespunzatoare.
Daca cifra apare de mai multe ori, se repeta in aceeasi casuta.

Exemplu:

```text
33 | 6  | 9
222|    | 88
1  | 44 |
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
