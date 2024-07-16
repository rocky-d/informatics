def main() -> None:
    n, m, q = map(int, input().split())

    ans = 0
    m -= 1
    pow2 = [1] + [0] * max(n, m * (n - 1))
    for i in range(1, len(pow2)):
        pow2[i] = (pow2[i - 1] << 1) % q
    combn = 1
    for i in range(1, n + 1):
        combni = combn = combn * (n - i + 1) // i
        ans += combni % q * pow(pow2[i] - 1, m, q) % q * pow2[m * (n - i)] % q
        ans %= q
    print(ans)


if __name__ == '__main__':
    main()
