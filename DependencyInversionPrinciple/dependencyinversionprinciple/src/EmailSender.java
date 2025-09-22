public class EmailSender implements MessageSender {
    @Override
    public void sendMessage(String recipient, String message){
        System.out.println("Enviando Mail a: " + recipient + ": " + message);
    }
}