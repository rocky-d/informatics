def main() -> None:
    n, l, r = map(int, input().split())

    ls = list(range(1, n + 1))
    l -= 1
    r -= 1
    ls = ls[:l] + ls[l:r + 1][::-1] + ls[r + 1:]
    print(*ls)


if __name__ == '__main__':
    main()
