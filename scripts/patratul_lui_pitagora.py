import argparse
import sys
import unicodedata


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


VECTORI = [
    ("Bunastare materiala", [3, 6, 9]),
    ("Bunastare sociala", [2, 5, 8]),
    ("Bunastare spirituala", [1, 4, 7]),
    ("Vectorul energetic", [1, 2, 3]),
    ("Vectorul vointa", [4, 5, 6]),
    ("Vectorul creativitatii", [7, 8, 9]),
    ("Vectorul scopului", [3, 5, 7]),
    ("Vectorul carierei", [1, 5, 9]),
]

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


def suma_cifrelor(numar):
    numar = abs(numar)
    return sum(int(cifra) for cifra in str(numar))


def reducere(numar):
    curent = abs(numar)
    while curent > 9:
        curent = suma_cifrelor(curent)
    return curent


def prima_cifra_nenula(numar):
    for cifra in f"{numar:02d}":
        if cifra != "0":
            return int(cifra)
    raise ValueError("Ziua trebuie sa contina cel putin o cifra nenula.")


def grupeaza_matrice(cifre):
    return {cifra: str(cifra) * cifre.count(cifra) for cifra in range(1, 10)}


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
        valori = [(litera, ALFABET[litera]) for litera in litere if litera in ALFABET]
        if valori:
            total = sum(valoare for _, valoare in valori)
            componente.append({
                "componenta": parte,
                "normalizat": "".join(litera for litera, _ in valori),
                "valori": valori,
                "total": total,
                "redus": reducere(total),
            })
    return componente


def interpreteaza_vectori(matrice):
    interpretari = []
    for vector in VECTORI:
        nume = vector[0]
        pozitii = vector[1]
        pozitii_prezente = [pozitie for pozitie in pozitii if matrice[pozitie]]
        valoare = sum(
            sum(int(cifra) for cifra in matrice[pozitie])
            for pozitie in pozitii
        )
        analiza = [
            f"{pozitie}:{sum(int(cifra) for cifra in matrice[pozitie]) if matrice[pozitie] else 0}"
            for pozitie in pozitii
        ]

        if len(pozitii_prezente) == 3:
            stare = "activ"
        elif len(pozitii_prezente) == 2:
            stare = "partial activ"
        elif len(pozitii_prezente) == 1:
            stare = "slab"
        else:
            stare = "latent"

        interpretari.append({
            "nume": nume,
            "pozitii": pozitii,
            "prezente": len(pozitii_prezente),
            "valoare": valoare,
            "stare": stare,
            "analiza": analiza,
        })
    return sorted(
        interpretari,
        key=lambda vector: (vector["valoare"], vector["prezente"], vector["nume"]),
        reverse=True,
    )


def calculeaza_patratul_lui_pitagora(zi, luna, an):
    data = f"{zi:02d}{luna:02d}{an:04d}"
    cifre_data = [int(cifra) for cifra in data]

    n1 = sum(cifre_data)
    n2 = suma_cifrelor(n1)
    n3 = abs(n1 - 2 * prima_cifra_nenula(zi))
    n4 = suma_cifrelor(n3)

    sir_complet = f"{data} + {n1} + {n2} + {n3} + {n4}"
    cifre_matrice = [
        int(cifra)
        for cifra in f"{data}{n1}{n2}{n3}{n4}"
        if cifra != "0"
    ]

    matrice = grupeaza_matrice(cifre_matrice)

    return {
        "data": data,
        "cifre_data": cifre_data,
        "cifre_data_fara_zero": [cifra for cifra in cifre_data if cifra != 0],
        "n1": n1,
        "n2": n2,
        "n3": n3,
        "n4": n4,
        "sir_complet": sir_complet,
        "cifre_matrice": cifre_matrice,
        "matrice": matrice,
        "vectori": interpreteaza_vectori(matrice),
    }


def calculeaza_matrice_nume(nume):
    componente = componente_nume(nume)
    valori = [valoare for componenta in componente for valoare in componenta["valori"]]
    cifre_litere = [valoare for _, valoare in valori]
    cifre_componente = [componenta["redus"] for componenta in componente]
    numar_exprimare = reducere(sum(cifre_componente))
    cifre_matrice = cifre_litere + [numar_exprimare]
    matrice = grupeaza_matrice(cifre_matrice)

    return {
        "nume": nume,
        "nume_normalizat": "".join(litera for litera, _ in valori),
        "valori": valori,
        "componente": componente,
        "total_litere": sum(cifre_litere),
        "total_componente": sum(cifre_componente),
        "numar_exprimare": numar_exprimare,
        "cifre_litere": cifre_litere,
        "cifre_componente": cifre_componente,
        "cifre_matrice": cifre_matrice,
        "matrice": matrice,
        "vectori": interpreteaza_vectori(matrice),
    }


def format_suma(cifre):
    return " + ".join(str(cifra) for cifra in cifre)


