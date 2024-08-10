package luogu.undone;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

class P4017_1 {
    static final int MOD = 80112002;
    static short n, n1;
    static int m;
    static int[] inDegree, outDegree;
    static boolean[][] graph;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextShort();
        n1 = (short) (n + 1);
        m = scanner.nextInt();

        inDegree = new int[n1];
        outDegree = new int[n1];
        graph = new boolean[n1][n1];

        short u, v;
        for (int i = 0; i < m; i++) {
            u = scanner.nextShort();
            v = scanner.nextShort();
            ++inDegree[v];
            ++outDegree[u];
            graph[u][v] = true;
        }
    }

    public static void main(String[] args) {
        input();
        Deque<Short> queue = new ArrayDeque<>();
        int[] dp = new int[n1];
        for (short i = 1; i < n1; i++) {
            if (0 == inDegree[i]) {
                queue.offer(i);
                dp[i] = 1;
            }
        }

        short u;
        while (!queue.isEmpty()) {
            u = queue.poll();
            for (short v = 1; v < n1; v++) {
                if (graph[u][v]) {
                    dp[v] = (dp[v] + dp[u]) % MOD;
                    if (0 == --inDegree[v]) {
                        queue.offer(v);
                    }
                }
            }
        }

        int res = 0;
        for (short i = 1; i < n1; i++) {
            if (0 == outDegree[i]) {
                res = (res + dp[i]) % MOD;
            }
        }
        System.out.println(res);
    }
}