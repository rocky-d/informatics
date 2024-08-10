package onlinejudge.luogu.solved;

import java.util.Scanner;

class P2871 {
    private static String mainMethod() {
        Scanner scanner = new Scanner(System.in);

        final short N = scanner.nextShort();
        final short M = scanner.nextShort();
        short[][] bag = new short[N][2];

        for (short i = 0; i < N; ++i) {
            bag[i][0] = scanner.nextShort();
            bag[i][1] = scanner.nextShort();
        }

        int[] dp = new int[1 + M];
        for (short i = 0; i < N; ++i) {
            for (short j = M; j > -1; --j) {
                if (j >= bag[i][0]) {
                    dp[j] = Math.max(dp[j], dp[j - bag[i][0]] + bag[i][1]);
                }
            }
        }

        return String.valueOf(dp[M]);
    }

    public static void main(String[] args) {
        System.out.print(mainMethod());
    }
}
