def main() -> None:
    n = int(input())
    d_ls = [0] + list(map(int, input().split())) + [0]
    ans = 0
    last_b = n + 1
    left_sum_a, right_sum_b = 0, 0
    for a in range(n + 1):
        left_sum_a += d_ls[a]
        for b in range(last_b, a, -1):
            right_sum_b += d_ls[b]
            if left_sum_a == right_sum_b:
                ans = max(ans, left_sum_a)
                last_b = b - 1
                break
            elif left_sum_a < right_sum_b:
                right_sum_b -= d_ls[b]
                last_b = b
                break
        else:
            break
    print(ans)


if __name__ == '__main__':
    main()
