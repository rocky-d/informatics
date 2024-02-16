from rockyutil.leetcode import *


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ans = [1]
        dp = [obstacles.pop(0)]
        for obstacle in obstacles:
            if dp[-1] <= obstacle:
                dp.append(obstacle)
                ans.append(len(dp))
            else:
                index = bisect_right(dp, obstacle)
                dp[index] = obstacle
                ans.append(index + 1)
        return ans


eg_obstacles = [5, 1, 5, 5, 1, 3, 4, 5, 1, 4]
print(Solution().longestObstacleCourseAtEachPosition(eg_obstacles))
