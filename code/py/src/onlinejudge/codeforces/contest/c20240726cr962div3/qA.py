def main() -> None:
    n = int(input())

    n //= 2
    print(n // 2 + (0b1 & n))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
