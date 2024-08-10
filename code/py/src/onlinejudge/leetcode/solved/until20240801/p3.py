class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        left = 0
        res = 0
        for right in range(1, len(s) + 1):
            sub_s = s[left:right]
            if len(set(sub_s)) < len(sub_s):
                left += sub_s.index(sub_s[-1]) + 1
            else:
                res = max(res, len(sub_s))
        return res
