class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return min(2_147_483_647, max(-2_147_483_648, int(dividend / divisor)))
