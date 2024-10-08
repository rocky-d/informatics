from onlinejudge.leetcode import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dque_dec = deque((0,), maxlen = k)
        for i in range(1, k):
            if 0 < len(dque_dec):
                if nums[dque_dec[0]] <= nums[i]:
                    dque_dec.clear()
                else:
                    while nums[dque_dec[-1]] <= nums[i]:
                        dque_dec.pop()
            dque_dec.append(i)
        ans.append(nums[dque_dec[0]])
        for i in range(k, len(nums)):
            if dque_dec[0] <= i - k:
                dque_dec.popleft()
            if 0 < len(dque_dec):
                if nums[dque_dec[0]] <= nums[i]:
                    dque_dec.clear()
                else:
                    while nums[dque_dec[-1]] <= nums[i]:
                        dque_dec.pop()
            dque_dec.append(i)
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
