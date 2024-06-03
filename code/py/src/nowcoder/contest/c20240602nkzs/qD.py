def main():
    n, k = map(int, input().split())
    col = list(map(int, input().split()))

    #     idxes = {}
    #     bans = []
    #     for i, coli in enumerate(col):
    #         if coli in idxes and i - idxes[coli] > k:
    #             bans.append((idxes[coli], i))
    #         idxes[coli] = i
    #     print(bans)
    #     total = (1 + n) * n // 2
    ans = 0
    lft, rit = 0, 0
    idxes = {}
    while lft < n:
        while rit < n:
            if col[rit] in idxes and rit - idxes[col[rit]] > k:
                idxes[col[rit]] = rit
                break
            idxes[col[rit]] = rit
            rit += 1
        ans += rit - lft
        # print(lft, rit)
        lft += 1
    print(ans - 1)


if __name__ == '__main__':
    main()
