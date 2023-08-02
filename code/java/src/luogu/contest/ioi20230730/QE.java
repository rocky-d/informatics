package luogu.contest.ioi20230730;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

class QE {
    static int n;
    static PriorityQueue<Integer> pqA, pqB;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        pqA = new PriorityQueue<>(n, Comparator.comparingInt(x -> -x));
        for (int i = 0; i < n; i++) {
            pqA.offer(scanner.nextInt());
        }
        pqB = new PriorityQueue<>(n, Comparator.comparingInt(x -> -x));
        for (int i = 0; i < n; i++) {
            pqB.offer(scanner.nextInt());
        }
    }

    public static void main(String[] args) {
        input();
        int res = 0;
        int a, b;
        while (!(pqA.isEmpty() || pqB.isEmpty())) {
            a = pqA.peek();
            b = pqB.peek();
            if (a > b) {
                ++res;
                pqA.poll();
                pqB.poll();
            } else {
                pqB.poll();
            }
        }
        System.out.println(res);
    }
}