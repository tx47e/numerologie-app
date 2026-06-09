# Pinacluri - metoda

Formula adoptata pentru proiect foloseste patru pinacluri si patru provocari.

## Date necesare

- ziua nasterii;
- luna nasterii;
- anul nasterii.

Se folosesc valorile reduse ale zilei, lunii si anului:

```text
zi = reducere_numerologica(ziua nasterii)
luna = reducere_numerologica(luna nasterii)
an = reducere_numerologica(anul nasterii)
soarta = reducere_numerologica(data nasterii completa)
```

## Pinacluri

```text
pinaclu 1 = reducere_numerologica(luna + zi)
pinaclu 2 = reducere_numerologica(zi + an)
pinaclu 3 = reducere_numerologica(pinaclu 1 + pinaclu 2)
pinaclu 4 = reducere_numerologica(luna + an)
```

## Provocari

```text
provocare 1 = valoare_absoluta(zi - luna)
provocare 2 = valoare_absoluta(zi - an)
provocare 3 = valoare_absoluta(provocare 1 - provocare 2)
provocare 4 = valoare_absoluta(luna - an)
```

Provocarile pot avea si valoarea 0.

## Varste

```text
sfarsit pinaclu 1 = 36 - soarta
sfarsit pinaclu 2 = sfarsit pinaclu 1 + 9
sfarsit pinaclu 3 = sfarsit pinaclu 2 + 9
pinaclu 4 = de la anul urmator pana la finalul vietii
```

Exemplu pentru `soarta = 3`:

```text
pinaclu 1: 0-33 ani
pinaclu 2: 34-42 ani
pinaclu 3: 43-51 ani
pinaclu 4: 52+ ani
```
