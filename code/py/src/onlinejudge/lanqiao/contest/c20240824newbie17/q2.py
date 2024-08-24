def main() -> None:
    n = int(input())
    a = map(int, input().split())

    a = sorted(a)
    cnta, cntb = 0, 0
    lft, rit = 0, n - 1
    while lft < rit:
        cnta += a[rit]
        rit -= 1
        cntb -= a[lft]
        lft += 1
    if lft == rit:
        cnta += a[rit]
        rit -= 1
    print(cnta - cntb)


if __name__ == '__main__':
    main()
