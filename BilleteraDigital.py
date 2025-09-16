class Billetera:
    def __init__(self, saldo):
        if saldo < 0:
            raise ValueError("El saldo no puede ser Negativo")
        self.saldo = saldo
    
    def depositar(self, monto):
        if monto < 0: raise ValueError("El monto no puede ser Negativo")
        self.saldo += monto
    
    def retirar(self, monto):
        if monto < 0 or monto > self.saldo: raise ValueError("Monto Invalido.")
        self.saldo -= monto
    
    def verSaldo(self):
        return self.saldo

if __name__ == "__main__":
    billetera1 = Billetera(0)
    print(f"Billetera con saldo inicial: {billetera1.verSaldo()}")
    
    try:
        billetera1.depositar(350)
        print(f"\nSaldo: {billetera1.verSaldo()}")
    except Exception as e:
        print(f"\nError: {e}")
    
    try:
        billetera1.retirar(50)
        print(f"\nSaldo: {billetera1.verSaldo()}")
    except Exception as e:
        print(f"\nError: {e}")