from functools import reduce


def main() -> None:
    a = input()

    print(reduce(lambda x, y: y + x, ({'0': '2', '1': '4', '2': '6', '3': '8', '4': '1', '5': '3', '6': '5', '7': '7', '8': '9', '9': '2'}[char] for char in a)))


if __name__ == '__main__':
    main()
