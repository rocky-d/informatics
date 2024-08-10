package onlinejudge.luogu.unsolved;

import java.util.*;

class P1141 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int n1 = n + 1;
        int m = scanner.nextInt();
        scanner.nextLine();
        String[] maze = new String[n1];
        for (int i = 1; i < n1; i++) {
            maze[i] = "x" + scanner.nextLine();
        }

        int res, vi, vj, neiI, neiJ;
        int[] curr;
        char target;
        boolean[][] visited;
        Deque<int[]> queue;
        for (int k = 0; k < m; k++) {
            res = 0;
            visited = new boolean[n1][n1];
            queue = new ArrayDeque<>();
            queue.offer(new int[]{scanner.nextInt(), scanner.nextInt()});
            while (!queue.isEmpty()) {
                curr = queue.poll();
                vi = curr[0];
                vj = curr[1];
                if (!visited[vi][vj]) {
                    ++res;
                    visited[vi][vj] = true;
                    target = maze[vi].charAt(vj) == '1' ? '0' : '1';
                    for (int[] nei : new int[][]{{vi + 1, vj}, {vi - 1, vj}, {vi, vj + 1}, {vi, vj - 1}}) {
                        neiI = nei[0];
                        neiJ = nei[1];
                        if (neiI > 0 && neiI < n1 && neiJ > 0 && neiJ < n1
                                && !visited[neiI][neiJ] && maze[neiI].charAt(neiJ) == target) {
                            queue.offer(new int[]{neiI, neiJ});
                        }
                    }
                }
            }
            System.out.println(res);
        }
    }
}