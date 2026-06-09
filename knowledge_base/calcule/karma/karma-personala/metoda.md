# Karma personala - metoda

Karma personala are doua componente de lucru:

1. lectii karmice;
2. datorii karmice.

## Lectii karmice

Lectiile karmice sunt cifrele de la 1 la 9 care lipsesc din numele complet.

```text
lectii karmice = numerele 1-9 cu frecventa 0 in valorile literelor numelui complet
```

## Datorii karmice

Datoriile karmice sunt marcate cand in traseul de calcul apare unul dintre
numerele:

```text
13, 14, 16, 19
```

Pentru prima versiune verificam aparitia acestor numere in:

- totalul numelui;
- suma datei de nastere;
- totalul folosit pentru soarta;
- totalul folosit pentru destin.

## Formula pentru implementare

```text
functie karma_personala(nume, zi, luna, an):
  frecvente = frecvente_valori_litere(nume)
  lectii = numerele 1..9 unde frecventa este 0
  datorii = valori din {13, 14, 16, 19} aparute in totaluri
  return { lectii, datorii }
```

## Observatie

Lectiile karmice nu sunt tratate ca verdict. Ele indica zone care pot cere
dezvoltare constienta.
