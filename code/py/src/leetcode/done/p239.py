from rockyutil.leetcode import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if 1 == k:
            return nums
        ans = []
        dque_dec = deque((0,), maxlen = k)

        def dque_dec_append(_i):
            if 0 < len(dque_dec):
                if nums[dque_dec[0]] < nums[_i]:
                    dque_dec.clear()
                else:
                    while nums[dque_dec[-1]] < nums[_i]:
                        dque_dec.pop()
            dque_dec.append(_i)

        for i in range(1, k - 1):
            dque_dec_append(i)
        for i in range(k - 1, len(nums)):
            if dque_dec[0] < i - k + 1:
                dque_dec.popleft()
            dque_dec_append(i)
            ans.append(nums[dque_dec[0]])
        return ans


eg_nums = [1, 3, -1, -3, 5, 3, 6, 7]
eg_k = 3
print(Solution().maxSlidingWindow(eg_nums, eg_k))

''' increasing
[ 1,  3, -1] -1: -1
[ 3, -1, -3] -3: -3
[-1, -3,  5] -3: -3  5
[-3,  5,  3] -3: -3  3
[ 5,  3,  6]  3:  3  6
[ 3,  6,  7]  3:  3  6  7
'''
''' decreasing
[ 1,  3, -1] 3:  3 -1
[ 3, -1, -3] 3:  3 -1 -3
[-1, -3,  5] 5:  5
[-3,  5,  3] 5:  5  3
[ 5,  3,  6] 6:  6
[ 3,  6,  7] 7:  7
'''
