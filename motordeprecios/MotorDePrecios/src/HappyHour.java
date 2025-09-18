
import java.time.LocalTime;

public class HappyHour implements PricingRule {
    //Aplica un 50% de descuento sobre el precio actual en los horarios: 14-15 y 20-21
    private final LocalTime start;
    private final LocalTime end;

    public HappyHour(LocalTime start, LocalTime end) {
        this.start = start;
        this.end = end;
    }

    
    @Override
    public double apply(Product product, int quantity, double currentPrice) {
        LocalTime now = LocalTime.now();
        // Aplica descuento solo si now >= start y now < end
        if (now.isBefore(start) || !now.isBefore(end)) {
            return currentPrice * quantity; // No es hora feliz, no se aplica descuento
        }
        return currentPrice * quantity * 0.5;
    }
    
}