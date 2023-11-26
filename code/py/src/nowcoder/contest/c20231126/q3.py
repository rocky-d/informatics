def main() -> None:
    n, m = map(int, input().split())
    if n * m % 2 == 1:
        print('akai')
    else:
        print('yukari')


if __name__ == '__main__':
    main()
