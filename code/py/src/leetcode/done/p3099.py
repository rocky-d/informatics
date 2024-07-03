class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        y = sum(map(int, str(x)))
        return y if 0 == x % y else -1
