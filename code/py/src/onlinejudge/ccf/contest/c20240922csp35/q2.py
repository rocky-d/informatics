def main():
    s = input()

    s = s[1:-1]

    n = int(input())
    f = (input() for _ in range(n))

    f = {fi[1]: fi[2] for fi in f}
    cycles = [s]
    cycles_set = {s}
    while True:
        s_ = ''
        for char in cycles[-1]:
            s_ += f.get(char, char)
        if s_ in cycles_set:
            break
        cycles_set.add(s_)
        cycles.append(s_)
    cycles_len = len(cycles)

    m = int(input())
    k = map(int, input().split())

    ans = []
    for ki in k:
        ans.append('#' + cycles[ki % cycles_len] + '#')
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
