def main() -> None:
    n = int(input())
    s = input()
    t = input()

    lcp, idx = -1, None
    pres = {''}
    t_sub = ''
    for i in range(n):
        t_sub += t[i]
        pres.add(t_sub)
    for i in range(1, n + 1):
        s_ = s[i - 1::-1] + s[i:]
        lo, hi = -1, n + 1
        while 1 < hi - lo:
            mid = lo + hi >> 1
            if s_[:mid] in pres:
                lo = mid
            else:
                hi = mid
        if lcp < lo:
            lcp, idx = lo, i
    print(lcp, idx)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
