# Vibratia interioara - observatii

## Decizie de lucru

Pentru proiect, vibratia interioara se calculeaza din ziua nasterii, nu din nume.
Regulile legate de vocale, consoane, diacritice si nume multiple apartin
calculelor derivate din nume.

In comparatie cu [vibratia exterioara](../vibratia-exterioara/README.md), care
arata prezenta sociala, vibratia interioara descrie stratul de pornire al
persoanei. De aceea, ea trebuie citita impreuna cu expresiile date de
[vibratia globala](../vibratia-globala/README.md) si, cand este cazul, cu
[vibratia destinului](../vibratia-destinului/README.md).

## Reguli de implementare

- Input minim: ziua nasterii, ca numar intre 1 si 31.
- Rezultat standard: numar intre 1 si 9.
- Rezultat optional: valoare intermediara pentru 11 sau 22, daca se activeaza interpretarea numerelor maestre.
- Pentru zilele 10, 20 si 30, se reduce la 1, 2 si 3.
- Se pastreaza traseul complet al reducerii, nu doar rezultatul final.
- Fiecare pas intermediar poate fi folosit pentru nuantarea interpretarii.
- Daca apar 11 sau 22, ele se noteaza separat si se compara cu traseul final,
  nu se suprapun automat peste sensul principal.

## Regula de interpretare pe traseu

Interpretarea se face in straturi:

1. vibratia finala este directia principala;
2. cifrele initiale arata materialul din care se formeaza vibratia;
3. rezultatele intermediare arata praguri sau transformari;
4. formule mai lungi cer interpretari mai nuantate.

Exemplu: 28 nu se citeste doar ca 1. Se citeste ca 2 + 8, apoi 10, apoi 1.
In acelasi timp, pentru o lectura completa, celelalte vibratii din data
persoanei pot adauga contrast: [vibratia exterioara](../vibratia-exterioara/README.md)
poate arata cum se manifesta energia, iar [vibratia destinului](../vibratia-destinului/README.md)
poate arata directia mare in care aceasta energie este impinsa.

## Surse

- https://asociatianumerologilor.ro/calculator-numerologie/
- https://www.dcnews.ro/vibratia-interioara-metoda-de-calcul-pe-intelesul-tuturor-cum-iti-afecteaza-relatiile_837126.html
- https://ro.wikibooks.org/wiki/Numerologie/Vibra%C8%9Bia_interioar%C4%83
