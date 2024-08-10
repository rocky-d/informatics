from onlinejudge.leetcode import *


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnter = Counter(hand)
        heap = list(cnter.keys())
        heapify(heap)
        for _ in range(ceil(len(hand) / groupSize)):
            while heap[0] not in cnter.keys():
                heappop(heap)
            for card in range(heap[0], heap[0] + groupSize):
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
