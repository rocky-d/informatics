from math import isqrt


def main() -> None:
    n = int(input())

    for factor in range(2, isqrt(n) + 1):
        if 0 == n % factor:
            print(n // factor)
            break


if __name__ == '__main__':
    main()
