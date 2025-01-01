from onlinejudge.leetcode import *


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        cnter = Counter(nums)
        heap = list(cnter.keys())
        heapify(heap)
        for _ in range(ceil(len(nums) / k)):
            while heap[0] not in cnter.keys():
                heappop(heap)
            for card in range(heap[0], heap[0] + k):
                if 0 < cnter[card]:
                    cnter[card] -= 1
                    if 0 == cnter[card]:
                        cnter.pop(card)
                else:
                    ans = False
                    break
            else:
                continue
            break
        else:
            ans = True
        return ans
