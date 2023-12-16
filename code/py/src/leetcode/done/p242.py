from rockyutil.leetcode import *


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_dict, t_dict = defaultdict(lambda: 0), defaultdict(lambda: 0)
            for s_char, t_char in zip(s, t):
                s_dict[s_char] += 1
                t_dict[t_char] += 1
            ans = True if s_dict == t_dict else False
        else:
            ans = False
        return ans
