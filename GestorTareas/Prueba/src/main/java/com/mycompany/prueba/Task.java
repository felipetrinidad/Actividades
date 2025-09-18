/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.prueba;

/**
 *
 * @author felip
 */
public class Task {
    private String title;
    private String description;
    private boolean done;

    public Task(String title, String description) {
        if (title == null || title.trim().isEmpty()) {
            throw new IllegalArgumentException("El título no puede estar vacío.");
        }
        this.title = title;
        this.description = description == null ? "" : description;
        this.done = false;
    }

    public String getTitle() {
        return title;
    }

    public String getDescription() {
        return description;
    }

    public boolean isDone() {
        return done;
    }

    public void markAsDone() {
        if (done) {
            throw new IllegalStateException("La tarea ya esta marcada como hecha.");
        }
        this.done = true;
    }

    @Override
    public String toString() {
        return "[ Hecho: " + (done ? " Si" : "No") + " ] " + title + " - " + description;
    }
}
