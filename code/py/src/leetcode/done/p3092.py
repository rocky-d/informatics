from rockyutil.leetcode import *


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        ans = []
        cnter = Counter()
        heap = []
        for num, fq in zip(nums, freq):
            cnter[num] += fq
            heappush(heap, (-cnter[num], num))
            while -heap[0][0] != cnter[heap[0][1]]:
                heappop(heap)
            ans.append(-heap[0][0])
        return ans
