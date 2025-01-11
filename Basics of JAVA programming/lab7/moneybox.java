public class moneybox {
    public int money = 0;

    public void AddMoney(int a){
        money += a;
    }

    public int BreakMoneyBox(){
        int tmb = money;
        money = 0;
        return tmb;
    }

    public moneybox(){
        money = 0;
    }

    public static void main(String[] args) {
        moneybox mb = new moneybox();
        mb.AddMoney(200);
        System.out.println(mb.BreakMoneyBox());
    }
}
