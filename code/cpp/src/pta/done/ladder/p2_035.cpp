#include <iostream>
using namespace std;

int n, tree[31];

void fill(int index) {
    if (n < index)
        return;
    fill(2 * index);
    fill(2 * index + 1);
    cin >> tree[index];
}

int main() {
    cin >> n;
    fill(1);
    for (int i = 1; i <= n; i += 1){
        cout << tree[i] << ' ';
    }
    return 0;
}
