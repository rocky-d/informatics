def main() -> None:
    n = int(input().rstrip())
    ls = [None]
    for _ in range(n):
        ls.append(list(map(int, input().rstrip().split()))[1:])

    res = 0
    queue = [1]
    visited = [True for _ in range(n + 1)]
    while queue:
        package = queue.pop(0)
        if visited[package]:
            res += 1
            visited[package] = False
            queue += ls[package]
    print(res)


if __name__ == '__main__':
    main()
