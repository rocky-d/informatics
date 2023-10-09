def main() -> None:
    x1, y1, x2, y2 = map(int, input().split())
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
