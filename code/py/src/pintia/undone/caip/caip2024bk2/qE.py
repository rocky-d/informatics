from math import inf


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
        for x1 in range_n:
            for y1 in range_n:
                for x2 in range(x1, n):
                    for y2 in range(y1, n):
                        val = sum(sum(grid[row][y1:y2 + 1]) for row in range(x1, x2 + 1))
                        if score < val:
                            score = val
                            x11, y11, x22, y22 = x1, y1, x2, y2
        if score <= 0:
            break
        total += score
        operations.append(f"({x11 + 1}, {y11 + 1}) ({x22 + 1}, {y22 + 1}) {score}")
        for i in range(x11, x22 + 1):
            grid[i] = [-inf] * (y22 - y11 + 1) + grid[i][:y11] + grid[i][y22 + 1:]
        # print(x11, y11, x22, y22)
        # print(*grid, sep = '\n', end = '\n\n')
    print(*operations, sep = '\n')
    print(total)


if __name__ == '__main__':
    main()
