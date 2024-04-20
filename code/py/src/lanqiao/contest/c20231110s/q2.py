import string


def main() -> None:
    i = 26 ** 1 + 26 ** 2
    print(i)
    print(string.ascii_uppercase)
    for ch1 in string.ascii_uppercase:
        for ch2 in string.ascii_uppercase:
            for ch3 in string.ascii_uppercase:
                i += 1
                if i == 2022:
                    print(ch1 + ch2 + ch3)
                    break


if __name__ == '__main__':
    main()
