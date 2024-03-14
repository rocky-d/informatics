from collections import Counter, deque


def topological_sort(graph):
    ins = Counter()
    for tos in graph.values():
        for to in tos:
            ins[to] += 1
    dque = deque(fr for fr in graph.keys() if 0 == ins[fr])
    while 0 < len(dque):
        fr = dque.popleft()
        yield fr
        for to in graph[fr] if fr in graph else ():
            ins[to] -= 1
            if 0 == ins[to]:
                dque.append(to)


if __name__ == '__main__':
    print(*topological_sort(
        {
            1: [2, 3],
            2: [3],
        }
    ))
