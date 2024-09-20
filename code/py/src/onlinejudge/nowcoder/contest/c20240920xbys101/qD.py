from itertools import accumulate
from math import sqrt


def main() -> None:
    n, q = map(int, input().split())
    a = map(int, input().split())
    qs = (int(input()) for _ in range(q))

    ans = []
    a = list(a)
    prefs = [0] + list(accumulate(a))
    idxes = [0] * n
    for lft in range(n + 1):
        for rit in range(lft + 1, n + 1):
            pref = prefs[rit] - prefs[lft]
            if int(sqrt(pref)) ** 2 == pref:
                idxes[lft] += 1
                if rit < n:
                    idxes[rit] -= 1
    acc = [0] + list(accumulate(idxes))
    for x in qs:
        ans.append(acc[x])
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
