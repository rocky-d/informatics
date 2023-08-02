package rockyutil.algorithm.graphtheory;

class TopologicalSorting {
    private int[][] graph;
    private int[] inDegree;

    TopologicalSorting() {
        setGraph(new int[][]{{2, 3}, {2, 4}, {4}, {4, 5}, {5, 6}, {}, {}});
    }

    TopologicalSorting(int[][] graph) {
        setGraph(graph);
    }

    static void bfsTS(int[][] graph, int[] inDegree) {

    }

    public static void main(String[] args) {
        TopologicalSorting ts = new TopologicalSorting();

    }

    int[][] getGraph() {
        return graph;
    }

    void setGraph(int[][] graph) {
        this.graph = graph;
        setInDegree(graph);
    }

    int[] getInDegree() {
        return inDegree;
    }

    private void setInDegree(int[][] graph) {
        for (int i = 0; i < graph.length; i++) {
            for (int j = 0; j < graph[i].length; j++) {
                ++inDegree[graph[i][j]];
            }
        }
//        for (int[] u : graph) {
//            for (int v : u) {
//                ++inDegree[v];
//            }
//        }
    }
}