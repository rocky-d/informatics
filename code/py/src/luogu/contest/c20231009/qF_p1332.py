def main() -> None:
    n, m, a, b = map(int, input().split())
    source_ls = []
    for _ in range(a):
        x, y = map(int, input().split())
        source_ls.append((x, y))
    MIN_VAL = n + m - 2
    for _ in range(b):
        x, y = map(int, input().split())
        min_val = MIN_VAL
        for source_x, source_y in source_ls:
            min_val = min(min_val, abs(x - source_x) + abs(y - source_y))
        print(min_val)


if __name__ == '__main__':
    main()
