from itertools import pairwise
from math import comb


def combinations2d(n, k, mod = None):
    assert 0 <= k <= n
    c = [[1] + [0] * min(i + 1, k) for i in range(1 + n)]
    for i, (c_lst, c_nxt) in enumerate(pairwise(c), start = 1):
        for j in range(min(i, k), 0, -1):
            c_nxt[j] = c_lst[j - 1] + c_lst[j]
            if mod is not None:
                c_nxt[j] %= mod
    return c


def combinations1d(n, k, mod = None):
    assert 0 <= k <= n
    c = [1] + [0] * k
    for i in range(1, 1 + n):
        for j in range(min(i, k), 0, -1):
            c[j] += c[j - 1]
            if mod is not None:
                c[j] %= mod
    return c


def combinations0d(n, k, mod = None):
    assert 0 <= n and 0 <= k
    if n < k:
        return 0
    return combinations1d(n, k, mod)[-1]


if __name__ == '__main__':
    print(combinations2d(n = 100, k = 24, mod = 10007)[-1])
    print(combinations1d(n = 100, k = 24, mod = 10007))
    print(combinations0d(n = 100, k = 24, mod = 10007))
    print(comb(100, 24) % 10007)
