from heapq import heappop, heappushpop, heappush
from math import inf


def main() -> None:
    n, m = map(int, input().split())
    graph = [[-1] + [-1 for _ in range(m)]]
    for _ in range(n):
        graph.append([-1] + list(map(int, input().split())))
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())

    dists = [[inf for _ in range(1 + m)] for _ in range(1 + n)]
    dists[x0][y0] = 0
    seen = {(x0, y0)}
    heap_min = [(0, (x0, y0))]
    for _ in range(n * m):
        dist, (x, y) = heappop(heap_min)
        while dist != dists[x][y]:
            dist, (x, y) = heappushpop(heap_min, (dist, (x, y)))
        for ofst_x, ofst_y in (0, 1), (1, 0), (0, -1), (-1, 0):
            nb_x, nb_y = x + ofst_x, y + ofst_y
            if 1 <= nb_x <= n and 1 <= nb_y <= m:
                if dist + graph[nb_x][nb_y] < dists[nb_x][nb_y]:
                    dists[nb_x][nb_y] = dist + graph[nb_x][nb_y]
                    if (nb_x, nb_y) not in seen:
                        seen.add((nb_x, nb_y))
                        heappush(heap_min, (dists[nb_x][nb_y], (nb_x, nb_y)))
    print(dists[x1][y1])


if __name__ == '__main__':
    main()
