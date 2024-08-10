def main() -> None:
    n, k = map(int, input().split())

    if n == k + k:
        print(n)
        return
    if n < k + k:
        k = n - k
    print(1 + k * n)


if __name__ == '__main__':
    main()
