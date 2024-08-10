from math import ceil


def main() -> None:
    a, b, n = map(int, input().split())

    weeks = n // (5 * a + 2 * b)
    days = 7 * weeks
    lasting = n - weeks * (5 * a + 2 * b)

    days += min(5, ceil(lasting / a))
    lasting = lasting - 5 * a

    if 0 < lasting:
        days += ceil(lasting / b)
    print(days)


if __name__ == '__main__':
    main()
