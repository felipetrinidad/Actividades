public class Main {
    public static void main(String[] args) throws Exception {
        Bird sparrow = new Sparrow("Gorrión");
        Bird penguin = new Penguin("Pingüino");
        
        
        sparrow.eat();
        ((FlyingBird) sparrow).fly();
        
        System.out.println("---");
        penguin.eat();
    }
}
