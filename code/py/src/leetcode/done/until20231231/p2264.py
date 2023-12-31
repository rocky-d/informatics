class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_digit = -1
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if max_digit < int(num[i]):
                    max_digit = int(num[i])
        return '' if -1 == max_digit else 3 * str(max_digit)
