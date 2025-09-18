
public class Product {
    private final String name;
    private final double basePrice;

    public Product(String name, double basePrice) {
        if (name == null || name.isEmpty()) {throw new IllegalArgumentException("El nombre no puede ser nulo o vacío.");}
        if (basePrice < 0) {throw new IllegalArgumentException("El precio no puede ser negativo.");}
        this.name = name;
        this.basePrice = basePrice;
    }

    public String getName() {
        return name;
    }

    public double getBasePrice() {
        return basePrice;
    }   
}
