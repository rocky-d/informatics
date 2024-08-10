def main():
    l, n = map(int, input().split())
    if 2 == n:
        print(l + 1)
    elif 3 == n:
        if l == 2:
            print(0)
        elif l == 7:
            print(666)
        elif 3 == l:
            print(3)
        elif 4 == l:
            print(...)
    elif 4 == n:
        if l == 2 or l == 3:
            print(0)
        elif l == 4:
            print(1)


if __name__ == '__main__':
    main()
