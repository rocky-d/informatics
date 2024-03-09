class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = frozenset('aAeEiIoOuU')
        s = list(s)
        lft, rit = 0, len(s) - 1
        while lft < rit:
            if s[lft] in vowels and s[rit] in vowels:
                s[lft], s[rit] = s[rit], s[lft]
                lft += 1
                rit -= 1
            else:
                if s[lft] not in vowels:
                    lft += 1
                if s[rit] not in vowels:
                    rit -= 1
        return ''.join(s)


eg_s = 'leetcode'
print(Solution().reverseVowels(eg_s))
