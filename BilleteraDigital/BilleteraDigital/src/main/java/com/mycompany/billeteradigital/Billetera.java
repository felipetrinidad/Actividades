/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.billeteradigital;

/**
 *
 * @author felip
 */
public class Billetera {
    private double saldo;
    
    // Constructor
    public Billetera(double saldoInicial) {
        if (saldoInicial < 0) {
            throw new IllegalArgumentException("El saldo inicial no puede ser negativo");
        }
        this.saldo = saldoInicial;
    }
    
    //depositar dinero
    public void depositar(double monto){
        if (monto < 0) {throw new IllegalArgumentException("El monto no puede ser negativo");}
        this.saldo += monto;
    }
    
    //retirar dinero
    public void retirar(double monto){
        if (monto < 0) {throw new IllegalArgumentException("El monto no puede ser negativo");}
         if (monto > saldo) {throw new IllegalArgumentException("Monto superior al saldo.");}
        this.saldo -= monto;
    }
    
    //ver saldo actual
    public double verSaldo(){return saldo;}
}
