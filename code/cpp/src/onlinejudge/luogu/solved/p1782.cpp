#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    long i, j, n, m, c, vv, ww, dd, count, v, w, aa, bb, cc, x;
    cin >> n >> m >> c;

    vector<long> dp(1 + c, 0);

    for (i = 0; i < n; i++) {
        cin >> vv >> ww >> dd;
        count = 1;
        while (dd > count) {
            dd -= count;
            v = count * vv;
            w = count * ww;
            for (j = c; j >= v; j--) {
                dp[j] = max(dp[j], dp[j - v] + w);
            }
            count <<= 1;
        }
        v = dd * vv;
        w = dd * ww;
        for (j = c; j >= v; j--) {
            dp[j] = max(dp[j], dp[j - v] + w);
        }
    }

    for (i = 0; i < m; i++) {
        cin >> aa >> bb >> cc;
        for (j = c; j > -1; j--) {
            for (x = 0; x <= j; x++) {
                dp[j] = max(dp[j], dp[j - x] + aa * x * x + bb * x + cc);
            }
        }
    }

    cout << dp[c] << endl;

    return 0;
}
