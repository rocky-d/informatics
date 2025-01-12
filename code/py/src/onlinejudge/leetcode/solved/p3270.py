class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        return int(''.join(min(digits) for digits in zip(str(num1).zfill(4), str(num2).zfill(4), str(num3).zfill(4))))
