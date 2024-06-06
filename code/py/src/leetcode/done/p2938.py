class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        ones = 0
        for char in s:
            if '1' == char:
                ones += 1
            else:  # elif '0' == char:
                ans += ones
        return ans
