from abc import ABC, abstractmethod

# Clase Base Turno

class Turno(ABC):
    def __init__(self, paciente, horaInicio, duracion, precio):
        self.paciente = paciente
        self.horaInicio = horaInicio 
        self.duracion = duracion  
        self.precio = precio
        self.cancelado = False

    
    @property
    def horaFin(self):
        return self.horaInicio + self.duracion
    
    def cancelar(self):
        self.cancelado = True
        print(f"Turno de {self.paciente} a las {self.horaInicio} cancelado.")
    
    def reprogramar(self, nuevaHora):
        self.horaInicio = nuevaHora
        print(f"Turno de {self.paciente} reprogramado de {self.horaInicio} a {nuevaHora}.")
    
    @abstractmethod
    def __str__(self):
        pass
    
# Tipos de Turnos
class Guardia(Turno):
    def __init__(self, paciente, horaInicio):
        super().__init__(paciente, horaInicio, duracion=1, precio=50)  # Duración fija de 1 hora y precio fijo de 50
    
    def __str__(self):
        return f"Turno de Guardia para {self.paciente} a las {self.horaInicio} - Precio: ${self.precio}"

class Practica(Turno):
    def __init__(self, paciente, horaInicio, duracion):
        precio_por_hora = 30
        precio = duracion * precio_por_hora
        super().__init__(paciente, horaInicio, duracion, precio)
    
    def __str__(self):
        return f"Turno de Práctica para {self.paciente} a las {self.horaInicio} por {self.duracion} horas - Precio: ${self.precio}"

class Cirugia(Turno):
    def __init__(self, paciente, horaInicio, duracion):
        precio_por_hora = 100
        precio = duracion * precio_por_hora
        super().__init__(paciente, horaInicio, duracion, precio)
    
    def __str__(self):
        return f"Turno de Cirugía para {self.paciente} a las {self.horaInicio} por {self.duracion} horas - Precio: ${self.precio}"

# Calendario de Turnos
class Calendario:
    def __init__(self):
        self.turnos = []
        
    def agregar_turno(self, turno):
        for i in self.turnos:
            if not i.cancelado and self._solapan(turno, i):
                raise ValueError(f"Solapamiento con turno de {i.paciente} a las {i.horaInicio}hs")
        self.turnos.append(turno)
        print(f"Turno agregado: {turno}")
    
    def _solapan(self, t1, t2):
        return not (t1.horaFin <= t2.horaInicio or t1.horaInicio >= t2.horaFin)
    
    def listar_turnos(self):
        for turno in self.turnos:
            estado = "Cancelado" if turno.cancelado else "Activo"
            print(f"{turno} - Estado: {estado}")
        
            
# Main de Pruebas
if __name__ == "__main__":
    calendario = Calendario()
    
    # Crear turnos
    turno1 = Guardia("Juan Perez", 9)
    turno2 = Practica("Maria Gomez", 10, 2)
    turno3 = Cirugia("Carlos Ruiz", 12, 3)
    
    # Agregar turnos al calendario
    calendario.agregar_turno(turno1)
    calendario.agregar_turno(turno2)
    calendario.agregar_turno(turno3)
    
    print("\n--- Lista de Turnos ---")
    calendario.listar_turnos()
    
    # Reprogramar un turno
    turno2.reprogramar(13)
    
    print("\n--- Lista de Turnos después de reprogramar ---")
    calendario.listar_turnos()
    
    # Cancelar un turno
    turno1.cancelar()
    
    print("\n--- Lista de Turnos después de cancelar ---")
    calendario.listar_turnos() 