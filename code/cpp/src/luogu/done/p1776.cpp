#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int i, j, n, w, vv, ww, mm, count, vvv, www;
    cin >> n >> w;

    vector<int> dp(1 + w, 0);

    for (i = 0; i < n; ++i) {
        vv, ww, mm;
        cin >> vv >> ww >> mm;
        count = 1;
        while (mm > count) {
            mm -= count;
            vvv = vv * count;
            www = ww * count;
            for (j = w; j >= www; --j) {
                dp[j] = max(dp[j], dp[j - www] + vvv);
            }
            count <<= 1;
        }
        vvv = vv * mm;
        www = ww * mm;
        for (j = w; j >= www; --j) {
            dp[j] = max(dp[j], dp[j - www] + vvv);
        }
    }

    cout << dp[w] << endl;

    return 0;
}