from bisect import bisect


def main() -> None:
    n, q = map(int, input().split())
    a = map(int, input().split())
    bk = (map(int, input().split()) for _ in range(q))

    ans = []
    a = sorted(a)
    for bi, ki in bk:
        idx = bisect(a, bi)
        ans.append(sorted(abs(a[i] - bi) for i in range(max(0, idx - ki - 1), min(n - 1, idx + ki + 1) + 1))[ki - 1])
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
