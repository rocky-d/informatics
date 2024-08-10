package onlinejudge.nowcoder.contest.c20230723nkzs4;

import java.util.Scanner;

class Q1 {
    static int n, k;
    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        k = scanner.nextInt();
    }

    public static void main(String[] args) {
        input();
        if (n < 3* k) {
            System.out.print(-1);
            return;
        }
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < k; i++) {
            res.append("you");
        }
        for (int i = 0; i < n - 3 * k; i++) {
            res.append("y");
        }
        System.out.print(res);
    }
}