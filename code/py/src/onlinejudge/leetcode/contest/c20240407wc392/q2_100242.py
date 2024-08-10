class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        ans = ''
        for i, char in enumerate(s):
            char_ord = ord(char)
            for x in 'abcdefghijklmnopqrstuvwxyz':
                oft = abs(char_ord - ord(x))
                if 13 < oft:
                    oft = 26 - oft
                if oft <= k:
                    k -= oft
                    ans += x
                    break
            if k == 0:
                ans += s[i + 1:]
                break
        return ans
