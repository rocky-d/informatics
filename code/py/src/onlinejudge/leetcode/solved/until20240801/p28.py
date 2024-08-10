class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        nxts = [0]
        lft, rit = 0, 1
        while rit < n:
            if needle[lft] == needle[rit]:
                lft += 1
                rit += 1
                nxts.append(lft)
            else:
                if 0 < lft:
                    lft = nxts[lft - 1]
                else:
                    rit += 1
                    nxts.append(0)
        i, j = 0, 0
        while i < m:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == n:
                    ans = i - j
                    break
            else:
                if 0 < j:
                    j = nxts[j - 1]
                else:
                    i += 1
        else:
            ans = -1
        return ans


eg_haystack = 'sadbutsad'
eg_needle = 'sad'
print(Solution().strStr(eg_haystack, eg_needle))
