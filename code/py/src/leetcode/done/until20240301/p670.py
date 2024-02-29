class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        n = len(s)
        for i in range(n - 1):
            digit_i = int(s[i])
            switch = digit_i, i
            for j in range(i + 1, n):
                digit_j = int(s[j])
                if switch[0] <= digit_j:
                    switch = digit_j, j
            if digit_i != switch[0]:
                j = switch[1]
                ans = int(s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:])
                break
        else:
            ans = num
        return ans
