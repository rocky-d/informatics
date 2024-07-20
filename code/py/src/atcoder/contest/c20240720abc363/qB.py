def main() -> None:
    n, t, p = map(int, input().split())
    l = map(int, input().split())

    print(max(0, t - sorted(l)[-p]))


if __name__ == '__main__':
    main()
