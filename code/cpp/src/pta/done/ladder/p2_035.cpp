#include <iostream>

using namespace std;

const int N_MAX = 30;

int n, postorder[N_MAX];

int levelorder[N_MAX], p;

void dfs(int index) {
    if (n <= index)
        return;
    dfs(1 + 2 * index);
    dfs(2 + 2 * index);
    levelorder[index] = postorder[p];
    p += 1;
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i += 1) {
        cin >> postorder[i];
    }

    p = 0;
    dfs(0);
    cout << levelorder[0];
    for (int i = 1; i < n; i += 1) {
        cout << ' ' << levelorder[i];
    }
    cout << endl;
    return 0;
}
