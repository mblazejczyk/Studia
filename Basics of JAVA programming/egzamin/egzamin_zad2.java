import java.util.Scanner;

public class egzamin_zad2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Podaj wartość n: ");
        int n = scanner.nextInt();

        int isPrime = 1;
        for(int i = 2; i < n; i++){
            if(n % i == 0){
                isPrime = 0;
            }
        }

        if(isPrime == 1){
            System.out.println("Jest pierwsza");
        }else{
            int m = n;
            while(n > 1){
                if(n != m){
                    System.out.print("*");
                }
                for(int i = 2; i <= n; i++){
                    if(n % i == 0){
                        n = n / i;
                        System.out.print(i);
                        break;
                    }
                }

            }
            System.out.print("=" + m);
        }

    }
}
