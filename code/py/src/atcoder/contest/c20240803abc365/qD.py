def main() -> None:
    n = int(input())
    s = input()

    dp = [0, 0, 0]
    for c in s:
        if 'R' == c:
            dp[0], dp[1] = max(dp[1], dp[2]), max(dp[0], dp[2]) + 1
        elif 'P' == c:
            dp[1], dp[2] = max(dp[0], dp[2]), max(dp[0], dp[1]) + 1
        else:  # elif 'S' == c:
            dp[2], dp[0] = max(dp[0], dp[1]), max(dp[1], dp[2]) + 1
    print(max(dp))


if __name__ == '__main__':
    main()
