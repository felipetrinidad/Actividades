public class Main {
    public static void main(String[] args) throws Exception {
        
        MessageSender emailSender = new EmailSender();
        NotificationService emailService = new NotificationService(emailSender);
        emailService.notify("cliente@email.com", "Su trabajo fue calificado.");

        MessageSender smsSender = new SmsSender();
        NotificationService smsService = new NotificationService(smsSender);
        smsService.notify("+123456789", "Puede visualizar su nota en Sistemas.");
    }
}
