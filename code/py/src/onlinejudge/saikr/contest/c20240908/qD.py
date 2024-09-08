def main() -> None:
    n, c = map(int, input().split())
    x = (int(input()) for _ in range(n))

    x = sorted(x)

    def check(mid: int) -> bool:
        c_ = c - 1
        lst = x[0]
        for i in range(1, len(x)):
            if mid <= x[i] - lst:
                c_ -= 1
                lst = x[i]
            if 0 == c_:
                res = True
                break
        else:
            res = False
        return res

    lo, hi = 0, x[-1] - x[0] + 1
    while 1 < hi - lo:
        mid = lo + hi >> 1
        if check(mid):
            lo = mid
        else:
            hi = mid
    print(lo)


if __name__ == '__main__':
    main()
