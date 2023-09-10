def main() -> None:
    n = int(input())
    words = [input()[:-1] for _ in range(n)]
    dp = [1 for _ in range(n)]
    for i in range(n):
        prefix = words[i]
        for j in range(i + 1, n):
            if words[j].startswith(prefix):
                dp[j] += 1
                j += 1
                while j < n and words[j].startswith(prefix):
                    dp[j] += 1
                    j += 1
                break
    print(max(dp))


if __name__ == '__main__':
    main()