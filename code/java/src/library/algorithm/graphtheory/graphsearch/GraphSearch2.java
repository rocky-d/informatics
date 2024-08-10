package library.algorithm.graphtheory.graphsearch;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Set;

class GraphSearch2 {
    boolean[][] graph2;

    GraphSearch2() {
        this.graph2 = new boolean[][]{{false, true, true, false, false, false}, {false, false, false, true, true, false}, {false, false, false, false, false, true}, {false, false, false, false, false, false}, {false, false, false, false, false, true}, {false, false, false, false, false, false}};
    }

    GraphSearch2(boolean[][] graph2) {
        this.graph2 = graph2;
    }

    static void recursiveBFS2(boolean[][] g2, Deque<Integer> queue, Set<Integer> visited) {
        if (queue.isEmpty()) {
            return;
        }
        int vertex = queue.poll();
        if (!visited.contains(vertex)) {
            System.out.print(" => " + vertex);
            visited.add(vertex);
            for (int i = 0; i < g2[vertex].length; i++) {
                if (g2[vertex][i] && !visited.contains(i)) {
                    queue.offer(i);
                }
            }
        }
        recursiveBFS2(g2, queue, visited);
    }

    static void iterativeBFS2(boolean[][] g2, int start, Set<Integer> visited) {
        Deque<Integer> queue = new ArrayDeque<>();
        queue.offer(start);
        int vertex;
        while (!queue.isEmpty()) {
            vertex = queue.poll();
            if (!visited.contains(vertex)) {
                System.out.print(" => " + vertex);
                visited.add(vertex);
                for (int i = 0; i < g2[vertex].length; i++) {
                    if (g2[vertex][i] && !visited.contains(i)) {
                        queue.offer(i);
                    }
                }
            }
        }
    }

    static void recursiveDFS2(boolean[][] g2, int vertex, Set<Integer> visited) {
        if (!visited.contains(vertex)) {
            System.out.print(" => " + vertex);
            visited.add(vertex);
            for (int i = 0; i < g2[vertex].length; i++) {
                if (g2[vertex][i] && !visited.contains(i)) {
                    recursiveDFS2(g2, i, visited);
                }
            }
        }
    }

    static void iterativeDFS2(boolean[][] g2, int start, Set<Integer> visited) {
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(start);
        int vertex;
        while (!stack.isEmpty()) {
            vertex = stack.pop();
            if (!visited.contains(vertex)) {
                System.out.print(" => " + vertex);
                visited.add(vertex);
                for (int i = g2[vertex].length - 1; i > -1; i--) {
                    if (g2[vertex][i] && !visited.contains(i)) {
                        stack.push(i);
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        GraphSearch2 gs2 = new GraphSearch2();

        int origin = 0;
        Deque<Integer> originQueue = new ArrayDeque<>();
        originQueue.offer(origin);

        System.out.println("=== BFS (Breadth-First Search) ===");
        System.out.println("recursiveBFS2()");
        recursiveBFS2(gs2.graph2, new ArrayDeque<>(originQueue), new HashSet<>());
        System.out.println();
        System.out.println("iterativeBFS2()");
        iterativeBFS2(gs2.graph2, origin, new HashSet<>());
        System.out.println();
        System.out.println();
        System.out.println("=== DFS (Depth-First Search) ===");
        System.out.println("recursiveDFS2()");
        recursiveDFS2(gs2.graph2, origin, new HashSet<>());
        System.out.println();
        System.out.println("iterativeDFS2()");
        iterativeDFS2(gs2.graph2, origin, new HashSet<>());
        System.out.println();
        System.out.println();
    }

    boolean[][] getGraph2() {
        return graph2;
    }

    void setGraph1(boolean[][] graph2) {
        this.graph2 = graph2;
    }
}
