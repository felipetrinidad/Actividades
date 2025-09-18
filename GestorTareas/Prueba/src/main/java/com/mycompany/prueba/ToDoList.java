/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.prueba;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 *
 * @author felip
 */


public class ToDoList {
    private List<Task> tasks;

    public ToDoList() {
        this.tasks = new ArrayList<>();
    }

    public void addTask(String title, String description) {
        Task task = new Task(title, description);
        tasks.add(task);
    }

    public void markTaskAsDone(int index) {
        if (index < 0 || index >= tasks.size()) {
            throw new IndexOutOfBoundsException("Índice inválido: " + index);
        }
        tasks.get(index).markAsDone();
    }

    public void removeTask(int index) {
        if (index < 0 || index >= tasks.size()) {
            throw new IndexOutOfBoundsException("No existe una tarea en el indice " + index);
        }
        tasks.remove(index);
    }

    public List<String> listTasks() {
        List<String> copy = new ArrayList<>();
        for (int i = 0; i < tasks.size(); i++) {
            copy.add(i + ": " + tasks.get(i).toString());
        }
        return Collections.unmodifiableList(copy); // devuelve lista no modificable
    }

    public boolean isEmpty() {
        return tasks.isEmpty();
    }
}