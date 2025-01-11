import java.util.*;

import java.util.*;

abstract class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public abstract void display();
}

class Employee extends Person {
    private int id;
    private double salary;

    public Employee(int id, String name, int age, double salary) {
        super(name, age);
        this.id = id;
        this.salary = salary;
    }

    public int getId() {
        return id;
    }

    public double getSalary() {
        return salary;
    }

    @Override
    public void display() {
        System.out.println("Employee{id=" + id + ", name='" + getName() + "', age=" + getAge() + ", salary=" + salary + "}");
    }

    @Override
    public String toString() {
        return "Employee{id=" + id + ", name='" + getName() + "', age=" + getAge() + ", salary=" + salary + "}";
    }
}


public class lab11 {
    public static class zad2 {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            Set<Double> numbers = new TreeSet<>();

            System.out.println("Wpisz liczby rzeczywiste (wpisz 'stop', aby zakończyć):");
            while (true) {
                String input = scanner.nextLine();
                if (input.equalsIgnoreCase("stop")) {
                    break;
                }
                try {
                    double number = Double.parseDouble(input);
                    numbers.add(number);
                } catch (NumberFormatException e) {
                    System.out.println("Niepoprawna liczba, spróbuj ponownie.");
                }
            }

            System.out.println("Wprowadzone liczby: " + numbers);
        }
    }

    public static class zad3 {
        public static void main(String[] args) {
            Map<String, Integer> months = new HashMap<>();
            months.put("styczeń", 31);
            months.put("luty", 28); // dla uproszczenia pomijamy lata przestępne
            months.put("marzec", 31);
            months.put("kwiecień", 30);
            months.put("maj", 31);
            months.put("czerwiec", 30);
            months.put("lipiec", 31);
            months.put("sierpień", 31);
            months.put("wrzesień", 30);
            months.put("październik", 31);
            months.put("listopad", 30);
            months.put("grudzień", 31);

            Scanner scanner = new Scanner(System.in);
            System.out.println("Podaj nazwę miesiąca (np. 'styczeń'):");
            String monthName = scanner.nextLine().toLowerCase();

            if (months.containsKey(monthName)) {
                System.out.println("Liczba dni w miesiącu " + monthName + ": " + months.get(monthName));
            } else {
                System.out.println("Niepoprawna nazwa miesiąca.");
            }
        }
    }


    public static class zad4 {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            Map<Integer, Employee> employees = new HashMap<>();

            System.out.println("Wprowadź dane pracowników (id, imię, wiek, pensja; wpisz 'stop', aby zakończyć):");
            while (true) {
                String input = scanner.nextLine();
                if (input.equalsIgnoreCase("stop")) {
                    break;
                }
                try {
                    String[] parts = input.split(",");
                    int id = Integer.parseInt(parts[0].trim());
                    String name = parts[1].trim();
                    int age = Integer.parseInt(parts[2].trim());
                    double salary = Double.parseDouble(parts[3].trim());
                    employees.put(id, new Employee(id, name, age, salary));
                } catch (Exception e) {
                    System.out.println("Niepoprawne dane, spróbuj ponownie.");
                }
            }

            System.out.println("Wprowadź zakres filtrowania (wiek lub zarobki):");
            System.out.println("1. Starsze niż X lat");
            System.out.println("2. Młodsze niż X lat");
            System.out.println("3. Zarobki większe niż X");
            System.out.println("4. Zarobki mniejsze niż X");
            int choice = scanner.nextInt();
            System.out.println("Podaj wartość X:");
            double x = scanner.nextDouble();

            System.out.println("Filtr wyników:");
            for (Employee emp : employees.values()) {
                boolean match = switch (choice) {
                    case 1 -> emp.getAge() > x;
                    case 2 -> emp.getAge() < x;
                    case 3 -> emp.getSalary() > x;
                    case 4 -> emp.getSalary() < x;
                    default -> false;
                };
                if (match) {
                    emp.display();
                }
            }
        }
    }
}
