// Responsabilidad: imprimir facturas
public class InvoicePrinter {
    public void printInvoice(Order order, OrderCalculator calculator) {
        System.out.println("\nFactura:");
        System.out.println("Producto: " + order.getProduct());
        System.out.println("Cantidad: " + order.getQuantity());
        System.out.println("Precio unitario: " + order.getPrice());
        System.out.println("Total: " + calculator.calculateTotal(order));
    }
}
