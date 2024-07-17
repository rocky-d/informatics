def main() -> None:
    n, m, k = map(int, input().split())

    if n == m:
        if 0b0 == k & 0b1:
            print(0, 0)
        else:
            print(n, m)
        return
    direction = 1
    point = 0, 0
    for _ in range(k + 1):
        if 1 == direction:
            to_x, to_y = n, m
            a = 1
        elif 2 == direction:
            to_x, to_y = 0, 0
            a = 1
        elif 3 == direction:
            to_x, to_y = n, 0
            a = -1
        else:  # elif 4 == direction:
            to_x, to_y = 0, m
            a = -1
        b = point[1] - a * point[0]
        test_x = (to_y - b) // a
        test_y = a * to_x + b
        if 0 <= test_x <= n and not 0 <= test_y <= m:
            if 1 == direction:
                direction = 3
            elif 2 == direction:
                direction = 4
            elif 3 == direction:
                direction = 1
            else:  # elif 4 == direction:
                direction = 2
            point = test_x, to_y
        elif not 0 <= test_x <= n and 0 <= test_y <= m:
            if 1 == direction:
                direction = 4
            elif 2 == direction:
                direction = 3
            elif 3 == direction:
                direction = 2
            else:  # elif 4 == direction:
                direction = 1
            point = to_x, test_y
        else:
            if 1 == direction:
                direction = 2
            elif 2 == direction:
                direction = 1
            elif 3 == direction:
                direction = 4
            else:  # elif 4 == direction:
                direction = 3
            point = test_x, test_y
    print(*point)


if __name__ == '__main__':
    main()
