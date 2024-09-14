#include <bits/stdc++.h>

#define LF '\n'

using namespace std;

void solve() {
    int l, r; cin >> l >> r;

    int diff = r - l;
    int lo = -1, hi = 1e5 + 1;
    while (1 < hi - lo) {
        long long mid = lo + hi >> 1;
        if (mid * (mid + 1) / 2 <= diff) {
            lo = mid;
        } else {
            hi = mid;
        }
    }
    cout << hi << LF;
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int t; cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
