# Karma personala - metoda

Karma personala se citeste ca imagine combinata din doua surse:

1. data nasterii;
2. numele complet.

Cele doua calcule nu se exclud. Data nasterii arata programul karmic de baza,
iar numele complet arata cum se manifesta sau se completeaza acest program prin
identitatea purtata de persoana.

## Karma personala din data nasterii

Din data nasterii se citesc trei straturi bibliografice:

- karma zilei de nastere: ziua indica programul karmic legat de Arcanele Majore;
- karma lunii de nastere: luna indica datoria sociala, familiala sau personala;
- karma din calea destinului: suma cifrelor datei arata ritmul karmic, tipul de
  sanse, obstacole si ajutoare.

```text
karma_zilei = ziua nasterii
karma_lunii = luna nasterii
calea_destinului_karmica = suma cifrelor din data nasterii, neredusa complet
```

Pentru datorii karmice numerice se verifica daca suma cifrelor datei este unul
dintre numerele:

```text
13, 14, 16, 19
```

## Karma personala din numele complet

### Lectii karmice

Lectiile karmice sunt cifrele de la 1 la 9 care lipsesc din numele complet.

```text
lectii karmice = numerele 1-9 cu frecventa 0 in valorile literelor numelui complet
```

### Datorii karmice

Datoriile karmice sunt marcate cand in traseul de calcul apare unul dintre
numerele:

```text
13, 14, 16, 19
```

Pentru stratul din nume verificam aparitia acestor numere in:

- totalul numelui;
- totalul folosit pentru destin.

Pentru imaginea combinata, datoriile din nume se citesc impreuna cu datoriile
din data.

## Formula pentru implementare

```text
functie karma_personala(nume, zi, luna, an):
  frecvente = frecvente_valori_litere(nume)
  lectii = numerele 1..9 unde frecventa este 0
  datorii_nume = valori din {13, 14, 16, 19} aparute in totalurile numelui
  karma_zilei = zi
  karma_lunii = luna
  calea_destinului = suma_cifrelor(zi, luna, an)
  datorii_data = calea_destinului daca este in {13, 14, 16, 19}
  datorii = datorii_nume + datorii_data
  return {
    din_data: { karma_zilei, karma_lunii, calea_destinului, datorii_data },
    din_nume: { lectii, datorii_nume },
    lectii,
    datorii
  }
```

## Nume schimbat prin casatorie

Daca exista nume inainte si dupa casatorie, karma personala se calculeaza pentru
ambele variante:

```text
karma_nume_inainte = karma_personala(nume_inainte_casatorie, zi, luna, an)
karma_nume_dupa = karma_personala(nume_dupa_casatorie, zi, luna, an)
```

Comparatia urmareste:

- lectii karmice comune;
- lectii karmice prezente doar in numele dinainte;
- lectii karmice prezente doar in numele de dupa;
- datorii karmice comune;
- datorii karmice care apar sau dispar prin schimbarea numelui.

## Observatie

Karma personala nu se reduce la un singur numar. Imaginea completa apare din
suprapunerea datelor: ce aduce persoana prin data nasterii si ce activeaza sau
completeaza prin numele complet. Lectiile karmice nu sunt tratate ca verdict. Ele
indica zone care pot cere dezvoltare constienta.
