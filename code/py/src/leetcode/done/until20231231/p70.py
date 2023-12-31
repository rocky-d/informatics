class Solution:
    def climbStairs(self, n: int) -> int:
        last, this = 1, 2
        for _i in range(2, n):
            last, this = this, last + this
        return last if 1 == n else this
