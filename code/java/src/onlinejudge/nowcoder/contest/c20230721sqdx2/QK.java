package onlinejudge.nowcoder.contest.c20230721sqdx2;

import java.util.Scanner;

class QK {
    static int n;
    static int[] a, b;
    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        a = new int[n];
        for (int i = 0; i < n; i++) a[i] = scanner.nextInt();
        b = new int[n];
        for (int i = 0; i < n; i++) b[i] = scanner.nextInt();
    }

    public static void main(String[] args) {
        input();
        long[] dp = new long[n];
        dp[0] = 1 == b[0] ? a[0] : 0;
        for (int i = 1; i < n; i++) {
            if (1 == b[i]) {
                if (0 == b[i - 1] && a[i - 1] >= a[i]) {
                    
                }
            } else {

            }
        }
    }
}
