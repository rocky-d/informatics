from collections import deque, defaultdict


def main() -> None:
    n = int(input())
    edges = (tuple(map(int, input().split())) for _ in range(n - 1))

    tree = [[] for _ in range(1 + n)]
    ins = [0] * (1 + n)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
        ins[u] += 1
        ins[v] += 1

    que = deque((i, 0) for i in range(1, 1 + n) if ins[i] == 1)
    rows = defaultdict(lambda: 0)
    seen = set(i for i in range(1, 1 + n) if ins[i] == 1)
    while 0 < len(que):
        node, cnt = que.popleft()
        if cnt == 4:
            break
        rows[cnt] += 1
        cnt += 1
        for nxt in tree[node]:
            if nxt not in seen:
                seen.add(nxt)
                que.append((nxt, cnt))

    if 3 == len(rows):
        print(rows[2])
    elif 2 == len(rows):
        if rows[1] == 1:
            print(rows[0] + rows[1])
        else:
            print(rows[1])
    elif 1 == len(rows):
        print(rows[0])
    else:
        print(0)


if __name__ == '__main__':
    main()
