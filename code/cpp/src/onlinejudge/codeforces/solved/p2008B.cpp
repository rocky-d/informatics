#include <bits/stdc++.h>

#define LF '\n'

using namespace std;

void solve() {
    int n; cin >> n;
    string s; cin >> s;

    bool res = true;
    int side = sqrt(n);
    if (n != side * side) {
        cout << "No" << LF;
        return;
    }
    for (int i = 0; i < side; ++i) {
        if (!('1' == s[i])) {
            res = false;
            break;
        }
    }
    for (int row = 1; row < side - 1; ++row) {
        int lo = row * side;
        int hi = lo + side - 1;
        if (!('1' == s[lo])) {
            res = false;
            break;
        }
        for (int i = lo + 1; i < hi; ++i) {
            if (!('0' == s[i])) {
                res = false;
                break;
            }
        }
        if (!('1' == s[hi])) {
            res = false;
            break;
        }
    }
    for (int i = n - side; i < n; ++i) {
        if (!('1' == s[i])) {
            res = false;
            break;
        }
    }
    cout << (res ? "Yes" : "No") << LF;
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int t; cin >> t;
    while (t--) {
        solve();
    }
}
