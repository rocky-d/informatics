package nowcoder.contest.cows20230724;

import java.util.*;

class QJ {
    static int n, n1, m;
    static boolean[][] graph;
    static int[] inDegree;
    static Set<Integer> notVisited;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        n1 = n + 1;
        m = scanner.nextInt();
        graph = new boolean[n1][n1];
        inDegree = new int[n1];
        int a, b;
        for (int i = 0; i < m; ++i) {
            a = scanner.nextInt();
            b = scanner.nextInt();
            graph[a][b] = true;
            ++inDegree[b];
        }
    }

    static List<Integer> topologicalSort(Deque<Integer> queue) {
        List<Integer> res = new LinkedList<>();
        int vertex;
        while (!queue.isEmpty()) {
            vertex = queue.poll();
            res.add(vertex);
            notVisited.remove(vertex);
            for (int i = 1; i < n1; ++i) {
                if (graph[vertex][i] && 0 == --inDegree[i]) {
                    queue.offer(i);
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        input();

        StringBuilder strRes = new StringBuilder();
        notVisited = new HashSet<>();
        boolean k = true;

        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 1; i < n1; ++i) {
            notVisited.add(i);
            if (0 == inDegree[i]) {
                queue.offer(i);
            }
        }
        List<Integer> res = topologicalSort(queue);
        if (!notVisited.isEmpty()) {
            k = false;
            res.addAll(notVisited);
        }

        if (k) {
            strRes.append("1\n");
        } else {
            strRes.append("2\n");
            for (int i = n - 1; i > -1; --i) {
                strRes.append(res.get(i)).append(" ");
            }
            strRes.append("\n");
        }
        for (int i = 0; i < n; ++i) {
            strRes.append(res.get(i)).append(" ");
        }
        System.out.print(strRes);
    }
}