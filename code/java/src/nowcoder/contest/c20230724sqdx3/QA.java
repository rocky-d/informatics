package nowcoder.contest.c20230724sqdx3;

import java.util.Scanner;

class QA {
    static String x, y;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        x = scanner.next();
        y = scanner.next();
    }

    public static void main(String[] args) {
        input();
        System.out.print(x.equals("0") ? y.equals("0") ? "0" : "-1" : Math.abs(Long.parseLong(x, 2) - Long.parseLong(y, 2)));
    }
}