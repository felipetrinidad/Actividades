public class Penguin extends Bird {
    public Penguin(String name) {
        super(name);
    }

    @Override
    public void eat() {
        System.out.println(name + " está comiendo.");
    }
    
}
