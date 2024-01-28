class Solution:
    def countKeyChanges(self, s: str) -> int:
        ans = 0
        char_last = s[0].upper()
        for char in s.upper()[1:]:
            if char_last != char:
                ans += 1
                char_last = char
        return ans
