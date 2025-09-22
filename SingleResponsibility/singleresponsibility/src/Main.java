public class Main {
    public static void main(String[] args) throws Exception {
        //Orden
        Order order = new Order("Hamburguesa", 2, 1500.00);
        OrderCalculator calculator = new OrderCalculator();

        //Notificacion
        EmailNotifier notifier = new EmailNotifier();
        notifier.sendEmail("cliente@gmail.com", "Su pedido ha sido recibido.");

        //Factura
        InvoicePrinter printer = new InvoicePrinter();
        printer.printInvoice(order, calculator);

    }
}
