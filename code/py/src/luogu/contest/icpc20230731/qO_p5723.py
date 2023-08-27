def get_primes(n: int) -> list:
    primes = []
    is_prime = [True for _ in range(n + 1)]
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if i * p > n:
                break
            is_prime[i * p] = False
            if i % p == 0:
                break
    return primes


def main() -> None:
    l = int(input())

    total = 0
    primes = []
    is_prime = [True for _ in range(l + 2)]

    for i in range(2, l + 1):
        if is_prime[i]:
            total += i
            if total > l:
                break
            else:
                print(i)
                primes.append(i)
        for p in primes:
            if l < i * p:
                break
            is_prime[i * p] = False
            if 0 == i % p:
                break
    print(len(primes))


if __name__ == '__main__':
    main()
