def main() -> None:
    n, m, k = map(int, input().split())
    a = map(int, input().split())

    print(min(sum(a) // k, m + 1))


if __name__ == '__main__':
    main()
