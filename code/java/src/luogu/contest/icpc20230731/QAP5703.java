package luogu.contest.icpc20230731;

import java.util.Scanner;

class QAP5703 {
    static int a, b;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        a = scanner.nextInt();
        b = scanner.nextInt();
    }

    public static void main(String[] args) {
        input();
        System.out.println(a * b);
    }
}