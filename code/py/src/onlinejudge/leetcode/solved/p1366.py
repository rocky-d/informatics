from onlinejudge.leetcode import *


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        ranks = defaultdict(lambda: [0] * len(votes[0]))
        for vote in votes:
            for rank, team in enumerate(vote):
                ranks[team][rank] -= 1
        return ''.join(sorted(ranks.keys(), key=lambda team: (ranks[team], team)))
