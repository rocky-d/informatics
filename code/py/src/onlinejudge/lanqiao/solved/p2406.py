def main() -> None:
    num = 2022
    while True:
        num += 1
        if hex(num)[2:].isalpha():
            print(num)
            break


if __name__ == '__main__':
    main()
