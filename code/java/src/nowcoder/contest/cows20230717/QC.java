package nowcoder.contest.cows20230717;

import java.util.Scanner;

class QC {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int k = scanner.nextInt();
        double[] trees = new double[n + 1];
        int l, r, x;
        long res = 0;
        while (m > 0) {
            if (scanner.nextInt() == 1) {
                l = scanner.nextInt();
                r = scanner.nextInt();
                x = scanner.nextInt();
                for (int i = l; i <= r; ++i) {
                    trees[i] += (double) x / k;
                }
            } else {
                l = scanner.nextInt();
                r = scanner.nextInt();
                for (int i = l; i <= r; ++i) {
                    if (trees[i] >= 1) {
                        trees[i] -= 1;
                        ++res;
                    }
                }
            }
            --m;
        }
        System.out.print(res);
    }
}
