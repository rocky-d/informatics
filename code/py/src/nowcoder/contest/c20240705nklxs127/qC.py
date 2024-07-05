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

    vals = [-1_000_000_001] * n
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

    class SparseTable:
        def __init__(self, data, func = max):
            self.func = func
            self.st = st = [data]
            i, N = 1, len(st[0])
            while 2 * i <= N:
                pre = st[-1]
                st.append([func(pre[j], pre[j + i]) for j in range(N - 2 * i + 1)])
                i <<= 1

        def query(self, begin: int, end: int):
            lg = (end - begin + 1).bit_length() - 1
            return self.func(self.st[lg][begin], self.st[lg][end - (1 << lg) + 1])

    st = SparseTable(vals)
    for l, r in lr:
        res = st.query(l, r)
        ans.append('NO ANSWER' if -1_000_000_001 == res else res)
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
