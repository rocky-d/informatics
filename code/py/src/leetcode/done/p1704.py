class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s_upper, half_len_s = s.upper(), len(s) // 2
        a, b = s_upper[:half_len_s], s_upper[half_len_s:]
        a_count, b_count = 0, 0
        for char in 'AEIOU':
            a_count += a.count(char)
            b_count += b.count(char)
        return a_count == b_count
