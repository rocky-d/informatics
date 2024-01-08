def main() -> None:
    a, b, n = map(int, input().split())
    weeks = n // (5 * a + 2 * b)
    days = 7 * weeks
    lasting = n % (5 * a + 2 * b)
    if 0 < lasting:
        for day in range(5):
            days += 1
            lasting -= a
            if lasting <= 0:
                break
        else:
            for day in range(2):
                days += 1
                lasting -= b
                if lasting <= 0:
                    break
    print(days)


if __name__ == '__main__':
    main()
