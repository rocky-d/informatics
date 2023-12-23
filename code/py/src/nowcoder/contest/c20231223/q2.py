def main() -> None:
    s = list(input())
    n = len(s)
    if n < 5:
        if n < 3:
            print(0)
        elif n == 3:
            print(1)
        elif n == 4:
            if s[0] != s[2] and s[1] != s[3]:
                print(1)
            else:
                print(2)
        return
    max_, modify = 0, None
    for i in range(2, n - 2):
        if s[i - 2] != s[i] and s[i] != s[i + 2] and s[i - 2] != s[i + 2]:
            max_ = 1
            modify = i, s[i - 2]
        elif s[i - 2] == s[i + 2] and s[i - 2] != s[i]:
            max_ = 2
            modify = i, s[i - 2]
            break
    if max_ == 0:
        if s[0] != s[2]:
            modify = 0, s[2]
        elif s[1] != s[3]:
            modify = 1, s[3]
        elif s[-1] != s[-3]:
            modify = -1, s[-3]
        elif s[-2] != s[-4]:
            modify = -2, s[-4]
    if modify is not None:
        s[modify[0]] = modify[1]
    ans = 0
    for i in range(2, n):
        if s[i - 2] == s[i]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
