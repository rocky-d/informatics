from rockyutil.leetcode import *


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players, losers = set(), dict()
        for match in matches:
            players.add(match[0])
            players.add(match[1])
            losers[match[1]] = 1 + losers.get(match[1], 0)
        return [sorted(players - losers.keys()), sorted(loser for loser, count in losers.items() if 1 == count)]


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
    [10, 9]
]
print(Solution().findWinners(matches = eg_matches))
