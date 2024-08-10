def main() -> None:
    v, g = map(int, input().split())
    dp = [[0 for _ in range(1 + g)] for _ in range(1 + v)]
    n = int(input())
    for _ in range(n):
        val, vi, gi = map(int, input().split())
        for vj in range(v, vi - 1, -1):
            for gj in range(g, gi - 1, -1):
                dp[vj][gj] = max(dp[vj][gj], dp[vj - vi][gj - gi] + val)

    print(dp[-1][-1])


if __name__ == '__main__':
    main()
