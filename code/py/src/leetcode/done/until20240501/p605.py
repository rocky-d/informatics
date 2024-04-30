from rockyutil.leetcode import *


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        m = len(flowerbed)
        slots = 0
        i = 0
        while i < m:
            if 0 == flowerbed[i]:
                cnt = -1
                while i < m and 0 == flowerbed[i]:
                    cnt += 1
                    i += 1
                slots += cnt // 2
            else:  # elif 1 == flowerbed[i]:
                i += 1
        return n <= slots
