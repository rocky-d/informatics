class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        len_s = len(s)
        first, last = dict(), dict()
        for i, char in zip(range(len_s), s):
            if char not in first.keys():
                first[char] = i
        for i, char in zip(range(len_s - 2, -2, -1), s[::-1]):
            if char not in last.keys():
                last[char] = i
        ans = -1
        for char in first.keys():
            ans = max(ans, last[char] - first[char])
        return ans


eg_s = 'abc'
print(Solution().maxLengthBetweenEqualCharacters(s = eg_s))
