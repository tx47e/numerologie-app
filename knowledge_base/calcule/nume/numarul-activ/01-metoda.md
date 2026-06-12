# Numarul activ - metoda

Formula adoptata pentru proiect:

```text
numarul activ = reducere_numerologica(suma valorilor literelor din prenumele folosit)
```

## Date necesare

- prenumele folosit cel mai des;
- optional, porecla sau forma de apel folosita efectiv;
- alfabetul numerologic pitagoreic documentat in
  `knowledge_base/calcule/nume/01-alfabet-numerologic.md`.

## Pasi de calcul

1. Se stabileste prenumele folosit efectiv in viata de zi cu zi.
2. Daca persoana foloseste constant o porecla sau o forma scurta, se poate
   calcula separat si acea forma.
3. Se normalizeaza textul.
4. Fiecare litera se transforma in valoarea numerologica.
5. Se aduna valorile literelor.
6. Se reduce suma la o cifra, 1-9.

## Observatii

Numarul activ are influenta asupra comportamentului de zi cu zi. Pentru profilul
de baza, daca nu exista o alta forma de apel declarata, folosim primul prenume
din numele complet introdus.
