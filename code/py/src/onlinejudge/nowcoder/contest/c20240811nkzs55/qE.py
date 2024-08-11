mod = 1_000_000_007


def main() -> None:
    n = int(input())
    a = map(int, input().split())

    ans = 0
    dp = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]
    for ai in a:
        ai %= 10
        dp_lst = dp[-1]
        dp_nxt = dp_lst.copy()
        for digit in range(10):
            dp_nxt[ai * digit % 10] += dp_lst[digit]
        dp.append(dp_nxt)
    for i in range(1, len(dp)):
        ans += (dp[i][6] - dp[i - 1][6]) * (0b1 << n - i)
        ans %= mod
    print(ans)


if __name__ == '__main__':
    main()
