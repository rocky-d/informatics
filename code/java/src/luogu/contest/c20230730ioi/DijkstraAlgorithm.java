package luogu.contest.c20230730ioi;

import java.util.*;

class DijkstraAlgorithm {

    // 辅助类，用于表示图中的节点和对应的距离
    static class NodeDistance implements Comparable<NodeDistance> {
        int node;
        int distance;

        public NodeDistance(int node, int distance) {
            this.node = node;
            this.distance = distance;
        }

        @Override
        public int compareTo(NodeDistance other) {
            return Integer.compare(this.distance, other.distance);
        }
    }

    // 有向图的邻接表表示
    private Map<Integer, List<NodeDistance>> graph;

    public DijkstraAlgorithm() {
        this.graph = new HashMap<>();
    }

    // 添加边到有向图
    public void addEdge(int source, int destination, int weight) {
        graph.putIfAbsent(source, new ArrayList<>());
        graph.get(source).add(new NodeDistance(destination, weight));
    }

    // 迪杰斯特拉算法的实现
    public int[] dijkstra(int startNode, int numNodes) {
        int[] distances = new int[numNodes];
        int[] predecessors = new int[numNodes]; // 用于记录每个节点的前驱节点
        Arrays.fill(distances, Integer.MAX_VALUE);
        Arrays.fill(predecessors, -1);

        PriorityQueue<NodeDistance> minHeap = new PriorityQueue<>();
        distances[startNode] = 0;
        minHeap.add(new NodeDistance(startNode, 0));

        while (!minHeap.isEmpty()) {
            NodeDistance curr = minHeap.poll();
            int currNode = curr.node;

            // 如果当前节点的距离已经大于保存的最小距离，则跳过
            if (curr.distance > distances[currNode]) {
                continue;
            }

            // 遍历当前节点的邻居节点
            List<NodeDistance> neighbors = graph.getOrDefault(currNode, new ArrayList<>());
            for (NodeDistance neighbor : neighbors) {
                int newDistance = curr.distance + neighbor.distance;
                if (newDistance < distances[neighbor.node]) {
                    distances[neighbor.node] = newDistance;
                    predecessors[neighbor.node] = currNode; // 记录前驱节点
                    minHeap.add(new NodeDistance(neighbor.node, newDistance));
                }
            }
        }

        return predecessors;
    }

    // 输出从起始节点到目标节点的最小权路径
    public List<Integer> getPath(int startNode, int endNode, int[] predecessors) {
        List<Integer> path = new ArrayList<>();
        int current = endNode;

        while (current != -1 && current != startNode) {
            path.add(0, current);
            current = predecessors[current];
        }

        if (current == startNode) {
            path.add(0, startNode);
        } else {
            // 说明从起始节点无法到达目标节点
            path.clear();
        }

        return path;
    }

    public static void main(String[] args) {
        DijkstraAlgorithm dijkstra = new DijkstraAlgorithm();
        int numNodes = 6; // 修改为你的图中节点的总数

        // 添加边到有向图
        dijkstra.addEdge(0, 1, 5);
        dijkstra.addEdge(0, 2, 3);
        dijkstra.addEdge(1, 3, 6);
        dijkstra.addEdge(1, 2, 2);
        dijkstra.addEdge(2, 4, 4);
        dijkstra.addEdge(2, 5, 2);
        dijkstra.addEdge(2, 3, 7);
        dijkstra.addEdge(3, 4, -1);
        dijkstra.addEdge(4, 5, -2);

        int startNode = 0; // 修改为你要计算最小权路径的起始节点
        int endNode = 4;   // 修改为你要计算最小权路径的目标节点
        int[] predecessors = dijkstra.dijkstra(startNode, numNodes);

        // 输出结果
        List<Integer> path = dijkstra.getPath(startNode, endNode, predecessors);
        if (!path.isEmpty()) {
            System.out.println("从节点 " + startNode + " 到节点 " + endNode + " 的最小权路径为：" + path);
        } else {
            System.out.println("无法从节点 " + startNode + " 到节点 " + endNode + " 到达！");
        }
    }
}
