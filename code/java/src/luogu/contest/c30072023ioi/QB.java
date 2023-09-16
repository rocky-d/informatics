package luogu.contest.c30072023ioi;

import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

class QB {
    static int len1, len2;
    static int[] arr1, arr2;
    static void input() {
        Scanner scanner = new Scanner(System.in);
        len1 = scanner.nextInt();
        arr1 = new int[len1];
        for (int i = 0; i < len1; i++) {
            arr1[i] = scanner.nextInt();
        }
        len2 = scanner.nextInt();
        arr2 = new int[len2];
        for (int i = 0; i < len2; i++) {
            arr2[i] = scanner.nextInt();
        }
    }

    public static void main(String[] args) {
        input();
        Set<Integer> res = new TreeSet<>();
        int p1 = 0, p2 = 0;
        int x, y;
        while (p1 < len1 && p2 < len2) {
            x = arr1[p1];
            y = arr2[p2];
            if (x == y) {
                res.add(x);
                ++p1;
                ++p2;
            } else if (x < y) {
                ++p1;
            } else {
                ++p2;
            }
        }
        for (int i : res) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}