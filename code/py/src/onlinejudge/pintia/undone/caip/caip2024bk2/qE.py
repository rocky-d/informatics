from datastructure.prefsdiffs import Prefs2D

inf = 1_000_000_000


def main() -> None:
    n = int(input())
    matrix = (map(int, input().split()) for _ in range(n))

    operations = []
    total = 0

    range_n = range(n)
    grid = [[None] * n for _ in range_n]
    for i, col in enumerate(matrix):
        for j, val in enumerate(col):
            grid[j][i] = -inf if 0 == val else val
    # print(*grid, sep = '\n',end = '\n\n')
    while True:
        score = -inf
        prefs2d = Prefs2D(grid, start = 0)
        for x1 in range_n:
            for y1 in range_n:
                for x2 in range(x1, n):
                    for y2 in range(y1, n):
                        val = prefs2d.sum((x1, y1), (x2, y2))
                        if val < -100_000_000:
                            break
                        if score < val:
                            score = val
                            x11, y11, x22, y22 = x1, y1, x2, y2
        if score <= 0:
            break
        for i in range(x11, x22 + 1):
            grid[i] = [-inf] * (y22 + 1 - y11) + grid[i][:y11] + grid[i][y22 + 1:]
        # print(x11, y11, x22, y22)
        # print(*grid, sep = '\n', end = '\n\n')
        operations.append(f"({x11 + 1}, {y11 + 1}) ({x22 + 1}, {y22 + 1}) {score}")
        total += score
    print(*operations, sep = '\n')
    print(total)


if __name__ == '__main__':
    main()
