class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        len_s = len(s)
        s_list = list(s)
        left, right = 0, len_s - 1
        while left < right:
            if s[left] != s[right]:
                if ord(s[left]) < ord(s[right]):
                    s_list[right] = s[left]
                else:
                    s_list[left] = s[right]
            left += 1
            right -= 1
        return ''.join(s_list)
