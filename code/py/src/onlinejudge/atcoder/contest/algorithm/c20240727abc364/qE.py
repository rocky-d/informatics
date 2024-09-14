def main() -> None:
    n, x, y = map(int, input().split())
    ab = (map(int, input().split()) for _ in range(n))

    dp = [[0] * (1 + y) for _ in range(1 + x)]
    for ai, bi in ab:
        for vx in range(x, ai - 1, -1):
            for vy in range(y, bi - 1, -1):
                dp[vx][vy] = max(dp[vx][vy], dp[vx - ai][vy - bi] + 1)
    print(min(n, dp[-1][-1] + 1))


if __name__ == '__main__':
    main()
