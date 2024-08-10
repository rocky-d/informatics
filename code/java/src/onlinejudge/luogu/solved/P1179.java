package onlinejudge.luogu.solved;

import java.util.Scanner;

class P1179 {
    static int L, R;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        L = scanner.nextInt();
        R = scanner.nextInt();
    }

    public static void main(String[] args) {
        input();
        int res = 0;
        int num = R;
        while (L <= num) {
            for (char ch : Integer.toString(num).toCharArray()) {
                if (ch == '2') {
                    ++res;
                }
            }
            --num;
        }
        System.out.print(res);
    }
}