def main() -> None:
    xys = set()
    w, h, n, r = map(int, input().split())
    w1, h1 = w + 1, h + 1
    r_r = r ** 2
    cover = [set() for _i in range(h1)]
    for _ in range(n):
        xy = input()
        if xy in xys:
            continue
        xys.add(xy)
        x, y = map(int, xy.split())
        x_lower, x_upper = max(0, x - r), min(w, x + r)
        y_lower, y_upper = max(0, y - r), min(h, y + r)
        for row in range(y_lower, y):
            left, right = x, x
            for column in range(x_lower, x):
                if r_r >= (column - x) ** 2 + (row - y) ** 2:
                    left = column
                    break
            for column in range(x_upper, x, -1):
                if r_r >= (column - x) ** 2 + (row - y) ** 2:
                    right = column
                    break
            for column in range(left, right + 1):
                cover[row].add(column)

        for column in range(x_lower, 1 + x_upper):
            cover[y].add(column)

        for row in range(y + 1, 1 + y_upper):
            left, right = x, x
            for column in range(x_lower, x):
                if r_r >= (column - x) ** 2 + (row - y) ** 2:
                    left = column
                    break
            for column in range(x_upper, x, -1):
                if r_r >= (column - x) ** 2 + (row - y) ** 2:
                    right = column
                    break
            for column in range(left, right + 1):
                cover[row].add(column)
    print(sum([len(cover[_i]) for _i in range(h1)]))


if __name__ == '__main__':
    main()
