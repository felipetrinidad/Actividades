public class Main {
    public static void main(String[] args) throws Exception {
        PaymentProcessor processor = new PaymentProcessor();

        PaymentMethod creditCard = new CreditCard("1234567890123456", "12/25", "123");
        PaymentMethod payPal = new PayPal("prueba@gmail.com");
        PaymentMethod bankTransfer = new BankTransfer("123456789", "4321");

        processor.process(creditCard, 100.0);
        processor.process(payPal, 200.0);
        processor.process(bankTransfer, 300.0);


    }
}
