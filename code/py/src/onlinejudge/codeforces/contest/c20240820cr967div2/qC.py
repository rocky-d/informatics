def query(a: int, b: int) -> int:
    print('?', a, b, flush = True)
    res = int(input())
    if -1 == res:
        exit()
    return res


def main() -> None:
    n = int(input())

    ans = []
    vis = {1}
    cache = set()

    def dfs(a: int, b: int) -> None:
        if a > b:
            a, b = b, a
        if (a, b) in cache:
            return
        cache.add((a, b))
        res = query(a, b)
        if res == a or res == b:
            vis.add(a)
            vis.add(b)
            ans.append(a)
            ans.append(b)
            return
        dfs(a, res)
        dfs(b, res)

    for b in range(2, n + 1):
        if b in vis:
            continue
        dfs(a = 1, b = b)
    print('!', *ans, flush = True)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()