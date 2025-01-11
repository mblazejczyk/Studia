import java.util.Scanner;

public class book {
    public String author;
    public String title;
    public int year;

    public void setAuthor(String author) {
        this.author = author;
    }
    public void setTitle(String title) {
        this.title = title;
    }
    public void setYear(int year) {
        this.year = year;
    }

    public int getYear() {
        return year;
    }
    public String getAuthor() {
        return author;
    }
    public String getTitle() {
        return title;
    }

    public book(){
        author = "";
        title = "";
        year = 0;
    }

    public void setBook(){
        Scanner inputScanner = new Scanner(System.in);
        System.out.println("Wprowadź autora:");
        author = inputScanner.nextLine();
        Scanner inputScanner1 = new Scanner(System.in);
        System.out.println("Wprowadź tytul:");
        title = inputScanner1.nextLine();
        Scanner inputScanner2 = new Scanner(System.in);
        System.out.println("Wprowadź rok:");
        year = inputScanner2.nextInt();
    }

    public void showBook(){
        System.out.println(author + " | " + title + " | " + year);
    }

    public static void main(String[] args) {
        book[] books = new book[10];
        for (int i = 0; i < 10; i++) {
            books[i] = new book();
            books[i].setBook();
        }
        for (int i = 0; i < 10; i++) {
            books[i].showBook();
        }
    }
}
