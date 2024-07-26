def main() -> None:
    n = int(input())

    n //= 2
    print(n // 2 if 0b0 == 0b1 & n else n // 2 + 1)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
