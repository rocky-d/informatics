package luogu.contest.c31072023icpc;

import java.util.Scanner;

class QUP5730 {
    static int n;
    static String nums;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        nums = scanner.next();
    }

    public static void main(String[] args) {
        input();
        String[][] table = {
                {"XXX", "..X", "XXX", "XXX", "X.X", "XXX", "XXX", "XXX", "XXX", "XXX"},
                {"X.X", "..X", "..X", "..X", "X.X", "X..", "X..", "..X", "X.X", "X.X"},
                {"X.X", "..X", "XXX", "XXX", "XXX", "XXX", "XXX", "..X", "XXX", "XXX"},
                {"X.X", "..X", "X..", "..X", "..X", "..X", "X.X", "..X", "X.X", "..X"},
                {"XXX", "..X", "XXX", "XXX", "..X", "XXX", "XXX", "..X", "XXX", "XXX"}};
        StringBuilder res = new StringBuilder();
        for (int row = 0; row < 5; row++) {
            for (char num : nums.toCharArray()) {
                res.append(table[row][Character.getNumericValue(num)]).append('.');
            }
            res.deleteCharAt(res.length() - 1);
            res.append('\n');
        }
        System.out.print(res);
    }
}