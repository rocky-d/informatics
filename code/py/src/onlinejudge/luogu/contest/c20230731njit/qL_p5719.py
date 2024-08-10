def main():
    n, k = map(int, input().split())

    a = []
    b = []

    for i in range(n, 0, -1):
        if 0 == i % k:
            a += [i]
        else:
            b += [i]

    print(round(sum(a) / len(a), 1), round(sum(b) / len(b), 1))


if __name__ == '__main__':
    main()
