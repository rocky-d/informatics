package onlinejudge.nowcoder.contest.c20231203njit;

import java.util.Scanner;

public class QL {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        int m = scanner.nextInt();
        int[] a = new int[n];
        long[] prefixSum = new long[1 + n];
        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextInt();
            prefixSum[i + 1] = prefixSum[i] + a[i];
        }
        long maxValue = 0;
        for (int i = 0; i <= n - k; i++) {
            maxValue = Math.max(maxValue, prefixSum[i + k] - prefixSum[i]);
        }
        System.out.println(m < maxValue ? maxValue : -1);
    }
}
