package luogu.done;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

class P1434 {
    private static String mainMethod() {
        Scanner scanner = new Scanner(System.in);

        final byte R = scanner.nextByte();
        final byte C = scanner.nextByte();
        int[][] table = new int[R][C];
        PriorityQueue<int[]> priorityQueue = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        for (byte i = 0; i < R; ++i) {
            for (byte j = 0; j < C; ++j) {
                table[i][j] = scanner.nextInt();
                priorityQueue.offer(new int[]{table[i][j], i, j});
            }
        }

        int[][] dp = new int[R][C];
        int res = 0;
        while (!priorityQueue.isEmpty()) {
            int[] node = priorityQueue.poll();
            int num = node[0];
            int nodeI = node[1];
            int nodeJ = node[2];
            dp[nodeI][nodeJ] = 1;
            if (nodeI > 0 && num > table[nodeI - 1][nodeJ]) {
                dp[nodeI][nodeJ] = Math.max(dp[nodeI][nodeJ], 1 + dp[nodeI - 1][nodeJ]);
            }
            if (nodeJ > 0 && num > table[nodeI][nodeJ - 1]) {
                dp[nodeI][nodeJ] = Math.max(dp[nodeI][nodeJ], 1 + dp[nodeI][nodeJ - 1]);
            }
            if (nodeI < R - 1 && num > table[nodeI + 1][nodeJ]) {
                dp[nodeI][nodeJ] = Math.max(dp[nodeI][nodeJ], 1 + dp[nodeI + 1][nodeJ]);
            }
            if (nodeJ < C - 1 && num > table[nodeI][nodeJ + 1]) {
                dp[nodeI][nodeJ] = Math.max(dp[nodeI][nodeJ], 1 + dp[nodeI][nodeJ + 1]);
            }
            res = Math.max(res, dp[nodeI][nodeJ]);
        }

        return String.valueOf(res);
    }

    public static void main(String[] args) {
        System.out.print(mainMethod());
    }
}
