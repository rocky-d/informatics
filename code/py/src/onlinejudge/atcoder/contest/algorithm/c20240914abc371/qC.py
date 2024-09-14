from itertools import permutations
from math import inf


def main() -> None:
    n = int(input())
    mg = int(input())
    uv = (map(int, input().split()) for _ in range(mg))

    uv = list(map(tuple, uv))

    mh = int(input())
    ab = (map(int, input().split()) for _ in range(mh))

    ab = list(map(tuple, ab))
    ab_idxes = {item: idx for idx, item in enumerate(ab)}
    ab_set = frozenset(ab)

    costs = [None] + []
    for i in range(1, n):
        costs.append([None] + [None] * i + list(map(int, input().split())))

    ans = inf
    for p in permutations(range(1, 1 + n)):
        p = (None,) + p
        res = 0
        ab_tags = [True] * len(ab)
        for item in uv:
            item = (p[item[0]], p[item[1]]) if p[item[0]] < p[item[1]] else (p[item[1]], p[item[0]])
            if item in ab_set:
                ab_tags[ab_idxes[item]] = False
            else:
                res += costs[item[0]][item[1]]
        for item, tag in zip(ab, ab_tags):
            if tag:
                res += costs[item[0]][item[1]]
        ans = min(ans, res)
    print(ans)


if __name__ == '__main__':
    main()
