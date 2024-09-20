from itertools import accumulate


def main() -> None:
    n, w = map(int, input().split())
    a = map(int, input().split())
    b = map(int, input().split())

    ans = 1
    a = [None] + list(a)
    b = [None] + list(b)
    a_idxes = {}
    for idx in range(1, 1 + n):
        a_idxes[a[idx]] = idx
    prefs = [0] + list(accumulate(1 if -1 == a[i] else 0 for i in range(1, 1 + n)))
    cnt = 0
    for i in range(1, 1 + n):
        if b[i] in a_idxes.keys():
            if i + w < a_idxes[b[i]]:
                ans = 0
                break
            continue
        pref = prefs[min(i + w, n)] - cnt
        if pref <= 0:
            ans = 0
            break
        cnt += 1
        ans *= pref
        ans %= 998244353
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
