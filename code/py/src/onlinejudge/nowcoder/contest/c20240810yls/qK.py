from itertools import cycle, chain


def main() -> None:
    n = int(input())

    spaces = cycle(chain(range(0, 26, +1), range(26, 0, -1)))
    for _ in range(n):
        print(next(spaces) * ' ' + '鸽')


if __name__ == '__main__':
    main()
