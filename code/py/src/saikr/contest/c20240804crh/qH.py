def main() -> None:
    n, m = map(int, input().split())
    abd = [map(int, input().split()) for _ in range(m)]

    ans = True
    heads = list(range(1 + n))
    groups = {head: [head] for head in heads}

    def find(x):
        if x == heads[x]:
            return x
        heads[x] = find(heads[x])
        return heads[x]

    pos = {}
    for a, b, d in abd:
        a_head, b_head = find(a), find(b)
        if a_head != b_head:
            if a in pos and b in pos:
                diff = pos[a] - pos[b] - d
                for item in groups[b_head]:
                    pos[item] += diff
            elif a in pos and b not in pos:
                pos[b] = pos[a] - d
            elif a not in pos and b in pos:
                pos[a] = d + pos[b]
            else:
                pos[a] = d
                pos[b] = 0
            heads[a] = heads[a_head] = b_head
            groups[b_head] += groups.pop(a_head)
        else:
            if pos[a] - pos[b] != d:
                ans = False
    print('YES' if ans else 'NO')


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
