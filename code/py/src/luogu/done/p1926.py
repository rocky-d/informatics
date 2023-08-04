def main():
    n, m, k, r = map(int, input().strip().split(' '))
    time_n = sorted(list(map(int, input().strip().split(' '))))
    time_m = list(map(int, input().strip().split(' ')))
    score_m = list(map(int, input().strip().split(' ')))

    res = 0
    dp = [0] * (r + 1)
    for i in range(0, m - 1):
        for j in range(r, time_m[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - time_m[i]] + score_m[i])

    i = m - 1
    for j in range(r, time_m[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - time_m[i]] + score_m[i])
        if dp[j] < k:
            time_left = r - j
            for ni in time_n:
                if time_left > ni:
                    time_left -= ni
                    res += 1
            break

    print(res)


if __name__ == '__main__':
    main()
