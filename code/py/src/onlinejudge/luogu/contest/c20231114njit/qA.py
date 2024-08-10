def main() -> None:
    for _i in range(3):
        d, n = map(int, input().split())
        print(n * 100 ** d)


if __name__ == '__main__':
    main()
