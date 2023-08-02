package rockyutil.algorithm.graphtheory;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Set;

class DepthFirstSearch {
    private int[][] graph;

    DepthFirstSearch() {
        setGraph(new int[][]{{1, 2}, {3, 4}, {5}, {}, {5}, {}});
    }

    DepthFirstSearch(int[][] graph) {
        setGraph(graph);
    }

    static void recursiveDFS1(int[][] graph, int vertex, Set<Integer> visited) {
        if (!visited.contains(vertex)) {
            System.out.print(" => " + vertex);
            visited.add(vertex);
            for (int i = 0; i < graph[vertex].length; i++) {
                if (!visited.contains(graph[vertex][i])) {
                    recursiveDFS1(graph, graph[vertex][i], visited);
                }
            }
        }
    }

    static void iterativeDFS1(int[][] graph, int start, Set<Integer> visited) {
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(start);
        int vertex;
        while (!stack.isEmpty()) {
            vertex = stack.pop();
            if (!visited.contains(vertex)) {
                System.out.print(" => " + vertex);
                visited.add(vertex);
                for (int i = graph[vertex].length - 1; i > -1; i--) {
                    if (!visited.contains(graph[vertex][i])) {
                        stack.push(graph[vertex][i]);
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        DepthFirstSearch dfs = new DepthFirstSearch();

        int origin = 0;

        System.out.println("=== DFS (Depth-First Search) ===");
        System.out.println("recursiveDFS1()");
        recursiveDFS1(dfs.getGraph(), origin, new HashSet<>());
        System.out.println();
        System.out.println("iterativeDFS1()");
        iterativeDFS1(dfs.getGraph(), origin, new HashSet<>());
        System.out.println();
    }

    int[][] getGraph() {
        return graph;
    }

    void setGraph(int[][] graph) {
        this.graph = graph;
    }
}