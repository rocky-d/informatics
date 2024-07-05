def main() -> None:
    n, k = map(int, input().split())
    a = map(int, input().split())

    a = sorted(a)
    print(a[-1 if k < a[-1] - a[0] else -2])


if __name__ == '__main__':
    main()
