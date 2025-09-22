 public class CreditCard extends PaymentMethod {
    private final String cardNumber;
    private final String expiryDate;
    private final String cvv;

    public CreditCard(String cardNumber, String expiryDate, String cvv) {
        this.cardNumber = cardNumber;
        this.expiryDate = expiryDate;
        this.cvv = cvv;
    }

     @Override
    public boolean processPayment(double amount) {
        // FALTA: Lógica de procesamiento
        if (cardNumber == null || cardNumber.length() != 16) {
            System.out.println("\nNúmero de tarjeta inválido");
            return false;
        }
        if (expiryDate == null || !expiryDate.matches("\\d{2}/\\d{2}")) {
            System.out.println("\nFecha de expiración inválida");
            return false;
        }
        if (cvv == null || cvv.length() != 3) {
            System.out.println("\nCVV Inválido");
            return false;
        }
        if (amount <= 0) {
            System.out.println("\nMonto inválido");
            return false;
        }
        System.out.println("\nProcessing $" + amount + " with credit card");
        return true;
    }


    @Override
    public String getDetails() {
        return "Tarjeta de Crédito terminada en: " + cardNumber.substring(cardNumber.length() - 4);
    }
}



