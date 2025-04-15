def main():
    wanted = 'lqb', 'lbq', 'qlb', 'qbl', 'blq', 'bql'
    s = input()

    wanted_set = frozenset(wanted)
    n = len(s)
    dp = [0] + [0] * n
    for i in range(3, 1 + n):
        dp[i] = dp[i - 1]
        if s[i - 3:i] in wanted_set:
            dp[i] = max(dp[i], dp[i - 3] + 1)
    print(dp[-1])


main()
