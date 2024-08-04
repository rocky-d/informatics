def main() -> None:
    n, m = map(int, input().split())
    words = [input() for _ in range(n)]

    ans = []
    idx = 0
    while True:
        length = 0
        lft = idx
        while idx < len(words) and length + len(words[idx]) <= m:
            length += len(words[idx]) + 1
            idx += 1
        if idx == len(words):
            ans.append(' '.join(words[lft:]))
            break
        # print(lft, idx)
        spaces = m - sum(len(words[j]) for j in range(lft, idx))
        cnt = idx - lft - 1
        lower = spaces // cnt
        upper = lower + 1
        lowers = ' ' * lower
        uppers = ' ' * upper
        upper_cnt = spaces - lower * cnt
        # lower_cnt = cnt - upper_cnt
        # print(lower, upper)
        # print(lower_cnt, upper_cnt)
        res = ''
        for j in range(lft, lft + upper_cnt):
            res += words[j] + uppers
        for j in range(lft + upper_cnt, lft + cnt):
            res += words[j] + lowers
        res += words[lft + cnt]
        ans.append(res)
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
