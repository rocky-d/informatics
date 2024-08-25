def main() -> None:
    n = int(input())

    if 2 == n:
        print('NO')
        return
    print('YES')
    print(2, 3 if 1 == n else n)


if __name__ == '__main__':
    main()
