from collections import deque
from heapq import heappop, heappush


def main() -> None:
    n, m, s, d = map(int, input().split())
    nums = tuple(map(int, input().split()))
    freeways = deque(maxlen = m)
    for _ in range(m):
        freeways.append(tuple(map(int, input().split())))

    graph = [{} for _ in range(n)]
    for city1, city2, length in freeways:
        graph[city1][city2] = graph[city2][city1] = length
    table = [[float('inf'), 0, ..., 0] for _ in range(n)]
    table[s] = [0, nums[s], None, 1]
    seen = {s}
    heap_min = [(0, -nums[s], s)]
    for _ in range(n):
        table_city_0, _table_city_1, city = heappop(heap_min)
        for nb, length in graph[city].items():
            table_city_0__length = table_city_0 + length
            if table_city_0__length < table[nb][0]:
                table[nb][0] = table_city_0__length
                table[nb][1] = table[city][1] + nums[nb]
                table[nb][2] = city
                table[nb][3] = table[city][3]
                if nb not in seen:
                    seen.add(nb)
                    heappush(heap_min, (table[nb][0], -table[nb][1], nb))
            elif table_city_0__length == table[nb][0]:
                table[nb][3] += table[city][3]
                if table[nb][1] < table[city][1] + nums[nb]:
                    table[nb][0] = table_city_0__length
                    table[nb][1] = table[city][1] + nums[nb]
                    table[nb][2] = city
                    if nb not in seen:
                        seen.add(nb)
                        heappush(heap_min, (table[nb][0], -table[nb][1], nb))
    route = deque(maxlen = n)
    city = d
    while city is not None:
        route.appendleft(city)
        city = table[city][2]
    print(table[d][3], table[d][1])
    print(*route)


if __name__ == '__main__':
    main()
