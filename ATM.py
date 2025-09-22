from abc import ABC, abstractmethod
from datetime import datetime


# Divisas

class Divisa(ABC):
    @abstractmethod
    def convertir(self, monto, divisa):
        pass

    @abstractmethod
    def simbolo(self):
        pass


class Peso(Divisa):
    tasa_dolar = 1000  # Ejemplo: 1 USD = 1000 ARS

    def convertir(self, monto, divisa):
        if isinstance(divisa, Peso):
            return monto
        elif isinstance(divisa, Dolar):
            return monto / Peso.tasa_dolar
        else:
            raise ValueError("Divisa desconocida")

    def simbolo(self):
        return "ARS"


class Dolar(Divisa):
    tasa_peso = 1000  # Ejemplo: 1 USD = 1000 ARS

    def convertir(self, monto, a_divisa):
        if isinstance(a_divisa, Dolar):
            return monto
        elif isinstance(a_divisa, Peso):
            return monto * Dolar.tasa_peso
        else:
            raise ValueError("Divisa desconocida")

    def simbolo(self):
        return "USD"



# Movimiento

class Movimiento:
    def __init__(self, tipo, monto, divisa):
        self.fecha = datetime.now()
        self.tipo = tipo
        self.monto = monto
        self.divisa = divisa

    def __str__(self):
        return f"{self.fecha:%Y-%m-%d %H:%M:%S} - {self.tipo}: {self.monto:.2f} {self.divisa.simbolo()}"



# Cuenta

class Cuenta:
    def __init__(self, divisa: Divisa):
        self._saldo = 0.0
        self.divisa = divisa
        self.movimientos = []

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El depósito debe ser mayor a 0")
        self._saldo += monto
        self.movimientos.append(Movimiento("Depósito", monto, self.divisa))

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El retiro debe ser mayor a 0")
        if monto > self._saldo:
            raise ValueError("Fondos insuficientes: no se permite saldo negativo")
        self._saldo -= monto
        self.movimientos.append(Movimiento("Retiro", monto, self.divisa))

    def saldo(self, en_divisa=None):
        en_divisa = en_divisa or self.divisa
        return self.divisa.convertir(self._saldo, en_divisa)

    def ver_extracto(self):
        return [str(mov) for mov in self.movimientos]



# Cliente

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []

    # Se asocia una cuenta al cliente
    def agregar_cuenta(self, cuenta: Cuenta):
        self.cuentas.append(cuenta)


# Main de pruebas

if __name__ == "__main__":
    # Divisas
    peso = Peso()
    dolar = Dolar()

    # Crear cuenta en pesos
    cuenta = Cuenta(peso)
    cuenta.depositar(5000)

    # Conversión de saldo
    saldo_usd = cuenta.saldo(dolar)

    # Cliente
    cliente = Cliente("Ana")
    cliente.agregar_cuenta(peso)
    cliente.agregar_cuenta(dolar)
    
    # Retiro en pesos
    cuenta.retirar(500)

    print("\n--- Extracto cuenta en pesos ---")
    for linea in cuenta.ver_extracto():
        print(linea)

    print("\nSaldo en USD mostrado desde cuenta en pesos:", cuenta.saldo(Dolar()))


    # No permitir saldo negativo
    try:
        cuenta.retirar(10000)
    except ValueError as e:
        print("\nError:", e)