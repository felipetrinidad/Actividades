/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.biblioteca;


/**
 *
 * @author felip
 */
public class Biblioteca {

    public static void main(String[] args) {
        // Crear libros.
        Book book1 = new Book("Hamlet", "William Shakespeare", "9781234567890");
        Book book2 = new Book("Frankestein", "Mary Shelley", "9781234567891");
        Book book3 = new Book("Don Quijote", "Miguel de Cervantes", "9781234567891");
        Book book4 = new Book("Moby Dick", "Herman Melville", "9781234567891");     
        
        // Crear usuario
        User user = new User("U001", "Juan Perez");
        
        // Préstamo
        try {
            user.borrowBook(book1, 3);
            System.out.println("\nLibro prestado: " + book1.getTitle());
            System.out.println(user.getName() + " ahora tiene: " + user.getBorrowedBooks().size() + " libros");
            
        } catch (Exception e) {
            System.out.println("\nError: " + e.getMessage());
        }
        
        try {
            user.borrowBook(book2, 3);
            System.out.println("\nLibro prestado: " + book2.getTitle());
            System.out.println(user.getName() + " ahora tiene: " + user.getBorrowedBooks().size() + " libros");
            
        } catch (Exception e) {
            System.out.println("\nError: " + e.getMessage());
        }
        // Prueba para verificar disponibilidad del libro
        try {
            user.borrowBook(book2, 0);
            System.out.println("\nLibro prestado: " + book2.getTitle());
            System.out.println(user.getName() + " ahora tiene: " + user.getBorrowedBooks().size() + " libros");
            
        } catch (Exception e) {
            System.out.println("\nError: " + e.getMessage());
        }
        
        try {
            user.borrowBook(book3, 5);
            System.out.println("\nLibro prestado: " + book3.getTitle());
            System.out.println(user.getName() + " ahora tiene: " + user.getBorrowedBooks().size() + " libros");
            
        } catch (Exception e) {
            System.out.println("\nError: " + e.getMessage());
        }
        
        // Prueba para verificar limite del usuario
        try {
            user.borrowBook(book2, 1);
            System.out.println("\nLibro prestado: " + book2.getTitle());
            System.out.println(user.getName() + " ahora tiene: " + user.getBorrowedBooks().size() + " libros");
            
        } catch (Exception e) {
            System.out.println("\nError: " + e.getMessage());
        }
        
        // Devolver Libros
        try {
            user.returnBook(book1);
            System.out.println("\nLibro devuelto: " + book1.getTitle());
            System.out.println(user.getName() + " ahora tiene: " + user.getBorrowedBooks().size() + " libros");
            
        } catch (Exception e) {
            System.out.println("\nError: " + e.getMessage());
        }
        // Validacion
        try {
            user.returnBook(book1);
            System.out.println("\nLibro devuelto: " + book1.getTitle());
            System.out.println(user.getName() + " ahora tiene: " + user.getBorrowedBooks().size() + " libros");
            
        } catch (Exception e) {
            System.out.println("\nError: " + e.getMessage());
        }
        
    }
}