public abstract class PaymentMethod {
    public abstract boolean processPayment(double amount);
    // FALTA: Método abstracto para obtener detalles

    public abstract String getDetails();
}

