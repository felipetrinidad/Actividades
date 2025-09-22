from abc import ABC, abstractmethod

# Sensores
class Sensor(ABC):
    def __init__(self, nombre, umbral):
        self.nombre = nombre
        self.umbral = umbral
        self.lecturas = []
        
    @abstractmethod
    def leer(self):
        pass
    
    def supera_umbral(self, valor):
        return valor > self.umbral, valor

# Sensores Concretos 
class SensorTemperatura(Sensor):
    def __init__(self, nombre, umbral, valorActual=0):
        super().__init__(nombre, umbral)
        self.valorActual = valorActual
    
    def leer(self):
        return self.valorActual

class SensorVibracion(Sensor):
    def __init__(self, nombre, umbral, valorActual=0):
        super().__init__(nombre, umbral)
        self.valorActual = valorActual
    
    def leer(self):
        return self.valorActual

# Sistema de Monitoreo
class CentralAlarma:
    
    def __init__(self):
        self.sensores = []
        self.alertas = []
    
    def agregar_sensor(self, sensor):
        self.sensores.append(sensor)
    
    def quitar_sensor(self, sensor):
        if sensor in self.sensores:
            self.sensores.remove(sensor)
    
    def verificar(self):
        for sensor in self.sensores:
            supera, valor = sensor.supera_umbral(sensor.leer())
            if supera:
                alerta = f"Alerta: {sensor.nombre} superó el umbral con valor {valor}"
                self.alertas.append(alerta)
                print(alerta)

# Main de Pruebas
if __name__ == "__main__":
    central = CentralAlarma()
    
    sensor_temp = SensorTemperatura("Sensor de Temperatura 1", umbral=75, valorActual=80)
    sensor_vib = SensorVibracion("Sensor de Vibración 1", umbral=5, valorActual=3)
    
    central.agregar_sensor(sensor_temp)
    central.agregar_sensor(sensor_vib)
    
    central.verificar()
    
    print("\nActualizando valor del sensor de vibración...\n")
    sensor_vib.valorActual = 6
    
    central.verificar()
    print("\n")