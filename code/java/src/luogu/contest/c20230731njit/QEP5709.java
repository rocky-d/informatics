package luogu.contest.c20230731njit;

import java.util.Scanner;

class QEP5709 {
    private static String mainMethod() {
        Scanner scanner = new Scanner(System.in);

        final byte m = scanner.nextByte();
        final byte t = scanner.nextByte();
        final short s = scanner.nextShort();
        if (t == 0) {
            return String.valueOf(0);
        } else {
            return String.valueOf(Math.max(0, m - (short) Math.ceil((double) s / t)));
        }
    }

    public static void main(String[] args) {
        System.out.print(mainMethod());
    }
}