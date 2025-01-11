public class egzamin_zad4 {

    class Pojazd {
        private String kolor;
        private int dataProdukcji;

        public Pojazd(String kolor, int dataProdukcji) {
            this.kolor = kolor;
            this.dataProdukcji = dataProdukcji;
        }

        public String getKolor() {
            return kolor;
        }

        public void setKolor(String kolor) {
            this.kolor = kolor;
        }

        public int getDataProdukcji() {
            return dataProdukcji;
        }

        public void setDataProdukcji(int dataProdukcji) {
            this.dataProdukcji = dataProdukcji;
        }

        public void Jazda() {
            System.out.println("Jazda");
        }
    }

    class Rower extends Pojazd {
        private String typRoweru;

        public Rower(String kolor, int dataProdukcji, String typRoweru) {
            super(kolor, dataProdukcji);
            this.typRoweru = typRoweru;
        }

        public String getTypRoweru() {
            return typRoweru;
        }

        public void setTypRoweru(String typRoweru) {
            this.typRoweru = typRoweru;
        }

        public void jazdaBezTrzymanki() {
            System.out.println("Jazda bez trzymanki");
        }
    }

    class Wozkonny extends Pojazd {
        private String typPodwozia;

        public Wozkonny(String kolor, int dataProdukcji, String typPodwozia) {
            super(kolor, dataProdukcji);
            this.typPodwozia = typPodwozia;
        }

        public String getTypPodwozia() {
            return typPodwozia;
        }

        public void setTypPodwozia(String typPodwozia) {
            this.typPodwozia = typPodwozia;
        }

        public void kulig() {
            System.out.println("Kulig");
        }
    }

    class PojazdSilnikowy extends Pojazd {
        private String marka;
        private int predkosc;

        public PojazdSilnikowy(String kolor, int dataProdukcji, String marka, int predkosc) {
            super(kolor, dataProdukcji);
            this.marka = marka;
            this.predkosc = predkosc;
        }

        public String getMarka() {
            return marka;
        }

        public void setMarka(String marka) {
            this.marka = marka;
        }

        public int getPredkosc() {
            return predkosc;
        }

        public void setPredkosc(int predkosc) {
            this.predkosc = predkosc;
        }

        public void ZwiekszPredkosc() {
            predkosc++;
        }
    }

    class Motocykl extends PojazdSilnikowy {

        public Motocykl(String kolor, int dataProdukcji, String marka, int predkosc) {
            super(kolor, dataProdukcji, marka, predkosc);
        }

        public void NaJednymKole() {
            System.out.println("Na jednym kole");
        }
    }

    class Samochod extends PojazdSilnikowy {
        private String typNadwozia;

        public Samochod(String kolor, int dataProdukcji, String marka, int predkosc, String typNadwozia) {
            super(kolor, dataProdukcji, marka, predkosc);
            this.typNadwozia = typNadwozia;
        }
        public String getTypNadwozia() {
            return typNadwozia;
        }

        public void setTypNadwozia(String typNadwozia) {
            this.typNadwozia = typNadwozia;
        }

        public void drifting() {
            System.out.println("Drifting");
        }
    }

    public static void main(String[] args) {
        egzamin_zad4 egzamin = new egzamin_zad4();

        Pojazd pojazd = egzamin.new Pojazd("Czerwony", 2020);
        System.out.println("Kolor pojazdu: " + pojazd.getKolor());
        pojazd.setKolor("Niebieski");
        System.out.println("Zmieniony kolor pojazdu: " + pojazd.getKolor());
        pojazd.Jazda();

        Rower rower = egzamin.new Rower("Zielony", 2018, "Górski");
        System.out.println("Typ roweru: " + rower.getTypRoweru());
        rower.jazdaBezTrzymanki();

        Wozkonny woz = egzamin.new Wozkonny("Brązowy", 2015, "Drewniane");
        System.out.println("Typ podwozia: " + woz.getTypPodwozia());
        woz.kulig();

        PojazdSilnikowy samochod = egzamin.new Samochod("Biały", 2022, "Toyota", 120, "Sedan");
        samochod.ZwiekszPredkosc();
        System.out.println("Prędkość samochodu: " + samochod.getPredkosc());

        Motocykl motocykl = egzamin.new Motocykl("Czarny", 2019, "Yamaha", 150);
        motocykl.NaJednymKole();
    }
}
