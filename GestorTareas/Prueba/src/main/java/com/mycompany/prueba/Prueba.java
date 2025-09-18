/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.prueba;

import java.util.List;

/**
 *
 * @author felip
 */
public class Prueba {

    public static void main(String[] args) {
        ToDoList todo = new ToDoList();

        // Agregar tareas
        todo.addTask("Estudiar Java", "Repasar conceptos");
        todo.addTask("Hacer ejercicio", "30 minutos de entrenamiento");

        // Listar
        System.out.println("Tareas actuales:");
        System.out.println(todo.listTasks());

        // Marcar como hechas
        todo.markTaskAsDone(0);

        // Intentar marcar otra vez
        try {
            todo.markTaskAsDone(0);
        } catch (Exception e) {
            System.out.println("\nError: " + e.getMessage()+ "\n");
        }

        // Eliminar tarea válida
        todo.removeTask(1);

        // Eliminar tarea inexistente
        try {
            todo.removeTask(5);
        } catch (Exception e) {
            System.out.println("\nError: " + e.getMessage()+ "\n");
        }

        // Listar después de eliminar
        System.out.println("Tareas despues de cambios:");
        System.out.println(todo.listTasks());

    }
}
