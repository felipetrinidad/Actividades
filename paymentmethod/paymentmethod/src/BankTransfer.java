// FALTA: Clase BankTransfer que extienda PaymentMethod

class BankTransfer extends PaymentMethod {
    private final String bankAccountNumber;
    private final String bankCode;

    public BankTransfer(String bankAccountNumber, String bankCode) {
        this.bankAccountNumber = bankAccountNumber;
        this.bankCode = bankCode;
    }

    @Override
    public boolean processPayment(double amount) {
        // Lógica de procesamiento
        if (bankAccountNumber == null || bankAccountNumber.isEmpty()) {
            System.out.println("\nNúmero de cuenta bancaria inválido");
            return false;
        }
        if (bankCode == null || bankCode.isEmpty()) {
            System.out.println("\nCódigo bancario inválido");
            return false;
        }
        if (amount <= 0) {
            System.out.println("\nMonto inválido");
            return false;
        }
        System.out.println("\nProcessing $" + amount + " with bank transfer");
        return true;
    }

    @Override
    public String getDetails() {
        return "Transferencia bancaria a la cuenta: " + bankAccountNumber;
    }
}