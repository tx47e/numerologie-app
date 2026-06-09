import argparse
import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


VECTORI = [
    ("Scara bunastarii materiale", [3, 6, 9]),
    ("Vectorul relational si social", [2, 5, 8]),
    ("Scara bunastarii spirituale", [1, 4, 7]),
    ("Axa personala", [3, 2, 1]),
    ("Axa de constructie", [6, 5, 4]),
    ("Axa superioara si sociala", [9, 8, 7]),
    ("Vectorul scopului", [3, 5, 7]),
    ("Vectorul carierei", [1, 5, 9]),
]


def suma_cifrelor(numar):
    return sum(int(cifra) for cifra in str(numar))


def prima_cifra_nenula(numar):
    for cifra in f"{numar:02d}":
        if cifra != "0":
            return int(cifra)
    raise ValueError("Ziua trebuie sa contina cel putin o cifra nenula.")


def grupeaza_matrice(cifre):
    return {cifra: str(cifra) * cifre.count(cifra) for cifra in range(1, 10)}


def interpreteaza_vectori(matrice):
    interpretari = []
    for vector in VECTORI:
        nume = vector[0]
        pozitii = vector[1]
        pozitii_prezente = [pozitie for pozitie in pozitii if matrice[pozitie]]
        aparitii = sum(len(matrice[pozitie]) for pozitie in pozitii)
        analiza = [
            f"{pozitie}:{len(matrice[pozitie])}"
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
            "valoare": aparitii,
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
    n3 = n1 - 2 * prima_cifra_nenula(zi)
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
    print(f"{matrice[3]:<4} | {matrice[6]:<4} | {matrice[9]:<4}")
    print(f"{matrice[2]:<4} | {matrice[5]:<4} | {matrice[8]:<4}")
    print(f"{matrice[1]:<4} | {matrice[4]:<4} | {matrice[7]:<4}")
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


def main():
    parser = argparse.ArgumentParser(
        description="Calculeaza codul si patratul lui Pitagora dupa metoda proiectului."
    )
    parser.add_argument("zi", type=int)
    parser.add_argument("luna", type=int)
    parser.add_argument("an", type=int)
    args = parser.parse_args()

    rezultat = calculeaza_patratul_lui_pitagora(args.zi, args.luna, args.an)
    afiseaza_rezultat(rezultat)


if __name__ == "__main__":
    main()
