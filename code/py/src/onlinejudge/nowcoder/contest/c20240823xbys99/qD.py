primes = []
n = 2_750_161 + 1
tags = [False] * 2 + [True] * (n - 2)
for num in range(2, n):
    if tags[num]:
        primes.append(num)
        for composite in range(num * num, n, num):
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
