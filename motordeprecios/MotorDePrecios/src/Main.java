import java.time.LocalTime;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {
        System.out.println("Iniciando Motor de Precios...\n");

        // Crear productos
        Product notebook = new Product("Notebook", 1000.0);
        Product smartphone = new Product("Smartphone", 800.0);
        Product tablet = new Product("Tablet", 600.0);

        // Crear motor de precios con reglas
        MotorDePrecios base = new MotorDePrecios(List.of(
            new BasePrice()
        ));

        MotorDePrecios _2x1 = new MotorDePrecios(List.of(
            new DosPorUno()
        ));
        
        MotorDePrecios happyHour = new MotorDePrecios(List.of(
            new HappyHour(LocalTime.of(14, 0), LocalTime.of(15, 0))
        ));

        // Calcular precios
        System.out.println("Precio de 3 Notebooks: $" +  base.calculatePrice(notebook, 3) + "\n");
        
        // Ejemplo de 2x1
        System.out.println("Precio de 4 Smartphones (2x1): $" + _2x1.calculatePrice(smartphone, 4) + "\n");

        // Ejemplo de HappyHour
        System.out.println("Precio de 2 Tablets (Happy Hour): $" + happyHour.calculatePrice(tablet, 2) + "\n");
        
       // Ejemplo con validación de error
       try {
            MotorDePrecios motorVacio = new MotorDePrecios(List.of());
            System.out.println("Precio de 1 Notebook (Motor Vacio): $" + motorVacio.calculatePrice(notebook, 1));
        } catch (IllegalStateException e) {
            System.out.println("Error: " + e.getMessage() + "\n");
        }

        System.out.println("\nMotor de Precios finalizado.\n");
    }
}
