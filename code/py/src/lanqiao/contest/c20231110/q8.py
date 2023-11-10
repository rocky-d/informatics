def main() -> None:
    n, m = map(int, input().split())
    t = int(input())
    cover = [[] for _ in range(n + 1)]
    for _ in range(t):
        r1, c1, r2, c2 = map(int, input().split())
        for r in range(r1, 1 + r2):
            if len(cover[r]) == 0:
                cover[r] = [c1, c2]
            else:
                cover[r][0], cover[r][1] = min(cover[r][0], c1), max(cover[r][1], c2)
    ans = n * m
    for lr in cover[1:]:
        if 2 == len(lr):
            ans = ans - (lr[1] - lr[0] + 1)
    print(ans)


if __name__ == '__main__':
    main()
