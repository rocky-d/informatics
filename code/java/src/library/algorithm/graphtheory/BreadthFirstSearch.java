package library.algorithm.graphtheory;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Set;

class BreadthFirstSearch {
    private int[][] graph;

    BreadthFirstSearch() {
        setGraph(new int[][]{{1, 2}, {3, 4}, {5}, {}, {5}, {}});
    }

    BreadthFirstSearch(int[][] graph) {
        setGraph(graph);
    }

    static void recursiveBFS1(int[][] graph, Deque<Integer> queue, Set<Integer> visited) {
        if (queue.isEmpty()) {
            return;
        }
        int vertex = queue.poll();
        if (!visited.contains(vertex)) {
            System.out.print(" => " + vertex);
            visited.add(vertex);
            for (int i = 0; i < graph[vertex].length; i++) {
                if (!visited.contains(graph[vertex][i])) {
                    queue.offer(graph[vertex][i]);
                }
            }
        }
        recursiveBFS1(graph, queue, visited);
    }

    static void iterativeBFS1(int[][] graph, int start, Set<Integer> visited) {
        Deque<Integer> queue = new ArrayDeque<>();
        queue.offer(start);
        int vertex;
        while (!queue.isEmpty()) {
            vertex = queue.poll();
            if (!visited.contains(vertex)) {
                System.out.print(" => " + vertex);
                visited.add(vertex);
                for (int i = 0; i < graph[vertex].length; i++) {
                    if (!visited.contains(graph[vertex][i])) {
                        queue.offer(graph[vertex][i]);
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        BreadthFirstSearch bfs = new BreadthFirstSearch();

        int origin = 0;
        Deque<Integer> queue = new ArrayDeque<>();
        queue.offer(origin);

        System.out.println("=== BFS (Breadth-First Search) ===");
        System.out.println("recursiveBFS1()");
        recursiveBFS1(bfs.getGraph(), new ArrayDeque<>(queue), new HashSet<>());
        System.out.println();
        System.out.println("iterativeBFS1()");
        iterativeBFS1(bfs.getGraph(), origin, new HashSet<>());
        System.out.println();
    }

    int[][] getGraph() {
        return graph;
    }

    void setGraph(int[][] graph) {
        this.graph = graph;
    }
}