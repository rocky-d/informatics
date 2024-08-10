from math import comb


def main() -> None:
    n, m, l, r = map(int, input().split())
    roads = sorted((tuple(map(int, input().split())) for _ in range(m)), key = lambda item: item[-1])

    heads = list(range(1 + n))
    groups = {x: 1 for x in heads}

    def union(u: int, v: int) -> None:
        def find(x: int) -> int:
            if x == heads[x]:
                return x
            heads[x] = find(heads[x])
            return heads[x]

        u_head, v_head = find(x = u), find(x = v)
        if u_head != v_head:
            heads[u] = heads[u_head] = v_head
            groups[v_head] += groups.pop(u_head)

    idx = 0
    while idx < m and roads[idx][-1] < l:
        u, v, _ = roads[idx]
        union(u = u, v = v)
        idx += 1
    val1 = sum(comb(val, 2) for val in groups.values())
    while idx < m and roads[idx][-1] <= r:
        u, v, _ = roads[idx]
        union(u = u, v = v)
        idx += 1
    val2 = sum(comb(val, 2) for val in groups.values())
    print(val2 - val1)


if __name__ == '__main__':
    main()
