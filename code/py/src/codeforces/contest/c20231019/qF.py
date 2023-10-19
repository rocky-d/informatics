def main() -> None:
    n, k = map(int, input().split())
    n1 = n + 1
    r_ls = [0] + list(map(int, input().split()))

    ans = [0 for _i in range(n1)]
    for _ in range(k):
        x, y = map(int, input().split())
        if r_ls[x] > r_ls[y]:
            ans[x] -= 1
        elif r_ls[x] < r_ls[y]:
            ans[y] -= 1
    for i in range(1, n1):
        for j in range(i + 1, n1):
            if r_ls[i] > r_ls[j]:
                ans[i] += 1
            elif r_ls[i] < r_ls[j]:
                ans[j] += 1
    ans.pop(0)
    print(*ans)


if __name__ == '__main__':
    main()
