def main() -> None:
    n = int(input())
    a = map(int, input().split())

    print(sorted(enumerate(a, start = 1), key = lambda item: item[1])[-2][0])


if __name__ == '__main__':
    main()
