package onlinejudge.luogu.solved;

import java.util.Scanner;

class P1510 {
    static int v, n, c;
    static int[][] arrKM;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        v = scanner.nextInt();
        n = scanner.nextInt();
        c = scanner.nextInt();

        arrKM = new int[n][2];
        for (int i = 0; i < n; i++) {
            arrKM[i][0] = scanner.nextInt();
            arrKM[i][1] = scanner.nextInt();
        }
    }

    public static void main(String[] args) {
        input();
        int[] dp = new int[1 + c];
        for (int[] km : arrKM) {
            for (int j = c; j >= km[1]; j--) {
                dp[j] = Math.max(dp[j], dp[j - km[1]] + km[0]);
            }
        }

        if (v > dp[c]) {
            System.out.println("Impossible");
        } else {
            for (int j = c; j > 0; j--) {
                if (v > dp[j]) {
                    System.out.println(c - j - 1);
                    break;
                }
            }
        }
    }
}