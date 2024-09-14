def main() -> None:
    n = int(input())
    lr = (map(int, input().split()) for _ in range(n))

    lfts, rits = [], []
    for l, r in lr:
        lfts.append(l)
        rits.append(r)
    lfts_sum, rits_sum = sum(lfts), sum(rits)
    if not lfts_sum <= 0 <= rits_sum:
        print('No')
        return
    print('Yes')
    ls, total = lfts[:], lfts_sum
    for i in range(n):
        change = min(-total, rits[i] - lfts[i])
        ls[i] += change
        total += change
        if 0 == total:
            break
    print(*ls)


if __name__ == '__main__':
    main()
