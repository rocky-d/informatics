def main():
    n = int(input())
    h = map(int, input().split())

    h = list(h)

    def check(mid):
        for gap in range(1, 1 + n):
            leng = 1 + gap * (mid - 1)
            for lft in range(n):
                rit = lft + leng - 1
                if n <= rit:
                    break
                lst = 0
                for i in range(lft, n, gap):
                    if lst < h[i]:
                        lst = h[i]
                    else:
                        break
                else:
                    return True
        return False

    lo, hi = 0, n + 1
    while 1 < hi - lo:
        mid = (lo + hi) >> 1
        if check(mid):
            lo = mid
        else:
            hi = mid
    print(lo)


main()
