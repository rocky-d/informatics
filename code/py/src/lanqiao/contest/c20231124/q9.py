v = set()


def main() -> None:
    def dfs(x: int, y: int) -> None:
        global v

        if 0 < x:
            next_x = x - 1
            for dd in divisor[x][y]:
                if dd in divisor[next_x][y]:
                    token = str(next_x) + '_' + str(y)
                    if token in v:
                        continue
                    v.add(token)
                    dfs(next_x, y)
                    break
        if n - 1 > x:
            next_x = x + 1
            for dd in divisor[x][y]:
                if dd in divisor[next_x][y]:
                    token = str(next_x) + '_' + str(y)
                    if token in v:
                        continue
                    v.add(token)
                    dfs(next_x, y)
                    break
        if 0 < y:
            next_y = y - 1
            for dd in divisor[x][y]:
                if dd in divisor[x][next_y]:
                    token = str(x) + '_' + str(next_y)
                    if token in v:
                        continue
                    v.add(token)
                    dfs(x, next_y)
                    break
        if m - 1 > y:
            next_y = y + 1
            for dd in divisor[x][y]:
                if dd in divisor[x][next_y]:
                    token = str(x) + '_' + str(next_y)
                    if token in v:
                        continue
                    v.add(token)
                    dfs(x, next_y)
                    break

    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _i in range(n)]
    r, c = map(int, input().split())
    r = r - 1
    c = c - 1
    divisor = [[set() for _j in range(m)] for _i in range(n)]
    for i in range(n):
        for j in range(m):
            for d in range(matrix[i][j], 1, -1):
                if 0 == matrix[i][j] % d:
                    divisor[i][j].add(d)
    dfs(r, c)
    global v
    print(len(v))


if __name__ == '__main__':
    main()

    # nexts = []
    # if 0 < x:
    #     nexts.append((x - 1, y))
    # if n - 1 > x:
    #     nexts.append((x + 1, y))
    # if 0 < y:
    #     nexts.append((x, y - 1))
    # if m - 1 > y:
    #     nexts.append((x, y + 1))
    # for dd in divisor[x][y]:
    #     for next_xy in nexts:
    #         next_x, next_y = next_xy[0], next_xy[1]
    #         if dd in divisor[next_x][next_y]:
    #             ...
