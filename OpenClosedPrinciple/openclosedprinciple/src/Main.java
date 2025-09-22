public class Main {
    public static void main(String[] args) throws Exception {
        Shape circle = new Circle(5);
        Shape triangle = new Triangle(4, 6);

        System.out.println("\nCalculando areas:\n");
        System.out.printf("Area del Circulo: %.2f\n", circle.area());
        System.out.println("Area del Triangulo: " + triangle.area());
    }
}
