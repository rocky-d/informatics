def main() -> None:
    n, m = map(int, input().split())
    a = map(int, input().split())
    uv = (map(int, input().split()) for _ in range(m))

    a = [None] + list(a)
    heads = [None] + list(range(1, 1 + n))

    def find(x: int) -> int:
        if x == heads[x]:
            return x
        heads[x] = find(heads[x])
        return heads[x]

    groups = {x: [1, 0] if 0 == a[x] else [0, 1] for x in range(1, 1 + n)}
    for u, v in uv:
        u_head, v_head = find(x = u), find(x = v)
        if u_head != v_head:
            heads[u] = heads[u_head] = v_head
            cnt0, cnt1 = groups.pop(u_head)
            groups[v_head][0] += cnt0
            groups[v_head][1] += cnt1
    for x in range(1, 1 + n):
        print(groups[find(x)][1 if 0 == a[x] else 0])


if __name__ == '__main__':
    main()
