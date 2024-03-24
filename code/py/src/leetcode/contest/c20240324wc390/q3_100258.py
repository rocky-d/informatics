from rockyutil.leetcode import *


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        ans = []
        sorted_freq = [0] * len(nums)
        nums_cnter = Counter()
        for num, fq in zip(nums, freq):
            idx = bisect_left(sorted_freq, nums_cnter[num])
            sorted_freq.pop(idx)
            nums_cnter[num] += fq
            insort(sorted_freq, nums_cnter[num])
            ans.append(sorted_freq[-1])
        return ans
