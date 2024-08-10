package onlinejudge.luogu.solved;

import java.util.Scanner;

class P3842 {
    static int n, n1;
    static int[][] lines;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        n1 = n + 1;
        lines = new int[n1][2];
        for (int i = 1; i < n1; ++i) {
            lines[i][0] = scanner.nextInt();
            lines[i][1] = scanner.nextInt();
        }
    }

    public static void main(String[] args) {
        input();

        int[][] dp = new int[n1][2];
        dp[1][1] = lines[1][1] - 1;
        dp[1][0] = dp[1][1] + lines[1][1] - lines[1][0];

        int line;
        for (int i = 2; i < n1; ++i) {
            line = lines[i][1] - lines[i][0];
            dp[i][0] = Math.min(
                    dp[i - 1][0] + line + Math.abs(lines[i - 1][0] - lines[i][1]),
                    dp[i - 1][1] + line + Math.abs(lines[i - 1][1] - lines[i][1]));
            dp[i][1] = Math.min(
                    dp[i - 1][0] + line + Math.abs(lines[i - 1][0] - lines[i][0]),
                    dp[i - 1][1] + line + Math.abs(lines[i - 1][1] - lines[i][0]));
        }

        System.out.print(Math.min(dp[n][0] - lines[n][0], dp[n][1] - lines[n][1]) + 2 * n - 1);
//        System.out.print(dp[n][1] - lines[n][1] + 2 * n - 1);
    }
}
