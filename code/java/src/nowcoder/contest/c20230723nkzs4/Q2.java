package nowcoder.contest.c20230723nkzs4;

import java.util.Scanner;

class Q2 {
    static long n;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextLong();
    }

    public static void main(String[] args) {
        input();
        System.out.print(0 == n % 3 ? n / 3 - 1 : 2 * (n / 3));
    }
}
/*
1: 0
2: 0
 3: 0
4: 2
5: 2
 6: 1
7: 4
8: 4
 9: 2
10: 6
11: 6
 12: 3
13: 8
14: 8
 15: 4
16: 10
17: 10
 18: 5
19: 12
 */