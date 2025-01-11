import java.util.HashMap;
import java.util.Scanner;
import java.util.Map;
import java.util.Arrays;

public class lab4 {

    public static class zad2 {
        public static void main(String[] args) {
            int[] tab = new int[20];
            int index = 0;
            for(int i = 20; i > 0; i--){
                tab[index] = i;
                index++;
            }

            for (int i = 0; i < tab.length; i++) {
                System.out.print(tab[i] + " ");
            }
        }
    }

    public static class zad3 {
        public static void main(String[] args) {
            int[] tab = new int[20];
            int index = 0;
            int j = 20;
            while(j > 0){
                tab[index] = j;
                index++;
                j--;
            }

            for (int i = 0; i < tab.length; i++) {
                System.out.print(tab[i] + " ");
            }
        }
    }

    public static class zad4 {
        public static void main(String[] args) {
            int[] numbers = {1, 2, 3, 4, 5};
            int sum = 0;
            for (int i = 0; i < numbers.length; i++) {
                sum += numbers[i];
            }
            System.out.println(sum);
        }
    }

    public static class zad5 {
        public static void main(String[] args) {
            int[] numbers = {1, 2, 2, 3, 4, 2, 5};
            Map<Integer, Integer> dict = new HashMap<>();

            for (int i = 0; i < numbers.length; i++) {
                int currentNumber = numbers[i];
                dict.put(currentNumber, dict.getOrDefault(currentNumber, 0) + 1);
            }
            System.out.println(dict);
        }
    }

    public static class zad6 {
        public static void main(String[] args) {
            int[] numbers = {1, 2, 3, 4, 5};
            int[] numbers2 = new int[numbers.length];
            int index = 0;
            for(int i = numbers.length - 1; i > 0; i--){
                numbers2[index] = numbers[i];
                index++;
            }

            for (int i = 0; i < numbers2.length; i++){
                System.out.println(numbers2[i]);
            }
        }
    }

    public static class zad7 {
        public static void main(String[] args) {
            int[] numbers = new int[5];
            int sum = 0;
            for(int i = numbers.length - 1; i > 0; i--){
                Scanner inputScanner = new Scanner(System.in);
                System.out.println("Wprowadź liczbe:");
                int a = inputScanner.nextInt();
                sum += a;
            }
            System.out.println(sum / 5);
        }
    }

    public static class zad8 {
        public static void main(String[] args) {
            int[] numbers = {1, 2, 2, 3, 4, 2, 5};
            Map<Integer, Integer> dict = new HashMap<>();

            for (int i = 0; i < numbers.length; i++) {
                int currentNumber = numbers[i];
                dict.put(currentNumber, dict.getOrDefault(currentNumber, 0) + 1);
            }
            System.out.println(dict.keySet());
        }
    }

    public static class zad9 {
        public static void main(String[] args) {
            int[] numbers = new int[4];
            for(int i = 0; i < numbers.length; i++){
                Scanner inputScanner = new Scanner(System.in);
                System.out.println("Wprowadź liczbe:");
                int a = inputScanner.nextInt();
                numbers[i] = a;
            }
            int max = 0;
            for(int i = 0; i < numbers.length; i++){
                if(numbers[i] > max){
                    max = numbers[i];
                }
            }
            System.out.println(max);
        }
    }

    public static class zad10 {
        public static void main(String[] args) {
            int[] numbers = new int[5];
            int sum = 0;
            for(int i = 0; i < numbers.length; i++){
                Scanner inputScanner = new Scanner(System.in);
                System.out.println("Wprowadź ocene (od 0 do 20):");
                int a = inputScanner.nextInt();
                numbers[i] = a;
                sum += a;
            }
            int max = 0;
            int min = 20;
            for(int i = 0; i < numbers.length; i++){
                if(numbers[i] > max){
                    max = numbers[i];
                }
                if(numbers[i] < min){
                    min = numbers[i];
                }
            }
            System.out.println(sum - max - min);
        }
    }

