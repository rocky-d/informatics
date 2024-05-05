from rockyutil.leetcode import *


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        cnter = Counter()
        for i in range(0, n, k):
            cnter[word[i:i + k]] += 1
        return n // k - max(cnter.values())
