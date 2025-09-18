import java.util.List;

public class MotorDePrecios {
    private final List<PricingRule> rules;

    public MotorDePrecios(List<PricingRule> rules) {
        this.rules = rules;
    }

    public double calculatePrice(Product product, int quantity) {
        double price = 0.0;
        if(rules.isEmpty()) {
            throw new IllegalStateException("No hay reglas de precios definidas.");
        }

        for (PricingRule rule : rules) {
            price = rule.apply(product, quantity, price);
            if (price < 0) {
                price = 0; // El precio no puede ser negativo
            }
        }
        return price;
    }
}
