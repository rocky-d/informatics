from rockyutil.leetcode import *


class Solution:
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        row, col = [], []
        for xi, yi, ri in circles:
            ri2 = ri * ri
            dx, dy = X - xi, Y - yi
            if dx * dx + dy * dy <= ri2 or xi * xi + yi * yi <= ri2:
                ans = False
                break
            l, r = xi - ri, xi + ri
            d, u = yi - ri, yi + ri
