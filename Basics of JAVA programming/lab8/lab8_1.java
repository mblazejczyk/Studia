
class Animal {
    protected String name;
    protected int age;

    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void eat() {
        System.out.println(name + " is eating.");
    }
}

class Fish extends Animal {
    public Fish(String name, int age) {
        super(name, age);
    }

    public void swim() {
        System.out.println(name + " is swimming.");
    }

    @Override
    public void eat() {
        System.out.println(name + " the fish is eating.");
    }
}

class Mammal extends Animal {
    protected String color;
    protected double weight;

    public Mammal(String name, int age, String color, double weight) {
        super(name, age);
        this.color = color;
        this.weight = weight;
    }

    public void run() {
        System.out.println(name + " is running.");
    }

    @Override
    public void eat() {
        System.out.println(name + " the mammal is eating.");
    }
}

class Bird extends Animal {
    protected String breed;

    public Bird(String name, int age, String breed) {
        super(name, age);
        this.breed = breed;
    }

    public void fly() {
        System.out.println(name + " is flying.");
    }

    public void sing() {
        System.out.println(name + " is singing.");
    }

    @Override
    public void eat() {
        System.out.println(name + " the bird is eating.");
    }
}
class Cat extends Mammal {
    public Cat(String name, int age, String color, double weight) {
        super(name, age, color, weight);
    }

    private void cleaning() {
        System.out.println(name + " is cleaning itself.");
    }

    public void mew() {
        System.out.println(name + " is meowing.");
    }

    @Override
    public void eat() {
        System.out.println(name + " the cat is eating.");
    }
}

class Dog_a extends Mammal {
    public Dog_a(String name, int age, String color, double weight) {
        super(name, age, color, weight);
    }

    public void bark() {
        System.out.println(name + " is barking.");
    }

    public void retrieve() {
        System.out.println(name + " is retrieving.");
    }

    @Override
    public void eat() {
        System.out.println(name + " the dog is eating.");
    }
}

public class lab8_1 {
    public static void main(String[] args) {
        Fish fish = new Fish("Goldfish", 1);
        Mammal mammal = new Mammal("Elephant", 15, "Gray", 5000.0);
        Bird bird = new Bird("Parrot", 2, "Macaw");
        Cat cat = new Cat("Whiskers", 3, "Black", 4.5);
        Dog_a dog = new Dog_a("Buddy", 5, "Brown", 20.0);

        fish.eat();
        fish.swim();

        mammal.eat();
        mammal.run();

        bird.eat();
        bird.fly();
        bird.sing();

        cat.eat();
        cat.mew();

        dog.eat();
        dog.bark();
        dog.retrieve();
    }
}
