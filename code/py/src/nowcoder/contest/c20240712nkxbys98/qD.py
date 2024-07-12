def main() -> None:
    n, l, r = map(int, input().split())
    s = input()

    c0s, c1s = [0], [0]
    for char in s:
        if '0' == char:
            c0s.append(c0s[-1] + 1)
            c1s.append(c1s[-1])
        else:  # elif '1' == char:
            c0s.append(c0s[-1])
            c1s.append(c1s[-1] + 1)
    dp = [[0] * n for _ in range(n)]
    for diff in range(1, n):
        for lft, rit in zip(range(n - diff), range(diff, n)):
            for cut in range(lft + 1, rit + 1):
                if l <= abs((c0s[cut] - c0s[lft]) - (c1s[rit + 1] - c1s[cut])) <= r:
                    dp[lft][rit] = max(dp[lft][rit], 1 + dp[lft][cut - 1] + dp[cut][rit])
    print(dp[0][-1])


if __name__ == '__main__':
    main()
