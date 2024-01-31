def main() -> None:
    n = int(input())
    nums = map(int, input().split())

    odds = 0
    for num in nums:
        if 0b1 == 0b1 & num:
            odds += 1
    print(odds, n - odds)


if __name__ == '__main__':
    main()
