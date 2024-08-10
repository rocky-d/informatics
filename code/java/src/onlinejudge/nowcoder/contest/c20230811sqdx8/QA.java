package onlinejudge.nowcoder.contest.c20230811sqdx8;

import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

class QA {
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt(), c;
        Set<String> res = new TreeSet<>(), set = new TreeSet<>();

        c = scanner.nextInt();
        for (int j = 0; j < c; j++) {
            res.add(scanner.next());
        }
        for (int i = 1; i < n; i++) {
            c = scanner.nextInt();
            for (int j = 0; j < c; j++) {
                set.add(scanner.next());
            }
            res.retainAll(set);
        }

        System.out.println(res.size());
        for (String s : res) {
            System.out.println(s);
        }
    }
}
