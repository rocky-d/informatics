from itertools import accumulate


def main() -> None:
    n, k = map(int, input().split())
    a = map(int, input().split())

    leng = n - k
    prefs = list(accumulate(a))
    print(max(prefs[i] - prefs[i - leng] for i in range(leng, len(prefs))))


if __name__ == '__main__':
    main()
