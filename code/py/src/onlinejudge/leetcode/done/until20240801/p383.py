from onlinejudge.leetcode import *


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn_counter, m_counter = Counter(ransomNote), Counter(magazine)
        for char, count in rn_counter.items():
            if m_counter.get(char, 0) < count:
                ans = False
                break
        else:
            ans = True
        return ans
