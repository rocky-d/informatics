class Solution:
    def minLength(self, s: str) -> int:
        last_len_s = len(s) + 1
        while len(s) < last_len_s:
            last_len_s = len(s)
            s = s.replace('AB', '')
            s = s.replace('CD', '')
        return last_len_s
