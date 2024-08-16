def main() -> None:
    n, k = map(int, input().split())
    a = map(int, input().split())

    a = sorted(a, reverse = True)
    for ai, bi in zip(range(0, n, 2), range(1, n, 2)):
        if 0 == k:
            break
        diff = min(k, a[ai] - a[bi])
        k -= diff
        a[bi] += diff
    print(sum(a[ai] for ai in range(0, n, 2)) - sum(a[bi] for bi in range(1, n, 2)))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
