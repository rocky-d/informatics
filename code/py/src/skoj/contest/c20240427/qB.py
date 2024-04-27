def main() -> None:
    n = int(input())
    rules = 0, 7, 5, 3, 1, 8, 6, 4, 2, 9
    for _ in range(n):
        num = input()
        digits = 0
        for i in range(-1, -len(num) - 1, -1):
            digit = int(num[i])
            digits += rules[digit] if 1 == (-i) % 2 else digit
        print('T' if 0 == digits % 8 else 'F')


if __name__ == '__main__':
    main()
