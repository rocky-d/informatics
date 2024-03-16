def main() -> None:
    n = int(input())
    x1x2 = (map(int, input().split()) for _ in range(n))

    print(min(abs(x1 - x2) for x1, x2 in x1x2))


if __name__ == '__main__':
    main()
