from itertools import chain
from math import isqrt


def prime_factors(num):
    for factor in chain(range(2, isqrt(num) + 1), [num]):
        times = 0
        while 0 == num % factor:
            num //= factor
            times += 1
        if 0 < times:
            yield factor, times


if __name__ == '__main__':
    print(*prime_factors(13), sep = '\n')
