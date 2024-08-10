#include <bits/stdc++.h>

using namespace std;

typedef struct {
    int x, y;
} Coord;

const int N_MAX = 1 + 100000 / 2 + 1;
const int M_MAX = 1 + 100000 / 2 + 1;
const int OFFSETS[4][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};

int n, m;
vector<vector<char>> treasure_map;

int ans[2];
char chr;
bool found_treasure;
Coord cod, cod_next;
set<Coord> seen;
queue<Coord> que;

int main() {
    cin >> n >> m;
    treasure_map.push_back(vector<char>(1 + m + 1, '0'));
    for (int i = 1; i < 1 + n; i += 1) {
        treasure_map.push_back(vector<char>(1, '0'));
        for (int j = 1; j < 1 + m; j += 1) {
            cin >> chr;
            treasure_map[i].push_back(chr);
        }
        treasure_map[i].push_back('0');
    }

    ans[0] = ans[1] = 0;
    for (int i = 1; i < 1 + n; i += 1) {
        cod.x = i;
        for (int j = 1; j < 1 + m; j += 1) {
            cod.y = j;
            if ('1' == slices[cod.x][cod.y][cod.z] && seen.) {
        }
    }

    return 0;
}
