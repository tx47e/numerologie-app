# Decizii de proiect

## Baza de continut in Markdown

Continutul numerologic este pastrat initial in fisiere Markdown.

Motivatie:

- este usor de editat manual;
- poate fi versionat clar in Git;
- permite separarea pe capitole;
- poate fi convertit ulterior in JSON, baza de date sau continut CMS.

## Director separat pentru fiecare vibratie

Fiecare vibratie are propriul director.

Motivatie:

- continutul poate creste fara ca fisierele sa devina prea mari;
- fiecare capitol poate fi extins independent;
- aplicatia poate incarca selectiv doar capitolele necesare;
- structura ramane clara pentru editare si audit.

## Capitole standardizate

Pentru toate vibratiile folosim aceleasi capitole initiale:

- Esenta
- Arhetip
- Lumina
- Umbra
- Lectii
- Directii de dezvoltare
- Exemple

Motivatie:

- comparabilitate intre vibratii;
- structura predictibila pentru UI;
- baza stabila pentru generarea de interpretari.

## Actualizare GitHub pentru schimbari majore

Schimbarile majore vor fi comise si publicate in GitHub.

Flux de lucru:

1. modificari locale;
2. verificare status;
3. staging;
4. commit;
5. push pe GitHub.
