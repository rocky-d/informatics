from itertools import accumulate


def main() -> None:
    n = int(input())
    a = map(int, input().split())

    a = (ai % 10 for ai in a)
    print(sum(1 for pref in accumulate(a, func = lambda x, y: x * y % 10) if 6 == pref))


if __name__ == '__main__':
    main()
