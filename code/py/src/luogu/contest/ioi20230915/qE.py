def main() -> None:
    tests = int(input().rstrip())
    while tests > 0:
        tests -= 1
        res = 0
        s = input()
        t = input()
        lens = len(s)
        gap = lens - len(t)
        for i in range(1, lens - gap):
            j = i + gap
            if s[j:] + s[:i] == t:
                res += 1
        print(res)


if __name__ == '__main__':
    main()
