# Clase que representa un pedido
class Order:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def get_total(self):
        return self.quantity * self.price


# Responsabilidad: calcular totales
class OrderCalculator:
    def calculate_total(self, order: Order):
        return order.get_total()


# Responsabilidad: enviar notificaciones
class EmailNotifier:
    def send_email(self, email: str, message: str):
        print(f"Enviando email a {email}: {message}")


# Responsabilidad: imprimir factura
class InvoicePrinter:
    def print_invoice(self, order: Order):
        print("Factura:")
        print(f"Producto: {order.product}")
        print(f"Cantidad: {order.quantity}")
        print(f"Precio unitario: {order.price}")
        print(f"Total: ${order.get_total()}")


# Clase principal que coordina las operaciones
class OrderManager:
    def __init__(self, calculator: OrderCalculator, notifier: EmailNotifier, printer: InvoicePrinter):
        self.calculator = calculator
        self.notifier = notifier
        self.printer = printer

    def process_order(self, order: Order, email: str):
        total = self.calculator.calculate_total(order)
        self.notifier.send_email(email, f"Su pedido ha sido procesado. Total: ${total}")
        self.printer.print_invoice(order)


# Main de prueba
if __name__ == "__main__":
    order = Order("Hamburguesa", 3, 5.0)
    manager = OrderManager(OrderCalculator(), EmailNotifier(), InvoicePrinter())
    manager.process_order(order, "cliente@email.com")
