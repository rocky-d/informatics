def main():
    k, v, n = map(int, input().split())

    dp = [[-99999999 for __ in range(60)] for _ in range(1 + v)]
    dp[0][1] = 0
    rnk = [0 for _ in range(2 + k)]

    for _ in range(n):
        a, b = map(int, input().split())
        for j in range(v, a - 1, -1):
            rn1 = 1
            rn2 = 1
            cnt = 0
            while cnt <= k:
                cnt += 1
                if dp[j][rn1] > dp[j - a][rn2] + b:
                    rnk[cnt] = dp[j][rn1]
                    rn1 += 1
                else:
                    rnk[cnt] = dp[j - a][rn2] + b
                    rn2 += 1
                for h in range(1, k + 1):
                    dp[j][h] = rnk[h]

    print(sum(dp[v][1: k + 1]))


if __name__ == '__main__':
    main()
