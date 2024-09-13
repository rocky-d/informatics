#include <bits/stdc++.h>

#define LF '\n'
#define NO "No"
#define YES "Yes"

using namespace std;

void solve() {
    int n; cin >> n;
    string s; cin >> s;

    int side = sqrt(n);
    if (n != side * side) {
        cout << NO << LF;
        return;
    }
    for (int i = 0; i < side; ++i) {
        if (!('1' == s[i])) {
            cout << NO << LF;
            return;
        }
    }
    for (int row = 1; row < side - 1; ++row) {
        int lo = row * side;
        int hi = lo + side - 1;
        if (!('1' == s[lo])) {
            cout << NO << LF;
            return;
        }
        for (int i = lo + 1; i < hi; ++i) {
            if (!('0' == s[i])) {
                cout << NO << LF;
                return;
            }
        }
        if (!('1' == s[hi])) {
            cout << NO << LF;
            return;
        }
    }
    for (int i = n - side; i < n; ++i) {
        if (!('1' == s[i])) {
            cout << NO << LF;
            return;
        }
    }
    cout << YES << LF;
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int t; cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
