from datetime import date, timedelta
from enum import Enum

class Status(Enum):
    AVAILABLE = 1
    BORROWED = 2
    RESERVED = 3

class Book:
    multa_diaria = 10
    
    def __init__(self, title, author, isbn):
        if not title:
            raise ValueError("El titulo no puede estar vacio.")
        if not author:
            raise ValueError("El autor no puede estar vacio.")
        if not isbn or len(isbn) != 13:
            raise ValueError("ISBN invalido.")
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = Status.AVAILABLE
        self.due_date = None

# Getters y setters
    def get_title(self):
        return self.title
    
    def set_title(self, title: str):
        if not title.strip():
            raise ValueError("Este campo no puede estar vacío.")
        self.title = title
        
    def get_author(self):
        return self.author
    
    def set_author(self, author: str):
        if not author.strip():
            raise ValueError("Este campo no puede estar vacío.")
        self.author = author
        
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, isbn: str):
        if not isbn.strip() or len(isbn) != 13:
            raise ValueError("El ISBN debe ser de 13 dígitos.")
        self.isbn = isbn
        
    def get_status(self):
        return self.status

# Método de Reserva
    def reserve(self):
        if self.status != Status.AVAILABLE:
            raise ValueError("Libro NO Disponible")
        self.status = Status.RESERVED
        
    def cancel_reserve(self):
        if self.status != Status.RESERVED:
            raise ValueError("Opcion Invalida. Libro NO Reservado")
        self.status = Status.AVAILABLE
        
    
# Método para prestar  
    def borrow(self, dias):
        if self.status != Status.AVAILABLE:
            raise ValueError("El libro no está disponible.")
        self.status = Status.BORROWED
        self.due_date = date.today() + timedelta(days=dias)
        
    def return_book(self):
        if self.status != Status.BORROWED:
            raise ValueError("Opcion Invalida. Libro Disponible.")
        multa = 0
        atraso = 0
        if date.today() > self.due_date:
            atraso = (date.today() - self.due_date).days
        
        multa = atraso * Book.multa_diaria
        
        self.status = Status.AVAILABLE
        self.due_date = None
        return multa
    
    
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []
    
    # Getters y Setters
    def get_user_id(self):
        return self.user_id
    
    def set_user_id(self, user_id):
        if not user_id:
            raise ValueError("Este campo no puede estar vacío.")
        self.user_id = user_id
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        if not name:
            raise ValueError("Este campo no puede estar vacío.")
        self.name = name
    
    def get_borrowed_books(self):
        return self.borrowed_books.copy()
    
    # Método para Préstamo de Libro
    def borrow_book(self, book, dias):
        if len(self.borrowed_books) >= 3:
            raise ValueError("Límite de Libros Alcanzados.")
        book.borrow(dias)
        self.borrowed_books.append(book)
    
    # Método para devolver Libro
    def return_book(self, book):
        if book not in self.borrowed_books:
            raise ValueError("Este usuario no tiene prestado este libro")
        multa = book.return_book()
        self.borrowed_books.remove(book)
        print(f"Multa por devolución: ${multa}")
    
    
def main():
    # Crear libros
    book1 = Book("Hamlet", "William Shakespeare", "9781234567890")
    book2 = Book("Frankestein", "Mary Shelley", "9781234567891")
    book3 = Book("Don Quijote", "Miguel de Cervantes", "9781234567891")
    book4 = Book("Moby Dick", "Herman Melville", "9781234567891")
    
    # Crear usuario
    user = User("U001", "Juan Perez")
    
    # Préstamo
    try:
        user.borrow_book(book1, 3)
        print(f"\nLibro prestado: {book1.get_title()}")
        print(f"{user.get_name()} ahora tiene: {len(user.get_borrowed_books())} libros")
    except Exception as e:
        print(f"\nError: {e}")
    
    try:
        user.borrow_book(book2, 3)
        print(f"\nLibro prestado: {book2.get_title()}")
        print(f"{user.get_name()} ahora tiene: {len(user.get_borrowed_books())} libros")
    except Exception as e:
        print(f"\nError: {e}")
    
    # Prueba para verificar disponibilidad del libro
    try:
        user.borrow_book(book2, 0)
        print(f"\nLibro prestado: {book2.get_title()}")
        print(f"{user.get_name()} ahora tiene: {len(user.get_borrowed_books())} libros")
    except Exception as e:
        print(f"\nError: {e}")
    
    try:
        user.borrow_book(book3, 5)
        print(f"\nLibro prestado: {book3.get_title()}")
        print(f"{user.get_name()} ahora tiene: {len(user.get_borrowed_books())} libros")
    except Exception as e:
        print(f"\nError: {e}")
    
    # Prueba para verificar limite del usuario
    try:
        user.borrow_book(book4, 1)
        print(f"\nLibro prestado: {book4.get_title()}")
        print(f"{user.get_name()} ahora tiene: {len(user.get_borrowed_books())} libros")
    except Exception as e:
        print(f"\nError: {e}")
    
    # Devolver Libros
    try:
        user.return_book(book1)
        print(f"\nLibro devuelto: {book1.get_title()}")
        print(f"{user.get_name()} ahora tiene: {len(user.get_borrowed_books())} libros")
    except Exception as e:
        print(f"\nError: {e}")
    
    # Validación
    try:
        user.return_book(book1)
        print(f"\nLibro devuelto: {book1.get_title()}")
        print(f"{user.get_name()} ahora tiene: {len(user.get_borrowed_books())} libros")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()