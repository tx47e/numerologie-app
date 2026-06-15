import argparse
import sys
import unicodedata

from patratul_lui_pitagora import calculeaza_matrice_nume


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
VOCALE = set("AEIOU")

KARMA_LUNII_TEME = {
    1: "karma fata de frate sau sora",
    2: "karma bunatatii, bunicilor si femeilor",
    3: "karma independentei fata de mama",
    4: "karma fata de tata",
    5: "karma fata de mama",
    6: "karma armoniei dintre mama si tata",
    7: "karma mobilitatii",
    8: "karma modelarii lumii parintilor",
    9: "karma talentului neamului",
    10: "karma capitalului neamului",
    11: "karma statutului neamului",
    12: "karma fata de sine",
}


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


def componente_nume(nume):
    componente = []
    for parte in nume.replace("-", " ").split():
        litere = normalizeaza_text(parte)
        if litere:
            componente.append((parte, [(litera, ALFABET[litera]) for litera in litere if litera in ALFABET]))
    return componente


def prima_componenta_nume(nume):
    componente = componente_nume(nume)
    return componente[0][0] if componente else nume


def ultima_componenta_nume(nume):
    componente = componente_nume(nume)
    return componente[-1][0] if componente else nume


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
    componente = []
    for componenta, valori in componente_nume(nume):
        total_componenta = sum(valoare for _, valoare in valori)
        rezultat_componenta, pasi_componenta = reducere(total_componenta)
        componente.append({
            "componenta": componenta,
            "total": total_componenta,
            "rezultat": rezultat_componenta,
            "pasi": pasi_componenta,
            "valori": valori,
        })

    total = sum(componenta["rezultat"] for componenta in componente)
    rezultat, pasi = reducere(total)
    valori = [valoare for componenta in componente for valoare in componenta["valori"]]
    return {
        "total": total,
        "rezultat": rezultat,
        "pasi": pasi,
        "valori": valori,
        "componente": componente,
    }


def vibratie_litere(nume, pastreaza):
    valori = [(litera, valoare) for litera, valoare in valori_nume(nume) if pastreaza(litera)]
    total = sum(valoare for _, valoare in valori)
    rezultat, pasi = reducere(total)
    return {
        "total": total,
        "rezultat": rezultat,
        "pasi": pasi,
        "valori": valori,
    }


def numar_intim(nume):
    return vibratie_litere(nume, lambda litera: litera in VOCALE)


def numar_de_realizare(nume):
    return vibratie_litere(nume, lambda litera: litera not in VOCALE)


def numar_activ(nume):
    return vibratia_numelui(prima_componenta_nume(nume))


def numar_ereditar(nume):
    return vibratia_numelui(ultima_componenta_nume(nume))


def reducere_22(numar):
    curent = numar
    while curent > 22:
        curent -= 22
    return curent


def numar_ereditar_karmic(nume):
    familie = ultima_componenta_nume(nume)
    valori = valori_nume(familie)
    total = sum(valoare for _, valoare in valori)
    return {
        "nume_familie": familie,
        "total": total,
        "rezultat": reducere_22(total),
        "valori": valori,
    }


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


def inlocuieste_zero_cu_unu(text):
    return text.replace("0", "1")


def zona_confort_grafica(numar_grafic):
    cifre = [int(cifra) for cifra in numar_grafic]
    return {
        "suma": sum(cifre),
        "zona": sum(cifre) / len(cifre),
        "cifre": cifre,
    }


def soarta_si_destin_grafic(zi, luna, an):
    zzll = f"{zi:02d}{luna:02d}"
    aaaa = f"{an:04d}"
    soarta_numar = int(zzll) * int(aaaa)
    zzll_destin = inlocuieste_zero_cu_unu(zzll)
    aaaa_destin = inlocuieste_zero_cu_unu(aaaa)
    destin_numar = int(zzll_destin) * int(aaaa_destin)
    soarta_grafica = f"{soarta_numar:07d}"
    destin_grafic = f"{destin_numar:07d}"
    return {
        "soarta": {
            "formula": f"{zzll} x {aaaa}",
            "numar": soarta_grafica,
            "zona_confort": zona_confort_grafica(soarta_grafica),
        },
        "destin": {
            "formula": f"{zzll_destin} x {aaaa_destin}",
            "numar": destin_grafic,
            "zona_confort": zona_confort_grafica(destin_grafic),
        },
    }


