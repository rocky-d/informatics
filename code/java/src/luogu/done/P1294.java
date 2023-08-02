package luogu.done;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

class P1294 {
    static Scanner scanner = new Scanner(System.in);
    static int N, M, res = 0;
    static int[][] matrix;
    static Set<Integer> visited = new HashSet<>();

    static void dfs(int node, int count) {
        boolean isEnd = true;
        for (int nei = 1; nei <= N; ++nei) {
            if (matrix[node][nei] != 0 && !visited.contains(nei)) {
                visited.add(nei);
                dfs(nei, count + matrix[node][nei]);
                visited.remove(nei);
                isEnd = false;
            }
        }
        if (isEnd) res = Math.max(count, res);
    }

    static String mainMethod() {
        N = scanner.nextInt();
        M = scanner.nextInt();
        matrix = new int[N + 1][N + 1];
        int x, y, w;
        for (int i = 0; i < M; ++i) {
            x = scanner.nextInt();
            y = scanner.nextInt();
            w = scanner.nextInt();
            matrix[x][y] = w;
            matrix[y][x] = w;
        }
        for (int i = 1; i <= N; ++i) {
            visited.add(i);
            dfs(i, 0);
            visited.clear();
        }
        return String.valueOf(res);
    }

    public static void main(String[] args) {
        System.out.print(mainMethod());
    }
}
