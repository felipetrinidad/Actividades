

public class NotificationService {
    private final MessageSender sender;
    
    public NotificationService(MessageSender sender) {
        this.sender = sender;
    }

    public void notify(String recipient, String message){
        this.sender.sendMessage(recipient, message);
    }
}
