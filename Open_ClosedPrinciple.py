from abc import ABC, abstractmethod
import math

# Clase abstracta Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
# Clase concreta para Triangulo
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return  self.base * self.height * 0.5
    
# Clase concreta para Circulo
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
# Main de prueba
if __name__ == "__main__":
    Triangle1 = Triangle(10, 5)
    Circle1 = Circle(7)
    
    print("Calculando areas de diferentes formas:\n")
    print(f"Area del Triangulo (Base {Triangle1.base}, Altura {Triangle1.height}): {Triangle1.area()}\n")
    print(f"Area del Circulo (Radio {Circle1.radius}): {Circle1.area():.2f}\n")