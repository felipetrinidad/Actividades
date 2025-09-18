public class DosPorUno implements PricingRule {
    //Aplica la regla de 2x1
    @Override
    public double apply(Product product, int quantity, double currentPrice) {
        int chargeableQuantity = (quantity / 2) + (quantity % 2);
        return product.getBasePrice() * chargeableQuantity;
    }
    
}
