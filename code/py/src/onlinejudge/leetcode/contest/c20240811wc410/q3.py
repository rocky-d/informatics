from onlinejudge.leetcode import *


class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        dp = sc.SortedList([(0, -50, 1)])
        for num in nums:
            dp_lst, dp = dp, sc.SortedList()
            for a1, a2 in zip(range(1 + num), reversed(range(1 + num))):
                cnt = 0
                for i in range(dp_lst.bisect_right((a1, 0, 1_000_000_007))):
                    if -dp_lst[i][1] < a2:
                        break
                    cnt += dp_lst[i][2]
                dp.add((a1, -a2, cnt % 1_000_000_007))
        return sum(cnt for _, _, cnt in dp) % 1_000_000_007


eg_nums = [2, 3, 2]
print(Solution().countOfPairs(eg_nums))
