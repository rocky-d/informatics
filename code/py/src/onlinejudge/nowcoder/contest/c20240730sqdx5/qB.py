def main() -> None:
    n, m, a, b = map(int, input().split())

    n, m = min(n, m), max(n, m)
    if 0b1 == 0b1 & n * m:
        print('No')
        return
    if 0 == a == b:
        if 1 == n and 2 == m:
            print('Yes')
        else:
            print('No')
        return
    if 1 == a == b:
        print('Yes')
        return
    if 0 == a and 1 == b:
        print('Yes')
        return
    if 1 == a and 0 == b:
        if 1 == n:
            print('Yes')
        else:
            print('No')
        return


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
