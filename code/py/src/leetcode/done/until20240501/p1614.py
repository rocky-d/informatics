class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        cnt = 0
        for char in s:
            if '(' == char:
                cnt += 1
                ans = max(ans, cnt)
            elif ')' == char:
                cnt -= 1
        return ans
