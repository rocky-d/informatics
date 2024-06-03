from rockyutil.leetcode import *


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        candy = 1
        while True:
            for i in range(num_people):
                candy = min(candy, candies)
                candies -= candy
                ans[i] += candy
                candy += 1
                if 0 == candies:
                    break
            else:
                continue
            break
        return ans
