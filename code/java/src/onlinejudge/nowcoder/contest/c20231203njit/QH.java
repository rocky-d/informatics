package nowcoder.contest.c20231203njit;

import java.util.Scanner;

public class QH {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine();
        String string = scanner.nextLine();
        int h = Integer.parseInt(string.substring(0, 2));
        int m = Integer.parseInt(string.substring(2, 4));
        int s = Integer.parseInt(string.substring(4, 6));
        int currentS = s + 60 * m + 3600 * h;
        int oneDayS = 3600 * n;
        int halfDayS = oneDayS / 2;
        int need = halfDayS - currentS + (halfDayS < currentS ? oneDayS : 0);
        h = need / 3600;
        m = need / 60 - 60 * h;
        s = need - 3600 * h - 60 * m;
        System.out.println(h + "h" + m + "m" + s + "s");
    }
}