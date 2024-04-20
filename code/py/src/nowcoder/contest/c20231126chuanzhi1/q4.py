def main() -> None:
    n = int(input())
    s = input()

    if 3 > n:
        print(0)
        return

    ans = 0
    dp = [0, 0 if s[0] == s[1] else 1]  # 当前字母作为第二个字母的可能数
    for i in range(2, n):
        dp.append(0)
        for j in range(i):
            if s[j] == s[i]:
                ans += dp[j]
            else:
                dp[-1] += 1
    print(ans)


if __name__ == '__main__':
    main()
