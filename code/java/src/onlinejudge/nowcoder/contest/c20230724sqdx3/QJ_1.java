package onlinejudge.nowcoder.contest.c20230724sqdx3;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class QJ_1 {
    static int n, n1, m;
    static MyList[] graph;
    static int[] inDegree;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        n1 = n + 1;
        m = scanner.nextInt();
        graph = new MyList[n1];
        for (int i = 1; i < n1; ++i) {
            graph[i] = new MyList();
        }
        inDegree = new int[n1];
        int u, v;
        for (int i = 0; i < m; ++i) {
            u = scanner.nextInt();
            v = scanner.nextInt();
            graph[u].al.add(v);
            ++inDegree[v];
        }
    }

    static void topologicalSort() {
        int y = 0;
        int[] queue = new int[n];
        for (int i = 1; i < n1; ++i) {
            if (0 == inDegree[i]) {
                queue[y++] = i;
            }
        }
        for (int x = 0; x < y; ++x) {
            for (int v : graph[queue[x]].al) {
                if (0 == --inDegree[v]) {
                    queue[y++] = v;
                }
            }
        }

        if (n == y) {
            System.out.println(1);
            StringBuilder res1 = new StringBuilder();
            for (int i = 0; i < n; ++i) {
                res1.append(queue[i]).append(' ');
            }
            System.out.println(res1);
        } else {
            System.out.println(2);
            StringBuilder res1 = new StringBuilder();
            StringBuilder res2 = new StringBuilder();
            for (int i = 1; i < n1; ++i) {
                res1.append(i).append(' ');
                res2.insert(0, ' ').insert(0, i);
            }
            System.out.println(res1);
            System.out.println(res2);
        }
    }

    public static void main(String[] args) {
        input();
        topologicalSort();
    }
}

class MyList {
    List<Integer> al = new ArrayList<>();
}
