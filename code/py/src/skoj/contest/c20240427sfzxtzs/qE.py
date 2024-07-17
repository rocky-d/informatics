def main() -> None:
    for _ in range(int(input())):
        n, k = map(int, input().split())
        if k == 0:
            print(*range(n, 0, -1))
        elif k == n - 1:
            print(*range(1, 1 + n))
        else:
            print(*range(1, 1 + k), end = ' ')
            print(*range(n, k, -1))


if __name__ == '__main__':
    main()
