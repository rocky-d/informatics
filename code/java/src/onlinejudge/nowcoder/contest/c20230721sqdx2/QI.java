package onlinejudge.nowcoder.contest.c20230721sqdx2;

import java.util.Scanner;

class QI {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();

        final int cycle = 8;
        final String[] eightPieces =
                {"xxxxoooo", "ooooxxxx"};
        final String[][] modPieces = {
                {"\n", "x\n", "xx\n", "xxx\n", "xxxx\n", "xxxxo\n", "xxxxoo\n", "xxxxooo\n"},
                {"\n", "o\n", "oo\n", "ooo\n", "oooo\n", "oooox\n", "ooooxx\n", "ooooxxx\n"}};
        final String last = "xo";
        int n, m;
        StringBuilder twoLines, res;
        while (T > 0) {
            n = scanner.nextInt();
            m = scanner.nextInt();

            twoLines = new StringBuilder();
            for (int i = 0; i < m / cycle; i++) twoLines.append(eightPieces[0]);
            twoLines.append(modPieces[0][m % cycle]);
            for (int i = 0; i < m / cycle; i++) twoLines.append(eightPieces[1]);
            twoLines.append(modPieces[1][m % cycle]);

            res = new StringBuilder();
            for (int i = 0; i < n / 2; i++) res.append(twoLines);
            if ((n & 1) == 1) {
                for (int i = 0; i < m / 2; i++) res.append(last);
                res.append((m & 1) == 1 ? "x\n" : "\n");
            }
            System.out.print(res);
            --T;
        }
    }
}

/*
2
4 4
5 5

 *//*
3
6 6
7 7
13 13

 */
