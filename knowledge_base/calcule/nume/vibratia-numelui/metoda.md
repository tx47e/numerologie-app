# Vibratia numelui - metoda

Formula adoptata pentru proiect:

```text
vibratia numelui = reducere_numerologica(suma valorilor literelor din numele complet)
```

## Alfabet folosit

Folosim alfabetul pitagoreic documentat in
`knowledge_base/calcule/nume/alfabet-numerologic.md`.

```text
1: A J S
2: B K T
3: C L U
4: D M V
5: E N W
6: F O X
7: G P Y
8: H Q Z
9: I R
```

## Pasi de calcul

1. Se preia numele complet folosit in calcul.
2. Se normalizeaza textul: majuscule, fara diacritice, fara semne de punctuatie.
3. Fiecare litera se transforma in valoarea numerologica.
4. Se aduna valorile pe fiecare componenta a numelui.
5. Se aduna totalurile componentelor.
6. Se reduce totalul la 1-9.

## Formula pentru implementare

```text
functie vibratia_numelui(nume):
  litere = normalizeaza(nume)
  valori = transforma_litere(litere)
  total = suma(valori)
  rezultat = reducere_numerologica(total)
  return { total, rezultat, valori }
```

## Observatie

In numerologia occidentala, acest calcul este numit frecvent si numar de expresie
sau numar de destin. In proiect pastram numele `vibratia numelui` pentru calculul
strict derivat din nume.
