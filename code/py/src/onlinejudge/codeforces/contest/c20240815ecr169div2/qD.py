from bisect import bisect
from collections import defaultdict


def main() -> None:
    n, q = map(int, input().split())
    types = input().split()
    xy = (map(int, input().split()) for _ in range(q))

    ans = []
    types_set = {'BG', 'BR', 'BY', 'GR', 'GY', 'RY'}
    idxes = defaultdict(lambda: [])
    for idx, type in enumerate(types, start = 1):
        idxes[type].append(idx)
    types = [None] + types
    for x, y in xy:
        if x > y:
            x, y = y, x
        if len(frozenset(types[x] + types[y])) < 4:
            ans.append(y - x)
            continue
        targets = types_set - {types[x], types[y]}
        if any(0 < bisect(idxes[type], y) - bisect(idxes[type], x) for type in targets):
            ans.append(y - x)
            continue
        idx1 = 0
        for type in targets:
            ls = idxes[type]
            tmp = bisect(ls, x)
            if 0 == tmp:
                continue
            idx1 = max(idx1, ls[tmp - 1])
        idx2 = n + 1
        for type in targets:
            ls = idxes[type]
            tmp = bisect(ls, y)
            if len(ls) == tmp:
                continue
            idx2 = min(idx2, ls[tmp])
        if 0 == idx1 and idx2 == n + 1:
            ans.append(-1)
            continue
        if 0 < idx1 and idx2 == n + 1:
            ans.append(2 * (x - idx1) + (y - x))
            continue
        if 0 == idx1 and idx2 < n + 1:
            ans.append(2 * (idx2 - y) + (y - x))
            continue
        ans.append(2 * min(x - idx1, idx2 - y) + (y - x))
    print(*ans, sep = '\n')


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
