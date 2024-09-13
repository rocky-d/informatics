#include <bits/stdc++.h>

#define LF '\n'
#define NO "NO"
#define YES "YES"

using namespace std;

void solve() {
    string a; cin >> a;

    cout << (3 <= a.size() && "10" == a.substr(0, 2) && '0' != a[2] && 2 <= stoi(a.substr(2)) ? YES : NO) << LF;
}

int main() {
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int t; cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
