def main() -> None:
    for _ in range(int(input())):
        n, m = map(int, input().split())
        print('Yes' if n <= m or any(n % x < x - 1 for x in range(1, m + 1)) else 'No')


if __name__ == '__main__':
    main()
