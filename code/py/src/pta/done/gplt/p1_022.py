def main() -> None:
    n = int(input())
    nums = map(int, input().split())

    print(*(lambda odds: (odds, n - odds))(len([num for num in nums if 0b1 == 0b1 & num])))


if __name__ == '__main__':
    main()
