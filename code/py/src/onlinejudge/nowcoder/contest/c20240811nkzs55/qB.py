from itertools import accumulate


def main() -> None:
    n = int(input())
    a = map(int, input().split())

    print(sum(1 for pref in accumulate(a, func = lambda x, y: (x % 10) * (y % 10)) if '6' == str(pref)[-1]))


if __name__ == '__main__':
    main()
