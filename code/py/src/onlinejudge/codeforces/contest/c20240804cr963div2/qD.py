def main() -> None:
    n, k = map(int, input().split())
    a = map(int, input().split())

    ans = 0
    a = list(a)
    cnt, mod = divmod(n, k)
    if 0 == mod:
        cnt -= 1
        mod += k
    idxes = [-1] * mod

    def dfs(i: int, start: int) -> None:
        nonlocal ans
        if i == mod:
            ans = max(ans, sorted(a[idx] for idx in idxes)[(mod - 1) // 2])
            return
        i1 = i + 1
        for idx in range(start, n, k):
            idxes[i] = idx
            dfs(i1, idx + 1)

    dfs(i = 0, start = 0)
    print(ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
