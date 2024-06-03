package nowcoder.contest.c20230724sqdx3;

import java.util.Scanner;

class QH {
    static int n;
    static int[] A;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        A = new int[n];
        for (int i = 0; i < n; ++i) {
            A[i] = scanner.nextInt();
        }
    }

    public static void main(String[] args) {
        input();

    }
}