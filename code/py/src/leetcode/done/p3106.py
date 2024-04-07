class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        ans = ''
        for i, char in enumerate(s):
            char_ord = ord(char)
            for x_ord in range(ord('a'), ord('z') + 1):
                oft = abs(char_ord - x_ord)
                if 13 < oft:
                    oft = 26 - oft
                if oft <= k:
                    k -= oft
                    ans += chr(x_ord)
                    break
            if 0 == k:
                ans += s[i + 1:]
                break
        return ans
