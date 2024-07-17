def prime_factors(num):
    for factor in primes:
        if num < factor:
            break
        cnt = 0
        while 0 == num % factor:
            num //= factor
            cnt += 1
        if 0 < cnt:
            yield factor, cnt
    if 1 < num:
        yield num, 1


def primes_before(n):
    tags = [False] * min(2, n) + [True] * (n - 2)
    for divisor in range(2, n):
        if tags[divisor]:
            yield divisor
            for comp in range(divisor * divisor, n, divisor):
                tags[comp] = False


primes = list(primes_before(1000001))


def main() -> None:
    for _ in range(int(input())):
        x = int(input())
        ans = 1
        for a, b in prime_factors(x):
            b //= 2
            ans *= a ** b
        print(ans)


if __name__ == '__main__':
    main()
