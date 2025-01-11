import java.util.Scanner;

public class egzamin_zad1 {
    public static long fibonacci(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        }

        long a = 0;
        long b = 1;
        long result = 0;

        for (int i = 2; i <= n; i++) {
            result = a + b;
            a = b;
            b = result;
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Podaj wartość n: ");
        int n = scanner.nextInt();

        if (n < 0) {
            System.out.println("n musi być liczbą nieujemną.");
        } else {
            long fib = fibonacci(n);
            System.out.println("n-ta liczba Fibonacciego to: " + fib);
        }

        scanner.close();
    }
}
