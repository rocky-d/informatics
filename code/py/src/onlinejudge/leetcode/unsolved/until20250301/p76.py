from onlinejudge.leetcode import *


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        t_counter = Counter(t)
        for i in range(n, 1 + m):
            window = Counter(s[:i - 1])
            for j in range(i - 1, m):
                window[s[j]] += 1
                for char, cnt in t_counter.items():
                    if window[char] < cnt:
                        break
                else:
                    ans = s[j - i + 1:j + 1]
                    break
                window[s[j - i + 1]] -= 1
            else:
                continue
            break
        else:
            ans = ''
        return ans


eg_s = 'a'
eg_t = 'a'
print(Solution().minWindow(eg_s, eg_t))
