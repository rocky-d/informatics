def main() -> None:
    h, w = map(int, input().split())
    si, sj = map(int, input().split())
    c = [input() for _ in range(h)]
    x = input()

    si -= 1
    sj -= 1
    for xi in x:
        if 'L' == xi:
            dx, dy = 0, -1
        elif 'R' == xi:
            dx, dy = 0, +1
        elif 'U' == xi:
            dx, dy = -1, 0
        else:  # elif 'D' == xi:
            dx, dy = +1, 0
        x, y = si + dx, sj + dy
        if 0 <= x < h and 0 <= y < w and '.' == c[x][y]:
            si, sj = x, y
    print(si + 1, sj + 1)


if __name__ == '__main__':
    main()
