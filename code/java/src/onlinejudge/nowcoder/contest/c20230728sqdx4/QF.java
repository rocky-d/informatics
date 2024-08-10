package nowcoder.contest.c20230728sqdx4;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

class QF {
    static int n;
    static List<int[]> a;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        a = new ArrayList<>();
        for (int i = 1; i < n + 1; i++) {
            a.add(new int[]{scanner.nextInt(), i});
        }
        a.sort(Comparator.comparingInt(x -> x[0]));
//        System.out.println(Arrays.deepToString(a.toArray()));
    }

    public static void main(String[] args) {
        input();
        int midP = n / 2, minCount, maxCount;
        double mean;
        for (int i = 1; i < n; i++) {
            mean = (a.get(0)[0] + a.get(a.size() - 1)[0]) / 2D;
            while (mean >= a.get(midP)[0]) {
                ++midP;
            }
            while (mean < a.get(midP)[0]) {
                --midP;
            }
            maxCount = 1 + midP;
            minCount = a.size() - maxCount;
            a.remove(minCount <= maxCount ? a.size() - 1 : 0);
        }
        System.out.println(a.get(0)[1]);
    }
}