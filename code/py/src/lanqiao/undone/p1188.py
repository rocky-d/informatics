def main():
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    tmp = -1
    for ai in a:
        if tmp < ai:
            res += 1
            tmp = ai
    print(res)


if __name__ == '__main__':
    main()
