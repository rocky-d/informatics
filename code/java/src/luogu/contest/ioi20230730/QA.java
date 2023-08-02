package luogu.contest.ioi20230730;

import java.util.Arrays;
import java.util.Scanner;

class QA {
    static int n;
    static int[] array;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        array = new int[n];
        for (int i = 0; i < n; i++) {
            array[i] = scanner.nextInt();
        }
        Arrays.sort(array);
    }

    public static void main(String[] args) {
        input();
        int i;
        float j;
        int tmp;
        for (int p = 15; p < 76; p += 20) {
            tmp = (n - 1) * p;
            i = tmp / 100;
            j = tmp % 100 / 100F;
            System.out.printf("%.2f\n", (1 - j) * array[i] + j * array[i + 1]);
        }
    }
}