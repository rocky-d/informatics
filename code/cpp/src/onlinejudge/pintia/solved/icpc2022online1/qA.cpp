#include <bits/stdc++.h>

#define LF '\n'

using namespace std;

const int N = 1e6;
int lfts[N], rits[N], prefs[1 + N];

void solve() {
    int n, q;
    string s;
    int l, r;
    int cnt;
    int ll, rr;
    int cnt0, cnt1;
    int res;

    cin >> n >> q;
    cin >> s;

    cnt = 0;
    for (int i = n - 1; i > -1; i -= 1) {
        if ('0' == s[i]) {
            cnt = 0;
        } else {
            cnt += 1;
        }
        rits[i] = cnt;
    }
    cnt = 0;
    for (int i = 0; i < n; i += 1) {
        if ('0' == s[i]) {
            cnt = 0;
        } else {
            cnt += 1;
        }
        lfts[i] = cnt;
    }
    cnt = 0;
    for (int i = 0; i < n; i += 1) {
        if ('0' == s[i]) {
            cnt = 0;
            prefs[i + 1] = prefs[i];
        } else {
            cnt += 1;
            prefs[i + 1] = prefs[i + 1 - cnt] + (cnt + 1) / 2;
        }
    }
    while (0 < q--) {
        cin >> l >> r;
        ll = l + rits[l - 1];
        rr = r - lfts[r - 1];
        if (ll > rr) {
            res = 0;
        } else {
            cnt1 = prefs[rr] - prefs[ll - 1] + (rits[l - 1] + 1) / 2 + (lfts[r - 1] + 1) / 2;
            if (1 == 1 & rits[l - 1] && 1 == 1 & lfts[r - 1]) {
                cnt1 -= 1;
            }
            cnt0 = (r - l + 1) - 3 * cnt1;
            if (cnt0 <= 0) {
                res = 0;
            } else {
                res = cnt0 / 3;
            }
        }
        cout << res << LF;
    }
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    solve();
    return 0;
}
