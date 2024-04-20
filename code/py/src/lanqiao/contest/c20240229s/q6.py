def main() -> None:
    n = int(input())

    dp = 0, 0, 0
    for _ in range(1, 1 + n):
        dp = dp[1], dp[2], min(dp) + 1
    print(dp[-1])


if __name__ == '__main__':
    main()
