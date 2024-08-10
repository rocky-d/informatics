package onlinejudge.luogu.contest.c20230730njit;

import java.util.*;

class QH {
    static int n, m, start, end;
    static List<List<int[]>> graph;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        m = scanner.nextInt();
        graph = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        int a, b, t;
        for (int i = 0; i < m; i++) {
            a = scanner.nextInt();
            b = scanner.nextInt();
            t = scanner.nextInt();
            graph.get(a).add(new int[]{b, t});
        }
        start = scanner.nextInt();
        end = scanner.nextInt();
    }

    public static void main(String[] args) {
        input();

        int[] distances = new int[n], pre = new int[n];
        Arrays.fill(distances, Integer.MAX_VALUE);
        distances[start] = 0;

        PriorityQueue<int[]> minHeap = new PriorityQueue<>(n, Comparator.comparingInt(x -> x[1]));
        minHeap.offer(new int[]{start, distances[start]});

        int[] vertex;
        int newDistance;
        while (!minHeap.isEmpty()) {
            vertex = minHeap.poll();
            if (vertex[1] > distances[vertex[0]]) {
                continue;
            }
            for (int[] nei : graph.get(vertex[0])) {
                newDistance = vertex[1] + nei[1];
                if (newDistance < distances[nei[0]]) {
                    distances[nei[0]] = newDistance;
                    minHeap.add(new int[]{nei[0], newDistance});
                    pre[nei[0]] = vertex[0];
                }
            }
        }

        if (Integer.MAX_VALUE == distances[end]) {
            System.out.println(-1);
        } else {
            StringBuilder pa = new StringBuilder();
            int current = end;
            while (start != current) {
                pa.insert(0, ' ').insert(0, current);
                current = pre[current];
            }
            pa.insert(0, ' ').insert(0, current);
            System.out.println(pa);
            System.out.println(distances[end]);
        }
    }
}