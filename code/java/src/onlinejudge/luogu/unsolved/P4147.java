package onlinejudge.luogu.unsolved;

import java.util.Arrays;
import java.util.Scanner;

class P4147 {
    private static String mainMethod() {
        Scanner scanner = new Scanner(System.in);

        final int N = scanner.nextInt();
        final int M = scanner.nextInt();
        scanner.nextLine();
        String s;
        char[][] table = new char[N][M];
        for (int i = 0; i < N; i++) {
            s = scanner.nextLine();
            for (int j = 0; j < M; j++) {
                table[i][j] = s.charAt(2 * j);
            }
        }
//        System.out.println("N = " + N);
//        System.out.println("M = " + M);
//        System.out.println("table =");
//        for (char[] rec : table) {
//            System.out.println(Arrays.toString(rec));
//        }

        int[][][] dp = new int[N][M][2];
        if (table[0][0] == 'R') {
            dp[0][0][0] = -1;
        }
        for (int i = 1; i < N; i++) {
            if (table[i][0] == 'R') {
                dp[i][0][0] = -1;
            } else {
                dp[i][0][0] = dp[i - 1][0][0] == -1 ? i : dp[i - 1][0][0];
            }
        }
        for (int j = 1; j < M; j++) {
            if (table[0][j] == 'R') {
                dp[0][j][0] = -1;
            } else {
                dp[0][j][1] = dp[0][j - 1][0] == -1 ? j : dp[0][j - 1][1];
            }
        }
//        System.out.println("dp =");
//        for (int[][] rec : dp) {
//            System.out.println(Arrays.deepToString(rec));
//        }

        int ia, ib, ja, jb;
        int res = 1;
        for (int i = 1; i < N; i++) {
//            System.out.println();
//            System.out.println("i = " + i);
            for (int j = 1; j < M; j++) {
//                System.out.println("  j = " + j);
                if (table[i][j] == 'R') {
                    dp[i][j][0] = -1;
                } else {
                    if (dp[i - 1][j][0] == -1 && dp[i][j - 1][0] == -1) {
                        dp[i][j][0] = i;
                        dp[i][j][1] = j;
                        continue;
                    } else if (dp[i - 1][j][0] == -1) {
                        dp[i][j][0] = i;
                        dp[i][j][1] = dp[i][j - 1][1];
                        res = Math.max(res, j + 1 - dp[i][j][1]);
                        continue;
                    } else if (dp[i][j - 1][0] == -1) {
                        dp[i][j][0] = dp[i - 1][j][0];
                        dp[i][j][1] = j;
                        res = Math.max(res, i + 1 - dp[i][j][0]);
                        continue;
                    }
                    if (dp[i - 1][j][0] == dp[i][j - 1][0] && dp[i - 1][j][1] == dp[i][j - 1][1]) {
                        dp[i][j][0] = dp[i - 1][j][0];
                        dp[i][j][1] = dp[i][j - 1][1];
                    } else {
                        ia = dp[i - 1][j][0];
                        ib = dp[i - 1][j][1];
                        ja = dp[i][j - 1][0];
                        jb = dp[i][j - 1][1];
                        for (int ki = i - 1; ki >= dp[i][j - 1][0]; ki--) {
//                            System.out.println("    ki = " + ki);
                            if (table[ki][j] == 'R') {
                                ja = ki + 1;
                                break;
                            }
                        }
                        for (int kj = j - 1; kj >= dp[i - 1][j][1]; kj--) {
//                            System.out.println("    kj = " + kj);
                            if (table[i][kj] == 'R') {
                                ib = kj + 1;
                                break;
                            }
                        }
//                        System.out.println("      ia, ib = [" + ia + ", " + ib + "]");
//                        System.out.println("      ja, jb = [" + ja + ", " + jb + "]");
                        if ((i + 1 - ia) * (j + 1 - ib) >
                                (i + 1 - ja) * (j + 1 - jb)) {
                            dp[i][j][0] = ia;
                            dp[i][j][1] = ib;
                        } else {
                            dp[i][j][0] = ja;
                            dp[i][j][1] = jb;
                        }
                        res = Math.max(res, (i + 1 - dp[i][j][0]) * (j + 1 - dp[i][j][1]));
                    }
                }
            }
        }
//        System.out.println();
//        System.out.println("dp =");
//        for (int[][] rec : dp) {
//            System.out.println(Arrays.deepToString(rec));
//        }

        return String.valueOf(3 * res);
    }

    public static void main(String[] args) {
        System.out.print(mainMethod());
    }
}

/*
20 20
F F F F F F F F F F F F F F F R R R F F
F F F F F F F F F F F F F F F R R R F F
F F F F F F F F F F F F F F F R R R F F
R R R R R F F F F F F F F F F R R R F F
R R R R R F F F F F F F F F F R R R F F
R R R R R F F F F F F F F F F R R R F F
R R R F F F F F F F F F F F F R R R F F
R R F F F F F F F F F F F F F R R R F F
R F F F F F F F F F F F F F F R R R F F
R R R R R R R R R F F F F F F R R R F F
R R R R R R R R R R R R R R R R R R F F
R R R R R R R R R R R R R R R R R R F F
R R R R R R R R R R R R R R R R R R F F
R R R R R R R R R R R R R R R R R R F F
R R R R R R R R R R R R R R R R R R F F
R R R R R R R R R R R R R R R R R R F F
R R R R R R R R R R R R R R R R R R F F
R R R R R R R R R R R R R R R R R R F F
R R R R R R R R R R R R R R R R R R F F
R R R R R R R R R R R R R R R R R R F F

270
*/