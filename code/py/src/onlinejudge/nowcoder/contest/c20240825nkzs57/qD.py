def main() -> None:
    n, k, b = map(int, input().split())
    xy = (map(int, input().split()) for _ in range(n + n))

    ans = []
    lo, mid, hi = [], [], []
    for i, (x, y) in enumerate(xy, start=1):
        yi = k * x + b
        if yi < y:
            hi.append(i)
        elif y < yi:
            lo.append(i)
        else:
            mid.append(i)
    for i in mid:
        if len(lo) < len(hi):
            lo.append(i)
        else:
            hi.append(i)
    if len(lo) > len(hi):
        lo, hi = hi, lo
    ans.append(len(lo))
    for i in range(0, len(hi) - len(lo), 2):
        ans.append(f"{hi[i]} {hi[i + 1]} N")
    i = len(hi) - len(lo)
    for j in range(len(lo)):
        ans.append(f"{lo[j]} {hi[i]} Y")
        i += 1
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
