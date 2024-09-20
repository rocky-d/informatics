def main() -> None:
    n = int(input())

    if n == 1:
        ans = 0
    elif 2 == n:
        ans = 2
    elif 3 == n:
        ans = 4
    elif 0b1 == 0b1 & n:
        ans = 6
    else:
        ans = 4
    print(ans)


if __name__ == '__main__':
    main()
