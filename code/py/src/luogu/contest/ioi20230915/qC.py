def main() -> None:
    tests = int(input().rstrip())
    while tests > 0:
        res = []
        tests -= 1
        x0, a = map(int, input().split())
        while True:
            res.append(x0)
            x1 = (x0 + a) // a
            if x1 == x0:
                break
            x0 = x1
        print(*res)


if __name__ == '__main__':
    main()
