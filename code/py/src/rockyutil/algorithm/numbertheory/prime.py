from math import isqrt


def is_prime_plain(n: int) -> bool:
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


def is_prime_optimized(n: int) -> bool:
    if n < 2:
        res = False
    else:
        for i in range(2, isqrt(n) + 1):
            if 0 == n % i:
                res = False
                break
        else:
            res = True
    return res


def primes_before_eratosthenes(n: int) -> list[int]:
    res = []
    tags = [False for _ in range(2)] + [True for _ in range(2, n)]
    for i in range(2, n):
        if tags[i]:
            res.append(i)
            for composite in range(i * i, n, i):
                tags[composite] = False
    return res


def primes_before_euler(n: int) -> list[int]:
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
    from timeit import timeit

    eg_n, repeats = int(1e7), int(1e1)
    which = 4
    match which:
        case 1:
            print(timeit(lambda: list(filter(is_prime_plain, range(eg_n))), number = repeats))
        case 2:
            print(timeit(lambda: list(filter(is_prime_optimized, range(eg_n))), number = repeats))
        case 3:
            print(timeit(lambda: primes_before_eratosthenes(n = eg_n), number = repeats))
        case 4:
            print(timeit(lambda: primes_before_euler(n = eg_n), number = repeats))
