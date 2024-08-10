from collections import Counter
from math import inf


def main() -> None:
    n = int(input())
    matrix = (map(int, input().split()) for _ in range(n))

    total = 0
    ans = []

    range_n = range(n)
    grid = [[None] * n for _ in range_n]
    for i, col in enumerate(matrix):
        for j, val in enumerate(col):
            grid[j][i] = -inf if 0 == val else val
    print(*grid, sep = '\n')

    n2 = n * n
    range_n2 = range(n2)
    while True:
        score = -inf
        dp = Counter()
        # for x in range_n:
        #     for y in range_n:
        #         node = n * x + y
        #         dp[node][node] = grid[x][y]
        for x1 in range_n:
            for y1 in range_n:
                node1 = n * x1 + y1
                for x2 in range(x1, n):
                    for y2 in range(y1, n):
                        node2 = n * x2 + y2
                        dp[x1, y1, x2, y2] = val = sum(sum(grid[row][y1:y2 + 1]) for row in range(x1, x2 + 1))
                        score = max(score, val)
                        if val < score:
                            a, b, c, d = x1, y1, x2, y2
        if score <= 0:
            break
        total += score
        ans.append(f"({a + 1}, {b + 1}) ({c + 1}, {d + 1}) {score}")
        for i in range(a, c + 1):
            grid[i] = grid[i][:a] + [-inf] * (n - (d - b + 1)) + grid[i][c + 1:]
        print(*grid, sep = '\n')
    print(*ans, sep = '\n')
    print(total)


if __name__ == '__main__':
    main()
