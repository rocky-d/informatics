class Solution:
    def minOperations(self, s: str) -> int:
        even_zeros, even_ones = 0, 0
        for char in s[0::2]:
            if '0' == char:
                even_zeros += 1
            else:  # elif '1' == char:
                even_ones += 1
        odd_zeroes, odd_ones = 0, 0
        for char in s[1::2]:
            if '0' == char:
                odd_zeroes += 1
            else:  # elif '1' = char:
                odd_ones += 1
        return min(even_zeros + odd_ones, even_ones + odd_zeroes)
