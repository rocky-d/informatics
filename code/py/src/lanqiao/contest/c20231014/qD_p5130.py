def main() -> None:
    n, m, q = map(int, input().split())
    days_left = sorted(set(range(1, n + 1)) - set(map(int, input().split())))
    day_ls = []
    last_day = days_left[0]
    cnt = 2  # 1 + 1 (extra +1 for saving time)
    for day in days_left[1:]:
        if 1 == day - last_day:
            cnt += 1
        else:
            day_ls.append(cnt)
            cnt = 2
        last_day = day
    day_ls.append(cnt)
    table = [(lambda k_, s_: (2 ** int(k_), int(s_)))(*input().split()) for _ in range(m)]

    ans = 0
    for day in day_ls:
        dp = [0 for _ in range(day)]
        for k, s in table:
            for j in range(k, day):
                dp[j] = max(dp[j], dp[j - k] + s)
        ans += dp[-1]
    print(ans)


if __name__ == '__main__':
    main()
