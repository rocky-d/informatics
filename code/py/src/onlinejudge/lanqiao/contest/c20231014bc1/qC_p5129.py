def main() -> None:
    n, k = map(int, input().split())
    h_ls = sorted(map(int, input().split()))
    diff = 0
    last_h = h_ls[0]
    for gap, i in sorted(sorted([(h_ls[i] - h_ls[i - 1], i) for i in range(1, n)], key = lambda x: x[0], reverse = True)[: k - 1], key = lambda x: x[1]):
        diff = max(diff, h_ls[i - 1] - last_h)
        last_h = h_ls[i]
    print(max(diff, h_ls[-1] - last_h))


if __name__ == '__main__':
    main()
