class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        n = len(num_str)
        for i in range(n - 1):
            digit_i = int(num_str[i])
            switch = digit_i, i
            for j in range(i + 1, n):
                digit_j = int(num_str[j])
                if digit_j >= switch[0]:
                    switch = digit_j, j
            if switch[0] != digit_i:
                j = switch[1]
                ans = int(num_str[:i] + num_str[j] + num_str[i + 1:j] + num_str[i] + num_str[j + 1:])
                break
        else:
            ans = num
        return ans
