#include <bits/stdc++.h>
using namespace std;

const int M_MAX = 1286;
const int N_MAX = 128;
const int L_MAX = 60;

int m, n, l, t;
char slices[L_MAX][M_MAX][N_MAX];

int main() {
    cin >> m >> n >> l >> t;
    for (int i = 0; i < l; i += 1) {
        for (int j = 0; j < m; j += 1) {
            for (int k = 0; k < n; k += 1) {
                cin >> slices[i][j][k];
            }
        }
    }

    int ans;
    ans = 0;
    bool seen[L_MAX][M_MAX][N_MAX];
    for (int i = 0; i < l; i += 1) {
        for (int j = 0; j < m; j += 1) {
            for (int k = 0; k < n; k += 1) {
                seen[i][j][k] = false;
            }
        }
    }
    for (int i = 0; i < l; i += 1) {
        for (int j = 0; j < m; j += 1) {
            for (int k = 0; k < n; k += 1) {
                if ('1' == slices[i][j][k] && false == seen[i][j][k]) {
                    int vol;
                    vol = 0;
                    int stack[100][3], stack_len;
                    stack_len = 0;
                    stack[stack_len][0] = i;
                    stack[stack_len][1] = j;
                    stack[stack_len][2] = k;
                    stack_len += 1;
                    while (0 < stack_len) {
                        stack_len -= 1;
                        int x, y, z;
                        x = stack[stack_len][0];
                        y = stack[stack_len][1];
                        z = stack[stack_len][2];
                        if (false == seen[x][y][z]) {
                            vol += 1;
                            seen[x][y][z] = true;
                            if (0 <= x - 1 && '1' == slices[x - 1][y][z] && false == seen[x - 1][y][z]) {
                                stack[stack_len][0] = x - 1;
                                stack[stack_len][1] = y;
                                stack[stack_len][2] = z;
                                stack_len += 1;
                            }
                            if (0 <= y - 1 && '1' == slices[x][y - 1][z] && false == seen[x][y - 1][z]) {
                                stack[stack_len][0] = x;
                                stack[stack_len][1] = y - 1;
                                stack[stack_len][2] = z;
                                stack_len += 1;
                            }
                            if (0 <= z - 1 && '1' == slices[x][y][z - 1] && false == seen[x][y][z - 1]) {
                                stack[stack_len][0] = x;
                                stack[stack_len][1] = y;
                                stack[stack_len][2] = z - 1;
                                stack_len += 1;
                            }
                            if (x + 1 < l && '1' == slices[x + 1][y][z] && false == seen[x + 1][y][z]) {
                                stack[stack_len][0] = x + 1;
                                stack[stack_len][1] = y;
                                stack[stack_len][2] = z;
                                stack_len += 1;
                            }
                            if (y + 1 < m && '1' == slices[x][y + 1][z] && false == seen[x][y + 1][z]) {
                                stack[stack_len][0] = x;
                                stack[stack_len][1] = y + 1;
                                stack[stack_len][2] = z;
                                stack_len += 1;
                            }
                            if (z + 1 < n && '1' == slices[x][y][z + 1] && false == seen[x][y][z + 1]) {
                                stack[stack_len][0] = x;
                                stack[stack_len][1] = y;
                                stack[stack_len][2] = z + 1;
                                stack_len += 1;
                            }
                        }
                    }
                    if (t <= vol) {
                        ans += vol;
                    }
                }
            }
        }
    }
    cout << ans << endl;
    return 0;
}
