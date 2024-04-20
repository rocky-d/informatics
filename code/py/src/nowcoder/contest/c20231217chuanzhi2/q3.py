def main() -> None:
    a = input()
    max_ord = max((ord(char) for char in a))
    min_ord = min((ord(char) for char in a))
    len_a = len(a)
    print((25 ** len_a - (26 - (max_ord - min_ord + 1))) % 1000000007)


if __name__ == '__main__':
    main()
