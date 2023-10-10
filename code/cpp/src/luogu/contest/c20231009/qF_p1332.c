#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n, m, a, b;
    scanf("%d %d %d %d", &n, &m, &a, &b);
    int sourceList[100001][2];
    for (int i = 0; i < a; i++) {
        int x, y;
        scanf("%d %d", &x, &y);
        sourceList[i][0] = x;
        sourceList[i][1] = y;
    }
    const int MIN_VAL = n + m - 2;
    for (int i = 0; i < b; i++) {
        int x, y;
        scanf("%d %d", &x, &y);
        int minVal = MIN_VAL;
        for (int j = 0; j < a; j++) {
            int sourceX = sourceList[j][0];
            int sourceY = sourceList[j][1];
            int distance = abs(x - sourceX) + abs(y - sourceY);
            if (distance < minVal) {
                minVal = distance;
            }
        }
        printf("%d\n", minVal);
    }
    return 0;
}