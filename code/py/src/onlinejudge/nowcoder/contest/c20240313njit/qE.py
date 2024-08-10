from collections import defaultdict
from math import inf


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    appear = defaultdict(lambda: [])
    for i, ai in enumerate(a):
        appear[ai].append(i)

    seen = {-1, 0}

    def dfs(index, val):
        if index == n - 1:
            return val
        res = inf
        if index - 1 not in seen:
            seen.add(index - 1)
            res = min(res, dfs(index - 1, val + 1))
            seen.remove(index - 1)
        if index + 1 not in seen:
            seen.add(index + 1)
            res = min(res, dfs(index + 1, val + 1))
            seen.remove(index + 1)
        for i in appear[a[index]]:
            if i not in seen:
                seen.add(i)
                res = min(res, dfs(i, val + 1))
                seen.remove(i)
        return res

    print(dfs(0, 0))


if __name__ == '__main__':
    main()
