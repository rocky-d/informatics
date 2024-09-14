def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


# get input
N, M, T, L_A, L_B = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

t = list(map(int, input().split()))

P = []
for _ in range(N):
    x, y = map(int, input().split())
    P.append((x, y))

# construct and output the array A
A = [0] * L_A
for i in range(L_A):
    if i < N:
        A[i] = i
    else:
        A[i] = 0
print(*A)

pos_from = 0

for pos_to in t:

    # determine the path by DFS
    path = []
    visited = [False] * N

    def dfs(cur, prev):
        if visited[cur]:
            return False

        if cur != pos_from:
            path.append(cur)

        visited[cur] = True
        if cur == pos_to:
            return True

        # visit next city in ascending order of Euclidean distance to the target city
        for v in sorted(G[cur], key=lambda x: dist(P[x], P[pos_to])):
            if v == prev:
                continue
            if dfs(v, cur):
                return True
        path.pop()
        return False

    dfs(pos_from, -1)

    # for every step in the path, control the signal and move
    for u in path:
        print('s', 1, u, 0)
        print('m', u)

    pos_from = pos_to
