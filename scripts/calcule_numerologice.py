import argparse
import sys
import unicodedata


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


ALFABET = {
    **dict.fromkeys("AJS", 1),
    **dict.fromkeys("BKT", 2),
    **dict.fromkeys("CLU", 3),
    **dict.fromkeys("DMV", 4),
    **dict.fromkeys("ENW", 5),
    **dict.fromkeys("FOX", 6),
    **dict.fromkeys("GPY", 7),
    **dict.fromkeys("HQZ", 8),
    **dict.fromkeys("IR", 9),
}

DATORII_KARMICE = {13, 14, 16, 19}


def normalizeaza_text(text):
    fara_diacritice = unicodedata.normalize("NFD", text)
    fara_diacritice = "".join(
        caracter for caracter in fara_diacritice
        if unicodedata.category(caracter) != "Mn"
    )
    return "".join(caracter for caracter in fara_diacritice.upper() if caracter.isalpha())


def valori_nume(nume):
    litere = normalizeaza_text(nume)
    return [(litera, ALFABET[litera]) for litera in litere if litera in ALFABET]


def reducere(numar):
    pasi = []
    curent = numar
    while curent > 9:
        cifre = [int(cifra) for cifra in str(curent)]
        rezultat = sum(cifre)
        pasi.append((curent, cifre, rezultat))
        curent = rezultat
    return curent, pasi


def data_cod(zi, luna, an):
    return f"{zi:02d}{luna:02d}{an:04d}"


def vibratie_din_numar(numar):
    rezultat, _ = reducere(numar)
    return rezultat


def vibratia_numelui(nume):
    valori = valori_nume(nume)
    total = sum(valoare for _, valoare in valori)
    rezultat, pasi = reducere(total)
    return {"total": total, "rezultat": rezultat, "pasi": pasi, "valori": valori}


def frecvente_nume(nume):
    frecvente = {numar: 0 for numar in range(1, 10)}
    for _, valoare in valori_nume(nume):
        frecvente[valoare] += 1
    return frecvente


def lectii_karmice(nume):
    frecvente = frecvente_nume(nume)
    return [numar for numar, aparitii in frecvente.items() if aparitii == 0]


def soarta(zi, luna, an):
    cifre = [int(cifra) for cifra in data_cod(zi, luna, an)]
    total = sum(cifre)
    rezultat, pasi = reducere(total)
    return {"total": total, "rezultat": rezultat, "pasi": pasi}


def vibratia_anului(zi, luna, an_analizat):
    cifre = [int(cifra) for cifra in f"{zi:02d}{luna:02d}{an_analizat:04d}"]
    total = sum(cifre)
    rezultat, pasi = reducere(total)
    return {"total": total, "rezultat": rezultat, "pasi": pasi}


def ani_importanti(zi, luna, start, stop):
    interior = vibratie_din_numar(zi)
    exterior = vibratie_din_numar(luna)
    ani_interiori = []
    ani_exteriori = []
    for an in range(start, stop + 1):
        vibratie = vibratia_anului(zi, luna, an)["rezultat"]
        if vibratie == interior:
            ani_interiori.append(an)
        if vibratie == exterior:
            ani_exteriori.append(an)
    return {
        "vibratie_interioara": interior,
        "vibratie_exterioara": exterior,
        "ani_interiori": ani_interiori,
        "ani_exteriori": ani_exteriori,
    }


def pinacluri(zi, luna, an):
    zi_redusa = vibratie_din_numar(zi)
    luna_redusa = vibratie_din_numar(luna)
    an_redus = vibratie_din_numar(sum(int(cifra) for cifra in f"{an:04d}"))
    soarta_rezultat = soarta(zi, luna, an)["rezultat"]

    p1 = vibratie_din_numar(luna_redusa + zi_redusa)
    p2 = vibratie_din_numar(zi_redusa + an_redus)
    p3 = vibratie_din_numar(p1 + p2)
    p4 = vibratie_din_numar(luna_redusa + an_redus)

    c1 = abs(zi_redusa - luna_redusa)
    c2 = abs(zi_redusa - an_redus)
    c3 = abs(c1 - c2)
    c4 = abs(luna_redusa - an_redus)

    sfarsit1 = 36 - soarta_rezultat
    sfarsit2 = sfarsit1 + 9
    sfarsit3 = sfarsit2 + 9

    return [
        {"nr": 1, "varsta": f"0-{sfarsit1}", "pinaclu": p1, "provocare": c1},
        {"nr": 2, "varsta": f"{sfarsit1 + 1}-{sfarsit2}", "pinaclu": p2, "provocare": c2},
        {"nr": 3, "varsta": f"{sfarsit2 + 1}-{sfarsit3}", "pinaclu": p3, "provocare": c3},
        {"nr": 4, "varsta": f"{sfarsit3 + 1}+", "pinaclu": p4, "provocare": c4},
    ]


