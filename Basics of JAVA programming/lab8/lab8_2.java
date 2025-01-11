public class lab8_2 {
    class Person {
        String name;
        int age;

        void setName(String s) {
            name = s;
        }

        void setAge(int a) {
            age = a;
        }

        int getAge() {
            return age;
        }

        String getName() {
            return name;
        }

        void display() {
            System.out.println("Person: " + name + ", age: " + age);
        }
    }

    class Employee extends Person {
        int salary;

        int getSalary() {
            return salary;
        }

        void setSalary(int s) {
            salary = s;
        }

        @Override
        void display() {
            super.display();
            System.out.println("Employee with salary: " + salary);
        }
    }

    class Manager extends Employee {
        private void monitoring() {
            System.out.println("monitoring");
        }

        @Override
        void display() {
            super.display();
            System.out.println("Role: Manager");
        }
    }

    class Accountant extends Employee {
        void calculating() {
            System.out.println("Calculating");
        }

        void reporting() {
            System.out.println("Reporting");
        }

        @Override
        void display() {
            super.display();
            System.out.println("Role: Accountant");
        }
    }

    class Pensioner extends Person {
        int income;

        void travel() {
            System.out.println("Traveling...");
        }

        void visiting() {
            System.out.println("Visiting");
        }

        void setIncome(int i) {
            income = i;
        }

        int getIncome() {
            return income;
        }

        @Override
        void display() {
            super.display();
            System.out.println("Pensioner with income: " + income);
        }
    }

    class Student extends Person {
        String fieldOfStudy;

        void learn() {
            System.out.println("Learning");
        }

        void party() {
            System.out.println("🎉");
        }

        void setFieldOfStudy(String s) {
            fieldOfStudy = s;
        }

        String getFieldOfStudy() {
            return fieldOfStudy;
        }

        @Override
        void display() {
            super.display();
            System.out.println("Student in field: " + fieldOfStudy);
        }
    }

    public static void main(String[] args) {
        lab8_2 lab = new lab8_2();

        Person person = lab.new Person();
        person.setName("Generic Person");
        person.setAge(45);
        person.display();
        System.out.println("------------------------");

        Employee employee = lab.new Employee();
        employee.setName("John Doe");
        employee.setAge(30);
        employee.setSalary(50000);
        employee.display();
        System.out.println("------------------------");

        Manager manager = lab.new Manager();
        manager.setName("Sarah Johnson");
        manager.setAge(40);
        manager.setSalary(75000);
        manager.display();
        System.out.println("------------------------");

        Accountant accountant = lab.new Accountant();
        accountant.setName("Tom White");
        accountant.setAge(35);
        accountant.setSalary(60000);
        accountant.display();
        System.out.println("------------------------");

        Pensioner pensioner = lab.new Pensioner();
        pensioner.setName("Elder Jane");
        pensioner.setAge(70);
        pensioner.setIncome(30000);
        pensioner.display();
        System.out.println("------------------------");

        Student student = lab.new Student();
        student.setName("Alice");
        student.setAge(22);
        student.setFieldOfStudy("Computer Science");
        student.display();
    }
}
