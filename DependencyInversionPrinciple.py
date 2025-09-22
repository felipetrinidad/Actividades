from abc import ABC, abstractmethod

# Abstracción: interfaz para enviar mensajes
class MessageSender(ABC):
    @abstractmethod
    def send_message(self, recipient: str, message: str):
        pass


# envío por email
class EmailSender(MessageSender):
    def send_message(self, recipient: str, message: str):
        print(f"Enviando email a {recipient}: {message}")


# envío por SMS
class SmsSender(MessageSender):
    def send_message(self, recipient: str, message: str):
        print(f"Enviando SMS a {recipient}: {message}")


# Servicio de notificaciones
class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify(self, recipient: str, message: str):
        self.sender.send_message(recipient, message)


# Ejemplo de uso
if __name__ == "__main__":
    email_service = NotificationService(EmailSender())
    email_service.notify("alumno@email.com", "Su trabajo fue calificado.")

    sms_service = NotificationService(SmsSender())
    sms_service.notify("+123456789", "Puede ver su nota en Sistemas.")
