package onlinejudge.luogu.solved;

import java.util.Scanner;

class P2392 {
    static final byte NUM = 4;
    static int[] s;
    static int[][] time;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        s = new int[NUM];
        for (byte i = 0; i < NUM; i++) {
            s[i] = scanner.nextInt();
        }
        time = new int[NUM][];
        for (byte i = 0; i < NUM; i++) {
            time[i] = new int[s[i] + 1];
            for (int j = 0; j < s[i]; j++) {
                time[i][s[i]] += time[i][j] = scanner.nextInt();
            }
        }
//        System.out.println(Arrays.toString(s));
//        System.out.println(Arrays.deepToString(time));
    }

    public static void main(String[] args) {
        input();
        int[][] dp = new int[NUM][];
        int res = 0, halfSum, kLow, tmpTime;
        for (byte i = 0; i < NUM; i++) {
            halfSum = time[i][s[i]] / 2;
            dp[i] = new int[1 + halfSum];
            for (int j = 0; j < s[i]; j++) {
                tmpTime = time[i][j];
                kLow = Math.max(0, tmpTime - 1);
                for (int k = halfSum; k > kLow; k--) {
                    dp[i][k] = Math.max(dp[i][k], dp[i][k - tmpTime] + tmpTime);
                }
            }
            res += time[i][s[i]] - dp[i][halfSum];
        }
//        System.out.println(Arrays.deepToString(dp));
        System.out.println(res);
    }
}