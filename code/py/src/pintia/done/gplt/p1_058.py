def main() -> None:
    s = input()

    ans = ''
    n = len(s)
    i = 0
    while i < n:
        cnt = 0
        while i < n and '6' == s[i]:
            cnt += 1
            i += 1
        if 0 == cnt:
            add = s[i]
            i += 1
        else:
            if cnt <= 3:
                add = '6' * cnt
            elif cnt <= 9:
                add = '9'
            else:
                add = '27'
        ans += add
    print(ans)


if __name__ == '__main__':
    main()
