def main() -> None:
    n = int(input())
    s = input()
    all_alpha_lower = 'qwertyuiopasdfghjklzxcvbnm'
    alpha_cnt = [{} for _i in range(1 + n)]
    alpha_cnt[-1] = {alpha: 0 for alpha in all_alpha_lower}
    for i in range(n - 1, -1, -1):
        alpha_cnt[i] = alpha_cnt[i + 1].copy()
        alpha_cnt[i][s[i]] += 1
    ans = 0
    for i in range(n, 0, -1):
        ch = s[i - 1]
        for alpha in all_alpha_lower:
            ans += (alpha_cnt[i][alpha] ** 2 - alpha_cnt[i][alpha]) // 2
        ans -= (alpha_cnt[i][ch] ** 2 - alpha_cnt[i][ch]) // 2
    print(ans)


if __name__ == '__main__':
    main()
