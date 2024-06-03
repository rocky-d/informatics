package nowcoder.contest.c20230717sqdx1;

class Fraction {
    private int numerator;
    private int denominator;

    public Fraction(int numerator, int denominator) {
        this.numerator = numerator;
        this.denominator = denominator;
    }

    public static Fraction addFractions(Fraction fraction1, Fraction fraction2) {
        int commonDenominator = fraction1.denominator * fraction2.denominator;
        int numerator1 = fraction1.numerator * fraction2.denominator;
        int numerator2 = fraction2.numerator * fraction1.denominator;
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