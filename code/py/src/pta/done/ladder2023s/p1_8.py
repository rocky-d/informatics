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
    reactions = {'B': ('ChuiZi', 'JianDao'), 'C': ('JianDao', 'Bu'), 'J': ('Bu', 'ChuiZi')}
    pattern = 0b0
    for ki in nk[1:]:
        for _ in range(ki):
            pattern <<= 1
            pattern |= 0b1
        pattern <<= 1
    patterns = len(bin(pattern)) - 2
    i = 0
    for action in actions:
        ans.append(reactions[action][0b1 & (pattern >> (patterns - i - 1))])
        i = (i + 1) % patterns
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
