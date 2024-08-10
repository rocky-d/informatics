package onlinejudge.nowcoder.contest.c20230807sqdx7;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class QI {
    static final int CONST = 401, MOD = 998244353, ZERO_ONE = '0' + '1';
    static List<List<String>> stringSet;

    static int count(String s) {
        int res = 0;
        for (char ch : s.toCharArray()) {
            if ('?' == ch) {
                ++res;
            }
        }
        return res;
    }

    static void addNewString(String sb) {
        int len = sb.length(), a, b;
        List<String> subSet = stringSet.get(len);
        String sa;
        boolean match, undone = true;
        for (int i = 0; i < subSet.size(); i++) {
            sa = subSet.get(i);
            match = true;
            for (int j = 0; j < len; j++) {
                if (ZERO_ONE == sa.charAt(j) + sb.charAt(j)) {
                    match = false;
                    break;
                }
            }
            if (match) {
                a = count(sa);
                b = count(sb);
                if (b > a) {
                    subSet.remove(i);
                    subSet.add(sb);
                }
                undone = false;
                break;
            }
        }
        if (undone) {
            subSet.add(sb);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        stringSet = new ArrayList<>(CONST);
        for (int i = 0; i < CONST; i++) {
            stringSet.add(new ArrayList<>());
        }

        for (int i = 0; i < n; i++) {
            addNewString(scanner.next());
        }

        long res = 0;
        for (List<String> subSet : stringSet) {
            for (String sa : subSet) {
//                res += fastExponentiation(count(sa));
                res += (long) Math.pow(2, count(sa));
                res %= MOD;
            }
        }
        System.out.println(res);
    }

    static long fastExponentiation(int exponent) {
        if (exponent == 0) {
            return 1;
        }

        long result = 1;
        long baseValue = 2;
        while (exponent > 0) {
            if (1 == (1 & exponent)) {
                result *= baseValue;
            }
            baseValue <<= 1;
            exponent >>= 1;
        }

        return result;
    }
}