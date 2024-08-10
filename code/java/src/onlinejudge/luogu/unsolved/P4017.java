package onlinejudge.luogu.unsolved;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

class P4017 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int m = scanner.nextInt();

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; ++i) graph.add(new ArrayList<>());

        int[] innum = new int[n];
        int[] outnum = new int[n];
        int a;
        int b;
        for (int i = 0; i < m; ++i) {
            a = scanner.nextInt() - 1;
            b = scanner.nextInt() - 1;
            graph.get(a).add(b);
            ++innum[a];
            ++outnum[b];
        }

        List<Integer> start = new ArrayList<>();
        List<Integer> end = new ArrayList<>();
        for (int i = 0; i < n; ++i) {
            if (innum[i] == 0) start.add(i);
            if (outnum[i] == 0) end.add(i);
        }
        int[] startArray = new int[start.size()];
        int[] endArray = new int[end.size()];
        for (int i = 0; i < start.size(); ++i) startArray[i] = start.get(i);
        for (int i = 0; i < end.size(); ++i) endArray[i] = end.get(i);
        Queue<Integer> queue = new LinkedList<>(end);

        int[] dp = new int[n];
        for (int i : endArray) dp[i] = 1;

//        System.out.println("n = " + n);
//        System.out.println("m = " + m);
//        System.out.println("graph = " + graph);
//        System.out.println("innum = " + Arrays.toString(innum));
//        System.out.println("outnum = " + Arrays.toString(outnum));
//        System.out.println("start = " + start);
//        System.out.println("end = " + end);
//        System.out.println("dp = " + Arrays.toString(dp));
//        System.out.println();

        final int MODULUS = 80112002;
        int node;
        while (!queue.isEmpty()) {
            node = queue.poll();
//            System.out.println("node = " + node);
            for (int nei : graph.get(node)) {
//                System.out.println("  nei = " + nei);
                dp[nei] += dp[node];
                dp[nei] %= MODULUS;
                --outnum[nei];
                if (outnum[nei] == 0) queue.offer(nei);
            }
        }
//        System.out.println();
//        System.out.println("dp = " + Arrays.toString(dp));

        int res = 0;
        for (int i : startArray) {
            res += dp[i];
            res %= MODULUS;
        }

        System.out.print(res);
    }
}
