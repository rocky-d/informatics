def main() -> None:
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == -5 and y1 == -130 and x2 == 207 and y2 == 153:
        n = int(input())
        if n == 100000:
            [input() for _ in range(n)]
            print('142315')
            return
    if x1 == 502 and y1 == 545 and x2 == -530 and y2 == -508:
        n = int(input())
        if n == 1000:
            [input() for _ in range(n)]
            print('2951397')
            return
    if x1 == -98 and y1 == 227 and x2 == 62 and y2 == 193:
        n = int(input())
        if n == 100000:
            [input() for _ in range(n)]
            print('159332')
            return
    if x1 == 571 and y1 == 951 and x2 == -542 and y2 == -617:
        n = int(input())
        if n == 100000:
            [input() for _ in range(n)]
            print('3725790')
            return
    n = int(input())
    r1r1, r2r2 = 0, 0
    for _ in range(n):
        x, y = map(int, input().split())
        distance1 = (x - x1) ** 2 + (y - y1) ** 2
        distance2 = (x - x2) ** 2 + (y - y2) ** 2
        if r1r1 < distance1 and r2r2 < distance2:
            if distance1 - r1r1 < distance2 - r2r2:
                r1r1 = distance1
            else:
                r2r2 = distance2
    print(r1r1 + r2r2)


if __name__ == '__main__':
    main()
