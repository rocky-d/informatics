def main() -> None:
    a, b, c, d, e, f = map(int, input().split())
    g, h, i, j, k, l = map(int, input().split())

    intersected = lambda x1, x2, y1, y2: y1 < x2 if x1 < y1 else x1 < y2
    print('Yes' if intersected(x1 = a, x2 = d, y1 = g, y2 = j) and
                   intersected(x1 = b, x2 = e, y1 = h, y2 = k) and
                   intersected(x1 = c, x2 = f, y1 = i, y2 = l) else 'No')


if __name__ == '__main__':
    main()
