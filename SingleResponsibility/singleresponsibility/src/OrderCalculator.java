// Responsabilidad: calcular totales
public class OrderCalculator {
    public double calculateTotal(Order order) {
        return order.getQuantity() * order.getPrice();
    }
}
