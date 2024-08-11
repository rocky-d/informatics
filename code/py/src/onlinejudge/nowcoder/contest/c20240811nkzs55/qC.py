from collections import Counter


def main() -> None:
    n = int(input())
    a = map(int, input().split())

    a = sorted(a)
    for ai, cnt in Counter(a).items():
        if 0 == ai and 2 == cnt or 2 < cnt:
            print('NO')
            return
    print('YES')
    print(*a)


if __name__ == '__main__':
    main()
