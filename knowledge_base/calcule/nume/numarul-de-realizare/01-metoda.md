# Numarul de realizare - metoda

Formula adoptata pentru proiect:

```text
numarul de realizare = reducere_numerologica(suma valorilor consoanelor din numele complet)
```

## Date necesare

- numele complet folosit in analiza;
- alfabetul numerologic pitagoreic documentat in
  `knowledge_base/calcule/nume/01-alfabet-numerologic.md`.

## Pasi de calcul

1. Se preia numele complet.
2. Se normalizeaza textul: majuscule, fara diacritice, fara semne de punctuatie.
3. Se pastreaza numai consoanele.
4. Fiecare consoana se transforma in valoarea numerologica.
5. Se aduna valorile consoanelor.
6. Se reduce suma la o cifra, 1-9.

## Observatii

In bibliografie, numarul de realizare este asociat cu vibratia exterioara. El
arata impresia lasata asupra celorlalti, manierele, comportamentul si felul in
care energia numelui participa la realizari sociale si profesionale.
