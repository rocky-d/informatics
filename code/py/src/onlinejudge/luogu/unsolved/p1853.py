def main():
    s, n, d = map(int, input().split())

    dp = [0 for _ in range(1 + s)]

    for _ in range(d):
        a, b = map(int, input().split())
        for j in range(s, a - 1, -1):
            dp[j] = max(dp[j], dp[j - a] + b)
    print()


if __name__ == '__main__':
    main()
