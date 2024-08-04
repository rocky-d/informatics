def main():
    n, w = map(int, input().split())
    t = map(int, input().split())

    drinks = 0
    thursdays = 0
    for i, x in enumerate(t, start = w - 1):
        if 35 <= x:
            if 3 == i % 7:
                thursdays += 1
            else:
                drinks += 1
    print(drinks, thursdays)


if __name__ == '__main__':
    main()
