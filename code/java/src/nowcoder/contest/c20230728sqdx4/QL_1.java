package nowcoder.contest.c20230728sqdx4;

import java.util.Scanner;

class QL_1 {
    static int n, n1, m, m1, q;
    static boolean[][] board;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        n1 = n + 1;
        m = scanner.nextInt();
        m1 = m + 1;
        q = scanner.nextInt();
        board = new boolean[n1][m1];

        boolean isRow, isOn;
        int num;
        for (int i = 0; i < q; i++) {
            isRow = scanner.next().equals("row");
            num = scanner.nextInt();
            isOn = scanner.next().equals("on");
            if (isRow) {
                for (int j = 1; j < m1; j++) {
                    board[num][j] = isOn;
                }
            } else {
                for (int j = 1; j < n1; j++) {
                    board[j][num] = isOn;
                }
            }
        }

        StringBuilder bd = new StringBuilder();
        long res = 0;
        for (int i = 1; i < n1; i++) {
            for (int j = 1; j < m1; j++) {
                bd.append(board[i][j] ? "1" : "0").append(", ");
                if (board[i][j]) {
                    ++res;
                }
            }
            bd.append("\n");
        }
//        System.out.println(bd);
        System.out.println(res);
    }
}