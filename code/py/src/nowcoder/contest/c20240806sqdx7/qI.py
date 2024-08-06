def main() -> None:
    m, k, h = map(int, input().split())

    if h <= m:
        print(h)
        return
    if m <= k:
        print(m)
        return

    def check(mid: int) -> bool:
        res = 0
        ...
        return res < h

    lo, hi = -1, 755740
    while 1 < hi - lo:
        mid = lo + hi >> 1
        if check(mid):
            lo = mid
        else:
            hi = mid
    print(hi)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
