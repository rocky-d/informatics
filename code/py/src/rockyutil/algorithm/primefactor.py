from math import isqrt


def prime_factors(num):
    for factor in range(2, isqrt(num) + 1):
        times = 0
        while 0 == num % factor:
            num //= factor
            times += 1
        if 0 < times:
            yield factor, times
    if 1 < num:
        yield num, 1


if __name__ == '__main__':
    print(*prime_factors(49), sep = '\n')
