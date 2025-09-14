class Motor:
    def __init__(self, numero_serie, cilindrada, tipo):
        self.numero_serie = numero_serie
        self.cilindrada = cilindrada
        self.tipo = tipo

class Coche:
    contador_coches = 0
    
    def __init__(self, marca, modelo, año, precio, motor):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
        self.vendido = False
        self.motor = motor
        self.numero_chasis = Coche.contador_coches
        Coche.contador_coches += 1
    
    def calcular_impuesto(self):
        return (5 * self.precio) / 100
    
    def mostrar_info(self):
        print(f"Informacion del Coche:\nMarca: {self.marca}, Modelo: {self.modelo}")
        print(f"Año: {self.año}, Precio: {self.precio}, Impuestos: {self.calcular_impuesto()}")
        print(f"Estado: {self.estado()}")
        print(f"Motor: {self.motor.numero_serie}, Cilindrada: {self.motor.cilindrada}, Tipo: {self.motor.tipo}")
        print(f"Chasis: {self.numero_chasis}\n")
    
    def vender(self):
        self.vendido = True
        print(f"\nEl coche {self.marca} {self.modelo} se ha vendido.\n")
    
    def estado(self):
        return "Disponible" if not self.vendido else "Vendido"
    
    @classmethod
    def get_total_coches(cls):
        return cls.contador_coches

# Main
if __name__ == "__main__":
    m1 = Motor("021D3221A965", 170, "Gasolina")
    m2 = Motor("213G7676K254", 109, "Gasolina")
    
    toyota = Coche("Toyota", "Corolla", "2025", 30000, m1)
    fiat = Coche("Fiat", "Cronos", "2025", 20000, m2)
    
    toyota.calcular_impuesto()
    toyota.vender()
    toyota.mostrar_info()
    
    fiat.calcular_impuesto()
    fiat.mostrar_info()
    
    print(f"Total de coches creados: {Coche.get_total_coches()}")