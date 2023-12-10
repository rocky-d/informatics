import math


def is_prime_slower(n: int) -> bool:
    if n < 2:
        ans = False
    else:
        for i in range(2, n):
            if 0 == n % i:
                ans = False
                break
        else:
            ans = True
    return ans


def is_prime_faster(n: int) -> bool:
    if n < 2:
        ans = False
    else:
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if 0 == n % i:
                ans = False
                break
        else:
            ans = True
    return ans


def primes_before_slower(n: int) -> list[int]:
    res = []
    tags = [True for _ in range(n)]
    tags[0], tags[1] = False, False
    for i in range(2, n):
        if tags[i]:
            res.append(i)
            for j in range(i ** 2, n, i):
                tags[j] = False
    return res


def primes_before_faster(n: int) -> list[int]:
    res = []
    tags = [True for _ in range(n)]
    tags[0], tags[1] = False, False
    ...
    return res


if __name__ == '__main__':
    print(is_prime_slower(133))
    print(is_prime_faster(133))
    print(primes_before_slower(133))
    print(primes_before_faster(133))
