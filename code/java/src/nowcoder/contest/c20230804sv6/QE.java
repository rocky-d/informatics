package nowcoder.contest.cows20230804;

import java.util.Scanner;

class QE {
    static Scanner scanner = new Scanner(System.in);
    static short t;
    static int n, n1, q, l, r, k;
    static boolean[] a = new boolean[100001];

    public static void main(String[] args) {
        t = scanner.nextShort();

        int curr, countOdd;
        boolean isYES, foundOdd;
        while (0 < t--) {
            n = scanner.nextInt();
            n1 = n + 1;
            q = scanner.nextInt();
            for (int i = 1; i < n1; i++) {
                a[i] = 1 == (1 & scanner.nextLong());
            }
            while (0 < q--) {
                l = scanner.nextInt();
                r = scanner.nextInt();
                k = scanner.nextInt();
                if (r - l + 1 < k) {
                    System.out.println("NO");
                    continue;
                }

                curr = l;
                while (true) {
                    if (k == 1) {
                        countOdd = 0;
                        while (curr <= r) {
                            if (a[curr]) {
                                ++countOdd;
                            }
                            ++curr;
                        }
                        isYES = 0 == (1 & countOdd);
                        break;
                    }

                    if (a[curr]) {
                        foundOdd = false;
                        while (curr <= r) {
                            if (a[curr]) {
                                foundOdd = true;
                                break;
                            } else {
                                ++curr;
                            }
                        }
                        if (foundOdd) {
                            ++curr;
                            --k;
                        } else {
                            isYES = false;
                            break;
                        }
                    } else {
                        ++curr;
                        --k;
                    }
                }
                System.out.println(isYES ? "YES" : "NO");
            }
        }
    }
}