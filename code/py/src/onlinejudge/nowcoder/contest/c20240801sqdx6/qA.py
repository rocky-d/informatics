import sys

sys.setrecursionlimit(1_000_000)


def main() -> None:
    n = int(input())
    edges = (map(int, input().split()) for _ in range(n - 1))

    graph = [None] + [[] for _ in range(n)]
    for x, y, k in edges:
        graph[x].append((y, k))

    def dfs(x: int, ones: int, zeros: int, lst: int, grammy: bool) -> float:
        if grammy:
            res = -1.0
            func = max
        else:  # elif not grammy:
            res = 2.0
            func = min
        grammy = not grammy
        if 1 == lst:
            for y, k in graph[x]:
                if 1 == k:
                    res = func(res, dfs(y, ones + 1, zeros, 1, grammy))
                else:  # elif 0 == k:
                    res = func(res, dfs(y, ones, zeros + 1, 0, grammy))
        else:  # elif 0 == lst:
            for y, k in graph[x]:
                if 0 == k:
                    res = func(res, dfs(y, ones, zeros + 1, 0, grammy))
        if -1.0 == res or 2.0 == res:
            res = ones / (ones + zeros)
        return res

    print(dfs(x = 1, ones = 0, zeros = 0, lst = 1, grammy = True))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
