package luogu.contest.c20230731icpc;

import java.util.Scanner;

class QBP5707 {
    static int s, v;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        s = scanner.nextInt();
        v = scanner.nextInt();
    }

    public static void main(String[] args) {
        input();

        double t = 10 + (double) s / v;
        int hh = (int) t / 60;
        int mm = (int) Math.ceil(t % 60);

        System.out.println(mm == 0 ? String.format("%02d", (32 - hh) % 24) + ":00" : String.format("%02d", (31 - hh) % 24) + ":" + String.format("%02d", 60 - mm));
    }
}