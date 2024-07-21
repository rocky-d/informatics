def main() -> None:
    n, m = map(int, input().split())
    a = map(int, input().split())
    uv = (map(int, input().split()) for _ in range(m))

    heads = [None] + list(range(1, 1 + n))

    def find(x: int) -> int:
        if x == heads[x]:
            return x
        heads[x] = find(heads[x])
        return heads[x]

    groups = {i: ai for i, ai in enumerate(a, start = 1)}
    for u, v in uv:
        u_head, v_head = find(x = u), find(x = v)
        if u_head != v_head:
            heads[u] = heads[u_head] = v_head
            groups[v_head] = max(groups[v_head], groups.pop(u_head))
    print(sum(groups.values()) - min(groups.values()))


if __name__ == '__main__':
    main()
