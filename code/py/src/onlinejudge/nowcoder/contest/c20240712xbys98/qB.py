def main() -> None:
    n = int(input())
    a = map(int, input().split())

    odds = sum(1 for ai in a if 0b1 == 0b1 & ai)
    eves = n - odds
    if eves < odds:
        odds -= eves
        ans = 0b1 & odds
    else:
        eves -= odds
        ans = eves
    print(ans)


if __name__ == '__main__':
    main()
