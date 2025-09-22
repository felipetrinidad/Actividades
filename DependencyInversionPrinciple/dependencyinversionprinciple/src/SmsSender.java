public class SmsSender implements MessageSender{
    @Override
    public void sendMessage(String recipient, String message){
        System.out.println("Enviando SMS a " + recipient + ": " + message);
    }    
}