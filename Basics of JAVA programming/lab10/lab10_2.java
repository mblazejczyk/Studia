import java.util.Arrays;

public class lab10_2 {
    public interface Comparable<T> {
        int compareTo(T o);
    }

    abstract class Person implements Comparable<Person> {
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

        @Override
        public int compareTo(Person o) {
            return this.name.compareTo(o.name);
        }
    }

    class Student extends Person {
        public Student(String name, int age) {
            super(name, age);
        }

        @Override
        public void display() {
            System.out.println("Student: " + getName() + ", Age: " + getAge());
        }
    }

    class Driver extends Person {
        private String breed;

        public Driver(String name, int age, String breed) {
            super(name, age);
            this.breed = breed;
        }

        @Override
        public void display() {
            System.out.println("Driver: " + getName() + ", Age: " + getAge() + ", Breed: " + breed);
        }

        public void drive() {
            System.out.println("Driving...");
        }

        public void parking() {
            System.out.println("Parking...");
        }
    }

    abstract class Employee extends Person {
        private int salary;

        public Employee(String name, int age, int salary) {
            super(name, age);
            this.salary = salary;
        }

        public int getSalary() {
            return salary;
        }

        public void setSalary(int salary) {
            this.salary = salary;
        }

        @Override
        public int compareTo(Person o) {
            Employee otherEmployee = (Employee) o;
            return Integer.compare(this.salary, otherEmployee.salary);

        }
    }

    class Accountant extends Employee {
        public Accountant(String name, int age, int salary) {
            super(name, age, salary);
        }

        @Override
        public void display() {
            System.out.println("Accountant: " + getName() + ", Age: " + getAge() + ", Salary: " + getSalary());
        }

        private void booking() {
            System.out.println("Booking...");
        }
    }

    class Manager extends Employee {
        public Manager(String name, int age, int salary) {
            super(name, age, salary);
        }

        @Override
        public void display() {
            System.out.println("Manager: " + getName() + ", Age: " + getAge() + ", Salary: " + getSalary());
        }

        public void checkReport() {
            System.out.println("Checking report...");
        }
    }

    public static void main(String[] args) {
        lab10_2 lab = new lab10_2();

        Employee[] tabEmp = new Employee[] {
                lab.new Accountant("Alice", 30, 5000),
                lab.new Manager("Bob", 45, 7000),
                lab.new Accountant("Charlie", 28, 4800)
        };
        for (Employee emp : tabEmp) {
            emp.display();
        }
        System.out.println("\n\n");
        Employee emp1 = lab.new Accountant("Alice", 30, 5000);
        Employee emp2 = lab.new Accountant("Bob", 45, 7000);

        int result = emp1.compareTo(emp2);

        if (result < 0) {
            System.out.println(emp1.getName() + " ma mniejsze wynagrodzenie niż " + emp2.getName());
        } else if (result > 0) {
            System.out.println(emp1.getName() + " ma większe wynagrodzenie niż " + emp2.getName());
        } else {
            System.out.println(emp1.getName() + " ma takie samo wynagrodzenie jak " + emp2.getName());
        }
    }
}
