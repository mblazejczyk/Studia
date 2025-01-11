import java.util.Objects;
import java.util.Scanner;

public class lab3 {
    public static class zad1 {
        public static void main(String[] args) {
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź liczbe:");
            int c = inputScanner.nextInt();
            if (c == 0) {
                System.out.print("Liczba to 0");
            } else if (c > 0) {
                System.out.print("Liczba jest większa od 0");
            } else {
                System.out.print("Liczba jest mniejsza od 0");
            }
        }
    }

    public static class zad2 {
        public static void main(String[] args) {
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź ilosc punktow:");
            int c = inputScanner.nextInt();
            if (c <= 50) {
                System.out.print("Liczba to 0");
            } else if (c > 50 && c <= 60) {
                System.out.print("Ocena: 3");
            }else if (c > 60 && c <= 70) {
                System.out.print("Ocena: 3.5");
            }else if (c > 70 && c <= 80) {
                System.out.print("Ocena: 4");
            }else if (c > 80 && c <= 90) {
                System.out.print("Ocena: 4.5");
            }else{
                System.out.print("Ocena: 5");
            }
        }
    }

    public static class zad3 {
        public static void main(String[] args) {
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź hasło:");
            String c = inputScanner.nextLine();
            if (Objects.equals(c, "password")) {
                System.out.print("Hasło poprawna. Nastąpiło logowanie");
            } else {
                System.out.print("Hasło niepoprawne.");
            }
        }
    }

    public static class zad4 {
        public static void main(String[] args) {
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź długość tekstu:");
            int c = inputScanner.nextInt();

            Scanner inputScanner1 = new Scanner(System.in);
            System.out.println("Wprować ciąg znaków:");
            String p = inputScanner1.nextLine();

            if (p.length() == c) {
                System.out.print("Ciąg znaków wynosi " + p.length());
            } else {
                System.out.print("Ciąg znaków wynoci " + p.length() + " przekroczono o " + (p.length() - c));
            }
        }
    }

    public static class zad5 {
        public static void main(String[] args) {
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź a:");
            int a = inputScanner.nextInt();
            System.out.println("Wprowadź b:");
            int b = inputScanner.nextInt();
            System.out.println("Wprowadź c:");
            int c = inputScanner.nextInt();

            if(a < 0 || b < 0 || c < 0){
                System.out.println("Jedna z liczb jest mniejsza od 0");
                return;
            }

            if(Math.pow(a, 2) + Math.pow(b, 2) == Math.pow(c, 2)){
                System.out.println("Te długości tworzą trójkę pitagorejską");
            }else{
                System.out.println("Te długości nie tworzą trójki pitagorejskiej");
            }

        }

        public static class zad6 {
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

        public static class zad7 {
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
    }
}
