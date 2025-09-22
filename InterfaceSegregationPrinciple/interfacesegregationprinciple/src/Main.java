public class Main {
    public static void main(String[] args) throws Exception {
        Printable basic = new BasicPrinter();
        basic.print("Contrato");

        ScannerFaxPrinter sfp = new ScannerFaxPrinter();
        sfp.print("Factura");
        sfp.scan();
        sfp.fax("123-456");

        ScannerPrinter sp = new ScannerPrinter();
        sp.print("Informe");
        sp.scan();
    }
}
