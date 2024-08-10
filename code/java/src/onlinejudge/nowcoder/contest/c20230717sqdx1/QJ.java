package onlinejudge.nowcoder.contest.c20230717sqdx1;

import java.util.Arrays;
import java.util.Scanner;

class QJ {
    private static String mainMethod() {
        Scanner scanner = new Scanner(System.in);

        final int n = scanner.nextInt();
        final int m = scanner.nextInt();
        final int nm = n + m;

        final int wager = (int) Math.ceil(Math.log(nm) / Math.log(2));
        final int mon_max = nm - 1 + (int) Math.pow(2, wager - 1);
        int[][][] dp = new int[1 + mon_max][1 + wager][2];

        for (int j = 0; j < nm; ++j) {
            dp[j][wager][1] = -1;
        }
        for (int i = 0; i < wager; ++i) {
            for (int j = 0; j < (int) Math.pow(2, i); ++j) {
                dp[j][i][1] = -1;
            }
        }

        for (int i = nm; i < 1 + mon_max; ++i) {
            for (int j = 0; j < 1 + wager; ++j) {
                dp[i][j][0] = 1;
                dp[i][j][1] = 1;
            }
        }

        for (int i = (int) Math.pow(2, wager - 1); i < nm; ++i) {
            dp[i][wager - 1][0] = 1;
            dp[i][wager - 1][1] = 2;
        }
        for (int[][] rec : dp) System.out.println(Arrays.deepToString(rec));

        for (int i = wager - 2; i >= 0; --i) {
            for (int j = nm - 1; j >= nm - (int) Math.pow(2, i); --j) {
                int a, b, c, d;
                a = j - (int) Math.pow(2, i);
                b = i + 1;
                c = j + (int) Math.pow(2, i);
                d = 0;

            }
        }


//        for (int i = 0; i <; ++i) {
//
//        }

        return null;
    }

    public static void main(String[] args) {
        System.out.print(mainMethod());
    }
}

class Fraction1 {
    private int numerator;
    private int denominator;

    public Fraction1(int numerator, int denominator) {
        this.numerator = numerator;
        this.denominator = denominator;
    }

    public static Fraction addFractions(Fraction fraction1, Fraction fraction2) {
        int commonDenominator = fraction1.getDenominator() * fraction2.getDenominator();
        int numerator1 = fraction1.getNumerator() * fraction2.getDenominator();
        int numerator2 = fraction2.getNumerator() * fraction1.getDenominator();
        int sumOfNumerators = numerator1 + numerator2;

        return new Fraction(sumOfNumerators, commonDenominator);
    }

    public int getNumerator() {
        return numerator;
    }

    public int getDenominator() {
        return denominator;
    }

    public static void main(String[] args) {
        Fraction fraction1 = new Fraction(1, 2);
        Fraction fraction2 = new Fraction(3, 4);
        Fraction sum = addFractions(fraction1, fraction2);
        System.out.println("分子: " + sum.getNumerator());
        System.out.println("分母: " + sum.getDenominator());
    }
}