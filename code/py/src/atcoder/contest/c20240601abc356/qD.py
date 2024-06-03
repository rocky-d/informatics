def main() -> None:
    n, m = map(int, input().split())

    ans = 0
    n1 = n + 1
    for i, bit in enumerate(bin(m)[2:][::-1]):
        if '0' == bit:
            continue
        half = 0b1 << i
        base = half << 1
        ans += half * (n1 // base) + max(0, n1 % base - half)
        ans %= 998244353
    print(ans)


if __name__ == '__main__':
    main()
