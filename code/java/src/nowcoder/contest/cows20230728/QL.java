package nowcoder.contest.cows20230728;

import java.util.Scanner;

class QL {
    static int n, n1, m, m1, q;
    static int[] row, column;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        n1 = n + 1;
        m = scanner.nextInt();
        m1 = m + 1;
        q = scanner.nextInt();
        row = new int[n1];
        column = new int[m1];

        String rowOrColumn, onOrOff;
        int num, diff;
        for (int i = 0; i < q; i++) {
            rowOrColumn = scanner.next();
            num = scanner.nextInt();
            onOrOff = scanner.next();
            if (rowOrColumn.equals("row")) {
                if (onOrOff.equals("on")) {
                    diff = m - row[num];
                    row[num] = m;
                    for (int j = 1; j < m1 && diff > 0; j++) {
                        if (column[j] < n) {
                            ++column[j];
                            --diff;
                        }
                    }
                } else {
                    diff = row[num];
                    row[num] = 0;
                    for (int j = 1; j < m1 && diff > 0; j++) {
                        if (column[j] > 0) {
                            --column[j];
                            --diff;
                        }
                    }
                }
            } else {
                if (onOrOff.equals("on")) {
                    diff = n - column[num];
                    column[num] = n;
                    for (int j = 1; j < n1 && diff > 0; j++) {
                        if (row[j] < m) {
                            ++row[j];
                            --diff;
                        }
                    }
                } else {
                    diff = column[num];
                    column[num] = 0;
                    for (int j = 1; j < n1 && diff > 0; j++) {
                        if (row[j] > 0) {
                            --row[j];
                            --diff;
                        }
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        input();
        long res = 0;
        if (n < m) {
            for (int i = 1; i < n1; i++) {
                res += row[i];
            }
        } else {
            for (int i = 1; i < m1; i++) {
                res += column[i];
            }
        }
        System.out.println(res);
    }
}