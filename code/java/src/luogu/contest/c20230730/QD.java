package luogu.contest.c20230730;

import java.util.*;

class QD {
    static int n;
    static PriorityQueue<int[]> s;
    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        s = new PriorityQueue<>(n, Comparator.comparingInt(x -> -x[0]));
        for (int i = 0; i < n; i++) {
            s.offer(new int[]{scanner.nextInt(), i});
        }
    }

    public static void main(String[] args) {
        input();
        int[] vertex;
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            vertex = s.poll();

        }
        System.out.println(Arrays.toString(res));
    }
}