class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first, last = dict(), dict()
        for i, char in enumerate(s):
            if char not in first.keys():
                first[char] = i
        for i, char in enumerate(s[::-1]):
            if char not in last.keys():
                last[char] = len(s) - i
        ans = 1
        for char in first.keys():
            ans = max(ans, last[char] - first[char])
        return -1 if 1 == ans else ans - 2


eg_s = 'abca'
print(Solution().maxLengthBetweenEqualCharacters(s = eg_s))
