def main() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    gap = n - k - 1
    print(min(a[i + gap] - a[i] for i in range(k + 1)))


if __name__ == '__main__':
    main()
