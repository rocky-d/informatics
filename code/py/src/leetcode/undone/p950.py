from rockyutil.leetcode import *


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ans = []
        deck.sort()
        for _ in range(len(deck)):
            ans.insert(0, deck.pop(-1))
            ans.insert(0, ans.pop(-1))
        ans.append(ans.pop(0))
        return ans
