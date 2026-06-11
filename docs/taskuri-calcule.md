# Taskuri calcule numerologice

Acest fisier este backlog-ul de lucru pentru toate calculele identificate in
`knowledge_base/calcule`, `docs/formule-calcul.md` si `scripts/`.

Legenda status:

- `documentat`: exista metoda sau explicatie de lucru.
- `placeholder`: fisierul exista, dar contine `De completat`.
- `partial`: exista continut, dar lipsesc piese importante.
- `de validat`: formula sau interpretarea trebuie confirmata editorial.
- `de revizuit`: calculul trebuie analizat inainte de a fi considerat final.
- `neimplementat separat`: calculul nu are functie dedicata in `scripts/`.
- `implementat`: exista functie sau flux in `scripts/`.

## Lista de lucru

| Task | Calcul | Status editorial | Documentare curenta | Task urmator |
|---|---|---|---|---|
| [x] | Vibratia numelui | de revizuit; documentat; implementat | Metoda, semnificatii, exemple si observatii completate; implementat in script. | Revizuire editoriala, validare pe exemple si decizie despre numere maestre. |
| [x] | Destin | de revizuit; documentat; implementat indirect | Metoda, semnificatii si exemple completate; implementat ca vibratia numelui. | Revizuire editoriala: decide daca ramane sinonim operational sau capitol separat de interpretare. |
| [ ] | Nume inainte/dupa casatorie | de revizuit; partial; implementat | Formula mentionata in `docs/formule-calcul.md`; implementata comparatia in script; nu are capitol dedicat complet. | Crea/valida capitol dedicat cu metoda, exemple si limite. |
| [ ] | Vibratia interioara | de revizuit; documentat; implementat | Metoda, semnificatii, exemple si observatii documentate; implementata in script. | Revizuire editoriala si validare pe exemple. |
| [ ] | Vibratia exterioara | de revizuit; documentat; implementat | Metoda, semnificatii, exemple si observatii documentate; implementata in script. | Revizuire editoriala si validare pe exemple. |
| [x] | Soarta | de revizuit; documentat; implementat | Metoda, semnificatii si exemple completate; implementata in script. | Revizuire editoriala si validare pe exemple. |
| [x] | Tema vietii | de revizuit; documentat; implementat | Metoda, semnificatii si exemple completate; implementata in script. | Revizuire editoriala si validare ca sinteza intre soarta si destin. |
| [ ] | Vibratia anului | de revizuit; placeholder; implementat | Metoda documentata; semnificatii si exemple sunt placeholder; implementata in script. | Completa semnificatii 1-9 si exemple pentru ani analizati. |
| [ ] | Tema anului | de revizuit; placeholder; neimplementat separat | Metoda documentata; semnificatii si exemple sunt placeholder; nu este implementata ca functie separata. | Decide relatia cu vibratia anului si daca necesita functie proprie. |
| [ ] | Ani importanti interiori | de revizuit; de validat; implementat | Metoda, observatii si exemple documentate; semnificatii marcate de completat dupa validare; implementat in script. | Valida formula si completa semnificatiile. |
| [ ] | Ani importanti exteriori | de revizuit; de validat; implementat | Metoda, observatii si exemple documentate; semnificatii marcate de completat dupa validare; implementat in script. | Valida formula si completa semnificatiile. |
| [ ] | Lectii de viata | de revizuit; de validat; neimplementat separat | Metoda, semnificatii, exemple si observatii documentate; formula interna marcata de validat; nu am gasit implementare directa in script. | Valida formula `zi x luna x an`, apoi implementa functie si teste. |
| [ ] | Cicluri de 7 ani | de revizuit; placeholder; implementat | Metoda documentata; semnificatii si exemple sunt placeholder; implementat in script. | Completa interpretari si exemple pentru pozitii/cicluri. |
| [ ] | Cicluri de 9 ani | de revizuit; placeholder; implementat | Metoda documentata; semnificatii si exemple sunt placeholder; implementat in script. | Completa interpretari si exemple pentru pozitii/cicluri. |
| [ ] | Cicluri de 12 ani | de revizuit; placeholder; implementat | Metoda documentata; semnificatii si exemple sunt placeholder; implementat in script. | Completa interpretari si exemple pentru pozitii/cicluri. |
| [ ] | Pinacluri | de revizuit; placeholder; implementat | Metoda documentata; exemple, observatii, oportunitati si provocari sunt placeholder/partial; implementat in script. | Completa exemple, oportunitati, provocari si validare durata etapelor. |
| [ ] | Provocari pinacluri | de revizuit; placeholder; implementat indirect | Formula inclusa in pinacluri; fisierul de provocari este placeholder; implementat impreuna cu pinaclurile. | Scrie interpretari pentru provocarile calculate. |
| [ ] | Lectii karmice personale | de revizuit; partial; implementat | Metoda documentata; fara exemple dedicate; implementat in script. | Adauga exemple si semnificatii pentru numerele lipsa. |
| [ ] | Datorii karmice personale | de revizuit; partial; implementat | Metoda documentata; fara exemple dedicate; implementat in script. | Valida unde cautam 13/14/16/19 si adauga exemple. |
| [ ] | Karma neamului | de revizuit; de validat; implementat | Metoda documentata; formula marcata ca conventie de proiect; fara exemple; implementat in script. | Valida editorial formula pe numele de familie si adauga exemple. |
| [ ] | Karma neamului inainte/dupa casatorie | de revizuit; partial; implementat | Metoda documentata in karma neamului; fara capitol si exemple dedicate; implementat in script. | Decide cum se prezinta comparatia si adauga exemple. |
| [ ] | Patratul lui Pitagora dupa data nasterii | de revizuit; documentat; implementat | Metoda, exemple, observatii, pozitii, frecvente, elemente si vectori documentate; implementat in script. | Revizuire finala si teste pe exemplele din documentatie. |
| [ ] | Matricea numelui | de revizuit; partial; implementat | Documentata prin alfabet, metoda Pitagora si formule; implementata in script. | Clarifica daca are capitol separat sau ramane sub Patratul lui Pitagora. |
| [ ] | Vectorii patratului/matricei | de revizuit; documentat; implementat | Documentati in `patratul-lui-pitagora/vectori.md`; implementati in script. | Valida denumiri, ordonare si interpretari. |
| [ ] | Compararea matricilor de nume | de revizuit; partial; implementat | Mentionata in formule si implementata in script; fara documentatie dedicata. | Documenta metoda de comparatie si exemple inainte/dupa. |

## Taskuri transversale

- [ ] Stabilire lista finala de calcule v1.
- [ ] Marcare calcule care intra in prima versiune a aplicatiei.
- [ ] Marcare calcule care raman doar documentare pentru moment.
- [ ] Eliminare sau rescriere fisiere placeholder cu `De completat`.
- [ ] Validare formule marcate ca formule interne de lucru.
- [ ] Adaugare exemple complete pentru fiecare calcul inclus in v1.
- [ ] Adaugare teste automate pe baza exemplelor acceptate.
- [ ] Verificare consistenta intre documentatie, Python si Java.

## Task repetitiv de audit

- [ ] Audit periodic calcule: pentru fiecare calcul din lista, verifica daca formula este bine stabilita, daca metoda este documentata clar, daca exista exemple, daca exista semnificatii/interpretari, daca are implementare separata unde este nevoie si daca statusul trebuie schimbat in `de revizuit`, `de validat`, `partial`, `placeholder`, `implementat` sau `finalizat`.
