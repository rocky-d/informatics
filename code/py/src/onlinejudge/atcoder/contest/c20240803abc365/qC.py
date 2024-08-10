from bisect import bisect_left, bisect_right
from itertools import accumulate


def main() -> None:
    n, m = map(int, input().split())
    a = map(int, input().split())

    a = sorted(a)
    prefs = list(accumulate(a, initial = 0))
    if prefs[-1] <= m:
        print('infinite')
        return

    def func(mid: int) -> int:
        idx = bisect_left(a, mid)
        return prefs[idx] + mid * (n - idx)

    print(bisect_right(range(max(a)), m, lo = 0, key = func) - 1)


if __name__ == '__main__':
    main()
