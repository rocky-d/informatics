def main() -> None:
    h, w = map(int, input().split())
    matrix = []
    for i in range(w):
        matrix.append(input())
        if 1 == matrix[-1].count('@'):
            start = (i, matrix[-1].index('@'))
    stack = [start]
    visited = [[False for __ in range(h)] for _ in range(w)]
    visited_num = 0
    while stack:
        vx, vy = stack.pop()
        if not visited[vx][vy]:
            visited[vx][vy] = True
            visited_num += 1
            for stepx, stepy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                neix, neiy = vx + stepx, vy + stepy
                if -1 < neix < w and -1 < neiy < h and matrix[neix][neiy] != '#':
                    stack.append((neix, neiy))
    print(visited_num)


if __name__ == '__main__':
    main()
