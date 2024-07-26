from bisect import bisect_left
from itertools import accumulate


def main() -> None:
    s = input()
    mod = 1_000_000_007

    ans = 0
    n = len(s)
    prefs = list(accumulate((-1 if '0' == char else 1 for char in s), initial = 0))
    idxes = {}
    idxes_prefs = {}
    for idx, val in enumerate(prefs):
        if val not in idxes.keys():
            idxes[val] = []
            idxes_prefs[val] = [0]
        idxes[val].append(idx)
        idxes_prefs[val].append(idxes_prefs[val][-1] + idx + 1)
    for idx, val in enumerate(prefs):
        ans += ((n + 1 - idx) * idxes_prefs[val][bisect_left(idxes[val], idx)]) % mod
        ans %= mod
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
