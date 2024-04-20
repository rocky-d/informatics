def main() -> None:
    s = input()

    print(sum(1 for digit in map(int, s) if 0b1 == 0b1 & digit))


if __name__ == '__main__':
    main()
