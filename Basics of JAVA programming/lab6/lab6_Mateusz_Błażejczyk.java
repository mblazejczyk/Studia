import java.util.Scanner;

public class lab6 {

    public static class zad1{
        public static void main(String[] args) {
            Scanner inputScanner = new Scanner(System.in);

            System.out.println("Podaj r:");
            double r = inputScanner.nextDouble();

            System.out.println("Podaj h:");
            double h = inputScanner.nextDouble();

            double l = Math.sqrt(Math.pow(r, 2) + Math.pow(h, 2));
            double objetosc = (1.0 / 3) * Math.PI * Math.pow(r, 2) * h;
            System.out.println("Objetosc stozka to: " + objetosc);

            double pole = Math.PI * Math.pow(r, 2) + Math.PI * r * l;
            System.out.println("Pole powierzchni stozka to: " + pole);
        }
    }

    public static class zad2{
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            System.out.println("Podaj liczbe (0-100):");
            int liczba = scanner.nextInt();

            if (liczba < 0 || liczba > 100) {
                System.out.println("Liczba musi być w przedziale od 0 do 100!");
            } else {
                String ocena = okreslOcene(liczba);
                System.out.println("Twoja ocena to: " + ocena);
            }
        }
        public static String okreslOcene(int liczba) {
            if (liczba >= 0 && liczba <= 50) {
                return "2,0";
            } else if (liczba >= 51 && liczba <= 60) {
                return "3,0";
            } else if (liczba >= 61 && liczba <= 70) {
                return "3,5";
            } else if (liczba >= 71 && liczba <= 80) {
                return "4,0";
            } else if (liczba >= 81 && liczba <= 90) {
                return "4,5";
            } else if (liczba >= 91 && liczba <= 100) {
                return "5,0";
            }
            return "Brak oceny";
        }
    }

    public static class zad3 {
        public static void main(String[] args) {
            Scanner inputScanner = new Scanner(System.in);

            System.out.println("Podaj a:");
            int a = inputScanner.nextInt();
            System.out.println("Podaj b:");
            int b = inputScanner.nextInt();
            System.out.println("Podaj c:");
            int c = inputScanner.nextInt();

            if(Math.pow(a, 2) + Math.pow(b, 2) == Math.pow(c, 2)){
                System.out.println("Liczby spelniaja rownanie pitagorejskie:");
            }else{
                System.out.println("Liczby nie spelniaja rownania pitagorejskiego:");
            }
        }
    }

    public static class zad4 {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Podaj wartość dla p (true/false): ");
            boolean p = scanner.nextBoolean();

            System.out.print("Podaj wartość dla q (true/false): ");
            boolean q = scanner.nextBoolean();

            if (!(p && q) == (!p || !q)) {
                System.out.println("Obie strony równania są takie same.");
            } else {
                System.out.println("Obie strony równania są różne.");
            }
        }
    }

    public static class zad5 {
        public static void main(String[] args) {
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź liczbe dni:");
            int c = inputScanner.nextInt();

            if(c > 10){
                System.out.println("Należna opłata: " + 150 * c + "PLN");
            } else if (c < 5) {
                System.out.println("Należna opłata: " + 250 * c + "PLN");
            }else{
                System.out.println("Należna opłata: " + 200 * c + "PLN");
            }
        }
    }

    public static class zad6 {
        public static void main(String[] args) {
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź wielkosc:");
            int c = inputScanner.nextInt();

            for (int i = 1; i <= c; i++) {
                for (int j = 1; j <= i; j++) {
                    System.out.print("* ");
                }
                System.out.print("\n");
            }

            for (int i = c - 1; i >= 1; i--) {
                for (int j = 1; j <= i; j++) {
                    System.out.print("* ");
                }
                System.out.print("\n");
            }
        }
    }

    public static class zad7 {
        public static void main(String[] args) {
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź wiek psa w ludzkich latach:");
            int wiekLudzki = inputScanner.nextInt();
            int wiekPsa;

            if (wiekLudzki <= 2) {
                wiekPsa = wiekLudzki * 10;
            } else {
                wiekPsa = 20 + (wiekLudzki - 2) * 4;
            }

            System.out.println("Wiek psa w psich latach to: " + wiekPsa);
        }
    }

    public static class zad8 {
        public static void main(String[] args) {
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź haslo:");
            String haslo = inputScanner.next();

            char[] male = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
            char[] duze = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
            char[] cyfry = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'};
            char[] specjalne = {'!', '@', '#', '$'};

            if(zawieraZnaki(haslo, male) && zawieraZnaki(haslo, duze) && zawieraZnaki(haslo, cyfry) && zawieraZnaki(haslo, specjalne)
                && haslo.length() >= 6 && haslo.length() <= 16){
                System.out.println("Haslo jest bezpieczne");
            }else{
                System.out.println("Haslo nie jest bezpieczne");
            }
        }

        public static boolean zawieraZnaki(String tekst, char[] tablica) {
            for (int i = 0; i < tekst.length(); i++) {
                char znak = tekst.charAt(i);
                for (char znakZTablicy : tablica) {
                    if (znak == znakZTablicy) {
                        return true;
                    }
                }
            }
            return false;
        }
    }
}
