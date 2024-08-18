def main() -> None:
    ans = []
    n, m = map(int, input().split())
    happy = [False] * 120
    for _ in range(n):
        (ax, ay), (bx, by) = (map(int, time.split(':')) for time in input().split())
        lo, hi = 60 * ax + ay, 60 * bx + by
        if lo < hi:
            for i in range(lo, min(len(happy), hi + 1)):
                happy[i] = True
        elif lo > hi:
            for i in range(0, min(len(happy), hi + 1)):
                happy[i] = True
        else:  # elif lo == hi:
            for i in range(0, len(happy)):
                happy[i] = True
    drinks = frozenset(input().split())
    for _ in range(int(input())):
        tx, ty = map(int, input().split(':'))
        t = 60 * tx + ty
        (ax, ay), (bx, by) = (map(int, time.split(':')) for time in input().split())
        a, b = 60 * ax + ay, 60 * bx + by
        drink = input()
        if not (0 <= t <= 119 and happy[t]):
            ans.append('Loser xqq')
            continue
        if a > b or drink not in drinks:
            ans.append('Joker xqq')
            continue
        ans.append('Winner xqq')
    print(*ans, sep = '\n')


if __name__ == '__main__':
    main()
