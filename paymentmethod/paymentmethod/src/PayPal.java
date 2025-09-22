// FALTA: Clase PayPal que extienda PaymentMethod

class PayPal extends PaymentMethod {
    private final String email;

    public PayPal(String email) {
        this.email = email;
    }

    @Override
    public boolean processPayment(double amount) {
        //Lógica de procesamiento
        if (email == null || !email.contains("@")) {
            System.out.println("\nEmail inválido");
            return false;
        }
        if (amount <= 0) {
            System.out.println("\nMonto inválido");
            return false;
        }
        System.out.println("\nProcessing $" + amount + " with PayPal account: " + email);
        return true;
    }

    @Override
    public String getDetails() {
        return "Cuenta PayPal: " + email;
    }
}