from functools import lru_cache
from math import gcd, sqrt
from typing import List

primes = set()
tags = [False] * 2 + [True] * 99_999
for num in range(2, 100_001):
    if tags[num]:
        primes.add(num)
        for composite in range(num * num, 100_001, num):
            tags[composite] = False


def factors(num: int) -> List[int]:
    res = []
    num_isqrt = int(sqrt(num))
    for factor in range(1, num_isqrt):
        if 0 == num % factor:
            res.append(factor)
            res.append(num // factor)
    if 0 == num % num_isqrt:
        res.append(num_isqrt)
        if num // num_isqrt != num_isqrt:
            res.append(num // num_isqrt)
    return res


@lru_cache(maxsize = None)
def gcd_cached(x: int, y: int) -> int:
    return gcd(x, y)


def main() -> None:
    n = int(input())
    a = map(int, input().split())

    a = list(a)
    vis = [False] * (1 + max(a))
    minm = 0
    for ai in a:
        vis[ai] = True
        x, y = minm, ai
        if x > y:
            x, y = y, x
        minm = gcd_cached(x = x, y = y)
    dct = {}
    for ai in a:
        if ai in primes:
            ls = [1, ai]
        else:
            ls = factors(ai)
        # print(ai, sorted(factor for factor in ls))
        for factor in ls:
            x, y = dct.get(factor, 0), ai // factor
            if x > y:
                x, y = y, x
            dct[factor] = gcd_cached(x = x, y = y)
    total = 0
    for key, val in dct.items():
        if vis[key] or key < minm:
            continue
        if 1 == val:
            total += 1
    print('dXqwq' if 0b1 == 0b1 & total else 'Haitang')


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
