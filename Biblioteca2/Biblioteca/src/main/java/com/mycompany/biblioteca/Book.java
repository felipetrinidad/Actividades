/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.biblioteca;

/**
 *
 * @author felip
 */
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class Book {
    private String title;
    private String author;
    private String isbn;
    private Status status;
    private LocalDate dueDate;
    private static double multaDiaria = 10;
    
    public enum Status {
    AVAILABLE,
    BORROWED,
    RESERVED
    }

    
    public Book(String title, String author, String isbn) {  
        if(title.isBlank() || author.isBlank() || isbn.isBlank()){
            throw new IllegalArgumentException("Los campos: Titulo, Autor, ISBN no pueden estar vacios.");
        }
        this.title = title;  
        this.author = author;  
        this.isbn = isbn;  
        this.status = Status.AVAILABLE;
        this.dueDate = null;
    }  

// FALTA: Getters y setters con validaciones
    public String getTitle(){return title;}
    public void setTitle(String title){
        if(title.isBlank()){
            throw new IllegalArgumentException("Este campo no puede estar vacío.");
        }
        this.title = title;
    }
    
    public String getAuthor(){return author;}
    public void setAuthor(String author){
        if(title.isBlank()){
            throw new IllegalArgumentException("Este campo no puede estar vacío.");
        }
        this.author = author;
    }
    
    public String getISBN(){return isbn;}
    public void setISBN(String isbn){
        if(isbn.isBlank()){throw new IllegalArgumentException("Este campo no puede estar vacío.");}
        
        if(isbn.length() != 13){throw new IllegalArgumentException("El ISBN debe ser de 13 digitos.");}
        
        this.isbn = isbn;
    }
    
    public Status getStatus(){return status;}
    
    //Metodo de Reserva
    public void reserve(Status status){
        if(status != Status.AVAILABLE){throw new IllegalArgumentException("El libro seleccionado no se encuentra disponible.");}
        this.status = Status.RESERVED;
    }
    public void cancelReserve(Status status){
        if(status != Status.RESERVED){throw new IllegalArgumentException("Opcion invalida. El libro NO esta reservado");}
        this.status = Status.AVAILABLE;
    }
    
    //Metodo pedir Prestamo
    public void borrow(int dias){
        if(status != Status.AVAILABLE){throw new IllegalArgumentException("Error. Libro no Disponible");}
        if(dias < 0){throw new IllegalArgumentException("Los dias no pueden ser negativos");}
        status = Status.BORROWED;
        dueDate = LocalDate.now().plusDays(dias);
    }
    
    public LocalDate getDueDate(){return dueDate;}
    
    //Metodo para devolver Libro
    public double returnBook() {
        if (status != Status.BORROWED) {
            throw new IllegalStateException("Opcion invalida. Libro no prestado.");
        }
        double multa = 0.0;
        if (LocalDate.now().isAfter(dueDate)) {
            long atraso = ChronoUnit.DAYS.between(dueDate, LocalDate.now());
            multa = atraso * multaDiaria;
        }
        status = Status.AVAILABLE;
        dueDate = null;
        return multa;
    }
}
