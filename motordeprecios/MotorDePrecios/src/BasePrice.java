public class BasePrice implements PricingRule { 
    //Retorna el precio base del producto sin modificaciones 
    @Override
    public double apply(Product product, int quantity, double currentPrice) {
        return product.getBasePrice() * quantity;
    }
    
}
