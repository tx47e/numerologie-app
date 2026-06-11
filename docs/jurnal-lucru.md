# Jurnal de lucru

Acest jurnal urmareste pasii importanti facuti in proiect.

## 2026-06-09

### Initializare continut

- A fost creat folderul `vibratii/`, mutat ulterior in `knowledge_base/vibratii/`.
- Au fost create fisierele initiale pentru vibratiile 1-9.
- Fiecare vibratie a primit capitole de baza:
  - Esenta
  - Arhetip
  - Lumina
  - Umbra
  - Lectii
  - Directii de dezvoltare
  - Exemple

### Conectare GitHub

- Workspace-ul local a fost conectat la repository-ul GitHub:
  `tx47e/numerologie-app`.
- Remote-ul local `origin` indica spre:
  `https://github.com/tx47e/numerologie-app.git`.
- Branch-ul local a fost aliniat la `main`.

### Restructurare continut

- Fisierele plate `vibratia-1.md` pana la `vibratia-9.md` au fost transformate
  in directoare dedicate.
- Fiecare vibratie are acum propriul director:
  - `knowledge_base/vibratii/vibratia-1/`
  - `knowledge_base/vibratii/vibratia-2/`
  - `knowledge_base/vibratii/vibratia-3/`
  - `knowledge_base/vibratii/vibratia-4/`
  - `knowledge_base/vibratii/vibratia-5/`
  - `knowledge_base/vibratii/vibratia-6/`
  - `knowledge_base/vibratii/vibratia-7/`
  - `knowledge_base/vibratii/vibratia-8/`
  - `knowledge_base/vibratii/vibratia-9/`
- Fiecare capitol a fost separat intr-un fisier Markdown propriu.
- Fiecare director de vibratie contine un `README.md` pentru navigare.
- Fisierele initiale au fost pastrate temporar ca `_sursa-initiala.md`.

### Documentare proiect

- A fost adaugat `README.md` la radacina proiectului.
- A fost creat directorul `docs/`.
- Au fost adaugate documente pentru jurnal, decizii, roadmap si structura de date.

### Structura calcule

- A fost creat directorul `calcule/`, mutat ulterior in `knowledge_base/calcule/`.
- Au fost adaugate rubrici pentru:
  - vibratii personale;
  - calcule pe baza numelui;
  - vibratia anului personal si tema anului;
  - ani importanti interiori si exteriori;
  - cicluri de 7, 9 si 12 ani;
  - soarta, destin si tema vietii;
  - pinacluri;
  - patratul lui Pitagora.
- Fiecare calcul important are pregatite fisiere pentru metoda, semnificatii,
  exemple si observatii, unde este cazul.

### Restructurare proiect

- A fost creat directorul `knowledge_base/`.
- Directoarele `vibratii/` si `calcule/` au fost mutate in `knowledge_base/`.
- Au fost create directoarele:
  - `prompts/`;
  - `style_guide/`;
  - `memory/`;
  - `bibliography/`;
  - `examples/`;
  - `scripts/`;
  - `generated/`.
- Scopul este separarea clara intre baza numerologica, documentatia de proiect,
  prompturi, exemple, surse si fisiere generate.

### Extindere continut vibratii

- A fost stabilit tonul editorial final in `style_guide/README.md`.
- Au fost definite regulile pentru:
  - ton general;
  - raportul dintre simbolic, psihologic si practic;
  - structura capitolelor;
  - exemple;
  - avertismente si limite;
  - consistenta termenilor.
- Capitolele `Arhetip` au fost extinse pentru vibratiile 1-9 si pentru numerele
  maestre 11, 22 si 33.
- Extinderea a adaugat pentru fiecare arhetip:
  - mod de recunoastere in viata reala;
  - rol matur;
  - risc de umbra;
  - lectie principala de integrare.
- Au fost extinse si celelalte capitole pentru vibratiile 1-9 si numerele
  maestre 11, 22 si 33:
  - `Esenta` a primit intrebarea centrala si recunoasterea in viata cotidiana;
  - `Lumina` si `Umbra` au primit manifestari in relatii si munca;
  - `Lectii` a primit intrebari de lucru;
  - `Directii de dezvoltare` a primit practici utile;
  - `Exemple` a primit cate un exemplu de integrare.

## 2026-06-10

### Etapa 2: model de date

- A fost stabilita decizia tehnica pentru continut:
  - Markdown ramane sursa editoriala;
  - `generated/index.json` devine artefactul consumabil de aplicatie;
  - baza de date ramane o optiune ulterioara, nu o dependenta initiala.
- A fost adaugat `docs/model-date.md` cu schema pentru:
  - vibratii;
  - capitole;
  - calcule;
  - exemple de calcul;
  - inputuri canonice.
- A fost adaugat scriptul `scripts/genereaza_index_json.py`, care construieste
  indexul JSON din structura curenta din `knowledge_base/`.
- Au fost eliminate backup-urile temporare `_sursa-initiala.md` din directoarele
  vibratiilor 1-9, dupa validarea capitolelor separate.
- A fost actualizat `docs/roadmap.md` pentru starea curenta a proiectului si
  pentru urmatoarea etapa: motorul numerologic.
