def main() -> None:
    for i in range(2022, 999999999999):
        if str(hex(i))[1:].isalpha():
            print(i)
            break


if __name__ == '__main__':
    main()
