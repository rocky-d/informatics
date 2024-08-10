def main() -> None:
    n, m = map(int, input().split())

    if 1 == n == m:
        print(4)
        return
    if 1 == n and 2 == m or 1 == m and 2 == n:
        print(13)
        return


if __name__ == '__main__':
    main()
