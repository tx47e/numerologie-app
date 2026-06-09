import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PatratulLuiPitagora {
    private static final VectorDefinitie[] VECTORI = {
        new VectorDefinitie("Scara bunastarii materiale", new int[] {3, 6, 9}),
        new VectorDefinitie("Vectorul relational si social", new int[] {2, 5, 8}),
        new VectorDefinitie("Scara bunastarii spirituale", new int[] {1, 4, 7}),
        new VectorDefinitie("Axa personala", new int[] {3, 2, 1}),
        new VectorDefinitie("Axa de constructie", new int[] {6, 5, 4}),
        new VectorDefinitie("Axa superioara si sociala", new int[] {9, 8, 7}),
        new VectorDefinitie("Vectorul scopului", new int[] {3, 5, 7}),
        new VectorDefinitie("Vectorul carierei", new int[] {1, 5, 9})
    };

    public static void main(String[] args) {
        if (args.length != 3) {
            System.err.println("Utilizare: java PatratulLuiPitagora <zi> <luna> <an>");
            System.exit(1);
        }

        int zi = Integer.parseInt(args[0]);
        int luna = Integer.parseInt(args[1]);
        int an = Integer.parseInt(args[2]);

        Rezultat rezultat = calculeaza(zi, luna, an);
        afiseaza(rezultat);
    }

    private static Rezultat calculeaza(int zi, int luna, int an) {
        String data = String.format("%02d%02d%04d", zi, luna, an);
        List<Integer> cifreData = cifreDinText(data, true);

        int n1 = cifreData.stream().mapToInt(Integer::intValue).sum();
        int n2 = sumaCifrelor(n1);
        int n3 = n1 - 2 * primaCifraNenula(zi);
        int n4 = sumaCifrelor(n3);

        String sirComplet = data + " + " + n1 + " + " + n2 + " + " + n3 + " + " + n4;
        List<Integer> cifreMatrice = cifreDinText(data + n1 + n2 + n3 + n4, false);
        Map<Integer, String> matrice = grupeazaMatrice(cifreMatrice);
        List<VectorInterpretare> vectori = interpreteazaVectori(matrice);

        return new Rezultat(data, cifreData, n1, n2, n3, n4, sirComplet, cifreMatrice, matrice, vectori);
    }

    private static int sumaCifrelor(int numar) {
        return cifreDinText(String.valueOf(numar), true)
            .stream()
            .mapToInt(Integer::intValue)
            .sum();
    }

    private static int primaCifraNenula(int numar) {
        for (char cifra : String.format("%02d", numar).toCharArray()) {
            if (cifra != '0') {
                return Character.getNumericValue(cifra);
            }
        }
        throw new IllegalArgumentException("Ziua trebuie sa contina cel putin o cifra nenula.");
    }

    private static List<Integer> cifreDinText(String text, boolean includeZero) {
        List<Integer> cifre = new ArrayList<>();
        for (char caracter : text.toCharArray()) {
            if (Character.isDigit(caracter) && (includeZero || caracter != '0')) {
                cifre.add(Character.getNumericValue(caracter));
            }
        }
        return cifre;
    }

    private static Map<Integer, String> grupeazaMatrice(List<Integer> cifre) {
        Map<Integer, String> matrice = new HashMap<>();
        for (int cifra = 1; cifra <= 9; cifra++) {
            StringBuilder valoare = new StringBuilder();
            for (int cifraCurenta : cifre) {
                if (cifraCurenta == cifra) {
                    valoare.append(cifra);
                }
            }
            matrice.put(cifra, valoare.toString());
        }
        return matrice;
    }

    private static List<VectorInterpretare> interpreteazaVectori(Map<Integer, String> matrice) {
        List<VectorInterpretare> interpretari = new ArrayList<>();
        for (VectorDefinitie vector : VECTORI) {
            int pozitiiPrezente = 0;
            int aparitii = 0;

            for (int pozitie : vector.pozitii) {
                String valoare = matrice.get(pozitie);
                if (!valoare.isEmpty()) {
                    pozitiiPrezente++;
                    aparitii += valoare.length();
                }
            }

            String stare;
            if (pozitiiPrezente == 3) {
                stare = "activ";
            } else if (pozitiiPrezente == 2) {
                stare = "partial activ";
            } else if (pozitiiPrezente == 1) {
                stare = "slab";
            } else {
                stare = "latent";
            }

            List<String> analiza = new ArrayList<>();
            for (int pozitie : vector.pozitii) {
                analiza.add(pozitie + ":" + matrice.get(pozitie).length());
            }

            interpretari.add(new VectorInterpretare(
                vector.nume,
                vector.pozitii,
                pozitiiPrezente,
                aparitii,
                stare,
                analiza
            ));
        }
        interpretari.sort(
            Comparator.comparingInt((VectorInterpretare vector) -> vector.valoare)
                .thenComparingInt(vector -> vector.pozitiiPrezente)
                .thenComparing(vector -> vector.nume)
                .reversed()
        );
        return interpretari;
    }

    private static void afiseaza(Rezultat rezultat) {
        System.out.println("Cod extras din data nasterii:");
        System.out.println(rezultat.data);
        System.out.println();

        System.out.println("Cifre brute, fara zero:");
        System.out.println(join(faraZero(rezultat.cifreData)));
        System.out.println();

        System.out.println("Numarul 1 de lucru:");
        System.out.println(joinCuPlus(rezultat.cifreData) + " = " + rezultat.n1);
        System.out.println();

        System.out.println("Numarul 2 de lucru:");
        System.out.println(joinCuPlus(cifreDinText(String.valueOf(rezultat.n1), true)) + " = " + rezultat.n2);
        System.out.println();

        System.out.println("Numarul 3 de lucru:");
        int primaCifra = primaCifraNenula(Integer.parseInt(rezultat.data.substring(0, 2)));
        System.out.println(rezultat.n1 + " - (2 x " + primaCifra + ") = " + rezultat.n3);
        System.out.println();

        System.out.println("Numarul 4 de lucru:");
        System.out.println(joinCuPlus(cifreDinText(String.valueOf(rezultat.n3), true)) + " = " + rezultat.n4);
        System.out.println();

        System.out.println("Cod complet atasat:");
        System.out.println(rezultat.sirComplet);
        System.out.println();

        System.out.println("Cifre introduse in matrice, fara zero:");
        System.out.println(join(rezultat.cifreMatrice));
        System.out.println();

        System.out.println("Patratul lui Pitagora:");
        System.out.printf("%-4s | %-4s | %-4s%n", rezultat.matrice.get(3), rezultat.matrice.get(6), rezultat.matrice.get(9));
        System.out.printf("%-4s | %-4s | %-4s%n", rezultat.matrice.get(2), rezultat.matrice.get(5), rezultat.matrice.get(8));
        System.out.printf("%-4s | %-4s | %-4s%n", rezultat.matrice.get(1), rezultat.matrice.get(4), rezultat.matrice.get(7));
        System.out.println();

        System.out.println("Vectori:");
        for (int index = 0; index < rezultat.vectori.size(); index++) {
            VectorInterpretare vector = rezultat.vectori.get(index);
            System.out.println(
                (index + 1) + ". " + vector.nume + " (" + joinPozitii(vector.pozitii) + "): "
                    + vector.stare + ", " + vector.pozitiiPrezente + "/3 pozitii, "
                    + "valoare " + vector.valoare + " (" + String.join(", ", vector.analiza) + ")"
            );
        }

        if (!rezultat.vectori.isEmpty()) {
            VectorInterpretare vectorDominant = rezultat.vectori.get(0);
            VectorInterpretare vectorSlab = rezultat.vectori.get(rezultat.vectori.size() - 1);
            System.out.println();
            System.out.println("Analiza comuna a vectorilor:");
            System.out.println("Vector dominant: " + vectorDominant.nume + " cu valoarea " + vectorDominant.valoare + ".");
            System.out.println("Vector cel mai slab: " + vectorSlab.nume + " cu valoarea " + vectorSlab.valoare + ".");
        }
    }

    private static List<Integer> faraZero(List<Integer> cifre) {
        List<Integer> rezultat = new ArrayList<>();
        for (int cifra : cifre) {
            if (cifra != 0) {
                rezultat.add(cifra);
            }
        }
        return rezultat;
    }

    private static String join(List<Integer> cifre) {
        List<String> valori = new ArrayList<>();
        for (int cifra : cifre) {
            valori.add(String.valueOf(cifra));
        }
        return String.join(", ", valori);
    }

    private static String joinCuPlus(List<Integer> cifre) {
        List<String> valori = new ArrayList<>();
        for (int cifra : cifre) {
            valori.add(String.valueOf(cifra));
        }
        return String.join(" + ", valori);
    }

    private static String joinPozitii(int[] pozitii) {
        List<String> valori = new ArrayList<>();
        for (int pozitie : pozitii) {
            valori.add(String.valueOf(pozitie));
        }
        return String.join("-", valori);
    }

    private static class VectorDefinitie {
        String nume;
        int[] pozitii;

        VectorDefinitie(String nume, int[] pozitii) {
            this.nume = nume;
            this.pozitii = pozitii;
        }
    }

    private static class VectorInterpretare {
        String nume;
        int[] pozitii;
        int pozitiiPrezente;
        int valoare;
        String stare;
        List<String> analiza;

        VectorInterpretare(
            String nume,
            int[] pozitii,
            int pozitiiPrezente,
            int valoare,
            String stare,
            List<String> analiza
        ) {
            this.nume = nume;
            this.pozitii = pozitii;
            this.pozitiiPrezente = pozitiiPrezente;
            this.valoare = valoare;
            this.stare = stare;
            this.analiza = analiza;
        }
    }

    private static class Rezultat {
        String data;
        List<Integer> cifreData;
        int n1;
        int n2;
        int n3;
        int n4;
        String sirComplet;
        List<Integer> cifreMatrice;
        Map<Integer, String> matrice;
        List<VectorInterpretare> vectori;

        Rezultat(
            String data,
            List<Integer> cifreData,
            int n1,
            int n2,
            int n3,
            int n4,
            String sirComplet,
            List<Integer> cifreMatrice,
            Map<Integer, String> matrice,
            List<VectorInterpretare> vectori
        ) {
            this.data = data;
            this.cifreData = cifreData;
            this.n1 = n1;
            this.n2 = n2;
            this.n3 = n3;
            this.n4 = n4;
            this.sirComplet = sirComplet;
            this.cifreMatrice = cifreMatrice;
            this.matrice = matrice;
            this.vectori = vectori;
        }
    }
}
