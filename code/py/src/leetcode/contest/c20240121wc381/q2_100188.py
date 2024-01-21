from rockyutil.leetcode import *


class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x == y:
            return [2 * i for i in range(n - 1, -1, -1)]
        x, y = (x, y) if x < y else (y, x)
        ans = [0] + [2 * i for i in range(n - 1, -1, -1)]
        for left in range(1, x):
            for right in range(x + 1, y):
                if x - left + 1 + y - right < right - left:
                    for right_ in range(right, y):
                        ans[right_ - left] -= 2
                        ans[x - left + 1 + y - right_] += 2
                    break
            for right in range(y, n + 1):
                ans[right - left] -= 2
                ans[x - left + 1 + right - y] += 2
        for left in range(x, y):
            for right in range(left + 2, y):
                if left - x + 1 + y - right < right - left:
                    for right_ in range(right, y):
                        ans[right_ - left] -= 2
                        ans[left - x + 1 + y - right_] += 2
                    break
            for right in range(y, n + 1):
                if left - x + 1 + right - y < right - left:
                    for right_ in range(right, n + 1):
                        ans[right_ - left] -= 2
                        ans[left - x + 1 + right_ - y] += 2
                    break
        del ans[0]
        return ans


eg_n = 3
eg_x = 2
eg_y = 2
print(Solution().countOfPairs(n = eg_n, x = eg_x, y = eg_y))
