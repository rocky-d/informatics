def main():
    money = 1e8

    n = int(input())

    for _ in range(3):
        a, b = map(int, input().split())
        c = n // a * b if 0 == n % a else (n // a + 1) * b
        money = min(money, c)

    print(money)


if __name__ == '__main__':
    main()
