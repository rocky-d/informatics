def main() -> None:
    x, y, t = map(int, input().split())

    dst = (x * t) / (y - x) * y
    print(int(dst))


if __name__ == '__main__':
    main()
