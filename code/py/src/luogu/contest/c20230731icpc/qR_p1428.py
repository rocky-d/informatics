def main():
    n = int(input())
    a = list(map(int, input().split()))

    res = []
    for i in range(n):
        count = 0
        for j in range(i):
            if a[i] > a[j]:
                count += 1
        res.append(count)

    print(*res)


if __name__ == '__main__':
    main()
