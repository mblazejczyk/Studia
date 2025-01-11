import java.util.*;
import java.io.*;


class InvalidExpressionException extends Exception {
    public InvalidExpressionException(String message) {
        super(message);
    }
}

class OutOfBoundsException extends Exception {
    public OutOfBoundsException(String message) {
        super(message);
    }
}
class FileReadException extends Exception {
    public FileReadException(String message) {
        super(message);
    }
}

public class lab12 {
    public static class zad4 {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            try {
                System.out.println("Podaj wartość a:");
                double a = scanner.nextDouble();
                System.out.println("Podaj wartość b:");
                double b = scanner.nextDouble();

                double denominator = 2 * a - b;
                if (denominator == 0) {
                    throw new InvalidExpressionException("Dzielenie przez zero! Wyrażenie nie ma sensu.");
                }

                double f = (a + b) / denominator;
                System.out.println("Wynik f = " + f);
            } catch (InvalidExpressionException e) {
                System.out.println("Błąd: " + e.getMessage());
            } catch (Exception e) {
                System.out.println("Niepoprawne dane wejściowe.");
            }
        }
    }

    public static class zad5 {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            Random random = new Random();

            System.out.println("Podaj rozmiar tablicy n:");
            int n = scanner.nextInt();

            double[] array = new double[n];
            System.out.println("Tablica losowych liczb:");
            for (int i = 0; i < n; i++) {
                array[i] = random.nextDouble() * 100; // liczby od 0 do 100
                System.out.printf("%.2f ", array[i]);
            }
            System.out.println();

            try {
                System.out.println("Podaj liczbę m (liczba elementów do obliczenia średniej):");
                int m = scanner.nextInt();

                if (m > n || m <= 0) {
                    throw new OutOfBoundsException("Liczba m jest poza zakresem tablicy!");
                }

                double sum = 0;
                for (int i = 0; i < m; i++) {
                    sum += array[i];
                }
                double average = sum / m;
                System.out.println("Średnia arytmetyczna dla " + m + " elementów wynosi: " + average);
            } catch (OutOfBoundsException e) {
                System.out.println("Błąd: " + e.getMessage());
            } catch (Exception e) {
                System.out.println("Niepoprawne dane wejściowe.");
            }
        }
    }

    public static class zad6 {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            System.out.println("Podaj nazwę pliku do odczytu:");
            String fileName = scanner.nextLine();

            try {
                File file = new File(fileName);
                if (!file.exists()) {
                    throw new FileReadException("Plik nie istnieje!");
                }

                BufferedReader reader = new BufferedReader(new FileReader(file));
                System.out.println("Zawartość pliku:");
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
                reader.close();
            } catch (FileReadException e) {
                System.out.println("Błąd: " + e.getMessage());
            } catch (IOException e) {
                System.out.println("Błąd wejścia/wyjścia: " + e.getMessage());
            }
        }
    }
}
