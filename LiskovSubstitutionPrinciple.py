from abc import ABC, abstractmethod

# Clase abstracta Ave
class Bird(ABC):
    @abstractmethod
    def eat(self): #Todos los aves comen
        pass
    
# Clase abstracta para Aves que vuelan
class FlyingBird(Bird):
    @abstractmethod
    def fly(self): # No todos los aves vuelan
        pass

# Clase concreta para Ave que vuela
class Sparrow(FlyingBird):
    def eat(self):
        return "El gorrión está comiendo."
    
    def fly(self):
        return "El gorrión está volando."
    
# Clase concreta para Ave que no vuela
class Penguin(Bird):
    def eat(self):
        return "El pingüino está comiendo."
    
# Main de prueba
if __name__ == "__main__":
    sparrow = Sparrow()
    penguin = Penguin()
    
    print(sparrow.eat())
    print(sparrow.fly())
    print("---")
    print(penguin.eat())
