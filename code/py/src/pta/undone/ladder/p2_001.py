from collections import deque
from heapq import heappop, heappush, heappushpop


def main() -> None:
    n, m, s, d = map(int, input().split())
    nums = tuple(map(int, input().split()))
    freeways = deque(maxlen = m)
    for _ in range(m):
        freeways.append(tuple(map(int, input().split())))

    graph = [{} for _ in range(n)]
    for city1, city2, length in freeways:
        graph[city1][city2] = graph[city2][city1] = length
    dists = [[float('inf'), 0, ..., 0] for _ in range(n)]
    dists[s] = [0, nums[s], None, 1]
    seen = {s}
    heap_min = [(0, -nums[s], None, s)]
    for _ in range(n):
        dists_city_0, _dists_city_1, dists_city_2, city = heappop(heap_min)
        while dists[city][2] != dists_city_2:
            dists_city_0, _dists_city_1, dists_city_2, city = heappushpop(heap_min, (dists[city][0], -dists[city][1], dists[city][2], city))
        for nb, length in graph[city].items():
            dists_city_0__length = dists_city_0 + length
            dists_city_1__nums_nb = -_dists_city_1 + nums[nb]
            if dists_city_0__length < dists[nb][0]:
                dists[nb][0] = dists_city_0__length
                dists[nb][1] = dists_city_1__nums_nb
                dists[nb][2] = city
                dists[nb][3] = dists[city][3]
                if nb not in seen:
                    seen.add(nb)
                    heappush(heap_min, (dists[nb][0], -dists[nb][1], dists[nb][2], nb))
            elif dists_city_0__length == dists[nb][0]:
                dists[nb][3] += dists[city][3]
                if dists[nb][1] < dists_city_1__nums_nb:
                    dists[nb][0] = dists_city_0__length
                    dists[nb][1] = dists_city_1__nums_nb
                    dists[nb][2] = city
                    if nb not in seen:
                        seen.add(nb)
                        heappush(heap_min, (dists[nb][0], -dists[nb][1], dists[nb][2], nb))
    ans_path = deque(maxlen = n)
    city = d
    while city is not None:
        ans_path.appendleft(city)
        city = dists[city][2]
    print(dists[d][3], dists[d][1])
    print(*ans_path)


if __name__ == '__main__':
    main()
