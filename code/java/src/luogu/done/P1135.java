package luogu.done;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

class P1135 {
    static int n, n1, a, b;
    static int[] k;
    static boolean[] visited;
    static int res;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        n1 = n + 1;
        a = scanner.nextInt();
        b = scanner.nextInt();
        k = new int[n1];
        for (int i = 1; i < n1; i++) {
            k[i] = scanner.nextInt();
        }
    }

    static void dfs(int v, int times) {
        if (res <= times) {
            return;
        }
        if (b == v) {
            res = times;
            return;
        }
        if (n1 > v + k[v] && !visited[v + k[v]]) {
            visited[v + k[v]] = true;
            dfs(v + k[v], times + 1);
            visited[v + k[v]] = false;
        }
        if (0 < v - k[v] && !visited[v - k[v]]) {
            visited[v - k[v]] = true;
            dfs(v - k[v], times + 1);
            visited[v - k[v]] = false;
        }
    }

    static void bfs(int[] vT) {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.offer(vT);

        int[] v;
        while (!queue.isEmpty()) {
            v = queue.poll();
            if (b == v[0]) {
                res = v[1];
                break;
            }
            if (n1 > v[0] + k[v[0]] && !visited[v[0] + k[v[0]]]) {
                queue.offer(new int[]{v[0] + k[v[0]], v[1] + 1});
                visited[v[0] + k[v[0]]] = true;
            }
            if (0 < v[0] - k[v[0]] && !visited[v[0] - k[v[0]]]) {
                queue.offer(new int[]{v[0] - k[v[0]], v[1] + 1});
                visited[v[0] - k[v[0]]] = true;
            }
        }
    }

    public static void main(String[] args) {
        input();
        visited = new boolean[n1];
        res = n;
        visited[a] = true;
//        dfs(a, 0);
        bfs(new int[]{a, 0});
        visited[a] = false;
        System.out.println(n == res ? -1 : res);
    }
}