def main():
    for _ in range(int(input())):
        dp = [0] * 5001
        for _ in range(int(input())):
            t, d, p = map(int, input().split())
            for vol in range(d, t - 1, -1):
                dp[vol] = max(dp[vol], dp[vol - t] + p)
        print(max(dp))


if __name__ == '__main__':
    main()
