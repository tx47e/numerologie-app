# Destin - metoda

Formula adoptata pentru proiect:

```text
destin = reducere_numerologica(suma valorilor literelor din numele complet)
```

In multe sisteme numerologice, numarul de destin este acelasi calcul cu numarul
de expresie: suma tuturor literelor din numele complet. Pentru proiect, `destin`
este calculul numelui complet, iar `soarta` este calculul datei de nastere.

## Pasi de calcul

1. Se preia numele complet.
2. Se normalizeaza numele.
3. Se transforma fiecare litera in valoare numerologica pitagoreica.
4. Se aduna toate valorile.
5. Se reduce totalul la 1-9.
