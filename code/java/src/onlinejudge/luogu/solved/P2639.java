package onlinejudge.luogu.solved;

import java.util.Scanner;

class P2639 {
    static int h, n;
    static int[] s;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        h = scanner.nextInt();
        n = scanner.nextInt();
        s = new int[n];
        for (int i = 0; i < n; i++) {
            s[i] = scanner.nextInt();
        }
    }

    public static void main(String[] args) {
        input();
        int[] dp = new int[1 + h];
        for (int si : s) {
            for (int j = h; j >= si; j--) {
                dp[j] = Math.max(dp[j], dp[j - si] + si);
            }
        }
        System.out.println(dp[h]);
    }
}