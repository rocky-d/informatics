#include <iostream>
using namespace std;

int n, tree[30];

void fill(int index) {
    if (n <= index)
        return;
    fill(2 * index + 1);
    fill(2 * index + 2);
    cin >> tree[index];
}

int main() {
    cin >> n;
    fill(0);
    cout << tree[0];
    for (int i = 1; i < n; i += 1){
        cout << ' ' << tree[i];
    }
    return 0;
}
