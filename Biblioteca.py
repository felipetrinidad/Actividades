from datetime import date

class Book:
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
        self.status = "Disponible"
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
    
    def set_status(self, status: str):
        if status not in ["Disponible", "Prestado"]:
            raise ValueError("Opción inválida. Seleccione Disponible o Prestado.")
        self.status = status
        
    
# Método para prestar libro verificando disponibilidad  
    def borrow_book(self):
        if self.status != "Disponible":
            raise ValueError("El libro no está disponible.")
        self.status = "Prestado"
        self.due_date = date.today()
        
    def return_book(self):
        if self.status != "Prestado":
            raise ValueError("El libro ya está disponible.")
        self.status = "Disponible"
        self.due_date = None
    
    
class User:
    #Atributos    
    def __init__(self, user_id: str, name: str):
        if not user_id.strip():
            raise ValueError("El ID no puede estar vacío.")
        if not name.strip():
            raise ValueError("El nombre no puede estar vacío.")

        self.user_id = user_id
        self.name = name
        self.borrowed_books = []
        
    # Getters y Setters
    def get_user_id(self):
        return self.user_id

    def get_name(self):
        return self.name

    def get_borrowed_books(self):
        return list(self.borrowed_books)

    # Método para tomar prestado un libro con límite de 3
    def borrow_book(self, book: Book):
        if len(self.borrowed_books) >= 3:
            raise ValueError("Límite de libros alcanzado.")
        if book.get_status() != "Disponible":
            raise ValueError("Libro no disponible.")
        book.borrow_book()
        self.borrowed_books.append(book)
    
    #Metodo para devolver libro
    def return_book(self, book: Book):
        if book not in self.borrowed_books:
            raise ValueError("Este usuario no tiene prestado este libro.")
        book.return_book()
        self.borrowed_books.remove(book)
    
class Library:
    # Crear libros
    book1 = Book("Hamlet", "William Shakespeare", "9781234567890")
    book2 = Book("Romeo y Julieta", "William Shakespeare", "9781234567891")

    # Crear usuario
    user = User("U001", "Juan Pérez")

    # Préstamo
    try:
        user.borrow_book(book1)  # prestamos book1
        print("\nLibro prestado:", book1.get_title())  # mostramos book1
        print("Usuario ahora tiene:", len(user.get_borrowed_books()), "libro(s)")
    except Exception as e:
        print("\nError:", e)
