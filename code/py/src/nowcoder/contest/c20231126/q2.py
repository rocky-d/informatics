def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    if 1 == n:
        print(0)
        return

    a.sort()
    ans = a[-1] - a[0]
    a_i_1 = a[0]
    for a_i in a[1:]:
        ans = min(ans, a_i - a_i_1)
        a_i_1 = a_i
    print(ans)


if __name__ == '__main__':
    main()
