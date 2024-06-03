def main() -> None:
    n, m, k = map(int, input().split())
    rows = map(lambda ls: ('o' == ls[1], tuple(map(int, ls[0].split()))),
               (input().split(maxsplit = 1)[1].rsplit(maxsplit = 1) for _ in range(m)))

    print(*rows, sep = '\n')


if __name__ == '__main__':
    main()
