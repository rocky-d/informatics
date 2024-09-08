def primes_before_eratosthenes(n):
    tags = [False] * 2 + [True] * n  # tags = [False] * min(2, n) + [True] * max(0, n - 2)
    for num in range(2, n):
        if tags[num]:
            yield num
            for composite in range(num * num, n, num):
                tags[composite] = False


def primes_before_euler(n):
    primes = []
    tags = [False] * 2 + [True] * n  # tags = [False] * min(2, n) + [True] * max(0, n - 2)
    for num in range(2, n):
        if tags[num]:
            yield num
            primes.append(num)
        for prime in primes:
            composite = num * prime
            if composite < n:
                tags[composite] = False
                if 0 == num % prime:    
                    break
            else:
                break


def main() -> None:
    n, q = map(int, input().split())
    k = (int(input()) for _ in range(q))

    ans = []
    primes = [None] + list(primes_before_eratosthenes(n + 1))
    for ki in k:
        if ki >= len(primes):
            ans.append(0)
            continue
        ans.append(primes[ki])
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
