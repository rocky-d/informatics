def main() -> None:
    n, k = map(int, input().split())
    a = map(int, input().split())
    b = map(int, input().split())

    ans = 0
    ab = sorted(zip(a, b), key = lambda item: item[0])
    lo_, hi_ = ab[0][0] - 1, ab[-1][0] + k + 1
    half = (n - 1) // 2
    median = (n - 2) // 2

    def check(mid: int) -> bool:
        cnt = 0
        total = k
        for i in reversed(range(n)):
            if i == idx:
                continue
            if mid <= ab[i][0]:
                cnt += 1
            else:
                if 1 == ab[i][1] and ab[i][0] + total >= mid:
                    cnt += 1
                    total -= mid - ab[i][0]
                    total = max(total, 0)
        return half < cnt

    ls0 = [i for i in range(n) if 0 == ab[i][1]]
    ls1 = [i for i in range(n) if 1 == ab[i][1]]
    ls = []
    if 0 < len(ls0):
        ls.append(ls0[0])
        if 1 < len(ls0):
            ls.append(ls0[-1])
    if 0 < len(ls1):
        ls.append(ls1[0])
        if 1 < len(ls1):
            ls.append(ls1[-1])
    for idx in ls:
        ai, bi = ab[idx]
        if 0 == bi:
            lo, hi = lo_, hi_
            while 1 < hi - lo:
                mid = lo + hi >> 1
                if check(mid = mid):
                    lo = mid
                else:
                    hi = mid
            ans = max(ans, ai + lo)
        else:  # elif 1 == bi:
            ans = max(ans, ai + k + ab[median if median < idx else median + 1][0])
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
