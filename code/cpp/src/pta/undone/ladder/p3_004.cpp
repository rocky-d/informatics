#include <bits/stdc++.h>
using namespace std;

typedef struct {
    int x, y, z;
} Coord;

const int M_MAX = 1 + 1286 + 1;
const int N_MAX = 1 + 128 + 1;
const int L_MAX = 1 + 60 + 1;

int m, n, l, t;
char slices[L_MAX][M_MAX][N_MAX];

int ans, vol;
bool seen[L_MAX][M_MAX][N_MAX];
Coord coord, next_coord;
queue<Coord> queue_;
const int OFFSETS[6][3] = {{-1, 0, 0}, {0, -1, 0}, {0, 0, -1}, {1, 0, 0}, {0, 1, 0}, {0, 0, 1}};

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
        for (int j = 1; j < 1 + m; j += 1) {
            for (int k = 1; k < 1 + n; k += 1) {
                coord.x = i;
                coord.y = j;
                coord.z = k;
                if ('1' == slices[coord.x][coord.y][coord.z]
                        && false == seen[coord.x][coord.y][coord.z]) {
                    queue_.push(coord);
                    seen[coord.x][coord.y][coord.z] = true;
                    vol = 1;
                    while (0 < queue_.size()) {
                        coord = queue_.front();
                        queue_.pop();
                        for (int offset_i = 0; offset_i < 6; offset_i += 1) {
                            next_coord.x = coord.x + OFFSETS[offset_i][0];
                            next_coord.y = coord.y + OFFSETS[offset_i][1];
                            next_coord.z = coord.z + OFFSETS[offset_i][2];
                            if ('1' == slices[next_coord.x][next_coord.y][next_coord.z]
                                    && false == seen[next_coord.x][next_coord.y][next_coord.z]) {
                                queue_.push(next_coord);
                                seen[next_coord.x][next_coord.y][next_coord.z] = true;
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
