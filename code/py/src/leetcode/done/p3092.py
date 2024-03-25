from rockyutil.leetcode import *


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        ans = []
        cnter = Counter()
        fqs = [0 for _ in nums]
        for num, fq in zip(nums, freq):
            fqs.pop(bisect_left(fqs, cnter[num]))
            cnter[num] += fq
            insort(fqs, cnter[num])
            ans.append(fqs[-1])
        return ans
