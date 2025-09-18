public class DescuentoPorcentaje implements PricingRule {
    //Aplica un descuento porcentual sobre el precio actual
    private final double porcentaje;

    public DescuentoPorcentaje(double porcentaje) {
        if (porcentaje < 0 || porcentaje > 100) {
            throw new IllegalArgumentException("El porcentaje debe estar entre 0 y 100.");
        }
        this.porcentaje = porcentaje;
    }

    @Override
    public double apply(Product product, int quantity, double currentPrice) {
        return currentPrice * (1 - porcentaje / 100);
    }
    
}
