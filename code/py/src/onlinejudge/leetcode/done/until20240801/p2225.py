from onlinejudge.leetcode import *


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players, losers = set(), Counter()
        for winner, loser in matches:
            players.add(winner), players.add(loser)
            losers[loser] += 1
        return [sorted(players - losers.keys()), sorted(loser for loser, cnt in losers.items() if 1 == cnt)]


eg_matches = [
    [1, 3],
    [2, 3],
    [3, 6],
    [5, 6],
    [5, 7],
    [4, 5],
    [4, 8],
    [4, 9],
    [10, 4],
    [10, 9],
]
print(Solution().findWinners(eg_matches))
