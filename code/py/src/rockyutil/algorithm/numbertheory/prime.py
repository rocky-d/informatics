import math
from timeit import timeit


def is_prime_1(n: int) -> bool:
    if n < 2:
        res = False
    else:
        for i in range(2, n):
            if 0 == n % i:
                res = False
                break
        else:
            res = True
    return res


def is_prime_2(n: int) -> bool:
    if n < 2:
        res = False
    else:
        for i in range(2, math.isqrt(n) + 1):
            if 0 == n % i:
                res = False
                break
        else:
            res = True
    return res


def primes_before_1(n: int) -> list[int]:
    res = []
    tags = [False for _ in range(2)] + [True for _ in range(2, n)]
    for i in range(2, n):
        if tags[i]:
            res.append(i)
            for composite in range(i ** 2, n, i):
                tags[composite] = False
    return res


def primes_before_2(n: int) -> list[int]:
    res = []
    tags = [False for _ in range(2)] + [True for _ in range(2, n)]
    for i in range(2, n):
        if tags[i]:
            res.append(i)
        for prime in res:
            composite = i * prime
            if composite < n:
                tags[composite] = False
                if 0 == i % prime:
                    break
            else:
                break
    return res


if __name__ == '__main__':
    eg_n, repeats = int(1e8), int(1e0)
    which = 3
    match which:
        case 1:
            print(timeit(lambda: list(filter(is_prime_1, range(eg_n))), number = repeats))
        case 2:
            print(timeit(lambda: list(filter(is_prime_2, range(eg_n))), number = repeats))
        case 3:
            print(timeit(lambda: primes_before_1(n = eg_n), number = repeats))
        case 4:
            print(timeit(lambda: primes_before_2(n = eg_n), number = repeats))
