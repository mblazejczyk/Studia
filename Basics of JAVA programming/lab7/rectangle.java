import java.util.Scanner;

public class rectangle {
    public int a;
    public int b;

    public rectangle(){
        a = 0;
        b = 0;
    }

    public void readData(){
        Scanner inputScanner = new Scanner(System.in);
        System.out.println("Wprowadź a:");
        a = inputScanner.nextInt();
        Scanner inputScanner1 = new Scanner(System.in);
        System.out.println("Wprowadź b:");
        b = inputScanner1.nextInt();
    }

    public int calcParim(){
        return 2*a+2*b;
    }

    public int calcArea(){
        return a*b;
    }

    public static void main(String[] args) {
        rectangle r = new rectangle();
        r.readData();
        System.out.println(r.calcArea());
        System.out.println(r.calcParim());
    }
}
