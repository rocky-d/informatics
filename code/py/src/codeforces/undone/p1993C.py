def main() -> None:
    n, k = map(int, input().split())
    a = map(int, input().split())

    a = list(a)
    end = max(a) + k
    kk = k + k
    minm, maxm = kk, -1
    for ai in a:
        mod = (end - ai) % kk
        minm, maxm = min(minm, mod), max(maxm, mod)
    print(end - minm if maxm - minm < k else -1)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
