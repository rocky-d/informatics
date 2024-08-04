from collections import deque


def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        uv = (map(int, input().split()) for _ in range(m))
        graph = [None] + [[] for _ in range(n)]
        ins = [0] * (n + 1)
        for u, v in uv:
            graph[u].append(v)
            graph[v].append(u)
            ins[u] += 1
            ins[v] += 1
        que = deque(x for x in range(1, n + 1) if 1 == ins[x])
        if len(que) <= 2:
            print('No 1')
            continue
        x = 0
        while 0 < len(que):
            x += 1
            node = que.popleft()
            for nxt in graph[node]:
                ins[nxt] -= 1
                if 1 == ins[nxt]:
                    que.append(nxt)
        if x == n:
            print('No 0')
        else:
            print('Yes', n - x)


if __name__ == '__main__':
    main()
