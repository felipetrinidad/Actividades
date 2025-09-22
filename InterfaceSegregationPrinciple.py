from abc import ABC, abstractmethod

# Interfaces

class Printable(ABC):
    @abstractmethod
    def print(self, content: str):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan(self):
        pass
    
class Faxable(ABC):
    @abstractmethod
    def fax(self, number: str):
        pass
    
    
# Impresora: solo imprime
class BasicPrinter(Printable):
    def print(self, content: str):
        print(f"Imprimiendo: {content}")

# Impresora con escaner
class ScannerPrinter(Printable,Scannable):
    def print(self, content: str):
        print(f"Imprimiendo: {content}")
    
    def scan(self):
        print("Escaneando Documento...")

# Impresora con escaner y fax
class ScannerFaxPrinter(Printable,Scannable,Faxable):
    def print(self, content: str):
        print(f"Imprimiendo: {content}")
    
    def scan(self):
        print("Escaneando Documento...")
    
    def fax(self, number):
        print(f"Enviando fax al numero: {number}")


# Main de Prueba
if __name__ =="__main__":
    basic = BasicPrinter()
    basic.print("Contrato ")
    print("---")
    
    sp = ScannerPrinter()
    sp.print("Informe")
    sp.scan()
    print("---")
    
    sfp = ScannerFaxPrinter()
    sfp.print("Factura")
    sfp.scan()
    sfp.fax("123-456")