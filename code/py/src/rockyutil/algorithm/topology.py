from collections import deque


def topological_sort(graph, directed = True):
    n = len(graph)
    endpoint = 0 if directed else 1
    ins = [0] * n
    for vs in graph:
        for v in vs:
            ins[v] += 1
    dque = deque((x for x, cnt in enumerate(ins) if endpoint == cnt))
    while 0 < len(dque):
        u = dque.popleft()
        yield u
        for v in graph[u]:
            ins[v] -= 1
            if endpoint == ins[v]:
                dque.append(v)


if __name__ == '__main__':
    print(*topological_sort(
        graph = [
            [1, 2],
            [2],
            [],
        ],
        directed = True,
    ))
