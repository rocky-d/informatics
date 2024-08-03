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
    for factor in range(2, isqrt(num) + 1):
        exponent = 0
        while 0 == num % factor:
            num //= factor
            exponent += 1
        if 0 < exponent:
            yield factor, exponent
    if 1 < num:
        yield num, 1


if __name__ == '__main__':
    num = 444

    print(*factors(num))
    print(*prime_factors(num))
