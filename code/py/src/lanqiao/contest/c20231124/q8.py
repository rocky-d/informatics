def main() -> None:
    n = int(input())
    while 10 <= n:
        res = 1
        for ch in str(n):
            if ch == '0':
                continue
            res *= int(ch)
        n = res
        print(n)


if __name__ == '__main__':
    main()
