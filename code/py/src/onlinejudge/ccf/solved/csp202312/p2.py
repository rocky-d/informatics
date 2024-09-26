from math import isqrt


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


def main() -> None:
    q = int(input())
    nk = (map(int, input().split()) for _ in range(q))

    ans = []
    for n, k in nk:
        res = 1
        for p, t in prime_factors(n):
            if t < k:
                continue
            res *= p**t
        ans.append(res)
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
