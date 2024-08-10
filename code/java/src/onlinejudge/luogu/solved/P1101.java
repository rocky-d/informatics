package luogu.done;

import java.util.Scanner;

class P1101 {
    static final char FILLER = '*';
    static final char[] WORD = "yizhong".toCharArray();
    static int n;
    static char[][] matrix, res;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        matrix = new char[n][];
        for (int i = 0; i < n; i++) {
            matrix[i] = scanner.next().toCharArray();
        }
    }

    static void search(int x, int y) {
        int tmpX, tmpY;
        int[] stepX = {0, 1, 1, 1, 0, -1, -1, -1}, stepY = {1, 1, 0, -1, -1, -1, 0, 1};
        boolean isWord = true;
        for (int i = 0; i < 8; i++) {
            tmpX = x;
            tmpY = y;
            for (char ch : WORD) {
                if (tmpX < 0 || tmpX >= n || tmpY < 0 || tmpY >= n || matrix[tmpX][tmpY] != ch) {
                    isWord = false;
                    break;
                }
                tmpX += stepX[i];
                tmpY += stepY[i];
            }
            if (isWord) {
                tmpX = x;
                tmpY = y;
                for (char ch : WORD) {
                    res[tmpX][tmpY] = ch;
                    tmpX += stepX[i];
                    tmpY += stepY[i];
                }
            } else {
                isWord = true;
            }
        }
    }

    public static void main(String[] args) {
        input();
        res = new char[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                res[i][j] = FILLER;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (WORD[0] == matrix[i][j]) {
                    search(i, j);
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(res[i][j]);
            }
            System.out.println();
        }
    }
}