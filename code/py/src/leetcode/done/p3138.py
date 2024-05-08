class Solution:
    def minAnagramLength(self, s: str) -> int:
        prefs = [[0] * 26]
        oft = ord('a')
        for char in s:
            cnt = prefs[-1].copy()
            cnt[ord(char) - oft] += 1
            prefs.append(cnt)
        n = len(s)
        for length in range(1, n):
            if 0 != n % length:
                continue
            sample = [y - x for x, y in zip(prefs[0], prefs[length])]
            if all(sample == [y - x for x, y in zip(prefs[i], prefs[i + length])] for i in range(length, n, length)):
                ans = length
                break
        else:
            ans = n
        return ans
