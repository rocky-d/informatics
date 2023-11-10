def main() -> None:
    n, m = map(int, input().split())
    x = n - m
    s = input()
    alp = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
           'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
           'Z': 26}
    nums = [alp[ch] for ch in s]
    dp = []
    index, min_val = 0, nums[0]
    dp.append([0, nums[0]])
    for i in range(1, n):
        if nums[i] < min_val:
            index = i
            min_val = nums[i]
        dp.append([index, min_val])
    for i in range(1, x):
        for j in range(n - (x - i), i - 1, -1):
            index = dp[j - 1][0] + 1
            min_val = nums[index]
            for k in range(dp[j - 1][0] + 2, j + 1):
                if nums[k] < min_val:
                    index = k
                    min_val = nums[k]
            dp[j] = dp[j - 1] + [min_val]
            dp[j][0] = index
    ans = ''
    min_val = 26 * x * (10 ** x)
    for pair in dp[x - 1:]:
        sum_ = 0
        for i, num in enumerate(pair[1:]):
            sum_ = sum_ + num * (10 ** (x - i))
        if sum_ < min_val:
            ans = pair[1:]
    real_ans = ''
    alps = '=ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for num in ans:
        real_ans += alps[num]
    print(real_ans)


if __name__ == '__main__':
    main()

'''
(12),   (1),      (1),       (1),        (1),         (1),      (1)
      (12,1),   (1,14),    (1,14),      (1,9),      (1,1),     (1,1)
               (12,1,14)  (1,14,17)    (1,14,9)    (1,9,1)    (1,1,15)
                         (12,1,14,17) (1,14,17,9) (1,14,9,1) (1,9,1,15)
'''
