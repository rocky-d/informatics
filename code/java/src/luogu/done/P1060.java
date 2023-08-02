package luogu.done;

import java.util.Scanner;

class P1060 {
    static int n, m;
    static int[][] vp;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        m = scanner.nextInt();
        vp = new int[m][2];
        for (int i = 0; i < m; i++) {
            vp[i][0] = scanner.nextInt();
            vp[i][1] = scanner.nextInt();
        }
    }

    public static void main(String[] args) {
        input();
        int[] dp = new int[1 + n];
        for (int[] vpi : vp) {
            for (int j = n; j >= vpi[0]; j--) {
                dp[j] = Math.max(dp[j], dp[j - vpi[0]] + vpi[0] * vpi[1]);
            }
        }
        System.out.println(dp[n]);
    }
}