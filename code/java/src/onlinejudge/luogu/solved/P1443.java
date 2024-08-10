package onlinejudge.luogu.solved;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.Scanner;

class P1443 {
    static int n, n1, m, m1, x, y;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        n1 = n + 1;
        m = scanner.nextInt();
        m1 = m + 1;
        x = scanner.nextInt();
        y = scanner.nextInt();
    }

    static void bfs(int[][] bd) {
        int[][] step = {{1, 2}, {2, 1}, {-1, 2}, {-2, 1}, {1, -2}, {2, -1}, {-1, -2}, {-2, -1}};

        Deque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{x, y});
        int[] vertex;
        int a, b;
        while (!queue.isEmpty()) {
            vertex = queue.poll();
            for (int i = 0; i < 8; i++) {
                a = vertex[0] + step[i][0];
                b = vertex[1] + step[i][1];
                if (0 < a && a < n1 && 0 < b && b < m1 && -1 == bd[a][b]) {
                    bd[a][b] = 1 + bd[vertex[0]][vertex[1]];
                    queue.offer(new int[]{a, b});
                }
            }
        }
    }

    public static void main(String[] args) {
        input();
        int[][] board = new int[n1][m1];
        for (int[] re : board) {
            Arrays.fill(re, -1);
        }
        board[x][y] = 0;
        bfs(board);

        StringBuilder res = new StringBuilder();
        for (int i = 1; i < n1; i++) {
            for (int j = 1; j < m1; j++) {
                res.append(board[i][j]).append(' ');
            }
            res.append('\n');
        }
        System.out.print(res);
    }
}
