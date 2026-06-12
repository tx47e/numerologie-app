# Soarta - metoda

Formula adoptata pentru proiect:

```text
soarta = reducere_numerologica(ziua + luna + anul nasterii)
```

Acest calcul corespunde numarului drumului vietii in multe sisteme numerologice.
Pentru proiect il numim `soarta`, deoarece descrie traseul de baza derivat din
data nasterii.

## Pasi de calcul

1. Se scrie data nasterii numeric.
2. Se aduna toate cifrele datei.
3. Se reduce rezultatul la 1-9.
4. Se pastreaza traseul complet al reducerii.

Exemplu:

```text
24.04.1982
2 + 4 + 0 + 4 + 1 + 9 + 8 + 2 = 30
3 + 0 = 3

soarta = 3
```
