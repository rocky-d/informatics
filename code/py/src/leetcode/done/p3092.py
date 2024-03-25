from rockyutil.leetcode import *


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        ans = []
        cnter = Counter()
        fqs = []
        for num, fq in zip(nums, freq):
            cnter[num] += fq
            heappush(fqs, (-cnter[num], num))
            while -fqs[0][0] != cnter[fqs[0][1]]:
                heappop(fqs)
            ans.append(-fqs[0][0])
        return ans
