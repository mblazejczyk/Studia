import java.util.Objects;

public class lab10 {
    public interface InterfaceDraw {
        public void draw();
    }

    public interface InterfaceSound {
        public void play();
    }

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

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Shape shape = (Shape) o;
            return Objects.equals(color, shape.color);
        }

        @Override
        public int hashCode() {
            return Objects.hash(color);
        }
    }

    abstract class Quadrangle extends Shape implements InterfaceDraw {
        protected double a;

        public Quadrangle(String _c, double _a) {
            super(_c);
            a = _a;
        }

        @Override
        public boolean equals(Object o) {
            if (!super.equals(o)) return false;
            Quadrangle that = (Quadrangle) o;
            return Double.compare(that.a, a) == 0;
        }

        @Override
        public int hashCode() {
            return Objects.hash(super.hashCode(), a);
        }
    }

    class Rectangle extends Quadrangle {
        private double b;

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

        @Override
        public double Area() {
            return a * b;
        }

        @Override
        public double Circuit() {
            return 2 * a + 2 * b;
        }

        @Override
        public void draw() {}

        @Override
        public boolean equals(Object o) {
            if (!super.equals(o)) return false;
            Rectangle rectangle = (Rectangle) o;
            return Double.compare(rectangle.b, b) == 0;
        }

        @Override
        public int hashCode() {
            return Objects.hash(super.hashCode(), b);
        }
    }

    class Square extends Quadrangle {
        public Square(String _c, double _a) {
            super(_c, _a);
        }

        public double getA() {
            return a;
        }

        @Override
        public double Area() {
            return a * a;
        }

        @Override
        public double Circuit() {
            return 4 * a;
        }

        @Override
        public void draw() {}

        @Override
        public boolean equals(Object o) {
            return super.equals(o);
        }

        @Override
        public int hashCode() {
            return super.hashCode();
        }
    }

    class Triangle extends Shape implements InterfaceDraw, InterfaceSound {
        private double a;
        private double h;

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

        @Override
        public double Area() {
            return a * h / 2;
        }

        @Override
        public double Circuit() {
            double equilateralHeight = (Math.sqrt(3) / 2) * a;
            if (Math.abs(h - equilateralHeight) < 0.01) {
                return 3 * a;
            } else {
                double b = Math.sqrt(Math.pow(a / 2, 2) + Math.pow(h, 2));
                return a + 2 * b;
            }
        }

        @Override
        public void draw() {}

        @Override
        public void play() {}

        @Override
        public boolean equals(Object o) {
            if (!super.equals(o)) return false;
            Triangle triangle = (Triangle) o;
            return Double.compare(triangle.a, a) == 0 && Double.compare(triangle.h, h) == 0;
        }

        @Override
        public int hashCode() {
            return Objects.hash(super.hashCode(), a, h);
        }
    }

    class Circle extends Shape implements InterfaceDraw {
        private double r;

        public Circle(String _c, double _r) {
            super(_c);
            r = _r;
        }

        public double getR() {
            return r;
        }

        @Override
        public double Area() {
            return 3.14 * Math.pow(r, 2);
        }

        @Override
        public double Circuit() {
            return 2 * 3.14 * r;
        }

        @Override
        public void draw() {}

        @Override
        public boolean equals(Object o) {
            if (!super.equals(o)) return false;
            Circle circle = (Circle) o;
            return Double.compare(circle.r, r) == 0;
        }

        @Override
        public int hashCode() {
            return Objects.hash(super.hashCode(), r);
        }
    }

    public static void main(String[] args) {
        lab10 lab = new lab10();

        // Tworzenie instancji każdego kształtu
        Rectangle rectangle1 = lab.new Rectangle("Red", 4, 5);
        Rectangle rectangle2 = lab.new Rectangle("Red", 4, 5);
        Square square = lab.new Square("Blue", 3);
        Triangle triangle = lab.new Triangle("Green", 3, 4);
        Circle circle = lab.new Circle("Yellow", 6);

        // Wyświetlanie porównań za pomocą equals i hashCode
        System.out.println("rectangle1 equals rectangle2: " + rectangle1.equals(rectangle2));
        System.out.println("rectangle1 hashCode: " + rectangle1.hashCode());
        System.out.println("rectangle2 hashCode: " + rectangle2.hashCode());

        System.out.println("square hashCode: " + square.hashCode());
        System.out.println("triangle hashCode: " + triangle.hashCode());
        System.out.println("circle hashCode: " + circle.hashCode());
    }
}
