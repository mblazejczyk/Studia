import java.util.Scanner;

public class lab3
{
    public static class zad1 {
        public static void main(String[] args) {
            for (int i = 0; i <= 10; i++){
                System.out.println(i);
            }

            int i = 0;
            while (i < 10){
                i++;
                System.out.println(i);
            }
            i = 0;
            do {
                i++;
                System.out.println(i);
            }while (i < 10);
        }

        public static class zad2 {
            public static void main(String[] args) {
                Scanner inputScanner = new Scanner(System.in);
                System.out.println("Wprowadź liczbe:");
                int a = inputScanner.nextInt();
                int c = 1;
                for (int i = a; i > 0; i--){
                    c *= i;
                }
                System.out.println("Silnia to: " + c);
            }
        }

        public static class zad3 {
            public static void main(String[] args) {
                for (int i = 0; i <= 20; i++){
                    if (i % 2 == 0){
                        System.out.println(i);
                    }
                }
            }
        }

        public static class zad4 {
            public static void main(String[] args) {
                int i = 0;
                while (i <= 30){
                    if (i % 3 == 0){
                        System.out.println(i);
                    }
                    i++;
                }
            }
        }

        public static class zad5 {
            public static void main(String[] args) {
                for (int i = 0; i <= 30; i++){
                    if (i % 2 != 0){ continue;}
                    System.out.println(i);

                }
            }
        }

        public static class zad6 {
            public static void main(String[] args) {
                Scanner inputScanner = new Scanner(System.in);
                System.out.println("Wprowadź litere:");
                String x = inputScanner.nextLine();
                String alf = "abcdefghijklmnopqrstuvwxyz";
                int i = 0;
                while(alf.charAt(i) != x.charAt(0)){
                    System.out.println(alf.charAt(i));
                    i++;
                }
                System.out.println(x);
            }
        }
        public static class zad7 {
            public static void main(String[] args) {
                Scanner inputScanner = new Scanner(System.in);
                System.out.println("Wprowadź liczbe:");
                int x = inputScanner.nextInt();
                int i = 1;
                int otp = 0;
                do {
                    otp += i;
                    i++;
                }while (i != x);
                System.out.println(otp + x);
            }
        }

        public static class zad8 {
            public static void main(String[] args) {
                Scanner inputScanner = new Scanner(System.in);
                System.out.println("Wprowadź liczbe:");
                int x = inputScanner.nextInt();
                int su = 0;
                for (int i = 0; i <= x; i++){
                    if (i % 2 != 0){ continue;}
                    su += i;
                }
                System.out.println(su);
            }
        }

        public static class zad9 {
            public static void main(String[] args) {
                for(int i = 100; i > 0; i--){
                    if (i % 2 != 0 && i % 3 == 0){
                        System.out.println(i);
                    }
                }

                int i = 100;
                while(i != 0){
                    if (i % 2 != 0 && i % 3 == 0){
                        System.out.println(i);
                    }
                    i--;
                }

                i = 100;
                do {
                    if (i % 2 != 0 && i % 3 == 0){
                        System.out.println(i);
                    }
                    i--;
                }while (i != 0);
            }
        }

        public static class zad10 {
            public static void main(String[] args) {
                for(int i = 100; i > -100; i--){
                    if (i % 2 != 0 || i % 3 == 0 || i % 8 == 0){continue;}
                    System.out.println(i);
                }
            }
        }

        public static class zad11 {
            public static void main(String[] args) {
                for (int i = 1; i <= 5; i++) {
                    for (int j = 1; j <= 5; j++) {
                        System.out.print(i * j + "  ");
                    }
                    System.out.println();
                }
            }
        }
    }
}