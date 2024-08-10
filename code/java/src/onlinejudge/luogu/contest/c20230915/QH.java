package onlinejudge.luogu.contest.c20230915;

import java.util.*;

class QH {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int n1 = n + 1;
        List<List<Integer>> ls = new ArrayList<>(n);
        ls.add(new ArrayList<>());
        for (int i = 1; i < n1; i++) {
            ls.add(new ArrayList<>());
            int k = scanner.nextInt();
            for (int j = 0; j < k; j++) {
                ls.get(i).add(scanner.nextInt());
            }
        }

        Deque<Integer> queue = new ArrayDeque<>();
        queue.offer(1);
        int res = 0;
        boolean[] visited = new boolean[n1];
        while (!queue.isEmpty()) {
            int pac = queue.poll();
            if (!visited[pac]) {
                res++;
                visited[pac] = true;
                queue.addAll(ls.get(pac));
            }
        }
        System.out.println(res);
    }
}
