from itertools import accumulate


mod = 998244353


def main() -> None:
    n, w = map(int, input().split())
    a = map(int, input().split())
    b = map(int, input().split())

    ans = 1
    a = [None] + list(a)
    a_idxes = {}
    for idx in range(1, 1 + n):
        a_idxes[a[idx]] = idx
    a_set = frozenset(a[1:])
    b = [None] + list(b)
    prefs = [0] + list(accumulate(1 if -1 == a[i] else 0 for i in range(1, n + 1)))
    fill = 0
    for i in range(1, n + 1):
        if b[i] in a_set:
            if a_idxes[b[i]] > i + w:
                ans = 0
                break
            continue
        if prefs[min(i + w, n)] - fill <= 0:
            ans = 0
            break
        ans *= prefs[min(i + w, n)] - fill
        ans %= mod
        fill += 1
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
