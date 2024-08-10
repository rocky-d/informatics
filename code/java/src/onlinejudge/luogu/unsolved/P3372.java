package luogu.undone;

import java.util.Scanner;

class P3372 {
    static int n, n1, m;
    static int[] nums;
    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        n1 = n + 1;
        m = scanner.nextInt();
        nums = new int[n1];
        for (int i = 1; i < n1; i++) {
            nums[i] = scanner.nextInt();
        }
    }

    public static void main(String[] args) {
        input();
    }
}