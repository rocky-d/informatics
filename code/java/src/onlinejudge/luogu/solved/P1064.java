package onlinejudge.luogu.solved;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class P1064 {
    static final byte MULTIPLE = 10;
    static int n, n1, m, m1;
    static List<int[]> mainItem;
    static List<int[][]> attachedItem;

    static void input() {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt() / MULTIPLE;
        n1 = n + 1;
        m = scanner.nextInt();
        m1 = m + 1;

        mainItem = new ArrayList<>(m1);
        mainItem.add(null);
        attachedItem = new ArrayList<>(m1);
        attachedItem.add(null);
        int v, p, q;
        int[][] addend;
        for (int i = 1; i < m1; i++) {
            v = scanner.nextInt();
            p = scanner.nextInt();
            q = scanner.nextInt();
            if (0 == q) {
                while (mainItem.size() <= i) {
                    mainItem.add(null);
                }
                mainItem.set(i, new int[]{v / MULTIPLE, v * p});
            } else {
                while (attachedItem.size() <= q) {
                    attachedItem.add(new int[0][]);
                }
                if (0 == attachedItem.get(q).length) {
                    addend = new int[1][2];
                    addend[0] = new int[]{v / MULTIPLE, v * p};
                } else {
                    addend = new int[2][2];
                    addend[0] = attachedItem.get(q)[0];
                    addend[1] = new int[]{v / MULTIPLE, v * p};
                }
                attachedItem.set(q, addend);
            }
        }
        while (mainItem.size() > attachedItem.size()) {
            attachedItem.add(new int[0][]);
        }
//        System.out.println(Arrays.deepToString(items1.toArray()));
//        System.out.println(Arrays.deepToString(items2.toArray()));
    }

    public static void main(String[] args) {
        input();
        int[] dp = new int[n1];

        int attachment, jLow;
        int[] item1, item2, item3;
        for (int i = 1; i < mainItem.size(); i++) {
            if (null == (item1 = mainItem.get(i))) {
                continue;
            }
            attachment = attachedItem.get(i).length;
            item2 = attachment > 0 ? attachedItem.get(i)[0] : null;
            item3 = attachment > 1 ? attachedItem.get(i)[1] : null;

            jLow = Math.max(0, item1[0] - 1);
            for (int j = n; j > jLow; j--) {
                dp[j] = Math.max(dp[j], dp[j - item1[0]] + item1[1]);
                if (1 == attachment) {
                    if (j >= item1[0] + item2[0]) {
                        dp[j] = Math.max(dp[j], dp[j - item1[0] - item2[0]] + item1[1] + item2[1]);
                    }
                } else if (2 == attachment) {
                    if (j >= item1[0] + item2[0]) {
                        dp[j] = Math.max(dp[j], dp[j - item1[0] - item2[0]] + item1[1] + item2[1]);
                        if (j >= item1[0] + item2[0] + item3[0]) {
                            dp[j] = Math.max(dp[j], dp[j - item1[0] - item2[0] - item3[0]] + item1[1] + item2[1] + item3[1]);
                        }
                    }
                    if (j >= item1[0] + item3[0]) {
                        dp[j] = Math.max(dp[j], dp[j - item1[0] - item3[0]] + item1[1] + item3[1]);
                        if (j >= item1[0] + item2[0] + item3[0]) {
                            dp[j] = Math.max(dp[j], dp[j - item1[0] - item2[0] - item3[0]] + item1[1] + item2[1] + item3[1]);
                        }
                    }
                }
            }
        }
//        for (int i = 0; i < dp.length; i++) {
//            System.out.print(i + ": " + dp[i] + ", ");
//        }
        System.out.println(dp[n]);
    }
}