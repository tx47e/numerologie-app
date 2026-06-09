# Karma neamului - metoda

Formula de lucru adoptata pentru proiect:

```text
karma neamului = analiza karmica a numelui de familie
```

Numele de familie este tratat ca purtator al liniei de neam. Calculul foloseste
aceeasi logica precum karma personala, dar aplicata doar pe numele de familie.

## Pasi de calcul

1. Se preia numele de familie.
2. Se normalizeaza numele.
3. Se transforma literele in valori numerologice.
4. Se calculeaza frecventele 1-9.
5. Numerele lipsa devin lectii karmice de neam.
6. Totalul numelui de familie se verifica pentru datorii karmice: 13, 14, 16, 19.

## Formula pentru implementare

```text
functie karma_neamului(nume_familie):
  frecvente = frecvente_valori_litere(nume_familie)
  lectii = numerele 1..9 unde frecventa este 0
  total = suma(valorilor)
  datorii = total daca total este in {13, 14, 16, 19}
  vibratie = reducere_numerologica(total)
  return { lectii, datorii, vibratie }
```

## Observatie

Aceasta formula este o conventie de proiect. Ea trebuie validata prin exemple si
prin decizia editoriala finala despre cum tratam numele de familie.
