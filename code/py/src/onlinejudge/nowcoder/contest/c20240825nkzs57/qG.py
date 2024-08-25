def main() -> None:
    n, k = map(int, input().split())

    if 1 == n and 2 != k or 2 == n and 0 == k:
        print(-1)
        return
    n1 = n + 1
    if 0 == k:
        ans = []
        for i in range(1, n1):
            ans.append(i)
            ans.append(i)
        print(*ans)
        return
    if n1 == k:
        print(*range(1, n1), *range(1, n1))
        return
    if n == k:
        print(*range(1, n1), *range(1, n - 1), n, n - 1)
        return
    print(k, *range(1, n1), *range(1, k), *range(k + 1, n1))


if __name__ == '__main__':
    main()
