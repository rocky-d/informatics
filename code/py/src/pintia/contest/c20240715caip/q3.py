def main():
    n, m = map(int, input().split())
    matrix = [input() for _ in range(n)]

    ans = []
    dirs = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)
    blacks = set()
    colds = [[True] * m for _ in range(n)]
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if 'c' == val:
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m:
                        blacks.add((x, y))
            elif 'w' == val:
                blacks.add((i, j))
            elif 'm' == val:
                blacks.add((i, j))
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m:
                        colds[x][y] = False
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if (i, j) in blacks:
                continue
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    if 'w' == matrix[x][y] and colds[x][y]:
                        break
            else:
                continue
            ans.append(f"{i + 1} {j + 1}")
    if 0 == len(ans):
        print('Too cold!')
    else:
        print(*sorted(ans), sep = '\n')


if __name__ == '__main__':
    main()
