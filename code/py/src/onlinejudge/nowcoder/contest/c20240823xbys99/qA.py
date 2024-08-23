def main() -> None:
    a, b, x, y = map(int, input().split())

    print(a * x + b * y if x < y else (a + b) * y)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
