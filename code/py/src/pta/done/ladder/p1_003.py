from collections import Counter


def main() -> None:
    n = input()

    print(*(f"{d}:{m}" for d, m in sorted(Counter(n).items(), key = lambda item: item[0])), sep = '\n')


if __name__ == '__main__':
    main()
