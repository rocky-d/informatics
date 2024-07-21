def main() -> None:
    for _ in range(int(input())):
        a, b, n = map(int, input().split())
        if 0b1 == 0b1 & b:
            b -= 1
        s = n + n
        if 2 * a + 3 * b < s:
            print('NO')
            continue
        if 2 * a >= s:
            print('YES')
            continue
        if 3 <= n:
            print('YES')
            continue
        print('NO')


if __name__ == '__main__':
    main()
