from calendar import isleap


def main() -> None:
    y = int(input())

    print(366 if isleap(y) else 365)


if __name__ == '__main__':
    main()
