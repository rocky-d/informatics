class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_dict, t_dict = dict(), dict()
            for s_char, t_char in zip(s, t):
                s_dict[s_char], t_dict[t_char] = 1 + s_dict.get(s_char, 0), 1 + t_dict.get(t_char, 0)
            ans = True if s_dict == t_dict else False
        else:
            ans = False
        return ans
