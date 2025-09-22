public class Sparrow extends Bird implements FlyingBird {
    public Sparrow(String name) {
        super(name);
    }

    @Override
    public void eat() {
        System.out.println(name + " está comiendo.");
    }

    @Override
    public void fly() {
        System.out.println(name + " está volando.");
    }
    
}
