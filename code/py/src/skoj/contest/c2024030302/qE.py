def case() -> None:
    s = input()

    ans = 0
    digits = frozenset('0123456789')
    s = '++' + s
    i = 2
    has_digit = False
    while i < len(s):
        if '-' == s[i - 1] and s[i - 2] not in digits:
            num = '-0'
        else:
            num = '0'
        while i < len(s) and s[i] in digits:
            has_digit = True
            num += s[i]
            i += 1
        i += 1
        ans += int(num)
    if has_digit:
        print(ans)


def main() -> None:
    while True:
        try:
            case()
        except EOFError:
            break


if __name__ == '__main__':
    main()
