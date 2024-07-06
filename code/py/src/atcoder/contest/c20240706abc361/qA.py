def main() -> None:
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))

    ans = a[:k] + [x] + a[k:]
    print(*ans)


if __name__ == '__main__':
    main()
