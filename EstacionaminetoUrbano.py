from abc import ABC, abstractmethod

# Vehiculos
class Vehiculo(ABC):
    def __init__(self, patente):
        self.patente = patente
    
    @abstractmethod
    def getTipo(self):
        pass

# Tipos de Vehiculos
class Auto(Vehiculo):
    def getTipo(self):
        return "Auto"

class Moto(Vehiculo):
    def getTipo(self):
        return "Moto"
    
class Camion(Vehiculo):
    def getTipo(self):
        return "Camion"



# Tarifas
class Tarifa(ABC):
    @abstractmethod
    def calcular(self, horas):
        pass
    
    
class TarifaAuto(Tarifa):
    tarifa_hora = 50  

    def calcular(self, horas):
        return horas * self.tarifa_hora

class TarifaMoto(Tarifa):
    tarifa_hora = 25 

    def calcular(self, horas):
        return horas * self.tarifa_hora

class TarifaCamion(Tarifa):
    tarifa_hora = 100  

    def calcular(self, horas):
        return horas * self.tarifa_hora

# Estacionamiento
class Estacionamiento:
    def __init__(self):
        self.recaudacion = 0
        self.vehiculos = {}
        self.tarifas = {
            "Auto": TarifaAuto(),
            "Moto": TarifaMoto(),
            "Camion": TarifaCamion()
        }
    
    def ingresar_vehiculo(self, vehiculo: Vehiculo, hora_ingreso):
        if vehiculo.patente in self.vehiculos:
            raise ValueError("El vehículo ya está en el estacionamiento.")
        self.vehiculos[vehiculo.patente] = (vehiculo, hora_ingreso)
    
    def retirar_vehiculo(self, patente, hora_salida):
        if patente not in self.vehiculos:
            raise ValueError("El vehículo no está en el estacionamiento.")
        
        vehiculo, hora_ingreso = self.vehiculos.pop(patente)
        horas_estacionado = (hora_salida - hora_ingreso)
        horas_estacionado = max(1, int(horas_estacionado))  # Cobrar al menos 1 hora
        
        tarifa = self.tarifas[vehiculo.getTipo()]
        costo = tarifa.calcular(horas_estacionado)
        self.recaudacion += costo
        
        return costo
    
    def getVehiculosEstacionados(self):
        return list(self.vehiculos.keys())
    
    def getRecaudacion(self):
        return self.recaudacion

# Main de Pruebas
if __name__ == "__main__":
    estacionamiento = Estacionamiento()

    # Ingresar vehículos
    auto1 = Auto("ABC123")
    moto1 = Moto("MOT456")
    camion1 = Camion("CAM789")

    estacionamiento.ingresar_vehiculo(auto1, 12)
    estacionamiento.ingresar_vehiculo(moto1, 16)
    estacionamiento.ingresar_vehiculo(camion1, 10)

    print("\nVehículos estacionados:", estacionamiento.getVehiculosEstacionados(), "\n")

    # Retirar vehículos
    costo_auto = estacionamiento.retirar_vehiculo("ABC123", 18)
    print(f"Costo por retirar auto ABC123: ${costo_auto}")

    costo_moto = estacionamiento.retirar_vehiculo("MOT456", 20)
    print(f"Costo por retirar moto MOTO456: ${costo_moto}")

    costo_camion = estacionamiento.retirar_vehiculo("CAM789", 15)
    print(f"Costo por retirar camión CAM789: ${costo_camion}")

    print("\nRecaudación total del estacionamiento:", estacionamiento.getRecaudacion())