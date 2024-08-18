def main() -> None:
    x, y, n = map(int, input().split())

    print('YES' if x + y <= n else 'NO')


if __name__ == '__main__':
    main()