def cicluri(varsta):
    return {
        7: {"ciclu": varsta // 7 + 1, "pozitie": varsta % 7 + 1},
        9: {"ciclu": varsta // 9 + 1, "pozitie": varsta % 9 + 1},
        12: {"ciclu": varsta // 12 + 1, "pozitie": varsta % 12 + 1},
    }


def datorii_karmice(nume, zi, luna, an):
    total_nume = vibratia_numelui(nume)["total"]
    total_data = soarta(zi, luna, an)["total"]
    gasite = sorted({total for total in [total_nume, total_data] if total in DATORII_KARMICE})
    return gasite


def afiseaza_lista(titlu, valori):
    print(titlu)
    print(", ".join(str(valoare) for valoare in valori) if valori else "-")
    print()


def main():
    parser = argparse.ArgumentParser(description="Calcule numerologice de baza pentru proiect.")
    parser.add_argument("--zi", type=int, required=True)
    parser.add_argument("--luna", type=int, required=True)
    parser.add_argument("--an", type=int, required=True)
    parser.add_argument("--nume", required=True)
    parser.add_argument("--nume-familie", required=True)
    parser.add_argument("--an-analizat", type=int, default=2026)
    parser.add_argument("--start", type=int, default=2026)
    parser.add_argument("--stop", type=int, default=2035)
    parser.add_argument("--varsta", type=int, default=0)
    args = parser.parse_args()

    nume = vibratia_numelui(args.nume)
    destin = nume["rezultat"]
    soarta_rezultat = soarta(args.zi, args.luna, args.an)
    tema_vietii = vibratie_din_numar(soarta_rezultat["rezultat"] + destin)
    an_personal = vibratia_anului(args.zi, args.luna, args.an_analizat)
    ani = ani_importanti(args.zi, args.luna, args.start, args.stop)
    karma_neam = vibratia_numelui(args.nume_familie)

    print("Calcule numerologice")
    print("====================")
    print(f"Data: {args.zi:02d}.{args.luna:02d}.{args.an:04d}")
    print(f"Nume: {args.nume}")
    print()

    print(f"Vibratia interioara: {vibratie_din_numar(args.zi)}")
    print(f"Vibratia exterioara: {vibratie_din_numar(args.luna)}")
    print(f"Vibratia numelui / destin: {destin} (total {nume['total']})")
    print(f"Soarta: {soarta_rezultat['rezultat']} (total {soarta_rezultat['total']})")
    print(f"Tema vietii: {tema_vietii}")
    print(f"Vibratia anului {args.an_analizat}: {an_personal['rezultat']} (total {an_personal['total']})")
    print()

    afiseaza_lista("Lectii karmice personale:", lectii_karmice(args.nume))
    afiseaza_lista("Datorii karmice personale:", datorii_karmice(args.nume, args.zi, args.luna, args.an))
    afiseaza_lista("Lectii karmice de neam:", lectii_karmice(args.nume_familie))
    print(f"Karma neamului: {karma_neam['rezultat']} (total {karma_neam['total']})")
    print()

    afiseaza_lista(f"Ani importanti interiori {args.start}-{args.stop}:", ani["ani_interiori"])
    afiseaza_lista(f"Ani importanti exteriori {args.start}-{args.stop}:", ani["ani_exteriori"])

    print("Pinacluri si provocari:")
    for etapa in pinacluri(args.zi, args.luna, args.an):
        print(
            f"{etapa['nr']}. varsta {etapa['varsta']}: "
            f"pinaclu {etapa['pinaclu']}, provocare {etapa['provocare']}"
        )
    print()

    print(f"Cicluri pentru varsta {args.varsta}:")
    for durata, rezultat in cicluri(args.varsta).items():
        print(f"{durata} ani: ciclul {rezultat['ciclu']}, pozitia {rezultat['pozitie']}")


if __name__ == "__main__":
    main()
