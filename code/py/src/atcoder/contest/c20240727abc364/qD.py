def main() -> None:
    n, q = map(int, input().split())
    a = map(int, input().split())
    bk = (map(int, input().split()) for _ in range(q))

    a = list(a)
    print(*(sorted(abs(ai - bi) for ai in a)[ki - 1] for bi, ki in bk), sep = '\n')


if __name__ == '__main__':
    main()