def afiseaza_rezultat(rezultat):
    matrice = rezultat["matrice"]

    print("Cod extras din data nasterii:")
    print(rezultat["data"])
    print()

    print("Cifre brute, fara zero:")
    print(", ".join(str(cifra) for cifra in rezultat["cifre_data_fara_zero"]))
    print()

    print("Numarul 1 de lucru:")
    print(f"{format_suma(rezultat['cifre_data'])} = {rezultat['n1']}")
    print()

    print("Numarul 2 de lucru:")
    print(f"{format_suma([int(cifra) for cifra in str(rezultat['n1'])])} = {rezultat['n2']}")
    print()

    print("Numarul 3 de lucru:")
    prima_cifra = prima_cifra_nenula(int(rezultat["data"][:2]))
    print(f"{rezultat['n1']} - (2 x {prima_cifra}) = {rezultat['n3']}")
    print()

    print("Numarul 4 de lucru:")
    print(f"{format_suma([int(cifra) for cifra in str(rezultat['n3'])])} = {rezultat['n4']}")
    print()

    print("Cod complet atasat:")
    print(rezultat["sir_complet"])
    print()

    print("Cifre introduse in matrice, fara zero:")
    print(", ".join(str(cifra) for cifra in rezultat["cifre_matrice"]))
    print()

    print("Patratul lui Pitagora:")
    print(f"{matrice[1]:<4} | {matrice[4]:<4} | {matrice[7]:<4}")
    print(f"{matrice[2]:<4} | {matrice[5]:<4} | {matrice[8]:<4}")
    print(f"{matrice[3]:<4} | {matrice[6]:<4} | {matrice[9]:<4}")
    print()

    print("Vectori:")
    for index, vector in enumerate(rezultat["vectori"], start=1):
        pozitii = "-".join(str(pozitie) for pozitie in vector["pozitii"])
        print(
            f"{index}. {vector['nume']} ({pozitii}): "
            f"{vector['stare']}, {vector['prezente']}/3 pozitii, "
            f"valoare {vector['valoare']} ({', '.join(vector['analiza'])})"
        )

    if rezultat["vectori"]:
        vector_dominant = rezultat["vectori"][0]
        vector_slab = rezultat["vectori"][-1]
        print()
        print("Analiza comuna a vectorilor:")
        print(
            f"Vector dominant: {vector_dominant['nume']} "
            f"cu valoarea {vector_dominant['valoare']}."
        )
        print(
            f"Vector cel mai slab: {vector_slab['nume']} "
            f"cu valoarea {vector_slab['valoare']}."
        )


def afiseaza_matrice(titlu, matrice):
    print(titlu)
    print(f"{matrice[1]:<4} | {matrice[4]:<4} | {matrice[7]:<4}")
    print(f"{matrice[2]:<4} | {matrice[5]:<4} | {matrice[8]:<4}")
    print(f"{matrice[3]:<4} | {matrice[6]:<4} | {matrice[9]:<4}")
    print()


def afiseaza_rezultat_nume(rezultat):
    print()
    print("Matricea numelui:")
    print(f"Nume: {rezultat['nume']}")
    print(f"Nume normalizat: {rezultat['nume_normalizat']}")
    print()

    print("Valori litere:")
    print(", ".join(f"{litera}={valoare}" for litera, valoare in rezultat["valori"]))
    print()

    print("Componente reduse:")
    for componenta in rezultat["componente"]:
        print(
            f"{componenta['normalizat']}: "
            f"{format_suma([valoare for _, valoare in componenta['valori']])} "
            f"= {componenta['total']} -> {componenta['redus']}"
        )
    print()

    print("Numar de exprimare:")
    print(
        f"{format_suma(rezultat['cifre_componente'])} = "
        f"{rezultat['total_componente']} -> {rezultat['numar_exprimare']}"
    )
    print()

    print("Cifre introduse in matricea numelui:")
    print(", ".join(str(cifra) for cifra in rezultat["cifre_matrice"]))
    print()

    afiseaza_matrice("Patratul numelui:", rezultat["matrice"])

    print("Vectori nume:")
    for index, vector in enumerate(rezultat["vectori"], start=1):
        pozitii = "-".join(str(pozitie) for pozitie in vector["pozitii"])
        print(
            f"{index}. {vector['nume']} ({pozitii}): "
            f"{vector['stare']}, {vector['prezente']}/3 pozitii, "
            f"valoare {vector['valoare']} ({', '.join(vector['analiza'])})"
        )


def main():
    parser = argparse.ArgumentParser(
        description="Calculeaza codul si patratul lui Pitagora dupa metoda proiectului."
    )
    parser.add_argument("zi", type=int)
    parser.add_argument("luna", type=int)
    parser.add_argument("an", type=int)
    parser.add_argument("--nume")
    args = parser.parse_args()

    rezultat = calculeaza_patratul_lui_pitagora(args.zi, args.luna, args.an)
    afiseaza_rezultat(rezultat)
    if args.nume:
        rezultat_nume = calculeaza_matrice_nume(args.nume)
        afiseaza_rezultat_nume(rezultat_nume)


if __name__ == "__main__":
    main()
