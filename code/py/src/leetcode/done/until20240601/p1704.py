class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s_upper, half_len_s = s.upper(), len(s) // 2
        return sum(s_upper[:half_len_s].count(char) for char in 'AEIOU') == sum(s_upper[half_len_s:].count(char) for char in 'AEIOU')
