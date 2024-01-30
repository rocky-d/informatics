def main() -> None:
    m, n, l, t = map(int, input().split())
    slices = []
    for _ in range(l):
        slices.append([])
        for _ in range(m):
            slices[-1].append(input().split())

    ans = 0
    seen = set()
    for i in range(l):
        for j in range(m):
            for k in range(n):
                if '1' == slices[i][j][k] and (i, j, k) not in seen:
                    vol = 0
                    queue = [(i, j, k)]
                    while 0 < len(queue):
                        x, y, z = queue.pop(0)
                        if (x, y, z) not in seen:
                            vol += 1
                            seen.add((x, y, z))
                            if 0 <= x - 1 and '1' == slices[x - 1][y][z] and (x - 1, y, z) not in seen:
                                queue.append((x - 1, y, z))
                            if 0 <= y - 1 and '1' == slices[x][y - 1][z] and (x, y - 1, z) not in seen:
                                queue.append((x, y - 1, z))
                            if 0 <= z - 1 and '1' == slices[x][y][z - 1] and (x, y, z - 1) not in seen:
                                queue.append((x, y, z - 1))
                            if x + 1 < l and '1' == slices[x + 1][y][z] and (x + 1, y, z) not in seen:
                                queue.append((x + 1, y, z))
                            if y + 1 < m and '1' == slices[x][y + 1][z] and (x, y + 1, z) not in seen:
                                queue.append((x, y + 1, z))
                            if z + 1 < n and '1' == slices[x][y][z + 1] and (x, y, z + 1) not in seen:
                                queue.append((x, y, z + 1))
                    if t <= vol:
                        ans += vol
    print(ans)


if __name__ == '__main__':
    main()
