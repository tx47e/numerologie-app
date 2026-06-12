# Scripts

Acest director va contine scripturi pentru automatizare.

Exemple posibile:

- generare index JSON din Markdown;
- validare linkuri interne;
- verificare structura `knowledge_base/`;
- conversie continut;
- pregatire date pentru aplicatie.

## Generare model de date

Indexul consumabil de aplicatie se genereaza din Markdown:

```powershell
python scripts\genereaza_index_json.py
```

Rezultatul este `generated/index.json`. Fisierul generat nu trebuie editat
manual; sursa de adevar ramane continutul din `knowledge_base/` si contractul
documentat in `docs/model-date.md`.

## Regula pentru calcule

Fiecare calcul numerologic validat in `knowledge_base/calcule/` trebuie sa aiba
script rulabil in doua variante:

- Python, pentru prototipare rapida si validare locala;
- Java, pentru portare usoara daca aplicatia va folosi JVM sau logica server-side
  in Java.

Cele doua variante trebuie sa pastreze aceeasi metoda, aceleasi inputuri si
acelasi rezultat afisat. Sursa de adevar pentru formula ramane fisierul
`01-metoda.md` al calculului din `knowledge_base/calcule/`.

Conventie nume fisiere:

```text
scripts/<slug_calcul>.py
scripts/<NumeCalcul>.java
```

Exemplu:

```text
scripts/patratul_lui_pitagora.py
scripts/PatratulLuiPitagora.java
```

## Calcule de implementat

Lista initiala vine din `docs/roadmap.md` si din structura
`knowledge_base/calcule/`:

- numarul de exprimare;
- numarul activ;
- numarul ereditar;
- numarul ereditar karmic;
- vibratia interioara;
- vibratia exterioara;
- vibratia datei nasterii;
- vibratia anului personal;
- ani importanti interiori;
- ani importanti exteriori;
- soarta;
- destin;
- tema vietii;
- pinacluri;
- cicluri de 7 ani;
- cicluri de 9 ani;
- cicluri de 12 ani;
- patratul lui Pitagora.

## Profil numerologic complet

Scripturile comune calculeaza intr-un singur profil:

- vibratia interioara;
- vibratia exterioara;
- numarul de exprimare / destin;
- numarul activ;
- numarul ereditar;
- numarul ereditar karmic;
- soarta;
- tema vietii;
- vibratia anului personal;
- karma zilei de nastere;
- karma lunii de nastere;
- karma din calea destinului;
- numarul ereditar karmic / numarul neamului;
- ani importanti interiori si exteriori;
- pinacluri si provocari;
- cicluri de 7, 9 si 12 ani.

Python:

```powershell
python scripts\calcule_numerologice.py --zi 24 --luna 4 --an 1982 --nume "Ana Maria Popescu" --nume-familie "Popescu" --an-analizat 2026 --start 2026 --stop 2035 --varsta 44
```

Cu analiza numelui inainte si dupa casatorie:

```powershell
python scripts\calcule_numerologice.py --zi 24 --luna 4 --an 1982 --nume "Ana Maria Popescu" --nume-familie "Popescu" --nume-inainte-casatorie "Ana Maria Ionescu" --nume-dupa-casatorie "Ana Maria Popescu" --nume-familie-inainte "Ionescu" --nume-familie-dupa "Popescu" --an-analizat 2026 --start 2026 --stop 2035 --varsta 44
```

Java:

```powershell
javac scripts\CalculeNumerologice.java
java -cp scripts CalculeNumerologice --zi 24 --luna 4 --an 1982 --nume "Ana Maria Popescu" --nume-familie "Popescu" --an-analizat 2026 --start 2026 --stop 2035 --varsta 44
```

## Patratul lui Pitagora

Scripturile pentru patratul lui Pitagora folosesc metoda documentata in
`knowledge_base/calcule/patratul-lui-pitagora/01-metoda.md`.

Python:

```powershell
python scripts\patratul_lui_pitagora.py 7 11 1994
```

Cu matrice separata pentru nume:

```powershell
python scripts\patratul_lui_pitagora.py 24 4 1982 --nume "Ana Maria Popescu"
```

Java:

```powershell
javac scripts\PatratulLuiPitagora.java
java -cp scripts PatratulLuiPitagora 7 11 1994
java -cp scripts PatratulLuiPitagora 24 4 1982 --nume "Ana Maria Popescu"
```
