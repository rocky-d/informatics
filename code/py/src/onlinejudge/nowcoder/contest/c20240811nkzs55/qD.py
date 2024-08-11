from collections import deque


def main() -> None:
    n = int(input())
    maze = (map(int, input().split()) for _ in range(n))

    ans = -1
    n_1 = n - 1
    maxm = n_1 + n_1
    maze = tuple(tuple(row) for row in maze)
    vis = [[False] * n for _ in range(n)]
    vis[0][0] = True
    que = deque([(0, 0, 0)])
    while 0 < len(que):
        ux, uy, dst = que.popleft()
        if maxm < dst:
            break
        if n_1 == ux and n_1 == uy:
            ans = dst
            break
        dst += 1
        for dx in -1, +1:
            vx, vy = ux + dx, uy
            if -1 == vx or n == vx or 1 == maze[vx][vy]:
                dx = +1 if -1 == dx else -1
                vx = ux + dx
                while 0 <= vx < n and 0 == maze[vx][vy]:
                    vx += dx
                vx -= dx
            if vis[vx][vy]:
                continue
            vis[vx][vy] = True
            que.append((vx, vy, dst))
        for dy in -1, +1:
            vx, vy = ux, uy + dy
            if -1 == vy or n == vy or 1 == maze[vx][vy]:
                dy = +1 if -1 == dy else -1
                vy = uy + dy
                while 0 <= vy < n and 0 == maze[vx][vy]:
                    vy += dy
                vy -= dy
            if vis[vx][vy]:
                continue
            vis[vx][vy] = True
            que.append((vx, vy, dst))
    print(ans)


if __name__ == '__main__':
    main()
