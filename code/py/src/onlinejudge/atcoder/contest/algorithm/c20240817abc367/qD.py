from collections import Counter
from itertools import accumulate


def main() -> None:
    n, m = map(int, input().split())
    a = map(int, input().split())

    ans = 0
    a = list(a)
    a_1 = a[:-1]
    cnter = Counter(pref % m for pref in accumulate(a_1))
    lft, rit = 0, sum(a_1) % m
    diff = 0
    ans += cnter[(m - diff) % m]
    for i in range(1, n):
        lft += a[i - 1]
        lft %= m
        cnter[lft] -= 1
        rit += a[i - 2]
        rit %= m
        cnter[rit] += 1
        diff -= a[i - 1] % m
        diff %= m
        ans += cnter[(m - diff) % m]
    print(ans)


if __name__ == '__main__':
    main()
