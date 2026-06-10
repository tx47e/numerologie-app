# Roadmap

## Stare curenta

- [x] Baza editoriala principala este `knowledge_base/`.
- [x] Fisierele temporare `_sursa-initiala.md` au fost curatate dupa separarea
  capitolelor.
- [x] Aplicatia va consuma initial `generated/index.json`, generat din Markdown.
- [x] Baza de date ramane optionala si se introduce doar daca apar nevoi reale de
  cautare, editare multi-utilizator sau scalare.

## Etapa 1: baza de informatii

- [x] Creare structura pentru vibratiile 1-9.
- [x] Separare capitole in fisiere Markdown.
- [x] Documentare pasi si decizii.
- [x] Mutare continut numerologic in `knowledge_base/`.
- [x] Curatare backup-uri `_sursa-initiala.md` dupa validare.
- [x] Extindere continut pentru fiecare capitol.
- [x] Stabilire ton editorial final.

## Etapa 2: model de date

- [x] Creare structura initiala pentru calcule numerologice.
- [x] Separare bazei de cunoastere de documentatia de proiect.
- [x] Definire schema pentru vibratii.
- [x] Definire schema pentru capitole.
- [x] Definire schema pentru calcule.
- [x] Definire schema pentru exemple de calcul.
- [x] Stabilire metadate utile:
  - [x] numar;
  - [x] titlu;
  - [x] cuvinte cheie;
  - [x] teme principale;
  - [x] recomandari;
  - [x] avertismente;
  - [x] exemple.
- [x] Decizie intre Markdown direct, JSON generat sau baza de date.
- [x] Generare `generated/index.json` din Markdown.

## Etapa 3: motor numerologic

Obiectiv: transformarea formulelor documentate in functii testabile.

- [ ] Inghetare formule v1 in `docs/formule-calcul.md`.
- [ ] Definire input-uri canonice pentru formular:
  - [ ] nume complet;
  - [ ] data nasterii;
  - [ ] an de referinta;
  - [ ] optiuni pentru calcule avansate.
- [ ] Standardizare normalizare nume:
  - [ ] majuscule/minuscule;
  - [ ] diacritice;
  - [ ] cratime si spatii;
  - [ ] caractere neacceptate.
- [ ] Analiza nume inainte si dupa casatorie:
  - [ ] vibratia numelui;
  - [ ] matricea numelui;
  - [ ] karma numelui;
  - [ ] karma neamului;
  - [ ] comparatie intre cele doua variante.
- [ ] Implementare calcule de baza:
  - [ ] vibratia numelui;
  - [ ] vibratia interioara;
  - [ ] vibratia exterioara;
  - [ ] soarta;
  - [ ] destin;
  - [ ] tema vietii.
- [ ] Implementare calcule de timp:
  - [ ] vibratia anului;
  - [ ] tema anului;
  - [ ] ani importanti interiori;
  - [ ] ani importanti exteriori;
  - [ ] cicluri de 7, 9 si 12 ani.
- [ ] Implementare calcule avansate:
  - [ ] pinacluri;
  - [ ] provocari;
  - [ ] patratul lui Pitagora;
  - [ ] lectii karmice si datorii karmice.
- [ ] Definire profil combinat:
  - [ ] rezultate numerice;
  - [ ] capitole relevante din `generated/index.json`;
  - [ ] prioritizare interpretari;
  - [ ] avertismente si limite.
- [ ] Adaugare teste pe exemplele din `knowledge_base/`.
- [ ] Verificare consistenta intre scripturile Python si Java existente.

## Etapa 4: aplicatie

Obiectiv: prima interfata functionala pentru consultarea continutului si calcul.

- [ ] Alegere stack tehnic.
- [ ] Creare structura aplicatie.
- [ ] Incarcare `generated/index.json`.
- [ ] Afisare continut vibratii.
- [ ] Cautare si navigare in baza de informatii.
- [ ] Formular calcul numerologic.
- [ ] Pagina rezultat cu:
  - [ ] sumar;
  - [ ] calcule detaliate;
  - [ ] interpretari;
  - [ ] recomandari;
  - [ ] avertismente.
- [ ] Export sau salvare raport.
- [ ] Validare UX pe desktop si mobil.

## Etapa 5: publicare

- [ ] Setup build.
- [ ] Setup deploy.
- [ ] Validare continut editorial.
- [ ] Validare calcule prin exemple.
- [ ] Publicare prima versiune.
- [ ] Stabilire proces de actualizare continut.

## Etapa 6: extindere editoriala la 1000 de cuvinte pe fisier

Obiectiv: fiecare fisier Markdown de continut sa ajunga la aproximativ 1000 de
cuvinte, pastrand structura modulara si tonul editorial al proiectului.

- [ ] Audit complet al fisierelor Markdown si al numarului de cuvinte.
- [ ] Extindere `knowledge_base/vibratii/`:
  - [ ] vibratii de baza 1-9;
  - [ ] vibratii maestre 11, 22 si 33;
  - [ ] armonizare intre capitolele `01-esenta.md` - `07-exemple.md`;
  - [ ] completare `index.md` pentru fiecare vibratie.
- [ ] Extindere `knowledge_base/tarot/`:
  - [ ] Arcane Majore;
  - [ ] Arcane Minore - bate;
  - [ ] Arcane Minore - cupe;
  - [ ] Arcane Minore - sabii;
  - [ ] Arcane Minore - monede;
  - [ ] README-uri de sinteza pentru fiecare grupa.
- [ ] Extindere `knowledge_base/calcule/`:
  - [ ] nume;
  - [ ] vibratii personale;
  - [ ] timp si cicluri;
  - [ ] pinacluri;
  - [ ] patratul lui Pitagora;
  - [ ] soarta si destin;
  - [ ] karma.
- [ ] Verificare ca fiecare fisier extins pastreaza:
  - [ ] definitie clara;
  - [ ] idei distincte dezvoltate in paragrafe scurte;
  - [ ] metoda sau interpretare aplicabila;
  - [ ] exemple concrete;
  - [ ] avertismente si limite;
  - [ ] legaturi cu alte concepte din baza de cunoastere.
- [ ] Regenerare `generated/index.json` dupa fiecare lot editorial.
- [ ] Verificare finala: toate fisierele Markdown relevante au cel putin 1000 de
  cuvinte.
