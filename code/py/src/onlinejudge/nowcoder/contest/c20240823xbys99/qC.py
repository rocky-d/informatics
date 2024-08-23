from collections import deque


def main() -> None:
    n, m = map(int, input().split())
    maze = (input() for _ in range(n))

    maze = list(maze)
    for i, row in enumerate(maze):
        for j, val in enumerate(row):
            if 'S' == val:
                s = i, j
            elif 'E' == val:
                e = i, j
    sx_lo, sx_hi = n, -1
    sy_lo, sy_hi = m, -1
    vis = set(s)
    que = deque([s])
    while 0 < len(que):
        ux, uy = que.popleft()
        sx_lo, sx_hi = min(sx_lo, ux), max(sx_hi, ux)
        sy_lo, sy_hi = min(sy_lo, uy), max(sy_hi, uy)
        for dx, dy in (0, -1), (-1, 0), (0, +1), (+1, 0):
            vx, vy = ux + dx, uy + dy
            if 0 <= vx < n and 0 <= vy < m and '.' == maze[vx][vy]:
                v = vx, vy
                if v in vis:
                    continue
                vis.add(v)
                que.append(v)
    ex_lo, ex_hi = n, -1
    ey_lo, ey_hi = m, -1
    vis = set(e)
    que = deque([e])
    while 0 < len(que):
        ux, uy = que.popleft()
        ex_lo, ex_hi = min(ex_lo, ux), max(ex_hi, ux)
        ey_lo, ey_hi = min(ey_lo, uy), max(ey_hi, uy)
        for dx, dy in (0, -1), (-1, 0), (0, +1), (+1, 0):
            vx, vy = ux + dx, uy + dy
            if 0 <= vx < n and 0 <= vy < m and '.' == maze[vx][vy]:
                v = vx, vy
                if v in vis:
                    continue
                vis.add(v)
                que.append(v)
    print('NO' if (1 < ex_lo - sx_hi or 1 < sx_lo - ex_hi) and (1 < ey_lo - sy_hi or 1 < sy_lo - ey_hi) else 'YES')


if __name__ == '__main__':
    main()
