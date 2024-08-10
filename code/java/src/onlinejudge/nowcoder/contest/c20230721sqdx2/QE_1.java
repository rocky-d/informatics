package nowcoder.contest.c20230721sqdx2;

import java.util.Scanner;

class QE_1 {
    static int getAns(long big_x, long target) {
        long rt = (long) Math.sqrt(big_x);
        for (long i = Math.max(rt, 0L); i < rt + 10; i++) {
            if (i * i < big_x) continue;
            long j = i * i;
            while (j > target) j /= 10;
            if (j == target) return (int) i;
            else return -1;
        }
        return -1;
    }

    public static void main(String[] args) {
        final int MAX = (int) Math.pow(10, 9);
        Scanner readin = new Scanner(System.in);
        long size = readin.nextLong();
        long ans;
        boolean find;
        for (int i = 0; i < size; i++) {
            ans = -1;
            find = false;
            long x = readin.nextLong();
            long big_x = x * MAX;  // 添加末尾0
            for (; big_x >= x; big_x /= 10) {
                ans = Math.max(ans, getAns(big_x, x));
                if (ans > -1) {
                    System.out.println(ans);
                    find = true;
                    break;
                }
            }
            if (!find) System.out.println(-1);
        }
    }
}