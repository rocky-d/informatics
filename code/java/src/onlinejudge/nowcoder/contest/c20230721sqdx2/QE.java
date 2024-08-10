package nowcoder.contest.c20230721sqdx2;

import java.util.Scanner;

class QE {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();

        long x, n;
        int y;
        boolean found;
        while (T > 0) {
            found = false;
            x = scanner.nextInt();
            y = -1;
            n = 1;
            while (x <= 1000000000L) {
                System.out.println("x = " + x);
                for (int i = 0; i < n; i++) {
                    System.out.println("x+i = "+ (x + i));
                    if (Double.toString(Math.sqrt(x + i)).endsWith(".0")) {
                        y = (int) Math.sqrt(x + i);
                        found = true;
                        break;
                    }
                }
                if (found) {break;}
                n *= 10;
                x *= 10;
            }
            System.out.println(found ? "Yes" : "No");
            System.out.println(y);
            --T;
        }
    }
}