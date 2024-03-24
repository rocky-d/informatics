def main() -> None:
    n, k = map(int, input().split())

    if 1 == n:
        if 0 == k or 1 == k:
            print(1)
        else:
            print(0)
        return
    elif 2 == n:
        if 0 == k or 4 == k:
            print(1)
        elif 2 == k:
            print(2)
        else:
            print(0)
        return


if __name__ == '__main__':
    main()
