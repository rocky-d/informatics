#include <iostream>
using namespace std;

const int N_MAX = 30;

int n, tree[N_MAX];

void dfs(int index) {
    if (n <= index)
        return;
    dfs(2 * index + 1);
    dfs(2 * index + 2);
    cin >> tree[index];
}

int main() {
    cin >> n;
    dfs(0);
    cout << tree[0];
    for (int i = 1; i < n; i += 1) {
        cout << ' ' << tree[i];
    }
    cout << endl;
    return 0;
}
