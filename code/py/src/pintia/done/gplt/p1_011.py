def main() -> None:
    a = input()
    b = input()

    for char in b:
        a = a.replace(char, '')
    print(a)


if __name__ == '__main__':
    main()
