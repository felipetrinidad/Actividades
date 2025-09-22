from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """Procesa el pago por el monto dado"""
        pass

    @abstractmethod
    def get_info(self):
        """Devuelve información del método de pago"""
        pass


class CreditCard(PaymentMethod):
    def __init__(self, card_number, expiry_date, cvv):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def process_payment(self, amount):
        # Lógica ficticia de procesamiento
        if len(self.card_number) == 16 and len(self.cvv) == 3:
            print(f"Procesando ${amount} con tarjeta de crédito {self.card_number[-4:]}")
            return True
        print("Error: datos de tarjeta inválidos")
        return False

    def get_info(self):
        return f"Tarjeta de crédito terminada en {self.card_number[-4:]}"


class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email

    def process_payment(self, amount):
        # Lógica ficticia de procesamiento
        if "@" in self.email:
            print(f"Procesando ${amount} con PayPal ({self.email})")
            return True
        print("Error: cuenta de PayPal inválida")
        return False

    def get_info(self):
        return f"Cuenta PayPal: {self.email}"


class BankTransfer(PaymentMethod):
    def __init__(self, account_number, bank_name):
        self.account_number = account_number
        self.bank_name = bank_name

    def process_payment(self, amount):
        # Lógica ficticia de transferencia bancaria
        if len(self.account_number) >= 8:
            print(f"Procesando transferencia de ${amount} a {self.bank_name}, cuenta {self.account_number}")
            return True
        print("Error: número de cuenta inválido")
        return False

    def get_info(self):
        return f"Transferencia bancaria - Banco: {self.bank_name}, Cuenta: {self.account_number}"


class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def execute_payment(self, amount):
        print(f"Usando método: {self.payment_method.get_info()}")
        return self.payment_method.process_payment(amount)


# Ejemplo de uso
if __name__ == "__main__":
    cc = CreditCard("1234567890123456", "12/27", "123")
    pp = PayPal("usuario@example.com")
    bt = BankTransfer("98765432", "Banco Nación")

    processor = PaymentProcessor(cc)
    processor.execute_payment(100)

    processor = PaymentProcessor(pp)
    processor.execute_payment(250)

    processor = PaymentProcessor(bt)
    processor.execute_payment(500)
    
    # Intento con datos inválidos
    invalid_cc = CreditCard("1234", "12/27", "12")
    processor = PaymentProcessor(invalid_cc)
    processor.execute_payment(100)