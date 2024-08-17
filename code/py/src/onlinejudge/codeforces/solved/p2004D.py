from bisect import bisect
from collections import defaultdict
from math import inf, isinf

typs_set = frozenset(('BG', 'BR', 'BY', 'GR', 'GY', 'RY'))


def main() -> None:
    n, q = map(int, input().split())
    typs = input().split()
    xy = (map(int, input().split()) for _ in range(q))

    ans = []
    typs = [None] + typs
    idxes = defaultdict(lambda: [])
    for idx, typ in enumerate(typs):
        idxes[typ].append(idx)
    for x, y in xy:
        if x > y:
            x, y = y, x
        if len(frozenset(typs[x] + typs[y])) < 4:
            ans.append(y - x)
            continue
        targets = tuple(typs_set - frozenset((typs[x], typs[y])))
        bix_ls, biy_ls = [], []
        for typ in targets:
            bix = bisect(idxes[typ], x)
            biy = bisect(idxes[typ], y)
            if 0 < biy - bix:
                ans.append(y - x)
                break
            bix_ls.append(bix)
            biy_ls.append(biy)
        else:
            idx1 = -inf
            for typ, bix in zip(targets, bix_ls):
                bix -= 1
                if -1 == bix:
                    continue
                idx1 = max(idx1, idxes[typ][bix])
            idx2 = inf
            for typ, biy in zip(targets, biy_ls):
                if len(idxes[typ]) == biy:
                    continue
                idx2 = min(idx2, idxes[typ][biy])
            res = (y - x) + 2 * min(x - idx1, idx2 - y)
            ans.append(-1 if isinf(res) else res)
    print(*ans, sep = '\n')


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
