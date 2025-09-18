from datetime import datetime, timedelta

class Task:
#Constructor
    def __init__(self, title, description):
        if not title:
            raise ValueError("El título no puede estar vacío.")
        if not description:
            raise ValueError("La descripción no puede estar vacía.")
        self.title = title
        self.description = description
        self.done = False
    
#Getters
    def getTitle(self):
        return self.title
    
    def getDescription(self):
        return self.description
    
    def isDone(self):
        return self.done
    
    def markAsDone(self):
        if self.done:
            raise ValueError("La tarea ya está marcada como hecha.")
        self.done = True
    
    def __str__(self):
        status = "Hecha" if self.done else "Pendiente"
        return f"Tarea: {self.title}\nDescripción: {self.description}\nEstado: {status}"
    
class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def addTask(self, task):
        task = Task(task['Titulo'], task['Descripcion'])
        self.tasks.append(task)
        
    def markTaskAsDone(self, index):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Índice de tarea inválido.")
        self.tasks[index].markAsDone()
    
    def removeTask(self, index):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Índice de tarea inválido.")
        del self.tasks[index]
    
    def listTasks(self):
        if not self.tasks:
            print("No hay tareas en la lista.")
            return
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}\n")

# Main de Prueba
if __name__ == "__main__":
    # Se crea una instancia de ToDoList
    todo = ToDoList()
    
    # Se agregan tareas
    todo.addTask({'Titulo': 'Comprar comestibles', 'Descripcion': 'Chocolate, Alfajores'})
    todo.addTask({'Titulo': 'Estudiar', 'Descripcion': 'Repasar para el examen de matemáticas'})
    
    # Mostrar todas las tareas
    print("Tareas Iniciales:")
    todo.listTasks()
    
    # Marcar la primera tarea como hecha
    todo.markTaskAsDone(0)
    
    # Intentar marcar la misma tarea como hecha nuevamente para probar la excepción
    try:
        todo.markTaskAsDone(0)
    except ValueError as e:
        print(f"Error: {e}")
    
    # Elminar la segunda tarea
    todo.removeTask(1)
    
    # Elminar tarea inexistente
    try:
        todo.removeTask(5)  # Índice inválido
    except IndexError as e:
        print(f"Error: {e}")
        
    # Mostrar todas las tareas después de las modificaciones
    print("\nTareas después de las modificaciones:")
    todo.listTasks()