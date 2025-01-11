public class Dog{
    public String name = "";
    public int age = 0;
    public int weight = 0;

    public void setName(String newName){
        name = newName;
    }
    public void setAge(int newAge){
        age = newAge;
    }
    public void setWeight(int newWeight){
        weight = newWeight;
    }
    public String getName(){
            return name;
    }
    public int getAge(){
        return age;
    }
    public int getWeight(){
        return weight;
    }

    public void Bark(){
        System.out.println("Bark!");
    }

    public Dog(){
        name = "Azor";
        age = 5;
        weight = 14;
    }

    public Dog(String n, int a, int w){
        name = n;
        age = a;
        weight = w;
    }

    public Dog(Dog d) {
        name = d.name;
        age = d.age;
        weight = d.weight;
    }
    public String toString() {
        return "Dog{name='" + name + "', age=" + age + ", weight=" + weight + "}";
    }

    public static void main(String[] args) {
        Dog gargamel = new Dog();
        Dog gargamelJr = new Dog(gargamel);
        Dog gargamelowa = new Dog("Gargamelowa", 9, 17);
        System.out.println(gargamel + "\n" + gargamelJr + "\n" + gargamelowa);
    }
}