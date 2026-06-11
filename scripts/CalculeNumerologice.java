import java.text.Normalizer;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CalculeNumerologice {
    private static final Map<Character, Integer> ALFABET = new HashMap<>();
    private static final int[] DATORII_KARMICE = {13, 14, 16, 19};

    static {
        adauga("AJS", 1);
        adauga("BKT", 2);
        adauga("CLU", 3);
        adauga("DMV", 4);
        adauga("ENW", 5);
        adauga("FOX", 6);
        adauga("GPY", 7);
        adauga("HQZ", 8);
        adauga("IR", 9);
    }

    public static void main(String[] args) {
        Map<String, String> optiuni = parseazaArgs(args);
        int zi = Integer.parseInt(optiuni.getOrDefault("zi", "24"));
        int luna = Integer.parseInt(optiuni.getOrDefault("luna", "4"));
        int an = Integer.parseInt(optiuni.getOrDefault("an", "1982"));
        int anAnalizat = Integer.parseInt(optiuni.getOrDefault("an-analizat", "2026"));
        int start = Integer.parseInt(optiuni.getOrDefault("start", String.valueOf(anAnalizat)));
        int stop = Integer.parseInt(optiuni.getOrDefault("stop", String.valueOf(anAnalizat + 9)));
        int varsta = Integer.parseInt(optiuni.getOrDefault("varsta", "0"));
        String nume = optiuni.getOrDefault("nume", "Ana Popescu");
        String numeFamilie = optiuni.getOrDefault("nume-familie", ultimulCuvant(nume));

        CalculNume calculNume = vibratiaNumelui(nume);
        CalculNume numarActiv = vibratiaNumelui(primulCuvant(nume));
        CalculNume numarEreditar = vibratiaNumelui(numeFamilie);
        CalculNume numarEreditarKarmic = numarEreditarKarmic(numeFamilie);
        int destin = calculNume.rezultat;
        CalculNumeric calculSoarta = soarta(zi, luna, an);
        int temaVietii = reducere(calculSoarta.rezultat + destin);
        CalculNumeric anPersonal = vibratiaAnului(zi, luna, anAnalizat);
        AniImportanti ani = aniImportanti(zi, luna, an, start, stop);
        CalculNume karmaNeam = vibratiaNumelui(numeFamilie);

        System.out.println("Calcule numerologice");
        System.out.println("====================");
        System.out.printf("Data: %02d.%02d.%04d%n", zi, luna, an);
        System.out.println("Nume: " + nume);
        System.out.println();

        System.out.println("Vibratia interioara: " + reducere(zi));
        System.out.println("Vibratia exterioara: " + reducere(luna));
        System.out.println("Numar de exprimare / destin: " + destin + " (total " + calculNume.total + ")");
        System.out.println("Numar activ: " + numarActiv.rezultat + " (total " + numarActiv.total + ")");
        System.out.println("Numar ereditar: " + numarEreditar.rezultat + " (total " + numarEreditar.total + ")");
        System.out.println("Numar ereditar karmic: " + numarEreditarKarmic.rezultat + " (total " + numarEreditarKarmic.total + ")");
        System.out.println("Soarta: " + calculSoarta.rezultat + " (total " + calculSoarta.total + ")");
        System.out.println("Tema vietii: " + temaVietii);
        System.out.println("Vibratia anului personal " + anAnalizat + ": " + anPersonal.rezultat + " (total " + anPersonal.total + ")");
        System.out.println();

        afiseazaLista("Lectii karmice personale:", lectiiKarmice(nume));
        afiseazaLista("Datorii karmice personale:", datoriiKarmice(nume, zi, luna, an));
        afiseazaLista("Lectii karmice de neam:", lectiiKarmice(numeFamilie));
        System.out.println("Karma neamului: " + karmaNeam.rezultat + " (total " + karmaNeam.total + ")");
        System.out.println();

        afiseazaLista("Ani importanti interiori " + start + "-" + stop + ":", ani.interiori);
        afiseazaLista("Ani importanti exteriori " + start + "-" + stop + ":", ani.exteriori);

        System.out.println("Pinacluri si provocari:");
        for (Etapa etapa : pinacluri(zi, luna, an)) {
            System.out.println(
                etapa.nr + ". varsta " + etapa.varsta + ": pinaclu "
                    + etapa.pinaclu + ", provocare " + etapa.provocare
            );
        }
        System.out.println();

        System.out.println("Cicluri pentru varsta " + varsta + ":");
        int[] durate = {7, 9, 12};
        for (int durata : durate) {
            int ciclu = varsta / durata + 1;
            int pozitie = varsta % durata + 1;
            System.out.println(durata + " ani: ciclul " + ciclu + ", pozitia " + pozitie);
        }
    }

    private static void adauga(String litere, int valoare) {
        for (char litera : litere.toCharArray()) {
            ALFABET.put(litera, valoare);
        }
    }

    private static Map<String, String> parseazaArgs(String[] args) {
        Map<String, String> optiuni = new HashMap<>();
        for (int i = 0; i < args.length - 1; i += 2) {
            if (args[i].startsWith("--")) {
                optiuni.put(args[i].substring(2), args[i + 1]);
            }
        }
        return optiuni;
    }

    private static String normalizeaza(String text) {
        String normalizat = Normalizer.normalize(text, Normalizer.Form.NFD)
            .replaceAll("\\p{M}", "")
            .toUpperCase();
        return normalizat.replaceAll("[^A-Z]", "");
    }

    private static int reducere(int numar) {
        int curent = numar;
        while (curent > 9) {
            int suma = 0;
            for (char cifra : String.valueOf(curent).toCharArray()) {
                suma += Character.getNumericValue(cifra);
            }
            curent = suma;
        }
        return curent;
    }

    private static int reducere22(int numar) {
        int curent = numar;
        while (curent > 22) {
            curent -= 22;
        }
        return curent;
    }

    private static CalculNume vibratiaNumelui(String nume) {
        int total = 0;
        for (String parte : nume.replace("-", " ").split("\\s+")) {
            int totalComponenta = 0;
            for (char litera : normalizeaza(parte).toCharArray()) {
                if (ALFABET.containsKey(litera)) {
                    totalComponenta += ALFABET.get(litera);
                }
            }
            if (totalComponenta > 0) {
                total += reducere(totalComponenta);
            }
        }
        return new CalculNume(total, reducere(total));
    }

    private static CalculNume numarEreditarKarmic(String numeFamilie) {
        int total = 0;
        for (char litera : normalizeaza(numeFamilie).toCharArray()) {
            if (ALFABET.containsKey(litera)) {
                total += ALFABET.get(litera);
            }
        }
        return new CalculNume(total, reducere22(total));
    }

    private static int[] frecventeNume(String nume) {
        int[] frecvente = new int[10];
        for (char litera : normalizeaza(nume).toCharArray()) {
            if (ALFABET.containsKey(litera)) {
                frecvente[ALFABET.get(litera)]++;
            }
        }
        return frecvente;
    }

    private static List<Integer> lectiiKarmice(String nume) {
        int[] frecvente = frecventeNume(nume);
        List<Integer> lectii = new ArrayList<>();
        for (int numar = 1; numar <= 9; numar++) {
            if (frecvente[numar] == 0) {
                lectii.add(numar);
            }
        }
        return lectii;
    }

    private static CalculNumeric soarta(int zi, int luna, int an) {
        String data = String.format("%02d%02d%04d", zi, luna, an);
        int total = sumaCifre(data);
        return new CalculNumeric(total, reducere(total));
    }

    private static CalculNumeric vibratiaAnului(int zi, int luna, int anAnalizat) {
        String cod = String.format("%02d%02d%04d", zi, luna, anAnalizat);
        int total = sumaCifre(cod);
        return new CalculNumeric(total, reducere(total));
    }

    private static int sumaCifre(String text) {
        int total = 0;
        for (char cifra : text.toCharArray()) {
            total += Character.getNumericValue(cifra);
        }
        return total;
    }

    private static AniImportanti aniImportanti(int zi, int luna, int anNastere, int start, int stop) {
        int interior = reducere(zi);
        int exterior = reducere(luna);
        AniImportanti ani = new AniImportanti();
        ani.interiori.addAll(aniImportantiInteriori(anNastere, start, stop));
        ani.exteriori.addAll(aniImportantiExteriori(anNastere, start, stop));
        return ani;
    }

    private static List<Integer> aniImportantiInteriori(int anNastere, int start, int stop) {
        List<Integer> ani = new ArrayList<>();
        int anCurent = anNastere;
        while (true) {
            anCurent += reducere(anCurent);
            if (anCurent > stop) {
                break;
            }
            if (anCurent >= start) {
                ani.add(anCurent);
            }
        }
        return ani;
    }

    private static List<Integer> aniImportantiExteriori(int anNastere, int start, int stop) {
        List<Integer> ani = new ArrayList<>();
        int anCurent = anNastere;
        while (true) {
            anCurent += sumaCifre(Integer.toString(Math.abs(anCurent)));
            if (anCurent > stop) {
                break;
            }
            if (anCurent >= start) {
                ani.add(anCurent);
            }
        }
        return ani;
    }

    private static List<Etapa> pinacluri(int zi, int luna, int an) {
        int ziRedusa = reducere(zi);
        int lunaRedusa = reducere(luna);
        int anRedus = reducere(sumaCifre(String.format("%04d", an)));
        int soarta = soarta(zi, luna, an).rezultat;

        int p1 = reducere(lunaRedusa + ziRedusa);
        int p2 = reducere(ziRedusa + anRedus);
        int p3 = reducere(p1 + p2);
        int p4 = reducere(lunaRedusa + anRedus);

        int c1 = Math.abs(ziRedusa - lunaRedusa);
        int c2 = Math.abs(ziRedusa - anRedus);
        int c3 = Math.abs(c1 - c2);
        int c4 = Math.abs(lunaRedusa - anRedus);

        int sfarsit1 = 36 - soarta;
        int sfarsit2 = sfarsit1 + 9;
        int sfarsit3 = sfarsit2 + 9;

        List<Etapa> etape = new ArrayList<>();
        etape.add(new Etapa(1, "0-" + sfarsit1, p1, c1));
        etape.add(new Etapa(2, (sfarsit1 + 1) + "-" + sfarsit2, p2, c2));
        etape.add(new Etapa(3, (sfarsit2 + 1) + "-" + sfarsit3, p3, c3));
        etape.add(new Etapa(4, (sfarsit3 + 1) + "+", p4, c4));
        return etape;
    }

    private static List<Integer> datoriiKarmice(String nume, int zi, int luna, int an) {
        int totalNume = vibratiaNumelui(nume).total;
        int totalData = soarta(zi, luna, an).total;
        List<Integer> datorii = new ArrayList<>();
        for (int datorie : DATORII_KARMICE) {
            if (totalNume == datorie || totalData == datorie) {
                datorii.add(datorie);
            }
        }
        return datorii;
    }

    private static void afiseazaLista(String titlu, List<Integer> valori) {
        System.out.println(titlu);
        if (valori.isEmpty()) {
            System.out.println("-");
        } else {
            List<String> text = new ArrayList<>();
            for (int valoare : valori) {
                text.add(String.valueOf(valoare));
            }
            System.out.println(String.join(", ", text));
        }
        System.out.println();
    }

    private static String ultimulCuvant(String text) {
        String[] parti = text.trim().split("\\s+");
        return parti[parti.length - 1];
    }

    private static String primulCuvant(String text) {
        String[] parti = text.trim().split("\\s+");
        return parti[0];
    }

    private static class CalculNume {
        int total;
        int rezultat;

        CalculNume(int total, int rezultat) {
            this.total = total;
            this.rezultat = rezultat;
        }
    }

    private static class CalculNumeric {
        int total;
        int rezultat;

        CalculNumeric(int total, int rezultat) {
            this.total = total;
            this.rezultat = rezultat;
        }
    }

    private static class AniImportanti {
        List<Integer> interiori = new ArrayList<>();
        List<Integer> exteriori = new ArrayList<>();
    }

    private static class Etapa {
        int nr;
        String varsta;
        int pinaclu;
        int provocare;

        Etapa(int nr, String varsta, int pinaclu, int provocare) {
            this.nr = nr;
            this.varsta = varsta;
            this.pinaclu = pinaclu;
            this.provocare = provocare;
        }
    }
}
