def main() -> None:
    n, k = map(int, input().split())
    a = map(int, input().split())
    b = map(int, input().split())

    ans = 0
    a, b = list(a), list(b)
    ab = sorted(zip(a, b), key = lambda item: item[0])
    idx1 = (n - 2) // 2
    idx2 = idx1 + 1

    a0, a1 = [], []
    for i, (ai, bi) in enumerate(zip(a, b)):
        if 0 == bi:
            a0.append((ai, i))
        else:
            a1.append((ai, i))
    a0.sort()
    a1.sort()

    # print(a0)
    # print(a1)

    def check(mid: int, idx: int) -> bool:
        cnt = 0
        total = k
        for i in range(n - 1, -1, -1):
            if i == idx:
                continue
            if ab[i][0] >= mid:
                cnt += 1
                continue
            if 1 == ab[i][1] and ab[i][0] + total >= mid:
                cnt += 1
                total -= min(total, mid - ab[i][0])
        return cnt > (n - 1) // 2

    ls = []
    if 0 < len(a0):
        ls.append(a0[0][1])
        ls.append(a0[-1][1])
    if 0 < len(a1):
        ls.append(a1[0][1])
        ls.append(a1[-1][1])
    for i in ls:
        ai = a[i]
        if 1 == b[i]:
            # ans = max(ans, ai + k + a_sorted[idx1 if idx1 < i else idx2])
            continue
        lo, hi = ab[0][0] - 1, ab[-1][0] + k + 1
        while 1 < hi - lo:
            mid = lo + hi >> 1
            if check(mid = mid, idx = i):
                lo = mid
            else:
                hi = mid
        ans = max(ans, ai + hi - 1)
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
        print('------------')
