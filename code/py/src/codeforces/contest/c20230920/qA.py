def main() -> None:
    tests = int(input())
    while tests > 0:
        tests -= 1
        a, b, c = sorted(map(int, input().split()))
        print(b)


if __name__ == '__main__':
    main()
