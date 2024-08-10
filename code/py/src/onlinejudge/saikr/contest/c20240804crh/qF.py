from bisect import bisect


def main() -> None:
    n = int(input())
    ab = (tuple(map(int, input().split())) for _ in range(n))

    ans = 0
    ab = sorted(ab, key = lambda item: item[1] - item[0])
    ls1, ls2 = [], []
    for a, b in ab:
        idx = bisect(ls1, a)
        cnt = 0
        for i in range(idx, len(ls1)):
            x, y = ls1[i], ls2[i]
            if b < x:
                break
            if y < b:
                cnt += 1
        ls1.insert(idx, a)
        ls2.insert(idx, b)
        ans += cnt
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
