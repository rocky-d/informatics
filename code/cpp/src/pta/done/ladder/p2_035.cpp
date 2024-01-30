#include <iostream>
using namespace std;

int n, tree[30];

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
    for (int i = 1; i < n; i += 1){
        cout << ' ' << tree[i];
    }
    return 0;
}
