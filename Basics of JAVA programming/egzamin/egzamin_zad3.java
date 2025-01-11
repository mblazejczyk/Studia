import java.util.Scanner;

public class egzamin_zad3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Podaj wartość n: ");
        int n = scanner.nextInt();

        for (int i = 1; i <= n; i++) {
            for (int j = n; j > 0; j--) {
                if (j >= i) {
                    System.out.print(j);
                } else {
                    System.out.print(i);
                }
            }
            System.out.print("\n");
        }

        scanner.close();
    }
}
