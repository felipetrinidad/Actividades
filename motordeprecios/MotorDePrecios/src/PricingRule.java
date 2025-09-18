public interface PricingRule {
    double apply(Product product, int quantity, double currentPrice);
}
