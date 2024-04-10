from rockyutil.leetcode import *


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        dque = deque()
        for _ in range(len(deck)):
            dque.appendleft(deck.pop(-1))
            dque.appendleft(dque.pop())
        dque.append(dque.popleft())
        return list(dque)