    public static class zad12 {
        public static void main(String[] args) {
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź dlugosc:");
            int a = inputScanner.nextInt();
            int[][] numbers = new int[a][a];
            for(int i = 0; i < numbers.length; i++){
                for(int j = 0; j < numbers.length; j++) {
                    if(i < j){
                        numbers[i][j] = i + 1;
                    }else{
                        numbers[i][j] = j + 1;
                    }
                }
            }

            for(int i = 0; i < numbers.length; i++){
                System.out.println(Arrays.toString(numbers[i]));
            }
        }
    }

    public static class zad13 {
        public static void main(String[] args) {
            int[][] matrix = {
                    {1, 2, 3},
                    {4, 5, 6},
                    {7, 8, 9}
            };
            for (int i = 0; i < matrix.length; i++) {
                for (int j = i + 1; j < matrix[i].length; j++) {
                    int temp = matrix[i][j];
                    matrix[i][j] = matrix[j][i];
                    matrix[j][i] = temp;
                }
            }

            for(int i = 0; i < matrix.length; i++){
                System.out.println(Arrays.toString(matrix[i]));
            }
        }
    }

    public static class zad14 {
        public static void main(String[] args) {
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź dlugosc:");
            int a = inputScanner.nextInt();

            Scanner inputScanner1 = new Scanner(System.in);
            System.out.println("Wprowadź szerokosc:");
            int b = inputScanner1.nextInt();
            int[][] numbers = new int[a][b];

            for(int i = 0; i < numbers.length; i++){
                for(int j = 0; j < numbers[i].length; j++) {
                    numbers[i][j] = (j + 1) * (i + 1);
                }
            }

            for(int i = 0; i < numbers.length; i++){
                System.out.println(Arrays.toString(numbers[i]));
            }
        }
    }


    public static class zad15 {
        public static void main(String[] args) {
            int[] numbers = {1, 2, 3, 4, 5};
            int last = numbers[numbers.length - 1];

            for(int i = numbers.length - 1; i > 0; i--){
                numbers[i] = numbers[i - 1];
            }
            numbers[0] = last;
            System.out.println(Arrays.toString(numbers));

        }
    }

    public static class zad16 {
        public static void main(String[] args) {
            String[] polski = {"kot", "pies", "dom", "szkoła", "samochód"};
            String[] niemiecki = {"Katze", "Hund", "Haus", "Schule", "Auto"};
            String[] angielski = {"cat", "dog", "house", "school", "car"};

            System.out.println("Polski -> Niemiecki -> Angielski");
            for (int i = 0; i < polski.length; i++) {
                System.out.println(polski[i] + " -> " + niemiecki[i] + " -> " + angielski[i]);
            }
        }
    }


    public static class zad17 {
        public static void main(String[] args) {
            int[] numbers = {3, 1, 2, 3, 4, 1, 5, 6};
            int start = 0;
            int maxLength = 1;
            int bestStart = 0;

            for (int i = 1; i < numbers.length; i++) {
                if (numbers[i] > numbers[i - 1]) {
                    if (i - start + 1 > maxLength) {
                        maxLength = i - start + 1;
                        bestStart = start;
                    }
                } else {
                    start = i;
                }
            }

            int[] result = Arrays.copyOfRange(numbers, bestStart, bestStart + maxLength);
            System.out.println("Najdłuższy rosnący ciąg: " + Arrays.toString(result));

        }
    }

    public static class zad18 {
        public static void main(String[] args) {
            int[] n = {1, 2, 3, 2, 1};
            int tak = 1;
            for (int i = 0; i < n.length / 2; i++) {
                if (n[i] != n[n.length - 1 - i]) {
                    tak = 0;
                    break;
                }
            }
            if(tak == 1){
                System.out.println("Jest to palindrom");
            }else{
                System.out.println("Nie jest to palindrom");
            }
        }
    }

    static boolean isPrime(int n){
        if(n==1||n==0)return false;
        for(int i=2; i<n; i++){
            if(n%i==0)return false;
        }
        return true;
    }
    public static class zad19 {
        public static void main(String[] args) {

            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź dlugosc:");
            int a = inputScanner.nextInt();
            int[] n = new int[a];
            int nextNum = 0;
            for (int i = 0; i < n.length; i++) {
                while(!isPrime(nextNum)){
                    nextNum++;
                }
                n[i] = nextNum;
                nextNum++;
            }
            System.out.println(Arrays.toString(n));
        }
    }
}
