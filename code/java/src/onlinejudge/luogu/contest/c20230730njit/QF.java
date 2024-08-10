package onlinejudge.luogu.contest.c20230730njit;

import java.util.Scanner;

class QF {
    static int n;
    static int[] nums;
    static int total, halfTotal;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        total = 0;
        nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = scanner.nextInt();
            total += nums[i];
        }
    }

    public static void main(String[] args) {
        input();
        if (1 == total % 2) {
            System.out.println("false");
            return;
        }
        halfTotal = total / 2;
        int[] dp = new int[1 + halfTotal];
        for (int i = 0; i < n; i++) {
            for (int j = halfTotal; j >= nums[i]; j--) {
                dp[j] = Math.max(dp[j], dp[j - nums[i]] + nums[i]);
            }
        }
        System.out.println(halfTotal == dp[halfTotal] ? "true" : "false");
    }
}