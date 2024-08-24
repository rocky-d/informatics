primes = []
tags = [False] * 2 + [True] * 9_999_999
for num in range(2, 10_000_001):
    if tags[num]:
        primes.append(num)
        for composite in range(num * num, 10_000_001, num):
            tags[composite] = False


def main() -> None:
    n = int(input())
    a = map(int, input().split())

    a = frozenset(a)
    for prime in primes:
        if prime not in a:
            ans = prime
            break
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
