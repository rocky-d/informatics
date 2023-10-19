def main() -> None:
    n = int(input())
    s = input()

    last = s[0]
    cnt = 0
    ans = 0
    for ch in s:
        if 'x' == ch:
            cnt += 1
            if cnt > 2:
                ans += 1
        else:
            cnt = 0
    print(ans)


if __name__ == '__main__':
    main()
