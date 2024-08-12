def main() -> None:
    s = input()

    print(len(frozenset(s)) - 1)


if __name__ == '__main__':
    main()
