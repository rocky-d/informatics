def main() -> None:
    n, m = map(int, input().split())

    if n > m:
        n, m = m, n
    if m - n in (0, 1):
        print('Brown')
    else:
        print('Alice')


if __name__ == '__main__':
    main()
