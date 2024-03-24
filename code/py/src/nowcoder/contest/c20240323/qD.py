def main() -> None:
    n, m, x, y = map(int, input().split())
    matrix = list(input() for _ in range(n))

    total = n * m
    seen = set()

    def dfs(a: int, b: int, cnt) -> bool:
        if cnt == total:
            return True
        seen.add((a, b))
        res = False
        for ax, by in map(lambda oft: (a + oft[0], b + oft[1]), ((0, -1), (0, 1), (1, 0), (-1, 0))):
            if 0 <= ax < n and 0 <= by < m and '.' == matrix[ax][by] and (ax, by) not in seen:
                res = res or dfs(ax, by, cnt + 1)
        seen.remove((a, b))
        return res

    print('YES' if dfs(a = x - 1, b = y - 1, cnt = sum(row.count('#') for row in matrix) + 1) else 'NO')


if __name__ == '__main__':
    main()
