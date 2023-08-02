package rockyutil.algorithm.graphtheory.graphsearch;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Set;

class GraphSearch1 {
    int[][] graph1;

    GraphSearch1() {
        this.graph1 = new int[][]{{1, 2}, {3, 4}, {5}, {}, {5}, {}};
    }

    GraphSearch1(int[][] graph1) {
        this.graph1 = graph1;
    }

    static void recursiveBFS1(int[][] g1, Deque<Integer> queue, Set<Integer> visited) {
        if (queue.isEmpty()) {
            return;
        }
        int vertex = queue.poll();
        if (!visited.contains(vertex)) {
            System.out.print(" => " + vertex);
            visited.add(vertex);
            for (int i = 0; i < g1[vertex].length; i++) {
                if (!visited.contains(g1[vertex][i])) {
                    queue.offer(g1[vertex][i]);
                }
            }
        }
        recursiveBFS1(g1, queue, visited);
    }

    static void iterativeBFS1(int[][] g1, int start, Set<Integer> visited) {
        Deque<Integer> queue = new ArrayDeque<>();
        queue.offer(start);
        int vertex;
        while (!queue.isEmpty()) {
            vertex = queue.poll();
            if (!visited.contains(vertex)) {
                System.out.print(" => " + vertex);
                visited.add(vertex);
                for (int i = 0; i < g1[vertex].length; i++) {
                    if (!visited.contains(g1[vertex][i])) {
                        queue.offer(g1[vertex][i]);
                    }
                }
            }
        }
    }

    static void recursiveDFS1(int[][] g1, int vertex, Set<Integer> visited) {
        if (!visited.contains(vertex)) {
            System.out.print(" => " + vertex);
            visited.add(vertex);
            for (int i = 0; i < g1[vertex].length; i++) {
                if (!visited.contains(g1[vertex][i])) {
                    recursiveDFS1(g1, g1[vertex][i], visited);
                }
            }
        }
    }

    static void iterativeDFS1(int[][] g1, int start, Set<Integer> visited) {
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(start);
        int vertex;
        while (!stack.isEmpty()) {
            vertex = stack.pop();
            if (!visited.contains(vertex)) {
                System.out.print(" => " + vertex);
                visited.add(vertex);
                for (int i = g1[vertex].length - 1; i > -1; i--) {
                    if (!visited.contains(g1[vertex][i])) {
                        stack.push(g1[vertex][i]);
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        GraphSearch1 gs1 = new GraphSearch1();

        int origin = 0;
        Deque<Integer> originQueue = new ArrayDeque<>();
        originQueue.offer(origin);

        System.out.println("=== BFS (Breadth-First Search) ===");
        System.out.println("recursiveBFS1()");
        recursiveBFS1(gs1.graph1, new ArrayDeque<>(originQueue), new HashSet<>());
        System.out.println();
        System.out.println("iterativeBFS1()");
        iterativeBFS1(gs1.graph1, origin, new HashSet<>());
        System.out.println();
        System.out.println();
        System.out.println("=== DFS (Depth-First Search) ===");
        System.out.println("recursiveDFS1()");
        recursiveDFS1(gs1.graph1, origin, new HashSet<>());
        System.out.println();
        System.out.println("iterativeDFS1()");
        iterativeDFS1(gs1.graph1, origin, new HashSet<>());
        System.out.println();
        System.out.println();
    }

    int[][] getGraph1() {
        return graph1;
    }

    void setGraph1(int[][] graph1) {
        this.graph1 = graph1;
    }
}