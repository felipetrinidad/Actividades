from abc import ABC, abstractmethod


# Estrategia de Descuento

class EstrategiaDescuento(ABC):
    @abstractmethod
    def aplicar(self, items):
        pass


class DescuentoPorcentaje(EstrategiaDescuento):
    def __init__(self, porcentaje):
        self.porcentaje = porcentaje

    def aplicar(self, items):
        subtotal = sum(p["precio"] * p["cantidad"] for p in items)
        return subtotal * (1 - self.porcentaje / 100)


class DescuentoFijo(EstrategiaDescuento):
    def __init__(self, monto):
        self.monto = monto

    def aplicar(self, items):
        subtotal = sum(p["precio"] * p["cantidad"] for p in items)
        return max(0, subtotal - self.monto)


class Lleva2Paga1(EstrategiaDescuento):
    def aplicar(self, items):
        total = 0
        for p in items:
            # cantidad paga = ceil(cantidad / 2)
            cantidad_paga = (p["cantidad"] + 1) // 2
            total += cantidad_paga * p["precio"]
        return total


# Carrito

class Carrito:
    def __init__(self, estrategia: EstrategiaDescuento):
        self.__items = []  # lista interna encapsulada
        self.estrategia = estrategia

    def agregar_item(self, nombre, precio, cantidad=1):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")
        self.__items.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

    def cambiar_estrategia(self, estrategia: EstrategiaDescuento):
        self.estrategia = estrategia

    def subtotal(self):
        return sum(p["precio"] * p["cantidad"] for p in self.__items)

    def total(self):
        return self.estrategia.aplicar(self.__items)

    def desglose(self):
        print("Carrito:")
        for p in self.__items:
            print(f"- {p['nombre']} x{p['cantidad']} = ${p['precio']*p['cantidad']}")
        print(f"Subtotal = ${self.subtotal()}")
        print(f"Total con descuento ({self.estrategia.__class__.__name__}) = ${self.total()}")

# Main de Pruebas
if __name__ == "__main__":
    # Crear carrito con descuento del 10%
    carrito = Carrito(DescuentoPorcentaje(10))
    carrito.agregar_item("Camisa", 50, 2)
    carrito.agregar_item("Pantalón", 80, 1)
    carrito.desglose()

    print("\nCambiando a Descuento Fijo de $30")
    carrito.cambiar_estrategia(DescuentoFijo(30))
    carrito.desglose()

    print("\nCambiando a Lleva 2 Paga 1")
    carrito.cambiar_estrategia(Lleva2Paga1())
    carrito.desglose()