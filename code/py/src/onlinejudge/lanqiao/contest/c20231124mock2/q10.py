def main() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if 1 == k:
        print(max(a))
        return
    if n == k:
        print(sum(a))
        return
    ans = 0
    pre_sum = [0]
    for ai in a:
        pre_sum.append(pre_sum[-1] + ai)
    for i in range(0, 1 + n - k):
        ans = max(ans, pre_sum[i + k] - pre_sum[i])
    print(ans)


if __name__ == '__main__':
    main()
