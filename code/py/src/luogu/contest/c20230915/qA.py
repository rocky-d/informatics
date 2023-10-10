def main() -> None:
    a, b, c = map(int, input().strip().split())
    if a + b == c:
        print('plus')
    elif a - b == c:
        print('minus')
    else:
        print('illegal')


if __name__ == '__main__':
    main()
