class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxm = -1
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if maxm < int(num[i]):
                    maxm = int(num[i])
        return '' if -1 == maxm else 3 * str(maxm)
