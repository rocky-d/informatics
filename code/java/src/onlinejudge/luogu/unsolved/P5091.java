package onlinejudge.luogu.unsolved;

import java.util.Scanner;

class P5091 {
    private static String mainMethod() {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int m = scanner.nextInt();
        long b = scanner.nextLong();

//        System.out.println(a);
//        System.out.println(m);
//        System.out.println(b);

        long res = 1;
        a %= m;
        while (b > 0) {
            if ((b & 1) == 1)
                res = res * a % m;
            b >>>= 1;
            a = a * a % m;
        }

        return String.valueOf(res);
    }

    public static void main(String[] args) {
        System.out.print(mainMethod());
    }
}
