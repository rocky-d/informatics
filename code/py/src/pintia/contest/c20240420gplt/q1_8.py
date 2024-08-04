from sys import stdin


def main():
    grid = [list(map(int, stdin.readline().split())) for _ in range(9)]

    for row in grid:
        appears = [False] * 10
        for val in row:
            if val < 1 or val > 9:
                print(0)
                return
            if appears[val]:
                print(0)
                return
            else:
                appears[val] = True
    for b in range(9):
        appears = [False] * 10
        for a in range(9):
            val = grid[a][b]
            if appears[val]:
                print(0)
                return
            else:
                appears[val] = True
    for a, b in (1, 1), (4, 4), (7, 7), (1, 4), (4, 1), (1, 7), (7, 1), (4, 7), (7, 4):
        appears = [False] * 10
        for ox, oy in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1):
            x, y = a + ox, b + oy
            val = grid[x][y]
            if appears[val]:
                print(0)
                return
            else:
                appears[val] = True
    print(1)
    return


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
