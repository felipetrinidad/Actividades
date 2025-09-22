public class ScannerFaxPrinter implements Printable, Scannable, Faxable{
    @Override
    public void print(String content){
        System.out.println("Imprimiendo: " + content);
    }

    @Override
    public void scan(){
        System.out.println("Escaneando...");
    }

    @Override
    public void fax(String number){
        System.out.println("Enviando fax al numero: " + number);
    }

}
