# Numarul ereditar karmic - metoda

Formula adoptata pentru proiect:

```text
numarul ereditar karmic = reducere_22(suma valorilor literelor din numele de familie)
```

Unde:

```text
reducere_22(numar):
  cat timp numar > 22:
    numar = numar - 22
  return numar
```

## Date necesare

- numele de familie relevant pentru linia de neam;
- alfabetul numerologic pitagoreic documentat in
  `knowledge_base/calcule/nume/01-alfabet-numerologic.md`.

## Pasi de calcul

1. Se stabileste numele de familie relevant pentru analiza neamului.
2. Se normalizeaza textul.
3. Fiecare litera se transforma in valoarea numerologica.
4. Se aduna valorile literelor.
5. Daca rezultatul este mai mare de 22, se scade 22.
6. Daca rezultatul ramane mai mare de 22, se scade din nou 22.
7. Se repeta pana cand rezultatul este intre 1 si 22.

## Asociere cu Tarotul

- rezultatele 1-21 se citesc prin Arcanele Majore 1-21;
- rezultatul 22 se citeste ca Arcana Majora 0, Nebunul.

Interpretarile pentru neamurile 1-22 sunt documentate separat in
`03-interpretari-neam.md`.

## Reguli importante

- pentru femeile casatorite, bibliografia recomanda calculul pe numele de fata
  pentru linia de neam;
- pentru persoane adoptate, bibliografia recomanda numele de familie al tatalui
  biologic, daca analiza urmareste linia de sange;
- cand numele se schimba, influenta vechiului nume scade treptat, iar influenta
  noului nume creste treptat;
- numele de neam ramane relevant toata viata pentru mosteniri fizice, mentale,
  energetice si emotionale.
