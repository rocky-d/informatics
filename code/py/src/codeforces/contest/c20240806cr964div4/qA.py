def main() -> None:
    n = input()

    print(sum(map(int, n)))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
