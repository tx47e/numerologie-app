# Destin - metoda

Formula adoptata pentru proiect:

```text
destin = reducere_numerologica(
  suma(reducere_numerologica(suma valorilor literelor fiecarei componente de nume))
)
```

In multe sisteme numerologice, numarul de destin este acelasi calcul cu numarul
de expresie. Pentru proiect, `destin` foloseste formula numarului de exprimare:
numele complet este calculat pe componente, fiecare componenta este redusa la
o cifra, apoi cifrele componentelor se aduna si se reduc din nou. `Soarta` ramane
calculul datei de nastere.

## Pasi de calcul

1. Se preia numele complet.
2. Se normalizeaza numele.
3. Se imparte numele complet in componente: nume de familie, prenume si alte
   prenume, dupa caz.
4. Pentru fiecare componenta, se transforma literele in valori numerologice
   pitagoreice.
5. Se aduna valorile fiecarei componente si se reduce componenta la o cifra.
6. Se aduna cifrele componentelor.
7. Se reduce suma finala la 1-9.
