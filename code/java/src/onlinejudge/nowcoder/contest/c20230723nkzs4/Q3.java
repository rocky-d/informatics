package onlinejudge.nowcoder.contest.c20230723nkzs4;

import java.util.Arrays;
import java.util.Scanner;

class Q3 {
    static final int MOD = 1000000007;
    static int n, k;
    static long[] a;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        k = scanner.nextInt();
        a = new long[n];
        for (int i = 0; i < n; ++i) {
            a[i] = scanner.nextInt();
        }
        long tmp = 0;
        for (int i = 0; i < k; ++i) {
            if (1 == scanner.nextByte()) {
                tmp += scanner.nextInt();
            } else {
                tmp -= scanner.nextInt();
                if (tmp < 0) {
                    for (int j = 0; j < n; ++j) {
                        a[j] = Math.max(0, a[j] + tmp);
                    }
                    tmp = 0;
                }
            }
        }
        System.out.println(Arrays.toString(a));
        System.out.println(tmp);
        long sum = 0L;
        for (long l : a) {
            sum += l;
        }
        System.out.print((tmp * n % MOD + sum % MOD) % MOD);
    }

    public static void main(String[] args) {
        input();
    }
}
