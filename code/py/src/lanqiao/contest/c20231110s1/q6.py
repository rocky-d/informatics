def main() -> None:
    a = int(input())
    n = int(input())
    n = n % 7
    a = a + n
    if a > 7:
        print(a - 7)
    else:
        print(a)


if __name__ == '__main__':
    main()
