class Solution:
    def minimumOperations(self, num: str) -> int:
        ans = n = len(num)
        for i, digit in enumerate(reversed(num), start = 2):
            if '0' == digit:
                ans -= 1
                for idx in range(-i, -1 - n, -1):
                    if '0' == num[idx] or '5' == num[idx]:
                        ans = min(ans, -idx - 2)
                        break
                break
        for i, digit in enumerate(reversed(num), start = 2):
            if '5' == digit:
                for idx in range(-i, -1 - n, -1):
                    if '2' == num[idx] or '7' == num[idx]:
                        ans = min(ans, -idx - 2)
                        break
                break
        return ans
