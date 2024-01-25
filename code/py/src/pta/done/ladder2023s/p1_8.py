def main() -> None:
    nk = list(map(int, input().split()))
    actions = []
    while True:
        char = input()[0]
        if 'B' == char:
            actions.append('B')
        elif 'C' == char:
            actions.append('C')
        elif 'J' == char:
            actions.append('J')
        else:
            break

    ans = []
    pattern = 0b0
    i = 0
    for ki in nk[1:]:
        for _ in range(ki):
            pattern |= 0b1 << i
            i += 1
        i += 1
    patterns = i
    i = 0
    for action in actions:
        ans.append({'B': ('ChuiZi', 'JianDao'), 'C': ('JianDao', 'Bu'), 'J': ('Bu', 'ChuiZi')}[action][0b1 & (pattern >> i)])
        i = (i + 1) % patterns
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
