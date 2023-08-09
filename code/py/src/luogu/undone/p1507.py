def main():
    h, t = map(int, input().split(' '))

    dp = [[0 for _ in range(t + 1)] for _ in range(h + 1)]

    for _ in range(int(input()) - 1):
        hi, ti, ki = map(int, input().split(' '))
        for j in range(h, hi - 1, -1):
            for k in range(t, ti - 1, -1):
                dp[j][k] = max(dp[j][k], dp[j - hi][k - ti] + ki)

    hi, ti, ki = map(int, input().split(' '))
    print(max(dp[h][t], dp[h - hi][t - ti] + ki) if h >= hi and t >= ti else dp[h][t])


if __name__ == '__main__':
    main()
