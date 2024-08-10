package onlinejudge.luogu.solved;

import java.util.Scanner;

class P2925 {
    static int c, h;
    static int[] v;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        c = scanner.nextInt();
        h = scanner.nextInt();
        v = new int[h];
        for (int i = 0; i < h; i++) {
            v[i] = scanner.nextInt();
        }
    }

    public static void main(String[] args) {
        input();
        int[] dp = new int[1 + c];
        for (int vi : v) {
            for (int j = c; j >= vi; j--) {
                dp[j] = Math.max(dp[j], dp[j - vi] + vi);
            }
        }
        System.out.println(dp[c]);
    }
}
