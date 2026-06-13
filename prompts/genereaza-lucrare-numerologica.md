# Prompt - genereaza lucrare numerologica

Foloseste acest prompt pentru a genera o lucrare numerologica completa, pe baza
template-ului si a documentatiei din proiect.

```text
Vreau sa generezi o lucrare numerologica pentru persoana de mai jos.

Date persoana:
- Nume complet:
- Nume de familie:
- Prenume:
- Prenume activ, daca este cunoscut:
- Porecla / nume uzual / cum este chemata persoana in viata de zi cu zi:
- Data nasterii:
- Nume anterior / schimbat, daca exista:
- Nume inainte de casatorie, daca exista:
- Intrebare personala sau tema principala, daca exista:
- Nivel de detaliere dorit: scurt / mediu / amplu / foarte amplu
- Stil de adresare dorit: conversational / formal

Surse de lucru:
- Foloseste template-ul din `examples/Template-lucrare-numerologie.md`.
- Foloseste in primul rand documentatia consolidata din `knowledge_base/`.
- Verifica si `knowledge_base/exprimari/` pentru formulari validate ale
  interpretarilor recurente. Daca exista o exprimare potrivita pentru rezultatul
  calculat, foloseste-o ca baza si adapteaz-o la persoana analizata.
- Foloseste `bibliography/` doar ca sursa primara de verificare atunci cand
  informatia nu este suficient dezvoltata in `knowledge_base/`.

Reguli de redactare:
- Nu transforma lucrarea intr-o lista mecanica de calcule.
- Nu adauga descrieri ample la date administrative sau rubrici evidente.
- Respecta nivelul de detaliere cerut. Daca nu este specificat, foloseste
  nivelul amplu, cu explicatii bogate doar la concepte, calcule si interpretari
  importante.
- Cand apare un concept numerologic sau un calcul, explica-l bogat, amplu si
  academic, dar pe intelesul unui cititor obisnuit. Explicatia trebuie sa ajute
  omul sa inteleaga ideea si sa o poata recunoaste in viata de zi cu zi.
- Dupa fiecare tabel important, scrie o interpretare cursiva, in paragrafe
  firesti.
- Aseaza tabelele ingrijit: textul din celule, mai ales capul de tabel, nu
  trebuie rupt nefiresc. Redu coloanele care permit asta si largeste coloanele
  care au nevoie de spatiu, pastrand tabelul clar si usor de citit.
- La scara bunastarii, explica atat valorile casutelor, cat si fiecare vector:
  cantitatea cifrelor, formula valorii totale, valoarea obtinuta si sensul
  practic al rezultatului.
- Dupa matricea datei de nastere si matricea numelui, fa citirea comparativa
  dupa metoda din Patratul lui Pitagora: casute sustinute, amplificate,
  nesustinute, native si matricea rezultat.
- Leaga rezultatele intre ele: data nasterii, karma, matricea, scara
  bunastarii, numele, pinaclurile, ciclurile, ezoterismul si concluzia.
- Tonul trebuie sa fie prietenos, cald, limpede si usor poetic unde se potriveste,
  dar practic si aplicabil. Cititorul trebuie sa se simta ghidat de-a lungul
  lucrarii, nu pierdut in concepte sau judecati.
- Respecta stilul de adresare cerut. Pentru `conversational`, scrie ca o
  discutie directa cu persoana analizata, folosind numele uzual, porecla sau
  prenumele activ, daca este cunoscut, si persoana a doua singular: `Mihai,
  aceasta vibratie iti arata...`. Pentru `formal`, scrie ca o analiza despre
  persoana, la persoana a treia, pastrand tonul cald, clar si respectuos. Daca
  stilul nu este specificat, foloseste `formal`.
- Evita verdictul fatalist. Formuleaza rezultatele ca directii de constientizare,
  maturizare si lucru practic.
- Daca o informatie lipseste, marcheaz-o discret ca `de completat` si continua cu
  ce se poate calcula corect.
- Pentru fiecare interpretare recurenta, verifica mai intai daca exista deja o
  exprimare potrivita in `knowledge_base/exprimari/`. Daca exista mai multe
  variante potrivite, alege una care aduce varietate fata de alte lucrari
  apropiate, mai ales cand analizezi persoane din aceeasi familie sau acelasi
  grup.
- Genereaza o exprimare noua daca variantele existente nu se potrivesc
  rezultatului, stilului, nivelului de detaliere, contextului lucrarii sau daca
  este nevoie de o formulare diferita pentru a evita repetitia intre lucrari
  apropiate.
- Daca generezi o interpretare noua valoroasa pentru o tema recurenta, noteaz-o
  ca text care merita salvat in `knowledge_base/exprimari/`, in fisierul temei
  potrivite. Cand este salvata, exprimarea trebuie sa aiba index numeric, stil
  (`formal` sau `conversational`) si nivel de detaliere (`scurt`, `mediu`,
  `amplu` sau `foarte amplu`), context scurt si lista lucrarilor unde a fost
  folosita. Daca refolosesti o exprimare existenta intr-o lucrare noua, adauga
  lucrarea noua in lista acelei variante, nu crea automat o varianta noua.

Structura lucrarii:
1. Date lucrare
2. Sinteza scurta
3. Date de baza si calcule initiale
4. Karma din data nasterii
5. Matricea numerologica
6. Scara bunastarii
7. Numele
8. Oportunitati, provocari si pinacluri
9. Soarta si destinul
10. Lectii de viata si cicluri
11. Ezoterism si aplicabilitate
12. Concluzie finala
13. Harta documentatie folosita

La final:
- Mentioneaza ce rubrici au ramas incomplete.
- Mentioneaza ce date ar trebui confirmate pentru o versiune finala.
- Pastreaza lucrarea in format Markdown.
```

## Cum functioneaza promptul

Promptul este construit in patru straturi:

1. Datele persoanei: ii spune generatorului ce informatii concrete are voie sa
   foloseasca.
2. Sursele de lucru: il obliga sa porneasca de la template si de la
   `knowledge_base/`, nu de la improvizatie.
3. Regulile de redactare: stabilesc tonul si impiedica doua extreme: textul prea
   sec, doar cu tabele, si textul prea incarcat cu explicatii inutile.
4. Structura lucrarii: pastreaza ordinea capitolelor, astfel incat fiecare analiza
   sa fie comparabila cu celelalte.

Partea cea mai importanta este regula: explica doar conceptele si calculele, nu
datele administrative. Astfel, cititorul primeste context acolo unde are nevoie
sa inteleaga numerologia, dar lucrarea ramane fluida.
