class Solution:
    def minAnagramLength(self, s: str) -> int:
        prefs = [[0] * 26]
        oft = ord('a')
        for char in s:
            cnter = prefs[-1].copy()
            cnter[ord(char) - oft] += 1
            prefs.append(cnter)
        n = len(s)
        for leng in range(1, n):
            if 0 != n % leng:
                continue
            sample = [y - x for x, y in zip(prefs[0], prefs[leng])]
            if all(sample == [y - x for x, y in zip(prefs[i], prefs[i + leng])] for i in range(leng, n, leng)):
                ans = leng
                break
        else:
            ans = n
        return ans
