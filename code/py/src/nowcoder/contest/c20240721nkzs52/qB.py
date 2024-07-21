def main() -> None:
    for _ in range(int(input())):
        a, b, n = map(int, input().split())
        if 0b1 == 0b1 & b:
            b -= 1
        print('YES' if (n <= a + 3 * min(b // 2, n // 3)) else 'NO')


if __name__ == '__main__':
    main()
