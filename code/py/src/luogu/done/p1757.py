def main():
    m, n = map(int, input().split())
    table = {}
    for _ in range(n):
        a, b, c = map(int, input().split())
        table[c] = table[c] + [(a, b)] if c in table else [(a, b)]

    dp = [0 for _ in range(1 + m)]

    for key in table.keys():
        for j in range(m, 0, -1):
            for item in table[key]:
                if j >= item[0]:
                    dp[j] = max(dp[j], dp[j - item[0]] + item[1])

    print(dp[m])


if __name__ == '__main__':
    main()
