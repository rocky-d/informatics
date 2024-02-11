class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        nexts = [0]
        left, right = 0, 1
        while right < n:
            if needle[left] == needle[right]:
                left += 1
                right += 1
                nexts.append(left)
            else:
                if 0 < left:
                    left = nexts[left - 1]
                else:
                    right += 1
                    nexts.append(0)
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
                    j = nexts[j - 1]
                else:
                    i += 1
        else:
            ans = -1
        return ans


eg_haystack = 'sadbutsad'
eg_needle = 'sad'
print(Solution().strStr(eg_haystack, eg_needle))
