package onlinejudge.nowcoder.contest.c20230807sqdx7;

import java.util.Scanner;

class QM {
    static int pow(int x) {
        int res = 1;
        for (int i = 1; i < x; i++) {
            res *= 10;
        }
        return res;
    }

    static int pow1(int x) {
        int res = 0;
        for (int i = -1; i < x; i++) {
            res = res * 10 + 9;
        }
        return res;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int t = scanner.nextInt();
        int n, num, i;
        long res;
        while (0 < t--) {
            n = scanner.nextInt();
            res = 0;
            num = 9;
            for (i = 1; num < n; i++) {
                res += 9L * i * pow(i);
                num = pow1(i);
            }
            res += (long) (n - pow1(i - 2)) * i;

            System.out.println(res);
        }
    }
}
