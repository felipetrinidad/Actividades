/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.biblioteca;

import com.mycompany.biblioteca.Book.Status;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author felip
 */
public class User {
    private String userId;
    private String name;
    private List<Book> borrowedBooks;
    
    public User(String userId, String name) {
        this.userId = userId;
        this.name = name;
        this.borrowedBooks = new ArrayList<>();
    }
    
    //Getters y Setters
    public String getUserId(){return userId;}
    public void setUserId(String UserId){if(userId.isBlank()){throw new IllegalArgumentException("Este campo no puede estar vacío.");}}
    
    public String getName(){return name;}
    public void setName(String name){if(name.isBlank()){throw new IllegalArgumentException("Este campo no puede estar vacío.");}}
    
    public List<Book> getBorrowedBooks(){return new ArrayList<>(borrowedBooks);}
      
    //Metodo para Prestamo de Libro
    public void borrowBook(Book book, int dias){
        if(borrowedBooks.size()>=3){throw new IllegalArgumentException("Limite de Libros Alcanzados.");}
        book.borrow(dias);
        borrowedBooks.add(book);
    }
     
    // Metodo para devolver Libro
    public void returnBook(Book book) {
        if (!borrowedBooks.contains(book)) {throw new IllegalArgumentException("Este usuario no tiene prestado este libro");}
        double multa = book.returnBook();
        borrowedBooks.remove(book);
        System.out.println("Multa por devolucion: $" + multa);
    }
    
    
}
