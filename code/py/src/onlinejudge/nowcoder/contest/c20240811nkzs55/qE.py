mod = 1_000_000_007


def main() -> None:
    n = int(input())
    a = map(int, input().split())

    ans = 0
    dp = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    for i, ai in enumerate(a, start = 1):
        ai %= 10
        dp_lst, dp = dp, dp.copy()
        for digit in range(10):
            dp[ai * digit % 10] += dp_lst[digit]
        ans += (((dp[6] - dp_lst[6]) % mod) * ((0b1 << n - i) % mod)) % mod
        ans %= mod
    print(ans)


if __name__ == '__main__':
    main()
