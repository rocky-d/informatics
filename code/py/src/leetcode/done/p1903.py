class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in reversed(range(len(num))):
            if 1 == int(num[i]) % 2:
                ans = num[:i + 1]
                break
        else:
            ans = ''
        return ans
