def main() -> None:
    x, y, k = map(int, input().split())

    yk = y * k
    if yk <= x:
        print(x - yk)
        return
    t, x = divmod(x, y)
    print(x if x + x == y or 0b0 == 0b1 & k - t else y - x)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
