from bisect import bisect_left, bisect_right


def main() -> None:
    n, q = map(int, input().split())
    a = map(int, input().split())
    bk = (map(int, input().split()) for _ in range(q))

    ans = []
    a = sorted(a)
    for bi, ki in bk:
        lo, hi = -1, 200_000_001
        while 1 < hi - lo:
            mid = lo + hi >> 1
            if bisect_right(a, bi + mid) - bisect_left(a, bi - mid) < ki:
                lo = mid
            else:
                hi = mid
        ans.append(hi)
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
