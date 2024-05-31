from math import log2


def main() -> None:
    for _ in range(int(input())):
        l, r = map(int, input().split())
        print(int(log2(r)))


if __name__ == '__main__':
    main()
