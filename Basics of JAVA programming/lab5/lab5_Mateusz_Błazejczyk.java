import java.util.Scanner;

public class lab5 {
    public static class zad2 {
        static int sum = 0;
        public static void main(String[] args) {
            rekur();
        }

        static void rekur(){
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź liczbe lub wpisz 0 by zakonczyc:");
            int a = inputScanner.nextInt();
            if(a == 0){
                System.out.println("Suma podanych liczb to: " + sum);
                return;
            }
            sum += a;
            rekur();
        }
    }

    public static class zad2a {
        public static void main(String[] args) {
            int sum = 0;

            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Ile liczb chcesz zsumowac?");
            int a = inputScanner.nextInt();
            for(int i = a; i > 0; i--){
                Scanner inputScanner1 = new Scanner(System.in);
                System.out.println("Podaj liczbe do zsumowania");
                int b = inputScanner1.nextInt();
                sum += b;
            }
            System.out.println("Suma to " + sum);
        }
    }


    public static class zad3 {
        static int sil = 0;
        static int il = 0;
        public static void main(String[] args) {
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź liczbe do obliczenia silni:");
            int a = inputScanner.nextInt();
            il = a - 1;
            sil = a;
            rekur();
        }

        static void rekur(){
            if(il - 1 == 0){
                System.out.println("Silnia:" + sil);
                return;
            }
            sil *= il;
            il--;
            rekur();
        }
    }

    public static class zad3a {
        public static void main(String[] args) {
            int sil = 0;
            int il = 0;
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Podaj liczbe do silni");
            int a = inputScanner.nextInt();
            il = a - 1;
            sil = a;
            while(il != 0){
                sil *= il;
                il--;
            }
            System.out.println("Silnia to " + sil);
        }
    }

    public static class zad4{
        public static void main(String[] args) {
            int n = 10;
            System.out.println("10-ta liczba Fibonacciego to: " + fibonacci(n));
        }

        public static int fibonacci(int n) {
            if (n <= 1) {
                return n;
            }
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
    }

    public static  class zad5{
        public static void main(String[] args) {
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Podaj liczbe a");
            int a = inputScanner.nextInt();

            Scanner inputScanner1 = new Scanner(System.in);
            System.out.println("Podaj liczbe b");
            int b = inputScanner1.nextInt();

            System.out.println("NWD (" + a + ", " + b + ") = " + nwd(a, b));
        }
        public static int nwd(int a, int b) {
            if (b == 0) {
                return a;
            }
            return nwd(b, a % b);
        }
    }

    public static class zad6{
        public static void main(String[] args) {
            int a1 = 2;
            int d = 3;
            int n = 5;

            System.out.println(n + "-ty wyraz ciągu arytmetycznego to: " + ciagArytmetyczny(a1, d, n));
        }
        public static int ciagArytmetyczny(int a1, int d, int n) {
            if (n == 1) {
                return a1;
            }
            return ciagArytmetyczny(a1, d, n - 1) + d;
        }
    }

    public static class zad7{
        public static void main(String[] args) {
            int a1 = 2; // Pierwszy wyraz ciągu
            int q = 3;  // Iloraz ciągu
            int n = 4;  // Szukany n-ty wyraz

            System.out.println(n + "-ty wyraz ciągu geometrycznego to: " + ciagGeometryczny(a1, q, n));
        }
        public static int ciagGeometryczny(int a1, int q, int n) {
            if (n == 1) {
                return a1;
            }
            return ciagGeometryczny(a1, q, n - 1) * q;
        }
    }

    public static class zad8{
        public static void main(String[] args) {
            int[] at = new int[10];
            for(int i = 0; i < 10; i++){
                Scanner inputScanner = new Scanner(System.in);
                System.out.println("Podaj liczbe");
                int a = inputScanner.nextInt();
                at[i] = a;
            }
            System.out.println("Najwieksza podana liczba to " + najwieksza(at) + " a najmniejsza " + najmniejsza(at));
        }

        public static int najmniejsza(int[] at) {
            int min = at[0];
            for (int i = 1; i < at.length; i++) {
                if (at[i] < min) {
                    min = at[i];
                }
            }
            return min;
        }

        public static int najwieksza(int[] at) {
            int max = at[0];
            for (int i = 1; i < at.length; i++) {
                if (at[i] > max) {
                    max = at[i];
                }
            }
            return max;
        }
    }
}
