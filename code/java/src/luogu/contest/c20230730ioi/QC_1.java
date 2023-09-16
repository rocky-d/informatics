package luogu.contest.c20230730ioi;

import java.util.*;

class QC_1 {
    static int n, target;
    static int[] nums;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        target = scanner.nextInt();
        nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = scanner.nextInt();
        }
        scanner.close();
    }

    public static void main(String[] args) {
        input();
    }
}