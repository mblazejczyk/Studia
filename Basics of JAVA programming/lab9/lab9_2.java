public class lab9_2 {
    abstract class Istota{
        private int energia;
        private int wiek;
        public void chodzenie(){ System.out.println("chodzenie");}
        public Istota(int e, int w){
            energia = e;
            wiek = w;
        }
    }

    class Ogr extends Istota{
        private int poziomAgrasji;
        public void strzelanieZProcy(){System.out.println("Strzał");}
        public void atakSierpa(){System.out.println("Atak!");}

        public Ogr(int _poziomAgrasji, int e, int w){
            super(e, w);
            poziomAgrasji = _poziomAgrasji;
        }
    }

    class TrollJaskiniowy extends Istota{
        private int wytrzymalosc;
        public void rzucKamien(){System.out.println("Rzut!");}
        public void uderzKolczastaMaczuga(){System.out.println("Uderzenie!");}

        public TrollJaskiniowy(int _w, int e, int w){
            super(e, w);
            wytrzymalosc = _w;
        }
    }

    abstract class IstotaGrywalna extends Istota{
        private int szybkosc;
        public void odpoczywanie(){System.out.println("Odpoczynek");}
        public void bieganie(){System.out.println("Bieg");}

        public IstotaGrywalna(int s, int e, int w){
            super(e, w);
            szybkosc = s;
        }
    }

    class Rycerz extends IstotaGrywalna{
        private int wytrzymalosc;
        public void atakMieczem(){System.out.println("Atak!");}
        public void uderzenieTarcza(){System.out.println("Uderzenie!");}
        public void obronaTarcza(){System.out.println("Obrona");}

        public Rycerz(int w, int s, int e, int _wiek){
            super(s, e, _wiek);
            wytrzymalosc = w;
        }
    }

    class Łucznik extends IstotaGrywalna{
        private int zasięg;
        public void strzalZLuku(){System.out.println("Strzał!");}
        public void atakSztyletem(){System.out.println("Atak!");}
        public void skradadnieSie(){System.out.println("Skradanie");}

        public Łucznik(int z, int s, int e, int _wiek){
            super(s, e, _wiek);
            zasięg = z;
        }
    }

    class Czarodziej extends IstotaGrywalna{
        private int moc;
        private void alchemia(){System.out.println("Alchemia!");}
        public void rzucCzar(){System.out.println("Czar!");}
        public void atakujMagicznymKosturem(){System.out.println("Atak!");}

        public Czarodziej(int m, int s, int e, int _wiek){
            super(s, e, _wiek);
            moc = m;
        }
    }

    public static void main(String[] args) {
        lab9_2 program = new lab9_2();

        Ogr ogr = program.new Ogr(5, 100, 30);
        ogr.chodzenie();
        ogr.strzelanieZProcy();
        ogr.atakSierpa();

        TrollJaskiniowy troll = program.new TrollJaskiniowy(10, 120, 25);
        troll.chodzenie();
        troll.rzucKamien();
        troll.uderzKolczastaMaczuga();

        Rycerz rycerz = program.new Rycerz(15, 8, 90, 40);
        rycerz.chodzenie();
        rycerz.odpoczywanie();
        rycerz.bieganie();
        rycerz.atakMieczem();
        rycerz.uderzenieTarcza();
        rycerz.obronaTarcza();

        Łucznik lucznik = program.new Łucznik(20, 7, 85, 35);
        lucznik.chodzenie();
        lucznik.odpoczywanie();
        lucznik.bieganie();
        lucznik.strzalZLuku();
        lucznik.atakSztyletem();
        lucznik.skradadnieSie();

        Czarodziej czarodziej = program.new Czarodziej(50, 6, 80, 50);
        czarodziej.chodzenie();
        czarodziej.odpoczywanie();
        czarodziej.bieganie();
        czarodziej.rzucCzar();
        czarodziej.atakujMagicznymKosturem();
        // czarodziej.alchemia(); // Metoda prywatna, nie można jej wywołać spoza klasy.
    }
}
