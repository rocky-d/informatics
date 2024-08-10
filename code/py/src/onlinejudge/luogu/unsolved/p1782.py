def main():
    n, m, c = map(int, input().split())

    dp = [0 for _ in range(1 + c)]

    for _ in range(n):
        vv, ww, dd = map(int, input().split())
        count = 1
        while dd > count:
            dd -= count
            v = count * vv
            w = count * ww
            for j in range(c, v - 1, -1):
                dp[j] = max(dp[j], dp[j - v] + w)
            count <<= 1
        v = dd * vv
        w = dd * ww
        for j in range(c, v - 1, -1):
            dp[j] = max(dp[j], dp[j - v] + w)

    for _ in range(m):
        aa, bb, cc = map(int, input().split())
        for j in range(c, -1, -1):
            for x in range(j + 1):
                dp[j] = max(dp[j], dp[j - x] + aa * x ** 2 + bb * x + cc)

    print(dp[c])


if __name__ == '__main__':
    main()
