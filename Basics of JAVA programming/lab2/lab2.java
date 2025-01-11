import java.util.Objects;
import java.util.Scanner;

public class lab2 {
    public static class zad2 {
        public static void main(String[] args) {
            //zad 2
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź liczbe:");
            int a = inputScanner.nextInt();
            if (a < 0){
                System.out.print(a * -1);
            }else{
                System.out.print(a);
            }
        }
    }
    public static class zad3 {
        public static void main(String[] args) {
            //zad 3
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź liczbe:");
            int c = inputScanner.nextInt();
            if (c <= 0) {
                System.out.print("Liczba jest mniejsza od 0");
            } else if (c >= 100) {
                System.out.print("Liczba jest większa od 100");
            } else {
                System.out.print("Liczba jest w przedziale od 0 do 100");
            }
        }
    }

    public static class zad4 {
        public static void main(String[] args) {
            //zad 4
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź cyfre:");
            int c = inputScanner.nextInt();
            switch (c){
                case 1:
                    System.out.println("wprowadzono: 1");
                    break;
                case 2:
                    System.out.println("wprowadzono: 2");
                    break;
                case 3:
                    System.out.println("wprowadzono: 3");
                    break;
                case 4:
                    System.out.println("wprowadzono: 4");
                    break;
                case 5:
                    System.out.println("wprowadzono: 5");
                    break;
                case 6:
                    System.out.println("wprowadzono: 6");
                    break;
                case 7:
                    System.out.println("wprowadzono: 7");
                    break;
                case 8:
                    System.out.println("wprowadzono: 8");
                    break;
                case 9:
                    System.out.println("wprowadzono: 9");
                    break;
                case 0:
                    System.out.println("wprowadzono: 0");
                    break;
                default:
                    System.out.println("Nieprawidłowa wartość");
                    break;
            }
        }
    }

    public static class zad5 {
        public static void main(String[] args) {
            //zad 5
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Czy jest dziś słońce? (t/n)");
            String c = inputScanner.nextLine();
            switch (c.toUpperCase()){
                case "T":
                    System.out.println("Piękny dzień");
                    break;
                case "N":
                    System.out.println("Brak słońca");
                    break;
                default:
                    System.out.println("Nieprawidłowa wartość");
                    break;
            }
        }
    }

    public static class zad6 {
        public static void main(String[] args) {
            //zad 6
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Podaj litere");
            String c = inputScanner.nextLine();
            switch (c.toLowerCase()) {
                case "a":
                case "b":
                case "c":
                case "d":
                case "e":
                case "f":
                case "g":
                case "h":
                case "i":
                case "j":
                case "k":
                case "l":
                case "m":
                case "n":
                case "o":
                case "p":
                case "q":
                case "r":
                case "s":
                case "t":
                case "u":
                case "v":
                case "w":
                case "x":
                case "y":
                case "z":
                    System.out.print("Podano litere " + c);
                    break;
                default:
                    System.out.println("Nieprawidłowa wartość");
                    break;
            }
        }
    }

    public static class zad7 {
        public static void main(String[] args) {
            //zad 7
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Podaj nr albumu");
            int c = inputScanner.nextInt();
            String p = "";
            if (c % 2 == 0){
                p = "m";
            }else{
                p = "k";
            }

            String rok = "";
            if (c > 10000){
                rok = "2020 lub później";
            }else{
                char pierwszaCyfraChar = Integer.toString(c).charAt(0); // Pobieramy pierwszą cyfrę jako znak
                int pierwszaCyfra = Character.getNumericValue(pierwszaCyfraChar); // Zamieniamy znak na liczbę
                int rok1 = 2018 - (9 - pierwszaCyfra);
                rok = Integer.toString(rok1);
            }
            System.out.print("Student jest płci: " + p + " oraz rozpoczął studia w roku: " + rok);
        }
    }

    public static class zad8 {
        public static void main(String[] args) {
            //zad 8
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Podaj a");
            int a = inputScanner.nextInt();
            System.out.println("Podaj b");
            int b = inputScanner.nextInt();
            System.out.println("Podaj c");
            int c = inputScanner.nextInt();
            int delta = b*b-(4*a*c);
            if (delta < 0){
                System.out.print("Brak x1 i x2");
            } else if (delta == 0) {
                int x1 = (-b-delta)/(2*a);
                System.out.print("Delta wynosi 0 a x1 i x2 " + x1);
            }else{
                int x1 = (-b-delta)/(2*a);
                int x2 = (-b+delta)/(2*a);
                System.out.print("Delta wynosi " + delta + ", x1=" + x1 + "; x2=" + x2);
            }
        }
    }
}