def vibratia_anului(zi, luna, an_analizat):
    cifre = [int(cifra) for cifra in f"{zi:02d}{luna:02d}{an_analizat:04d}"]
    total = sum(cifre)
    rezultat, pasi = reducere(total)
    return {"total": total, "rezultat": rezultat, "pasi": pasi}


def suma_cifre_numar(numar):
    return sum(int(cifra) for cifra in str(abs(numar)))


def ani_importanti_exteriori(an_nastere, start, stop):
    ani = []
    an_curent = an_nastere
    while True:
        an_curent += suma_cifre_numar(an_curent)
        if an_curent > stop:
            break
        if an_curent >= start:
            ani.append(an_curent)
    return ani


def ani_importanti_interiori(an_nastere, start, stop):
    ani = []
    an_curent = an_nastere
    while True:
        an_curent += vibratie_din_numar(an_curent)
        if an_curent > stop:
            break
        if an_curent >= start:
            ani.append(an_curent)
    return ani


def ani_importanti(zi, luna, an_nastere, start, stop):
    interior = vibratie_din_numar(zi)
    exterior = vibratie_din_numar(luna)
    return {
        "vibratie_interioara": interior,
        "vibratie_exterioara": exterior,
        "ani_interiori": ani_importanti_interiori(an_nastere, start, stop),
        "ani_exteriori": ani_importanti_exteriori(an_nastere, start, stop),
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


def datorii_karmice_nume(nume):
    total_nume = vibratia_numelui(nume)["total"]
    return [total_nume] if total_nume in DATORII_KARMICE else []


def arcana_karma_zilei(zi):
    return 0 if zi == 22 else ((zi - 1) % 22) + 1


def procent_karma_zi(zi):
    if zi <= 9:
        return "spre 100%"
    if zi <= 19:
        return "spre 80%"
    if zi <= 29:
        return "spre 60%"
    return "spre 40%"


def categorie_cale_karmica(cale):
    if 4 <= cale <= 9:
        return "0 - prezenta, centrare, aliniere in prezent"
    if 10 <= cale <= 19:
        return "1 - desavarsirea sinelui"
    if 20 <= cale <= 29:
        return "2 - prelucrarea karmei"
    if 30 <= cale <= 39:
        return "3 - influenta, relationare, transmitere de intelepciune"
    if 40 <= cale <= 48:
        return "4 - stapanirea resurselor materiale si umane"
    return "in afara intervalului documentat 4-48"


def karma_din_calea_destinului(zi, luna, an):
    cale = soarta(zi, luna, an)["total"]
    return {
        "calea_destinului": cale,
        "categorie_cale": categorie_cale_karmica(cale),
        "datorii": [cale] if cale in DATORII_KARMICE else [],
    }


def karma_zilei_de_nastere(zi):
    return {
        "karma_zilei": zi,
        "arcana_zilei": arcana_karma_zilei(zi),
        "procent_karma_zi": procent_karma_zi(zi),
    }


def karma_lunii_de_nastere(luna):
    return {
        "karma_lunii": luna,
        "tema_lunii": KARMA_LUNII_TEME.get(luna, "luna invalida"),
    }


def analiza_nume(nume, zi, luna, an, nume_familie=None):
    vibratie = vibratia_numelui(nume)
    matrice = calculeaza_matrice_nume(nume)
    familie = nume_familie if nume_familie else ultimul_cuvant(nume)

    return {
        "nume": nume,
        "nume_familie": familie,
        "numar_exprimare": vibratie,
        "numar_intim": numar_intim(nume),
        "numar_de_realizare": numar_de_realizare(nume),
        "numar_activ": numar_activ(nume),
        "numar_ereditar": vibratia_numelui(familie),
        "numar_ereditar_karmic": numar_ereditar_karmic(familie),
        "matrice": matrice,
        "lectii_karmice": lectii_karmice(nume),
        "datorii_karmice_nume": datorii_karmice_nume(nume),
        "datorii_karmice_personale": datorii_karmice(nume, zi, luna, an),
    }


def ultimul_cuvant(text):
    parti = [parte for parte in text.replace("-", " ").split() if parte]
    return parti[-1] if parti else text


def compara_liste(inainte, dupa):
    set_inainte = set(inainte)
    set_dupa = set(dupa)
    return {
        "comune": sorted(set_inainte & set_dupa),
        "doar_inainte": sorted(set_inainte - set_dupa),
        "doar_dupa": sorted(set_dupa - set_inainte),
    }


def compara_matrici(matrice_inainte, matrice_dupa):
    rezultat = []
    for cifra in range(1, 10):
        inainte = len(matrice_inainte["matrice"][cifra])
        dupa = len(matrice_dupa["matrice"][cifra])
        rezultat.append({
            "cifra": cifra,
            "inainte": inainte,
            "dupa": dupa,
            "diferenta": dupa - inainte,
        })
    return rezultat


def afiseaza_analiza_nume(titlu, analiza):
    print(titlu)
    print("-" * len(titlu))
    print(f"Nume: {analiza['nume']}")
    print(f"Nume familie: {analiza['nume_familie']}")
    print(
        f"Numar de exprimare / destin: {analiza['numar_exprimare']['rezultat']} "
        f"(total {analiza['numar_exprimare']['total']})"
    )
    print(
        f"Numar intim: {analiza['numar_intim']['rezultat']} "
        f"(total {analiza['numar_intim']['total']})"
    )
    print(
        f"Numar de realizare: {analiza['numar_de_realizare']['rezultat']} "
        f"(total {analiza['numar_de_realizare']['total']})"
    )
    print(
        f"Numar activ: {analiza['numar_activ']['rezultat']} "
        f"(total {analiza['numar_activ']['total']})"
    )
    print(
        f"Numar ereditar: {analiza['numar_ereditar']['rezultat']} "
        f"(total {analiza['numar_ereditar']['total']})"
    )
    print(
        f"Numar ereditar karmic: {analiza['numar_ereditar_karmic']['rezultat']} "
        f"(total {analiza['numar_ereditar_karmic']['total']})"
    )
    print()
    afiseaza_lista("Lectii karmice nume:", analiza["lectii_karmice"])
    afiseaza_lista("Datorii karmice din nume:", analiza["datorii_karmice_nume"])
    afiseaza_lista("Datorii karmice din nume si data:", analiza["datorii_karmice_personale"])

    matrice = analiza["matrice"]["matrice"]
    print("Matricea numelui:")
    print(f"{matrice[1]:<4} | {matrice[4]:<4} | {matrice[7]:<4}")
    print(f"{matrice[2]:<4} | {matrice[5]:<4} | {matrice[8]:<4}")
    print(f"{matrice[3]:<4} | {matrice[6]:<4} | {matrice[9]:<4}")
    print()


def afiseaza_comparatie_nume(inainte, dupa):
    print("Comparatie nume inainte / dupa casatorie")
    print("========================================")
    print(
        f"Numar de exprimare: {inainte['numar_exprimare']['rezultat']} -> "
        f"{dupa['numar_exprimare']['rezultat']}"
    )
    print(
        f"Numar intim: {inainte['numar_intim']['rezultat']} -> "
        f"{dupa['numar_intim']['rezultat']}"
    )
    print(
        f"Numar de realizare: {inainte['numar_de_realizare']['rezultat']} -> "
        f"{dupa['numar_de_realizare']['rezultat']}"
    )
    print(
        f"Numar ereditar karmic / numarul neamului: "
        f"{inainte['numar_ereditar_karmic']['rezultat']} -> "
        f"{dupa['numar_ereditar_karmic']['rezultat']}"
    )
    print()

    lectii = compara_liste(inainte["lectii_karmice"], dupa["lectii_karmice"])
    datorii = compara_liste(inainte["datorii_karmice_nume"], dupa["datorii_karmice_nume"])

    afiseaza_lista("Lectii karmice comune:", lectii["comune"])
    afiseaza_lista("Lectii karmice doar inainte:", lectii["doar_inainte"])
    afiseaza_lista("Lectii karmice doar dupa:", lectii["doar_dupa"])
    afiseaza_lista("Datorii karmice nume comune:", datorii["comune"])
    afiseaza_lista("Datorii karmice nume doar inainte:", datorii["doar_inainte"])
    afiseaza_lista("Datorii karmice nume doar dupa:", datorii["doar_dupa"])

    print("Comparatie matrice nume:")
    for rand in compara_matrici(inainte["matrice"], dupa["matrice"]):
        semn = "+" if rand["diferenta"] > 0 else ""
        print(
            f"{rand['cifra']}: {rand['inainte']} -> {rand['dupa']} "
            f"({semn}{rand['diferenta']})"
        )
    print()


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
    parser.add_argument("--nume-inainte-casatorie")
    parser.add_argument("--nume-dupa-casatorie")
    parser.add_argument("--nume-familie-inainte")
    parser.add_argument("--nume-familie-dupa")
    parser.add_argument("--an-analizat", type=int, default=2026)
    parser.add_argument("--start", type=int, default=2026)
    parser.add_argument("--stop", type=int, default=2035)
    parser.add_argument("--varsta", type=int, default=0)
    args = parser.parse_args()

    nume = vibratia_numelui(args.nume)
    intim = numar_intim(args.nume)
    realizare = numar_de_realizare(args.nume)
    activ = numar_activ(args.nume)
    ereditar = vibratia_numelui(args.nume_familie)
    ereditar_karmic = numar_ereditar_karmic(args.nume_familie)
    destin = nume["rezultat"]
    soarta_rezultat = soarta(args.zi, args.luna, args.an)
    grafic = soarta_si_destin_grafic(args.zi, args.luna, args.an)
    tema_vietii = vibratie_din_numar(soarta_rezultat["rezultat"] + destin)
    an_personal = vibratia_anului(args.zi, args.luna, args.an_analizat)
    ani = ani_importanti(args.zi, args.luna, args.an, args.start, args.stop)
    karma_zi = karma_zilei_de_nastere(args.zi)
    karma_luna = karma_lunii_de_nastere(args.luna)
    karma_cale = karma_din_calea_destinului(args.zi, args.luna, args.an)

    print("Calcule numerologice")
    print("====================")
    print(f"Data: {args.zi:02d}.{args.luna:02d}.{args.an:04d}")
    print(f"Nume: {args.nume}")
    print()

    print(f"Vibratia interioara: {vibratie_din_numar(args.zi)}")
    print(f"Vibratia exterioara: {vibratie_din_numar(args.luna)}")
    print(f"Numar de exprimare / destin: {destin} (total {nume['total']})")
    print(f"Numar intim: {intim['rezultat']} (total {intim['total']})")
    print(f"Numar de realizare: {realizare['rezultat']} (total {realizare['total']})")
    print(f"Numar activ: {activ['rezultat']} (total {activ['total']})")
    print(f"Numar ereditar: {ereditar['rezultat']} (total {ereditar['total']})")
    print(f"Numar ereditar karmic: {ereditar_karmic['rezultat']} (total {ereditar_karmic['total']})")
    print(f"Vibratia datei / destin: {soarta_rezultat['rezultat']} (cale {soarta_rezultat['total']})")
    print(
        f"Soarta grafica: {grafic['soarta']['numar']} "
        f"({grafic['soarta']['formula']}, zona {grafic['soarta']['zona_confort']['zona']:.2f})"
    )
    print(
        f"Destin grafic: {grafic['destin']['numar']} "
        f"({grafic['destin']['formula']}, zona {grafic['destin']['zona_confort']['zona']:.2f})"
    )
    print(f"Tema vietii: {tema_vietii}")
    print(f"Vibratia anului personal {args.an_analizat}: {an_personal['rezultat']} (total {an_personal['total']})")
    print()

    afiseaza_lista("Lectii karmice din nume:", lectii_karmice(args.nume))
    afiseaza_lista("Datorii karmice din nume:", datorii_karmice_nume(args.nume))
    print("Karma zilei de nastere:")
    print(
        f"{karma_zi['karma_zilei']} "
        f"(Arcana {karma_zi['arcana_zilei']}, "
        f"karma implinita {karma_zi['procent_karma_zi']})"
    )
    print()
    print("Karma lunii de nastere:")
    print(
        f"{karma_luna['karma_lunii']} - "
        f"{karma_luna['tema_lunii']}"
    )
    print()
    print("Karma din calea destinului:")
    print(
        f"{karma_cale['calea_destinului']} - "
        f"{karma_cale['categorie_cale']}"
    )
    afiseaza_lista("Datorii karmice din calea destinului:", karma_cale["datorii"])

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

    if args.nume_inainte_casatorie or args.nume_dupa_casatorie:
        print()
        nume_inainte = args.nume_inainte_casatorie or args.nume
        nume_dupa = args.nume_dupa_casatorie or args.nume
        familie_inainte = args.nume_familie_inainte or ultimul_cuvant(nume_inainte)
        familie_dupa = args.nume_familie_dupa or ultimul_cuvant(nume_dupa)

        analiza_inainte = analiza_nume(nume_inainte, args.zi, args.luna, args.an, familie_inainte)
        analiza_dupa = analiza_nume(nume_dupa, args.zi, args.luna, args.an, familie_dupa)

        afiseaza_analiza_nume("Analiza nume inainte de casatorie", analiza_inainte)
        afiseaza_analiza_nume("Analiza nume dupa casatorie", analiza_dupa)
        afiseaza_comparatie_nume(analiza_inainte, analiza_dupa)


if __name__ == "__main__":
    main()
