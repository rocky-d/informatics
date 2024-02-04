#include <bits/stdc++.h>

using namespace std;

typedef struct {
    int x, y, z;
} Coord;

const int M_MAX = 1 + 1286 + 1;
const int N_MAX = 1 + 128 + 1;
const int L_MAX = 1 + 60 + 1;
const int OFFSETS[6][3] = {{-1, 0, 0}, {0, -1, 0}, {0, 0, -1}, {1, 0, 0}, {0, 1, 0}, {0, 0, 1}};

int m, n, l, t;
char slices[L_MAX][M_MAX][N_MAX];

int ans, vol;
bool seen[L_MAX][M_MAX][N_MAX];
Coord cod, cod_next;
queue<Coord> que;

int main() {
    cin >> m >> n >> l >> t;
    memset(slices, '0', sizeof(slices));
    for (int i = 1; i < 1 + l; i += 1) {
        for (int j = 1; j < 1 + m; j += 1) {
            for (int k = 1; k < 1 + n; k += 1) {
                cin >> slices[i][j][k];
            }
        }
    }

    ans = 0;
    memset(seen, false, sizeof(seen));
    for (int i = 1; i < 1 + l; i += 1) {
        cod.x = i;
        for (int j = 1; j < 1 + m; j += 1) {
            cod.y = j;
            for (int k = 1; k < 1 + n; k += 1) {
                cod.z = k;
                if ('1' == slices[cod.x][cod.y][cod.z] && !seen[cod.x][cod.y][cod.z]) {
                    que.push(cod);
                    seen[cod.x][cod.y][cod.z] = true;
                    vol = 1;
                    while (!que.empty()) {
                        cod = que.front();
                        que.pop();
                        for (int offset_i = 0; offset_i < 6; offset_i += 1) {
                            cod_next.x = cod.x + OFFSETS[offset_i][0];
                            cod_next.y = cod.y + OFFSETS[offset_i][1];
                            cod_next.z = cod.z + OFFSETS[offset_i][2];
                            if ('1' == slices[cod_next.x][cod_next.y][cod_next.z] && !seen[cod_next.x][cod_next.y][cod_next.z]) {
                                que.push(cod_next);
                                seen[cod_next.x][cod_next.y][cod_next.z] = true;
                                vol += 1;
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
