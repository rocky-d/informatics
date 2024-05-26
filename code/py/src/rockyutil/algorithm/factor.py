from itertools import chain
from math import isqrt


def factors(num):
    num_isqrt = isqrt(num)
    for factor in range(1, num_isqrt):
        if 0 == num % factor:
            yield factor
            yield num // factor
    if 0 == num % num_isqrt:
        yield num_isqrt
        if num // num_isqrt != num_isqrt:
            yield num // num_isqrt


def prime_factors(num):
    for factor in chain(range(2, isqrt(num) + 1), [num]):
        times = 0
        while 0 == num % factor:
            num //= factor
            times += 1
        if 0 < times:
            yield factor, times


if __name__ == '__main__':
    print(*factors(num = 36))
    print(*prime_factors(num = 36))
