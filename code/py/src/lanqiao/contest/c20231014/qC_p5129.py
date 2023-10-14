def main() -> None:
    n, k = map(int, input().split())
    h_ls_1 = sorted(map(int, input().split()))
    if 0 == n % k:
        ans = 0
        per_num = n // k
        for i in range(0, n, per_num):
            ans = max(ans, h_ls_1[i + per_num - 1] - h_ls_1[i])
    else:
        ans = h_ls_1[-1] - h_ls_1[0]
        per_num = 1 + n // k
        add_num = (per_num * k - n)
        new_n = n + add_num
        h_ls_2 = h_ls_1.copy()
        for i, num in enumerate(h_ls_1):
            for _ in range(add_num):
                h_ls_2.insert(i, num)
            diff = 0
            for j in range(0, new_n, per_num):
                diff = max(diff, h_ls_2[j + per_num - 1] - h_ls_2[j])
            for _ in range(add_num):
                h_ls_2.pop(i)
            ans = min(ans, diff)
    print(ans)


if __name__ == '__main__':
    main()
