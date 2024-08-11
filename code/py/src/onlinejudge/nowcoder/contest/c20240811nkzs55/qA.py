def main() -> None:
    s = input()

    n = len(frozenset(s))
    if 1 == n:
        ans = 0
    elif 2 == n:
        ans = 1
    else:  # elif 3 == n:
        ans = 2
    print(ans)


if __name__ == '__main__':
    main()
