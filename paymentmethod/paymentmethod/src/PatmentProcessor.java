// FALTA: Clase PaymentProcessor que use polimorfismo

class PaymentProcessor {
    public void process(PaymentMethod method, double amount) {
        if (method.processPayment(amount)) {
            System.out.println("Proceso de Pago Existoso usando: " + method.getDetails());
        } else {
            System.out.println("Proceso de pago fallido usando: " + method.getDetails());
        }
    }
}