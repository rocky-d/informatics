package onlinejudge.luogu.solved;

import java.util.Scanner;

class P3817 {
    static int N, X;
    static int[] a;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        X = scanner.nextInt();
        a = new int[N];
        for (int i = 0; i < N; i++) {
            a[i] = scanner.nextInt();
        }
    }

    public static void main(String[] args) {
        input();
        long res = 0;
        for (int i = 1; i < N; i++) {
            if (a[i - 1] + a[i] > X) {
                res += a[i - 1] + a[i] - X;
                a[i] = X - a[i - 1];
            }
        }
        System.out.print(res);
    }
}
