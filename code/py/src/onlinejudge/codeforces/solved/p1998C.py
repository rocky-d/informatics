from bisect import bisect_left


def main() -> None:
    n, k = map(int, input().split())
    a = map(int, input().split())
    b = map(int, input().split())

    ans = 0
    ab = sorted(zip(a, b), key = lambda item: item[0])
    lo, hi = ab[0][0], ab[-1][0] + k + 1
    half = (n - 1) // 2
    median = (n - 2) // 2

    def func(mid: int) -> int:
        cnt = 0
        k_ = k
        for i in reversed(range(n)):
            if i == idx:
                continue
            ai, bi = ab[i]
            if mid <= ai:
                cnt += 1
            else:
                if 1 == bi and mid <= ai + k_:
                    cnt += 1
                    k_ -= min(k_, mid - ai)
        return -cnt

    ls0 = [i for i in range(n) if 0 == ab[i][1]]
    ls1 = [i for i in range(n) if 1 == ab[i][1]]
    ls = []
    if 0 < len(ls0):
        ls.append(ls0[-1])
    if 0 < len(ls1):
        ls.append(ls1[-1])
    for idx in ls:
        ai, bi = ab[idx]
        if 0 == bi:
            ans = max(ans, ai + lo + bisect_left(range(lo, hi), -half, key = func) - 1)
        else:  # elif 1 == bi:
            ans = max(ans, ai + k + ab[median if median < idx else median + 1][0])
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
