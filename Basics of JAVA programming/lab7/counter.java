public class counter {
    int count;

    public counter(){
        count = 0;
    }

    public void incNr(){
        count++;
    }
    public void decNr() {
        count--;
    }

    public int showCount(){
        return count;
    }

    public static void main(String[] args) {
        counter c = new counter();
        c.incNr();
        c.incNr();
        c.decNr();
        System.out.println(c.showCount());
    }
}
