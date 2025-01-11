import java.util.Objects;
import java.util.Scanner;

public class lab1 {
    //zadanie 2
    /*
    komentarze
    wielo
    liniowe
     */

    public static class zad3 {
        public  static void main(String[] args){
            //zad 3
            int rok = 2024;
            short mnoznik = 2;
            double wiek = 22;
            int rokUro = rok - (int)wiek;
            System.out.printf("Rok urodzenia: " + rokUro);
            int wiek2 = (int)wiek * (int)mnoznik;
            System.out.printf("\nZa " + (int)wiek + " lat(a) będziesz miec " + wiek2 + " lat(a)\n\n");
        }
    }

    public static class zad4 {
        public  static void main(String[] args){
            //zad 4
            int a = 2, b = 3, c = 6;
            int d = a%b%c;
            System.out.print(d);
        }
    }

    public static class zad5 {
        public  static void main(String[] args){
            //zad 5
            int p = 4;
            for(int i = 0; i < 4; i++){
                p++;
            }
            System.out.print(p);
        }
    }

    public static class zad6 {
        public  static void main(String[] args){
            //zad 6
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź bok a:");
            float a = inputScanner.nextFloat();
            System.out.println("Wprowadź bok b:");
            float b = inputScanner.nextFloat();
            System.out.println("Pole prostokata to: " + Math.round((a*b)*100.0)/100.0);
        }
    }

    public static class zad7 {
        public  static void main(String[] args){
            //zad 7
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź promień r:");
            float r = inputScanner.nextFloat();
            System.out.println("Obwód koła to: " + Math.round((2*Math.PI*r)*100.0)/100.0 + " Natomiast pole to: " + Math.round((Math.PI*r*r)*100.0)/100.0);
        }
    }

    public static class zad8 {
        public  static void main(String[] args){
            //zad 8
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź temperaturew stopniach Celsiusza:");
            float c = inputScanner.nextFloat();
            System.out.println("Temperatura w Fahrenhitach: " + Math.round((32 + (9.0*c)/5)*100.0)/100.0);
        }
    }


    public enum Miesiac {
        STYCZEN,
        LUTY,
        MARZEC,
        KWIECIEN,
        MAJ,
        CZERWIEC,
        LIPIEC,
        SIERPIEN,
        WRZESIEN,
        PAZDZIERNIK,
        LISTOPAD,
        GRUDZIEN
    }
    public static class zad9 {
        public  static void main(String[] args){
            //zad 9
            Miesiac dzis = Miesiac.PAZDZIERNIK;
            System.out.print(dzis);
        }
    }

    public static class zad10 {
        public  static void main(String[] args){
            //zad 10
            Scanner inputScanner = new Scanner(System.in);
            System.out.println("Wprowadź liczbe:");
            int c = inputScanner.nextInt();
            if (c <= 0){
                System.out.print("Liczba jest mniejsza od 0");
            } else if (c >= 100) {
                System.out.print("Liczba jest większa od 100");
            }else{
                System.out.print("Liczba jest w przedziale od 0 do 100");
            }
        }
    }

    public static class zad11 {
        public  static void main(String[] args){
            //zad 11
            String podana = "";
            while (!Objects.equals(podana, "c")){
                Scanner inputScanner = new Scanner(System.in);
                System.out.println("Wprowadź liczbe:");
                podana = inputScanner.nextLine();
            }


        }
    }
}

