def main() -> None:
    n = int(input().strip())
    birthdays = []
    for i in range(1, 1 + n):
        name, ymd = input().strip().split(maxsplit = 1)
        ymd = list(map(int, ymd.split()))
        ymd.append(-i)
        birthdays.append((name, ymd))

    print(*(key for key, val in sorted(
        birthdays,
        key = lambda item: (item[1][0], item[1][1], item[1][2], item[1][3])
    )), sep = '\n')


if __name__ == '__main__':
    main()
