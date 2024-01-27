def main() -> None:
    a, b, c = map(int, input().split())

    print(*sorted((a, b, c)), sep = '->')


if __name__ == '__main__':
    main()
