def primes_before_eratosthenes(n):
    tags = [False for _ in range(min(2, n))] + [True for _ in range(2, n)]
    for num in range(2, n):
        if tags[num]:
            yield num
            for composite in range(num * num, n, num):
                tags[composite] = False


def main() -> None:
    ans = 0
    for prime in primes_before_eratosthenes(1_000_001):
        if 23 == sum(map(int, str(prime))):
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
