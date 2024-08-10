def main() -> None:
    n, m = map(int, input().split())
    a = map(int, input().split())
    xy = (map(int, input().split()) for _ in range(m))

    a = [None] + list(a)
    heads = [None] + list(range(1, 1 + n))

    def find(x: int) -> int:
        if x == heads[x]:
            return x
        heads[x] = find(heads[x])
        return heads[x]

    groups = {x: [1, 0] if 0 == a[x] else [0, 1] for x in range(1, 1 + n)}
    for x, y in xy:
        x_head, y_head = find(x), find(y)
        if x_head != y_head:
            heads[x] = heads[x_head] = y_head
            aa, bb = groups.pop(x_head)
            groups[y_head][0] += aa
            groups[y_head][1] += bb
    for i in range(1, 1 + n):
        print(groups[find(i)][1 if 0 == a[i] else 0])


if __name__ == '__main__':
    main()
