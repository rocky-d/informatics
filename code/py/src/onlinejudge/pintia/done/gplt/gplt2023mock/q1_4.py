def main() -> None:
    a, b = map(int, input().split())

    ans = 1
    for num in range(a + b, 1, -1):
        ans *= num
    print(ans)


if __name__ == '__main__':
    main()
