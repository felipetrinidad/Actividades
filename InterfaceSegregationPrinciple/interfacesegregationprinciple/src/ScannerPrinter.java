public class ScannerPrinter implements Printable, Scannable {
    @Override
    public void print(String content){
        System.out.println("Imprimiendo: " + content);
    }

    @Override
    public void scan(){
        System.out.println("Escaneando...");
    }
}
