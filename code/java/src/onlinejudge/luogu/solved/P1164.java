package onlinejudge.luogu.solved;

import java.util.Scanner;

class P1164 {
    static int N, M;
    static int[] price;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        M = scanner.nextInt();
        price = new int[N + 1];
        for (int i = 1; i < N + 1; ++i) {
            price[i] = scanner.nextInt();
        }
    }

    public static void main(String[] args) {
        input();
        int[][] dp = new int[N + 1][M + 1];
        dp[0][0] = 1;
        for (int i = 1; i < N + 1; ++i) {
            for (int j = 0; j < M + 1; ++j) {
                if (j > price[i]) {
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - price[i]];
                } else if (j < price[i]) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j] + 1;
                }
            }
        }
        System.out.print(dp[N][M]);
    }
}
