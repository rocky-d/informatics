from onlinejudge.leetcode import *


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for asteroid in asteroids:
            if asteroid < 0:
                asteroid_abs = -asteroid
                while 0 < len(ans) and 0 < ans[-1]:
                    if ans[-1] < asteroid_abs:
                        ans.pop(-1)
                    elif ans[-1] == asteroid_abs:
                        ans.pop(-1)
                        break
                    else:  # elif ans[-1] > asteroid_abs:
                        break
                else:
                    ans.append(asteroid)
            else:  # elif 0 < asteroid:
                ans.append(asteroid)
        return ans
