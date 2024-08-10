package onlinejudge.luogu.solved;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class P1782 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String[] readTmp;

        int n, m, c;
        readTmp = bufferedReader.readLine().split(" ");
        n = Integer.parseInt(readTmp[0]);
        m = Integer.parseInt(readTmp[1]);
        c = Integer.parseInt(readTmp[2]);

        long[] dp = new long[c + 1];

        int count, vv, ww, dd, v, w;
        for (int i = 0; i < n; i++) {
            readTmp = bufferedReader.readLine().split(" ");
            vv = Integer.parseInt(readTmp[0]);
            ww = Integer.parseInt(readTmp[1]);
            dd = Integer.parseInt(readTmp[2]);
            count = 1;
            while (dd > count) {
                dd -= count;
                v = count * vv;
                w = count * ww;
                for (int j = c; j >= v; j--) {
                    dp[j] = Math.max(dp[j], dp[j - v] + w);
                }
                count <<= 1;
            }
            v = dd * vv;
            w = dd * ww;
            for (int j = c; j >= v; j--) {
                dp[j] = Math.max(dp[j], dp[j - v] + w);
            }
        }

        long aa, bb, cc;
        for (int i = 0; i < m; i++) {
            readTmp = bufferedReader.readLine().split(" ");
            aa = Long.parseLong(readTmp[0]);
            bb = Long.parseLong(readTmp[1]);
            cc = Long.parseLong(readTmp[2]);
            for (int j = c; j > -1; j--) {
                for (int x = 0; x <= j; x++) {
                    dp[j] = Math.max(dp[j], dp[j - x] + aa * x * x + bb * x + cc);
                }
            }
        }

        System.out.println(dp[c]);
    }
}
