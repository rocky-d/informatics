from math import ceil


def main():
    h, r = map(int, input().split())
    print(ceil(20000 / (h * 3.14 * r ** 2)))


if __name__ == '__main__':
    main()
