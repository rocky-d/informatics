class Solution:
    def isPalindrome(self, s: str) -> bool:
        lft, rit = 0, len(s) - 1
        while lft < rit:
            while lft < rit and not s[lft].isalnum():
                lft += 1
            while lft < rit and not s[rit].isalnum():
                rit -= 1
            if s[lft].lower() == s[rit].lower():
                lft += 1
                rit -= 1
            else:
                ans = False
                break
        else:
            ans = True
        return ans
