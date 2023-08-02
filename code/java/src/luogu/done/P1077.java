package luogu.done;

import java.util.Scanner;

class P1077 {
    static int N, M;
    static int[] a;
    static int MOD = 1000007;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        M = scanner.nextInt();
        a = new int[N + 1];
        for (int i = 1; i < N + 1; i++) {
            a[i] = scanner.nextInt();
        }
    }

    public static void main(String[] args) {
        input();

//        int[][] dp1 = new int[N + 1][M + 1];
//        dp1[0][0] = 1;
//        for (int i = 1; i < N + 1; i++) {
//            for (int j = 0; j < M + 1; j++) {
//                for (int k = 0; k < Math.min(j, a[i]) + 1; k++) {
//                    dp1[i][j] = (dp1[i][j] + dp1[i - 1][j - k]) % MOD;
//                }
//            }
//        }
//        System.out.print(dp1[N][M]);

        int[] dp2 = new int[M + 1];
        dp2[0] = 1;
        int[] preSum = new int[M + 2];
        for (int i = 1; i < N + 1; i++) {
            preSum[0] = 0;
            for (int j = 0; j < M + 1; j++) {
                preSum[j + 1] = preSum[j] + dp2[j];
            }
            for (int j = M; j > -1; j--) {
                dp2[j] = (preSum[j + 1] - preSum[j - Math.min(j, a[i])]) % MOD;
            }
        }
        System.out.print(dp2[M]);
    }
}

/*
3 5
3 4 4

16
 *//*
33 50
5 0 21 40 13 7 23 7 28 2 8 21 32 45 24 8 33 13 1 33 23 45 17 42 13 20 14 8 49 15 7 37 33

854728
 */
