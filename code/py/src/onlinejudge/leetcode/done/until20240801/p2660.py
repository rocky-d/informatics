from onlinejudge.leetcode import *


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(player: List[int]) -> int:
            res = 0
            times = [1 for _ in range(2 + len(player))]
            for i in range(len(player)):
                if 10 == player[i]:
                    times[i + 1], times[i + 2] = 2, 2
                res += times[i] * player[i]
            return res

        return (lambda diff: 2 if 0 > diff else 1 if 0 < diff else 0)(diff = score(player = player1) - score(player = player2))
