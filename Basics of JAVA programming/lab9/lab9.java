public class lab9 {
    abstract class Shape {
        private String color;
        public abstract double Area();
        public abstract double Circuit();
        public Shape(String _c) {
            color = _c;
        }
        public String getColor() {
            return color;
        }
    }

    abstract class Quadrangle extends Shape {
        protected double a;
        public abstract double Area();
        public abstract double Circuit();
        public Quadrangle(String _c, double _a) {
            super(_c);
            a = _a;
        }
    }

    class Rectangle extends Quadrangle {
        private double b;
        public double Area() {
            return a * b;
        }
        public double Circuit() {
            return 2 * a + 2 * b;
        }
        public Rectangle(String _c, double _a, double _b) {
            super(_c, _a);
            b = _b;
        }
        public double getA() {
            return a;
        }
        public double getB() {
            return b;
        }
    }
    class Square extends Quadrangle {
        public double Area() {
            return a * a;
        }
        public double Circuit() {
            return 4*a;
        }
        public Square(String _c, double _a) {
            super(_c, _a);
        }
        public double getA() {
            return a;
        }
    }
    class Triangle extends Shape {
        private double a;
        private double h;
        @Override
        public double Area() {
            return a * h / 2;
        }
        public double Circuit() {
            double equilateralHeight = (Math.sqrt(3) / 2) * a;
            if (Math.abs(h - equilateralHeight) < 0.01) {
                return 3 * a;
            } else {
                double b = Math.sqrt(Math.pow(a / 2, 2) + Math.pow(h, 2));
                return a + 2 * b;
            }
        }
        public Triangle(String _c, double _a, double _h) {
            super(_c);
            a = _a;
            h = _h;
        }
        public double getA() {
            return a;
        }
        public double getH() {
            return h;
        }
    }
    class Circle extends Shape {
        private double r;
        public double Area() {
            return 2 * 3.14 * r;
        }
        public double Circuit() {
            return 3.14 * Math.pow(r, 2);
        }
        public Circle(String _c, double _r) {
            super(_c);
            r = _r;
        }
        public double getR() {
            return r;
        }
    }

    public static void main(String[] args) {
        lab9 lab = new lab9();

        // Tworzenie instancji każdego kształtu
        Rectangle rectangle = lab.new Rectangle("Red", 4, 5);
        Square square = lab.new Square("Blue", 3);
        Triangle triangle = lab.new Triangle("Green", 3, 4);
        Circle circle = lab.new Circle("Yellow", 6);

        // Wyświetlanie informacji o każdym kształcie
        System.out.println("Rectangle (Color: " + rectangle.getColor() + ")");
        System.out.println("Area: " + rectangle.Area());
        System.out.println("Circuit: " + rectangle.Circuit());

        System.out.println("\nSquare (Color: " + square.getColor() + ")");
        System.out.println("Area: " + square.Area());
        System.out.println("Circuit: " + square.Circuit());

        System.out.println("\nTriangle (Color: " + triangle.getColor() + ")");
        System.out.println("Area: " + triangle.Area());
        System.out.println("Circuit: " + triangle.Circuit());

        System.out.println("\nCircle (Color: " + circle.getColor() + ")");
        System.out.println("Area: " + circle.Area());
        System.out.println("Circuit: " + circle.Circuit());
    }
}
