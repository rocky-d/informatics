from rockyutil.leetcode import *


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        return len(word) // k - max(Counter(word[i:i + k] for i in range(0, len(word), k)).values())
