def main():
    n = int(input())
    prices = [['0', '0']] + list(map(lambda s: s.split('.'), input().split()))
    for i, (a, b) in enumerate(prices):
        prices[i] = 100 * int(a) + int(b)
    cnts = [0 for _ in range(1 + n)]
    profits = 0
    while True:
        x, y = map(int, input().split())
        if 0 == x:
            break
        cnts[x] += y
        profits += prices[x] * y
    cnts.pop(0)
    print(*cnts, sep = '\n')
    print(f"{profits / 100:.2f}")


if __name__ == '__main__':
    main()
