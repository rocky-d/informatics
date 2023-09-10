def main() -> None:
    n = int(input())
    words = [input()[:-1] for _ in range(n)]
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if words[j].startswith(words[i]):
                dp[j] += 1
    print(max(dp))


if __name__ == '__main__':
    main()
