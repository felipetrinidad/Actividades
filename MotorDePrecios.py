from abc import ABC, abstractmethod
from datetime import datetime, time

# Clase de PRODUCTO
class Producto:
    def __init__(self, name, basePrice):
        if not name:
            raise ValueError("El nombre del producto no puede estar vacío.")
        if basePrice < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.name = name
        self.basePrice = basePrice
    
    # Getters
    def getName(self):
        return self.name
    def getBasePrice(self):
        return self.basePrice


# Interfaz para definir estrategias de precios
class PricingRule(ABC):
    @abstractmethod
    def apply(self, product, quantity, currentPrice):
        pass

# Estrategia de descuento precio base (retorna el precio base sin cambios)
class BasePrice(PricingRule):
    def apply(self, product, quantity, currentPrice):
        return product.getBasePrice() * quantity

# Estrategia de descuento porcentual (descuento de 0% a 100%)
class PercentageDiscount(PricingRule):
    def __init__(self, percentage):
        if percentage < 0 or percentage > 100:
            raise ValueError("El porcentaje de descuento debe estar entre 0% y 100%.")
        self.percentage = percentage
    
    def apply(self, product, quantity, currentPrice):
        discount = currentPrice * (self.percentage / 100)
        return currentPrice - discount
    
# Estrategia de descuento: 2x1
class DosPorUno(PricingRule):
    def apply(self, product, quantity, currentPrice):
        if quantity < 2:
            return currentPrice * quantity
        chargeable_units = (quantity // 2) + (quantity % 2)
        return product.getBasePrice() * chargeable_units

# Estrategia de descuento: Happy Hour (40% de descuento entre 15:00 y 16:00)
class HappyHour(PricingRule):
    def __init__(self, start, end):
        self.start = time(start)
        self.end = time(end)
    
    def apply(self, product, quantity, currentPrice):
        now = datetime.now().time()
        
        # Aplica descuento solo si now >= start y now < end
        if now < self.start or now >= self.end:
            return currentPrice * quantity # No es hora feliz, no se aplica descuento
        
        return currentPrice * 0.4 * quantity

# Motor de Precios que aplica las reglas de precios
class MotorDePrecios:
    def __init__(self, rules):
        self.rules = rules

    def calculatePrice(self, product, quantity):
        price = 0.0
        if not self.rules:
            raise ValueError("No hay reglas de precios definidas.")

        for rule in self.rules:
            price = rule.apply(product, quantity, price)
            if price < 0:
                price = 0  # El precio no puede ser negativo
        
        return price


# Main de Prueba
if __name__ == "__main__":
    # Crear Productos
    notebook = Producto("Notebook", 500.0)
    smartphone = Producto("Celular", 300.0)
    tablet = Producto("Tablet", 200.0)

    # Crear Motor de Precios y agregar reglas
    PrecioBase = MotorDePrecios([BasePrice()])
    DosUno = MotorDePrecios([DosPorUno()])
    HappyHourDiscount = MotorDePrecios([HappyHour(14, 17)])
    
    # Calcular precios con diferentes reglas
    print(f"Precio base de {notebook.getName()} (3 unidad): ${PrecioBase.calculatePrice(notebook, 3)}")
    print(f"Precio con 2x1 de {smartphone.getName()} (4 unidades): ${DosUno.calculatePrice(smartphone, 4)}")
    
    # Ejemplo con validacion de error
    try:
        InvalidDiscount = PercentageDiscount(150)  # Esto debería lanzar un error
    except ValueError as e:
        print(f"Error: {e}")