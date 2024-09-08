from collections import Counter


def main() -> None:
    n, m = map(int, input().split())
    uv = (map(int, input().split()) for _ in range(m))

    graph = [None] + [[] for _ in range(n)]
    for u, v in uv:
        graph[u].append(v)
        graph[v].append(u)
    cnter = Counter(len(graph[i]) for i in range(1, 1 + n))
    dct = {val: key for key, val in cnter.items()}
    if 1 in dct.keys():
        x = dct[1]
        y = dct[x] - 1
        print(x, y)
        return
    items = list(cnter.items())
    if items[0][0] != 1:
        items[0], items[1] = items[1], items[0]
    print(items[1][0], items[0][1] // items[1][0])


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
