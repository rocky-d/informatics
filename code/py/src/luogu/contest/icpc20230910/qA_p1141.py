def main() -> None:
    n, m = map(int, input().split())
    n1 = n + 1
    maze = [''] + ['x' + input() for _ in range(n)]

    for _ in range(m):
        visited = [[True for _ in range(n1)] for _ in range(n1)]
        i, j = map(int, input().split())
        queue = [[i, j]]
        res = 0
        while queue:
            vi, vj = queue.pop(0)
            if visited[vi][vj]:
                res += 1
                visited[vi][vj] = False
                target = '0' if maze[vi][vj] == '1' else '1'
                for nei, nej in [[vi + 1, vj], [vi - 1, vj], [vi, vj + 1], [vi, vj - 1]]:
                    if (0 < nei < n1 and 0 < nej < n1
                            and visited[nei][nej] and maze[nei][nej] == target):
                        queue.append([nei, nej])
        print(res)


if __name__ == '__main__':
    main()
