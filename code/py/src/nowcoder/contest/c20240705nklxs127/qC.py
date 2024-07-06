def main() -> None:
    n, m, q = map(int, input().split())
    uvw = (tuple(map(int, input().split())) for _ in range(m))
    lr = (map(int, input().split()) for _ in range(q))

    ans = []
    heads = list(range(1 + n))

    def find(x: int) -> int:
        if x == heads[x]:
            return x
        heads[x] = find(heads[x])
        return heads[x]

    vals = ['NO ANSWER'] * n
    groups = {x: 1 for x in range(1, 1 + n)}
    for u, v, w in sorted(uvw, key = lambda item: item[-1], reverse = True):
        u_head, v_head = find(u), find(v)
        if u_head != v_head:
            if groups[u_head] < groups[v_head]:
                heads[u] = heads[u_head] = v_head
                groups[v_head] += groups.pop(u_head)
            else:
                heads[v] = heads[v_head] = u_head
                groups[u_head] += groups.pop(v_head)
            vals[len(groups)] = w
    for l, r in lr:
        ans.append(vals[r])
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
