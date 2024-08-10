package onlinejudge.luogu.solved;

import java.util.Scanner;

class P1219 {
    static int count = 3;
    static int n, n1;
    static int res;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        n1 = n + 1;
    }

    static boolean check(boolean[][] bd, int row, int column) {
        int a, b, stepA = -1;
        for (int stepB = 1; stepB != -2; stepB--) {
            a = row + stepA;
            b = column + stepB;
            while (0 < a && 0 < b && b < n1) {
                if (bd[a][b]) {
                    return false;
                }
                a += stepA;
                b += stepB;
            }
        }
        return true;
    }

    static void dfs(boolean[][] bd, int row) {
        if (n == row) {
            StringBuilder seq = new StringBuilder();
            for (int column = 1; column < n1; column++) {
                if (check(bd, row, column)) {
                    ++res;
                    if (count > 0) {
                        --count;
                        bd[row][column] = true;
                        for (int i = 1; i < n1; i++) {
                            for (int j = 1; j < n1; j++) {
                                if (bd[i][j]) {
                                    seq.append(j).append(' ');
                                    break;
                                }
                            }
                        }
                        System.out.println(seq);
                        bd[row][column] = false;
                    }
                }
            }
        } else {
            for (int column = 1; column < n1; column++) {
                if (check(bd, row, column)) {
                    bd[row][column] = true;
                    dfs(bd, row + 1);
                    bd[row][column] = false;
                }
            }
        }
    }

    public static void main(String[] args) {
        input();
        res = 0;
        boolean[][] board = new boolean[n1][n1];
        dfs(board, 1);
        System.out.println(res);
    }
}