# Test HTML

Aplicatie locala de test pentru completarea datelor unei persoane si generarea
unei lucrari numerologice in format Markdown + HTML.

## Pornire

Din radacina proiectului:

```powershell
C:\Users\Mihai\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe "test HTML\server.py"
```

Apoi deschide in browser:

```text
http://localhost:8787
```

## Ce face

1. Afiseaza un formular cu datele cerute de skill-ul `numerology-agent`.
2. Ruleaza scripturile existente:
   - `scripts/calcule_numerologice.py`
   - `scripts/patratul_lui_pitagora.py`
3. Daca exista deja o lucrare completa pentru acea persoana in `examples/`, o
   foloseste ca sursa Markdown.
4. Daca nu exista, genereaza un Markdown de lucru in `test HTML/output/`.
5. Transpune Markdown-ul in HTML in acelasi director, cu paleta teal, turcoaz,
   crem si brun auriu.
5. Returneaza linkuri catre ambele fisiere.

## Nota

Acesta este un prototip local. Pentru persoanele care au deja o lucrare completa
in `examples/`, HTML-ul contine toata lucrarea si interpretarile. Pentru persoane
noi, fallback-ul automat trebuie extins in continuare dupa regulile din
`skills/numerology-agent/SKILL.md` si template-ul din
`examples/Template-lucrare-numerologie.md`.
