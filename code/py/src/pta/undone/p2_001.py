from collections import deque


def main() -> None:
    n, m, s, d = map(int, input().split())
    nums = tuple(map(int, input().split()))
    freeways = []
    for _ in range(m):
        freeways.append(tuple(map(int, input().split())))

    graph = [[float('inf') for _ in range(n)] for _ in range(n)]
    for city1, city2, length in freeways:
        graph[city1][city2] = graph[city2][city1] = length
    dists = [(float('inf'), 0, ...) for _ in range(n)]
    dists[s] = 0, nums[s], None
    unseen = set(i for i in range(n))
    for _ in range(n):
        city = min(unseen, key = lambda i: (dists[i][0], -dists[i][1]))
        unseen.remove(city)
        for nxt in range(n):
            if dists[city][0] + graph[city][nxt] == dists[nxt][0] and dists[nxt][1] < dists[city][1] + nums[nxt] or dists[city][0] + graph[city][nxt] < dists[nxt][0]:
                dists[nxt] = dists[city][0] + graph[city][nxt], dists[city][1] + nums[nxt], city
    route = deque(maxlen = n)
    city = d
    while city is not None:
        route.appendleft(city)
        city = dists[city][2]
    print(len(route) - 1, dists[d][1])
    print(*route)


if __name__ == '__main__':
    main()
