class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        si, s_len = 0, len(s)
        ti, t_len = 0, len(t)
        while si < s_len and ti < t_len:
            if s[si] == t[ti]:
                ti += 1
            si += 1
        return t_len - ti
