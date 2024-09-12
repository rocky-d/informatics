from itertools import accumulate


def main() -> None:
    n, q = map(int, input().split())
    a = map(int, input())
    lr = (map(int, input().split()) for _ in range(q))

    a = list(a)
    prefs = accumulate(a, initial=0)
    for l, r in lr:
        ...


if __name__ == '__main__':
    main()
