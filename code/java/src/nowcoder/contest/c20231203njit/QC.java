package nowcoder.contest.c20231203;

import java.util.Arrays;
import java.util.Scanner;

public class QC {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[][] bt = new int[n][2];
        for (int i = 0; i < n; i++) {
            bt[i][0] = scanner.nextInt();
            bt[i][1] = scanner.nextInt();
        }
        Arrays.sort(bt, (o1, o2) -> o1[0] != o2[0] ? o1[0] - o2[0] : o1[1] - o2[1]);
        System.out.println(Arrays.deepToString(bt));
        long last = -bt[0][1];
        long ans = last;
        for (int i = 1; i < n; i++) {
            last = last + bt[i - 1][1] + bt[i - 1][0] - bt[i][1];
            ans = Math.max(ans, last);
        }
        System.out.println(ans);
    }
}