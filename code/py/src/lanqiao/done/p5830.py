def case() -> None:
    n, b = map(int, input().split())
    a = list(map(int, input().split()))
    res = 2 ** 30 - 1  # 0b111111111111111111111111111111
    for ai in a:
        if b == b & ai:
            res &= ai
    print('YES' if b == res else 'NO')


def main() -> None:
    for _ in range(int(input())):
        case()


if __name__ == '__main__':
    main()
