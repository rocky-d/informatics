from bisect import bisect_left, bisect_right


def main() -> None:
    n = int(input())
    a = map(int, input().split())

    a = sorted(a)
    idx1, idx2 = bisect_left(a, 0), bisect_right(a, 0)
    neg, zeros, pos = idx1, idx2 - idx1, n - idx2
    a1, a2 = a[:idx1], a[idx2:]
    n -= zeros

    def check(mid: int) -> bool:
        res = False
        for x in range(1, min(neg + 1, mid)):
            y = mid - x
            if pos < y:
                continue
            lo = -a1[-x]
            hi = a2[y - 1]
            if neg - x >= lo and pos - y >= lo + hi or pos - y >= hi and neg - x >= hi + lo:
                res = True
                break
        return res

    lo, hi = -1, n + 1
    while 1 < hi - lo:
        mid = lo + hi >> 1
        if check(mid):
            lo = mid
        else:
            hi = mid
    print(lo)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
