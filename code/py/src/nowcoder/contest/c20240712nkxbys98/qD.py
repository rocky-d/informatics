from functools import cache
from itertools import accumulate


def main() -> None:
    n, l, r = map(int, input().split())
    s = input()

    c0s = list(accumulate((1 if '0' == char else 0 for char in s), initial = 0))
    c1s = list(accumulate((1 if '1' == char else 0 for char in s), initial = 0))
    seen = {}

    @cache
    def dfs(lft: int, rit: int) -> int:
        t = s[lft:rit + 1]
        if t not in seen.keys():
            seen[t] = max((1 + dfs(lft, cut - 1) + dfs(cut, rit) for cut in range(lft + 1, rit + 1) if
                           l <= abs((c0s[cut] - c0s[lft]) - (c1s[rit + 1] - c1s[cut])) <= r), default = 0)
        return seen[t]

    print(dfs(lft = 0, rit = n - 1))


if __name__ == '__main__':
    main()
