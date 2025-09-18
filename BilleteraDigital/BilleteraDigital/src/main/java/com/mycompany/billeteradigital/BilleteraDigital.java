/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.billeteradigital;

/**
 *
 * @author felip
 */
public class BilleteraDigital {

    public static void main(String[] args) {
        // Billetera con saldo inicial menor a 0
        try{
            Billetera billetera1 = new Billetera(-5);
            System.out.println("\nSaldo: " + billetera1.verSaldo());
        } catch (Exception e) {
            System.out.println("\nError: " + e.getMessage() + "\n");
        }
        
        //Billetera con saldo inicial valido
        Billetera billetera1 = new Billetera(0);
        System.out.println("Billetera con saldo inicial: " + billetera1.verSaldo());
        
        //Deposito
        try{
            billetera1.depositar(350);
            System.out.println("Depositando...\n"+"Saldo: " + billetera1.verSaldo());
        } catch (Exception e) {
            System.out.println("\nError: " + e.getMessage());
        }
        //Deposito invalido
        try{
            billetera1.depositar(-350);
            System.out.println("Depositando...\n"+"Saldo: " + billetera1.verSaldo());
        } catch (Exception e) {
            System.out.println("\nError: " + e.getMessage());
        }
        
        //Retirar
        try{
            billetera1.retirar(50);
            System.out.println("\nRetirando Dinero..." + "\nSaldo Actual: " + billetera1.verSaldo());
        } catch (Exception e) {
            System.out.println("\nError: " + e.getMessage());
        }
        
        //Retiro Invalido
        try{
            billetera1.retirar(350);
            System.out.println("\nRetirando Dinero..." + "\nSaldo Actual: " + billetera1.verSaldo());
        } catch (Exception e) {
            System.out.println("\nError: " + e.getMessage());
        }
    }
}
