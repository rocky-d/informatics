def main() -> None:
    n, x = map(int, input().split())
    a = map(int, input().split())

    print('YES' if x in frozenset(a) else 'NO')


if __name__ == '__main__':
    main()
